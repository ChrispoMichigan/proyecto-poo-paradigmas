from schemes.invoices import InvoiceCreate
from models.invoices import ModelInvoices
from controllers.customers import ControllerCustomers
from controllers.items import ControllerItems

class ControllerInvoices():
    @staticmethod
    async def get_all(id_user: int):
        data = await ModelInvoices.get_all(id_user)
        data['mensaje'] = f'{len(data['data'])} facturas obtenidos'

        if len(data['data']) == 0:
            data['data'] = None
            return data

        for i, invoice in enumerate(data['data']):
            customer = await ControllerCustomers.get_by_id(invoice['customer_id'])
            item = await ControllerItems.get_by_id(invoice['item_id'])

            data['data'][i]['customer'] = customer['data']
            data['data'][i]['item'] = item['data']

        return data