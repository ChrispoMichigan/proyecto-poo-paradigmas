from fastapi import APIRouter

from backend.models.users import ModelUsers

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    users = await ModelUsers.get_users()
    return users