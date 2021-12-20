from sqlalchemy import create_engine, Boolean, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from schema import ItemCreate
from config import ENV

import os

if ENV == 'local':
    engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
else:
    SQLALCHEMY_DATABASE_URL = os.getenv('DB_URI', '')
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price_in_paise = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, default=False)


def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def get_one(db:Session, id:int):
    return db.query(Item).filter(Item.id == id).one()

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item