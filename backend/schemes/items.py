from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ItemType(Enum):
    fisico = "fisico"
    digital = "digital"

class ItemCreate(BaseModel):
    user_id: int
    code: str 
    type: ItemType
    denomination: str
    price: float
    weight: Optional[float] = None 
    license: Optional[str] = None 