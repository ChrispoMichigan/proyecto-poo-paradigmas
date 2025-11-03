
from models.customers import ModelCustomers
from schemes.customers import CustomerCreate

from models.users import ModelUsers

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
        data = await ModelCustomers.get_by_id(id)
        if not data['status']:
            return data
        data = await ModelCustomers.delete_by_id(id)
        data['mensaje'] = f'Usuario con el id {id} borrado exitosamente'
        data['data'] = None
        return data
    
    async def get_by_id(id: int):
        data = await ModelCustomers.get_by_id(id)
        
        if not data['status']:
            return data
        
        if len(data['data']) == 0:
            data['status'] = False
            data['mensaje'] = f'Usuario con el id {id} no encontrado'
            data['data'] = None
            return data

        data['mensaje'] = f'Usuario encontrado con el id {id}'
        return data

    @staticmethod
    async def create(customer: CustomerCreate):
        
        user_main = await ControllerCustomers.get_by_id(customer.user_id)

        if not user_main['status']:
            return user_main

        data = await ModelCustomers.create(customer)

        if not data['status']:
            return data
        
        user_create = await ModelCustomers.get_by_id(data['data']['last_insert_id'])

        return user_create