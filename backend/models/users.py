
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
        data = await BaseDeDatos.query(f"SELECT id, username, created_at FROM users WHERE id = {id}")
        
        if not data['status']:
            return data
        
        if len(data['data']) == 0:
            data['mensaje'] = f'Usuario con el id {id} no encontrado'
            return data

        data['mensaje'] = f'Usuario encontrado con el id {id}'
        return data
    @staticmethod
    async def create():
        return {
            "status": True,
            "id": 1,
            "username": "Juan"
        }