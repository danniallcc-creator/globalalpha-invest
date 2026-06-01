from fastapi import FastAPI, Query, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List, Optional
import json
import os

from backend.app.services.trends_service import TrendsService
from backend.app.services.market_service import MarketService
from backend.app.services.report_service import ReportService
from backend.app.services.tiktok_service import TikTokService
from backend.app.services.local_ecom_service import LocalEcomService
from backend.app.services.competitor_service import CompetitorService
from backend.app.services.customs_service import CustomsService
from backend.app.database import SessionLocal, init_db, User, Favorite, ChatLog

app = FastAPI(title="Cross-border Export Intelligence API")

# Initialize DB on startup
@app.on_event("startup")
def startup():
    init_db()

# Mount Static Files
app.mount("/reports", StaticFiles(directory="static/reports"), name="reports")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mock Database for Countries
COUNTRIES_DB = [
    {"name": "美国", "region": "北美", "gdp_per_capita": 76000, "pop": 332, "growth": 2.1, "e_comm": 15, "infra": 9, "hs_categories": ["建材", "能源"]},
    {"name": "德国", "region": "欧洲", "gdp_per_capita": 51000, "pop": 83, "growth": 1.5, "e_comm": 12, "infra": 9, "hs_categories": ["建材", "能源"]},
    {"name": "澳大利亚", "region": "亚太", "gdp_per_capita": 65000, "pop": 26, "growth": 2.5, "e_comm": 10, "infra": 8, "hs_categories": ["建材", "能源"]},
    {"name": "巴西", "region": "新兴", "gdp_per_capita": 9000, "pop": 214, "growth": 4.5, "e_comm": 8, "infra": 6, "hs_categories": ["建材", "能源"]},
    {"name": "印尼", "region": "新兴", "gdp_per_capita": 4500, "pop": 273, "growth": 5.2, "e_comm": 9, "infra": 5, "hs_categories": ["建材", "能源"]},
]

# Load Compliance Data
with open("../../data/compliance/building_materials.json", "r", encoding="utf-8") as f:
    BUILDING_DATA = json.load(f)
with open("../../data/compliance/industry_compliance.json", "r", encoding="utf-8") as f:
    INDUSTRY_DATA = json.load(f)

COMPLIANCE_DATA = BUILDING_DATA + INDUSTRY_DATA

@app.get("/")
def read_root():
    return {"message": "Welcome to Cross-border Intelligence API"}

@app.get("/api/compass")
def get_compass(category: str = Query(..., description="Product category like '户外储能'")):
    # Basic ranking logic
    # In real app, this would use a complex weighted formula
    results = {
        "profit_market": sorted(COUNTRIES_DB, key=lambda x: x["gdp_per_capita"], reverse=True)[:2],
        "mass_market": sorted(COUNTRIES_DB, key=lambda x: x["pop"], reverse=True)[:1],
        "blue_ocean": sorted(COUNTRIES_DB, key=lambda x: x["growth"], reverse=True)[:2]
    }
    return {
        "category": category,
        "recommendations": results
    }

@app.get("/api/compliance")
def search_compliance(q: str):
    matches = [item for item in COMPLIANCE_DATA if q in item["category"]]
    return matches

@app.get("/api/market")
def get_market_data():
    rates = MarketService.get_exchange_rates()
    gold = MarketService.get_gold_price()
    
    # Accurate Forex Logic (handling direct vs inverse rates)
    # Using real-time/reference data from the service
    return {
        "gold": gold,
        "forex": [
            {"pair": "USD/CNY", "rate": rates.get("USD") if rates.get("source") == "ExchangeRate-API" else rates.get("USD")},
            {"pair": "EUR/CNY", "rate": rates.get("EUR") if rates.get("source") == "ExchangeRate-API" else rates.get("EUR")},
            {"pair": "JPY/CNY", "rate": rates.get("JPY") if rates.get("source") == "ExchangeRate-API" else rates.get("JPY")},
            {"pair": "AUD/CNY", "rate": rates.get("AUD") if rates.get("source") == "ExchangeRate-API" else rates.get("AUD")},
            {"pair": "GBP/CNY", "rate": rates.get("GBP") if rates.get("source") == "ExchangeRate-API" else rates.get("GBP")}
        ],
        "last_update": rates.get("last_update"),
        "source": rates.get("source")
    }

from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class FavoriteRequest(BaseModel):
    username: str
    item: str

class ChatRequest(BaseModel):
    message: str
    username: Optional[str] = "guest"
    lang: Optional[str] = "zh"

