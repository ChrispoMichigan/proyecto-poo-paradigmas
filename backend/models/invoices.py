from db import BaseDeDatos
from schemes.invoices import InvoiceCreate

class ModelInvoices():
    @staticmethod
    async def get_all(user_id: int) -> dict:
        try:
            data = await BaseDeDatos.query("SELECT id, customer_id, item_id, amount, created_at FROM invoices WHERE user_id = ?", (user_id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
        
    async def get_by_id(id: int) -> dict:
        try:
            data = await BaseDeDatos.query("SELECT id, customer_id, item_id, amount, created_at FROM invoices WHERE id = ?", (id,))
            return data
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }
    
    @staticmethod
    async def create(invoice: InvoiceCreate):

        try:
            invoice_create = await BaseDeDatos.query('INSERT INTO invoices(user_id, customer_id, item_id, amount) values(?, ?, ?, ?)', (invoice.user_id, invoice.customer_id, invoice.item_id, invoice.amount,))
            return invoice_create
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}" 
            }