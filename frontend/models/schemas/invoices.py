from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    user_id: int
    customer_id: int
    item_id: int
    amount: int