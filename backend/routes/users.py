from fastapi import APIRouter

from models.users import ModelUsers

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    users = await ModelUsers.get_all()
    return users