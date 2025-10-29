
from db import BaseDeDatos

class ModelUsers():
    @staticmethod
    async def get_all():
        return await BaseDeDatos.query("SELECT id, username, created_at FROM users")
    
    @staticmethod
    async def get_by_id():
        return {
            "status": True,
            "id": 1,
            "username": "Juan"
        }
    @staticmethod
    async def create():
        return {
            "status": True,
            "id": 1,
            "username": "Juan"
        }