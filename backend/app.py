from fastapi import FastAPI

from routes.users import users_router
from routes.customers import customers_router

app = FastAPI()

# python -m uvicorn app:app --reload --port 8000

# Rutas de usuarios
app.include_router(users_router, prefix="/users", tags=["users"])

# Rutas de clientes
app.include_router(customers_router, prefix="/customers", tags=["customers"])

@app.get("/")
async def root():
    return {
        "status": True,
        "message": "ok, API EN FUNCIONAMIENTO",
        "data": None
        }