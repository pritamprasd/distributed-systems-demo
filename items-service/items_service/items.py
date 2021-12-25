from typing import List
from fastapi import APIRouter, HTTPException
from schema import Item, ItemCreate
from models import SessionLocal, get_all, create_item, get_one
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.orm.exc import NoResultFound


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

items_router = APIRouter()

@items_router.get("/items/{id}", response_model=Item)
def get_one_item(id: int, db: Session = Depends(get_db)):
    try:
        return get_one(db, id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Id: {id}, not found in system")


@items_router.get("/items")
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = get_all(db, skip, limit)
    return {
        'items': items
    }


@items_router.post("/items", response_model=Item)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)
