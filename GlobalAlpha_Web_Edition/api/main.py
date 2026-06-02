import json
import os
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import FastAPI, Query, Depends, HTTPException, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

# Import local services
from services.trends_service import TrendsService
from services.market_service import MarketService
from services.report_service import ReportService
from services.tiktok_service import TikTokService
from services.local_ecom_service import LocalEcomService
from services.competitor_service import CompetitorService
from services.customs_service import CustomsService
from services.payment_service import PaymentService
from database import SessionLocal, init_db, User, Favorite, ChatLog, TeamReport, get_password_hash

# JWT Configuration
SECRET_KEY = "CROSS_BORDER_SECRET_KEY_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

app = FastAPI(title="GlobalAlpha Web Edition")

# Initialize DB on startup
@app.on_event("startup")
def startup():
    init_db()
    # Ensure PublicGuest exists for Web Edition
    db = SessionLocal()
    guest = db.query(User).filter(User.username == "PublicGuest").first()
    if not guest:
        guest = User(
            username="PublicGuest", 
            hashed_password=get_password_hash("guest_pwd"), 
            company_id=999,
            role="Admin",
            credits=999
        )
        db.add(guest)
        db.commit()
    db.close()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(db: Session = Depends(get_db)):
    # Web Edition: No Auth required, always return the PublicGuest
    user = db.query(User).filter(User.username == "PublicGuest").first()
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Load Compliance Data
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
COMPLIANCE_DATA = []
for filename in ["building_materials.json", "industry_compliance.json", "food_industry.json", "medical_industry.json", "customs_master.json"]:
    try:
        with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
            COMPLIANCE_DATA.extend(json.load(f))
    except Exception as e:
        print(f"Warning: Could not load {filename}: {e}")

# API Endpoints
@app.post("/api/auth/register")
def register(username: str, password: str, company_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pwd = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_pwd, company_id=company_id)
    db.add(new_user)
    db.commit()
    return {"status": "success"}

@app.post("/api/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer", "username": user.username}

@app.get("/api/market")
def get_market_data():
    rates = MarketService.get_exchange_rates()
    gold = MarketService.get_gold_price()
    return {
        "gold": gold,
        "forex": [
            {"pair": "USD/CNY", "rate": rates.get("USD")},
            {"pair": "EUR/CNY", "rate": rates.get("EUR")},
            {"pair": "JPY/CNY", "rate": rates.get("JPY")},
            {"pair": "AUD/CNY", "rate": rates.get("AUD")},
            {"pair": "GBP/CNY", "rate": rates.get("GBP")}
        ]
    }

@app.get("/api/intel")
def get_full_intel(category: str):
    # Simulated Intel Aggregation
    pricing = CompetitorService.get_pricing_analysis(category)
    customs = CustomsService.get_customs_stats(category)
    compliance = [item for item in COMPLIANCE_DATA if any(w in item["category"].lower() for w in category.lower().split())]
    
    # Mock recommendation logic
    countries = [
        {"name": "美国", "gdp_per_capita": 76000, "pop": 332, "growth": 2.1},
        {"name": "德国", "gdp_per_capita": 51000, "pop": 83, "growth": 1.5},
        {"name": "澳大利亚", "gdp_per_capita": 65000, "pop": 26, "growth": 2.5}
    ]
    
    return {
        "recommendations": {
            "profit_market": countries[:2],
            "mass_market": countries[1:2],
            "blue_ocean": countries[2:3]
        },
        "compliance_info": compliance,
        "pricing_analysis": pricing,
        "customs_stats": customs
    }

@app.get("/api/user/me")
def get_user_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "credits": current_user.credits}

@app.get("/api/report/generate")
def generate_report(category: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.credits <= 0:
        raise HTTPException(status_code=402, detail="Insufficient credits")
    
    filename = f"{category}_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"
    file_path = os.path.join("static", "reports", filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    intel_data = get_full_intel(category)
    ReportService.generate_pdf(category, intel_data, file_path)
    
    current_user.credits -= 1
    new_report = TeamReport(category=category, filename=filename, company_id=current_user.company_id, user_id=current_user.id, created_at=datetime.now().strftime("%Y-%m-%d %H:%M"))
    db.add(new_report)
    db.commit()
    
    return {"download_url": f"/reports/{filename}"}

@app.get("/api/team/reports")
def get_team_reports(query: Optional[str] = None, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    q = db.query(TeamReport).filter(TeamReport.company_id == current_user.company_id)
    if query: q = q.filter(TeamReport.category.contains(query))
    return q.order_by(TeamReport.id.desc()).all()

@app.get("/api/team/members")
def get_team_members(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    members = db.query(User).filter(User.company_id == current_user.company_id).all()
    return [{"username": m.username, "role": m.role} for m in members]

@app.post("/api/team/invite")
def invite_member(username: str, role: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_user = User(username=username, hashed_password=get_password_hash("123456"), company_id=current_user.company_id, role=role)
    db.add(new_user)
    db.commit()
    return {"status": "success"}

# Static Files & Frontend
app.mount("/reports", StaticFiles(directory="static/reports"), name="reports")
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
