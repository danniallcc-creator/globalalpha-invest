from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

SQLALCHEMY_DATABASE_URL = "sqlite:///./cross_border.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="analyst") # analyst, manager, admin
    company_id = Column(Integer, index=True) # For multi-tenant collaboration
    credits = Column(Integer, default=3) # New: Users start with 3 free reports
    favorites = relationship("Favorite", back_populates="owner")
    team_reports = relationship("TeamReport", back_populates="creator")

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

class TeamReport(Base):
    __tablename__ = "team_reports"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    filename = Column(String)
    created_at = Column(String)
    company_id = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="team_reports")

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="favorites")

class ChatLog(Base):
    __tablename__ = "chat_logs"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    message = Column(Text)
    reply = Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    # Create a default Public User for Web Edition (No login required mode)
    public_user = db.query(User).filter(User.username == "PublicGuest").first()
    if not public_user:
        hashed_pwd = pwd_context.hash("public_guest_pwd_2026")
        public_user = User(username="PublicGuest", hashed_password=hashed_pwd, company_id=1001, credits=999, role="Admin")
        db.add(public_user)
        db.commit()
    db.close()
