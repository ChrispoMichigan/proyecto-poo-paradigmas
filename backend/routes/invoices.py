from fastapi import APIRouter

invoices_router = APIRouter()

@invoices_router.get("/{user_id}")
async def get_invoices(user_id: int):
    return {}

@invoices_router.get("/{id}")
async def get_by_id(id: int):
    return {}

@invoices_router.delete("/{id}")
async def delete_by_id(id: int):
    return {}

@invoices_router.post("/")
async def create():
    return {}