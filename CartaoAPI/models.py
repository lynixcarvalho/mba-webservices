from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    cliente_id: str
    limite: float


class UpdateItem(BaseModel):
    limite: float
