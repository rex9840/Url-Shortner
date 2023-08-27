from sqlalchemy import BOOLEAN,Column,String,Boolean,Integer
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from .config import get_settings 

engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}, pool_pre_ping=True 
    
)

sessionLocal = sessionmaker(
    autocommit=False ,autoflush=False , bind=engine 
)


Base =declarative_base()

class URL(Base): 
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String , unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)


print(URL.secret_key)