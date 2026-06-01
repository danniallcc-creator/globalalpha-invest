from fastapi import FastAPI, Query
from typing import List, Optional
import json

from backend.app.services.trends_service import TrendsService

app = FastAPI(title="Cross-border Export Intelligence API")

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
    COMPLIANCE_DATA = json.load(f)

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
    return {
        "gold": {"price": 2345.67, "unit": "USD/oz", "change": "+0.5%"},
        "forex": [
            {"pair": "USD/CNY", "rate": 7.24},
            {"pair": "EUR/CNY", "rate": 7.85},
            {"pair": "JPY/CNY", "rate": 0.046},
            {"pair": "AUD/CNY", "rate": 4.81},
            {"pair": "GBP/CNY", "rate": 9.21}
        ]
    }

from pydantic import BaseModel

# Mock User & Favorites DB
USERS_DB = {"admin": "password123"}
USER_FAVORITES = {"admin": []}

class LoginRequest(BaseModel):
    username: str
    password: str

class FavoriteRequest(BaseModel):
    username: str
    item: str

@app.post("/api/login")
def login(req: LoginRequest):
    if req.username in USERS_DB and USERS_DB[req.username] == req.password:
        return {"status": "success", "username": req.username}
    return {"status": "error", "message": "Invalid credentials"}

@app.post("/api/favorites/add")
def add_favorite(req: FavoriteRequest):
    if req.username not in USER_FAVORITES:
        USER_FAVORITES[req.username] = []
    if req.item not in USER_FAVORITES[req.username]:
        USER_FAVORITES[req.username].append(req.item)
    return {"status": "success", "favorites": USER_FAVORITES[req.username]}

@app.get("/api/favorites/{username}")
def get_favorites(username: str):
    return USER_FAVORITES.get(username, [])

@app.get("/api/report/generate")
def generate_report(category: str):
    # Generating a structured report summary
    report_content = f"""
# {category} 跨境出海深度报告
日期: 2026-06-01
---
## 1. 核心发现
- **首选利润国**: 德国, 澳大利亚
- **首选规模国**: 美国
- **首选蓝海国**: 巴西, 印度尼西亚

## 2. 行业趋势与合规
- **趋势**: LiFePO4 电池与 1.5H 快充成为标配。
- **合规**: 美国 UL 2743, 欧洲 CE-LVD 认证为准入红线。

## 3. AI 专家建议
针对该品类，建议重点布局具备“极端天气适应性”的产品，主攻德国冬季市场。
    """
    return {"status": "success", "report_preview": report_content, "download_url": f"/reports/{category}_report.pdf"}

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
