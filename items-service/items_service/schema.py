from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price_in_paise: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    is_deleted: bool

    class Config:
        orm_mode = True