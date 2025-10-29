
from db import BaseDeDatos

class ModelUsers():
    @staticmethod
    async def get_all():
        data = await BaseDeDatos.query("SELECT id, username, created_at FROM users")
        if not data['status']:
            return data
        data['mensaje'] = f'Se encontraron {len(data['data'])} usuarios'
        return data
    
    @staticmethod
    async def get_by_id(id: int):
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