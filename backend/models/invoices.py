from db import BaseDeDatos
from schemes.invoices import InvoiceCreate

class ModelInvoices():
    @staticmethod
    async def get_all(user_id) -> dict:
        try:
            data = await BaseDeDatos.query("SELECT id, customer_id, item_id, amount, created_at FROM invoices WHERE user_id = ?", (user_id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }