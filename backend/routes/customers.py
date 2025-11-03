from fastapi import APIRouter
from schemes.customers import CustomerCreate
from controllers.customers import ControllerCustomers

customers_router = APIRouter()

@customers_router.get("/{user_id}")
async def get_all(user_id: int):
    data = await ControllerCustomers.get_all(user_id)
    return data

@customers_router.delete("/{id}")
async def delete_by_id(id: int):
    data = await ControllerCustomers.delete_by_id(id)
    return data

@customers_router.post("/")
async def create(customer: CustomerCreate):
    data = await ControllerCustomers.create(customer)
    return data