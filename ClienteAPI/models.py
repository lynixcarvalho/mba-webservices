from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    # _id: str
    name: str
    address: str
    gen_card: bool
    card: Optional[list] = []


class UpdateItem(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    card: Optional[list] = []
