from db import BaseDeDatos
from schemes.items import ItemCreate
class ModelItems():
    @staticmethod
    async def get_all(user_id) -> dict:
        try:
            data = await BaseDeDatos.query("SELECT id, code, type, denomination, price, weight, license, created_at FROM items WHERE user_id = ?", (user_id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
    @staticmethod
    async def create_digital(item: ItemCreate):

        try:
            item_create = await BaseDeDatos.query('INSERT INTO items(user_id, code, type, denomination, price, license) values(?, ?, ?, ?, ?, ?)', (item.user_id, item.code, item.type.value, item.denomination, item.price, item.license,))
            return item_create
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
        
    @staticmethod
    async def create_physical(item: ItemCreate):
        try:
            item_create = await BaseDeDatos.query('INSERT INTO items(user_id, code, type, denomination, price, weight) values(?, ?, ?, ?, ?, ?)', (item.user_id, item.code, item.type.value, item.denomination, item.price, item.weight,))
            return item_create
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
    
    @staticmethod
    async def get_by_id(id: int):
        try:
            data = await BaseDeDatos.query("SELECT id, code, type, denomination, price, weight, license, created_at FROM items WHERE id = ?", (id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
        
    @staticmethod
    async def delete_by_id(id: int):
        try:
            data = await BaseDeDatos.query("DELETE FROM items WHERE id = ?", (id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }