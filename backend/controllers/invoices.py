from schemes.invoices import InvoiceCreate
from models.invoices import ModelInvoices
from controllers.customers import ControllerCustomers
from controllers.items import ControllerItems

class ControllerInvoices():
    @staticmethod
    async def get_all(id_user: int):
        data = await ModelInvoices.get_all(id_user)
        #data['mensaje'] = f'{len(data['data'])} facturas obtenidos'
        if not data['status']:
            return data
        
        if len(data['data']) == 0:
            data['data'] = None
            return data

        for i, invoice in enumerate(data['data']):
            customer = await ControllerCustomers.get_by_id(invoice['customer_id'])
            item = await ControllerItems.get_by_id(invoice['item_id'])

            data['data'][i]['customer'] = customer['data']
            data['data'][i]['item'] = item['data']

        return data
    
    async def get_by_id(id: int):
        data = await ModelInvoices.get_by_id(id)
        
        if not data['status']:
            return data
        
        if len(data['data']) == 0:
            data['status'] = False
            data['mensaje'] = f'Factura con el id {id} no encontrado'
            data['data'] = None
            return data

        data['mensaje'] = f'Factura encontrado con el id {id}'
        return data
    
    @staticmethod
    async def create(invoice: InvoiceCreate):
        
        data = await ModelInvoices.create(invoice)
        print(data)

        if not data['status']:
            return data
        
        invoice_create = await ControllerInvoices.get_by_id(data['data']['last_insert_id'])

        return invoice_create
    
    @staticmethod
    async def delete_by_id(id: int):
        data = await ControllerInvoices.get_by_id(id)
        if not data['status']:
            return data
        data = await ModelInvoices.delete_by_id(id)
        if not data['status']:
            return data
        data['mensaje'] = f'Factura con el id {id} borrado exitosamente'
        data['data'] = None
        return data