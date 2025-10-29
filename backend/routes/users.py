from fastapi import APIRouter

from controllers.users import ControllerUsers

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    return await ControllerUsers.get_users()