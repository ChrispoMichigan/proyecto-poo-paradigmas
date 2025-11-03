from pydantic import BaseModel
from datetime import datetime

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    dni: str

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    dni: str
    created_at: datetime