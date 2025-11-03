from fastapi import APIRouter
from controllers.items import ControllerItems

items_router = APIRouter()

@items_router.get("/{user_id}")
async def get_users(user_id: int):
    data = await ControllerItems.get_all(user_id)
    return data

@items_router.get("/{id}")
async def get_by_id(id: int):
    return {}

@items_router.delete("/{id}")
async def delete_by_id(id: int):
    return {}

@items_router.post("/")
async def create():
    return {}

