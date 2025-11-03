from fastapi import APIRouter
from controllers.items import ControllerItems
from schemes.items import ItemCreate

items_router = APIRouter()

@items_router.get("/{user_id}")
async def get_users(user_id: int):
    data = await ControllerItems.get_all(user_id)
    return data

@items_router.get("/{id}")
async def get_by_id(id: int):
    data = ControllerItems.get_by_id(id)
    return data

@items_router.delete("/{id}")
async def delete_by_id(id: int):
    data = await ControllerItems.delete_by_id(id)
    return data

@items_router.post("/")
async def create(item: ItemCreate):
    item_create = await ControllerItems.create(item)
    return item_create

