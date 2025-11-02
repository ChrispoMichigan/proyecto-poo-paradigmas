from fastapi import APIRouter

from models.users import ModelUsers

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    users = await ModelUsers.get_all()
    return users

@users_router.get("/{id}")
async def get_by_id(id: int):
    user = await ModelUsers.get_by_id(id)
    return user

@users_router.delete("/{id}")
async def delete_by_id(id: int):
    data = await ModelUsers.delete_by_id(id)
    return data

@users_router.post("/")
async def create(user_data: dict):
    data = await ModelUsers.create(user_data)
    return data