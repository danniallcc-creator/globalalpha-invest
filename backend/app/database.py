from sqlalchemy import create_all, Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./cross_border.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="analyst") # analyst, manager, admin
    company_id = Column(Integer, index=True) # For multi-tenant collaboration
    favorites = relationship("Favorite", back_populates="owner")
    team_reports = relationship("TeamReport", back_populates="creator")

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
