from fastapi import APIRouter


items_router = APIRouter()

@items_router.get("/")
async def get_users():
    return {}

@items_router.get("/{id}")
async def get_by_id(id: int):
    return {}

@items_router.delete("/{id}")
async def delete_by_id(id: int):
    return {}

@items_router.post("/")
async def create():
    return {}

