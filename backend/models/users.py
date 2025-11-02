

from db import BaseDeDatos

class ModelUsers():
    @staticmethod
    async def get_all() -> dict:
        try:
            data = await BaseDeDatos.query("SELECT id, username, created_at FROM users")
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
        
    
    @staticmethod
    async def get_by_id(id: int):
        try:
            data = await BaseDeDatos.query("SELECT id, username, created_at FROM users WHERE id = ?", (id,))
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
            data = await BaseDeDatos.query("DELETE FROM users WHERE id = ?", (id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
        

    @staticmethod
    async def create(username, password):
        try:
            user_create = await BaseDeDatos.query('INSERT INTO users(username, password) values(?, ?)', (username, password,))
            return user_create
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
    
    @staticmethod
    async def get_by_username(username: str):
        try:
            user = await BaseDeDatos.query('SELECT username FROM users WHERE username = ?', (username,))
            return user
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }