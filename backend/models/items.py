from db import BaseDeDatos

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