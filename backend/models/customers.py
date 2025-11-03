

from db import BaseDeDatos
from schemes.customers import CustomerCreate
class ModelCustomers():
    @staticmethod
    async def get_all(user_id: int) -> dict:
        try:
            data = await BaseDeDatos.query("SELECT id, first_name, last_name, dni, created_at FROM customers WHERE user_id = ?", (user_id,))
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
            data = await BaseDeDatos.query("DELETE FROM customers WHERE id = ?", (id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }

    @staticmethod
    async def create(customer: CustomerCreate):
        try:
            customer_create = await BaseDeDatos.query('INSERT INTO customers(user_id, first_name, last_name, dni) values(?, ?, ?, ?)', (customer.user_id, customer.first_name, customer.last_name, customer.dni,))
            return customer_create
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }