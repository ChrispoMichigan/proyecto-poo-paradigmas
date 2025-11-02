from fastapi import APIRouter

from controllers.users import ControllerUsers

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    users = await ControllerUsers.get_all()
    return users

@users_router.get("/{id}")
async def get_by_id(id: int):
    user = await ControllerUsers.get_by_id(id)
    return user

@users_router.delete("/{id}")
async def delete_by_id(id: int):
    data = await ControllerUsers.delete_by_id(id)
    return data

@users_router.post("/")
async def create(user_data: dict):
    data = await ControllerUsers.create(user_data)
    return data