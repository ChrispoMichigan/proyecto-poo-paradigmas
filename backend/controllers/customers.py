
from models.customers import ModelCustomers
from schemes.customers import CustomerCreate

class ControllerCustomers():
    @staticmethod
    async def get_all(id_user: int):
        data = await ModelCustomers.get_all(id_user)
        data['mensaje'] = f'{len(data['data'])} usuario obtenidos'

        if len(data['data']) == 0:
            data['data'] = None
        
        return data
    
    @staticmethod
    async def delete_by_id(id: int):

        return {}
    
    @staticmethod
    async def create(customer: CustomerCreate):
        print(customer.user_id)
        print(customer.first_name)
        print(customer.last_name)
        print(customer.dni)
        return {}