@app.post("/api/ai-chat")
def ai_chat(req: ChatRequest):
    # Simple RAG Simulation: Search local DB for context
    query = req.message.lower()
    lang = req.lang
    context = ""
    for item in COMPLIANCE_DATA:
        if any(word in item["category"].lower() for word in query.split()) or \
           any(word in query for word in item["category"].lower().split()):
            if lang == "en":
                context = f"Advice for {item['category']}: {item['suggestion']}. Strategy: {item['breakthrough']}."
            else:
                context = f"关于{item['category']}的合规建议是：{item['suggestion']}。具体策略：{item['breakthrough']}。"
            break
    
    if context:
        if lang == "en":
            response = f"Hello! Regarding '{req.message}', I found the following professional advice:\n\n{context}\n\nFor a deeper report, click 'Generate Report'."
        else:
            response = f"您好！针对您问的‘{req.message}’，我为您检索到了以下专业建议：\n\n{context}\n\n如果您还需要深入的国别报告，可以点击‘生成报告’按钮。"
    else:
        if lang == "en":
            response = f"Received your query: '{req.message}'. I currently cover Electronics, Maternal, Clothing, and Energy. Please be more specific."
        else:
            response = f"收到您的咨询：‘{req.message}’。目前我主要掌握建材、电子、母婴、服装和新能源市场的合规情报。如果是这几个领域，您可以问得更具体些。"
    
    return {"status": "success", "reply": response}

@app.post("/api/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == req.username).first()
    if not user:
        # Auto-create for demo
        user = User(username=req.username, password=req.password)
        db.add(user)
        db.commit()
        return {"status": "success", "username": req.username, "msg": "New account created"}
    
    if user.password == req.password:
        return {"status": "success", "username": req.username}
    return {"status": "error", "message": "Invalid credentials"}

@app.post("/api/favorites/add")
def add_favorite(req: FavoriteRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == req.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if exists
    exists = db.query(Favorite).filter(Favorite.user_id == user.id, Favorite.item == req.item).first()
    if not exists:
        new_fav = Favorite(item=req.item, user_id=user.id)
        db.add(new_fav)
        db.commit()
    return {"status": "success", "favorites": [f.item for f in user.favorites]}

@app.get("/api/favorites/{username}")
def get_favorites(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return []
    return [f.item for f in user.favorites]

@app.get("/api/intel")
def get_full_intel(category: str):
    """Aggregate all intelligence data for the UI and Report."""
    compass_data = get_compass(category)
    ai_insight = TrendsService.get_ai_insight(category)
    ecom_trends = LocalEcomService.get_all_platforms()
    tiktok_trends = TikTokService.get_trending_videos(category)
    pricing_analysis = CompetitorService.get_pricing_analysis(category)
    customs_stats = CustomsService.get_customs_stats(category)
    
    compliance_info = [
        item for item in COMPLIANCE_DATA 
        if any(word in item["category"].lower() for word in category.lower().split())
    ]
    
    market_details = {}
    for group in compass_data["recommendations"].values():
        for country in group:
            market_details[country["name"]] = {
                "gdp": f"{country['gdp_per_capita'] / 1000:.1f}k",
                "population": country["pop"]
            }
            
    return {
        "recommendations": compass_data["recommendations"],
        "ai_insight": ai_insight,
        "ecom_trends": ecom_trends,
        "tiktok_trends": tiktok_trends,
        "compliance_info": compliance_info,
        "market_details": market_details,
        "pricing_analysis": pricing_analysis,
        "customs_stats": customs_stats
    }

@app.get("/api/report/generate")
def generate_report(category: str):
    # 1. Fetch data for the report
    compass_data = get_compass(category)
    ai_insight = TrendsService.get_ai_insight(category)
    ecom_trends = LocalEcomService.get_all_platforms()
    tiktok_trends = TikTokService.get_trending_videos(category)
    pricing_analysis = CompetitorService.get_pricing_analysis(category)
    customs_stats = CustomsService.get_customs_stats(category)
    
    # 2. Get Compliance Data specific to this category
    compliance_info = [
        item for item in COMPLIANCE_DATA 
        if any(word in item["category"].lower() for word in category.lower().split())
    ]
    
    # 3. Get Market Details (Macro data for the report)
    market_details = {}
    for group in compass_data["recommendations"].values():
        for country in group:
            market_details[country["name"]] = {
                "gdp": f"{country['gdp_per_capita'] / 1000:.1f}k",
                "population": country["pop"]
            }
    
    report_data = {
        "recommendations": compass_data["recommendations"],
        "ai_insight": ai_insight,
        "ecom_trends": ecom_trends,
        "tiktok_trends": tiktok_trends,
        "compliance_info": compliance_info,
        "market_details": market_details,
        "pricing_analysis": pricing_analysis,
        "customs_stats": customs_stats
    }
    
    filename = f"{category.replace(' ', '_')}_report.pdf"
    file_path = f"static/reports/{filename}"
    
    # Generate actual PDF
    ReportService.generate_pdf(category, report_data, file_path)
    
    return {
        "status": "success", 
        "download_url": f"http://localhost:8000/reports/{filename}"
    }

@app.get("/api/sourcing")
def get_ai_sourcing(category: str):
    tk = TrendsService.get_tiktok_trends(category)
    az = TrendsService.get_amazon_trends(category)
    insight = TrendsService.get_ai_insight(category)
    
    return {
        "Amazon": az,
        "TikTok": tk,
        "AI_Suggestion": insight
    }

@app.get("/api/tiktok/trending")
def get_tiktok_videos(category: str = "portable power station"):
    videos = TikTokService.get_trending_videos(category)
    return {"status": "success", "videos": videos}

@app.get("/api/ecom/trending")
def get_local_ecom_trends():
    trends = LocalEcomService.get_all_platforms()
    return {"status": "success", "platforms": trends}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
