from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    cliente_id: str
    card: dict[str, Union[str, int]] = None


class UpdateItem(BaseModel):
    limite: float
