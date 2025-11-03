from pydantic import BaseModel
from datetime import datetime

class CustomerCreate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    dni: str

class Customer(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    dni: str
    created_at: datetime