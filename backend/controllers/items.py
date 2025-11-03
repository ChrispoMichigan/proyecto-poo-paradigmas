
from models.items import ModelItems
from controllers.users import ControllerUsers
from schemes.items import ItemCreate
class ControllerItems():
    @staticmethod
    async def get_all(user_id: int):

        found_user = await ControllerUsers.get_by_id(user_id)

        if not found_user['status']:
            return found_user

        data = await ModelItems.get_all(user_id)
        data['mensaje'] = f'{len(data['data'])} productos obtenidos'
        return data
    
    @staticmethod
    async def get_by_id(id: int):
        data = await ModelItems.get_by_id(id)
        
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
    async def create(item: ItemCreate):
        found_user = await ControllerUsers.get_by_id(item.user_id)

        if not found_user['status']:
            return found_user
        
        data = {}

        if item.type.value == "digital":
            data = await ModelItems.create_digital(item)
        else:
            data = await ModelItems.create_physical(item)
        
        if not data['status']:
            return data
        
        item_create = await ControllerItems.get_by_id(data['data']['last_insert_id'])

        if item_create['data'][0]['type'] == 'digital':
            item_create['data'][0].pop('weight')
        else:
            item_create['data'][0].pop('license')

        item_create['mensaje'] = 'Producto creado correctamente'

        return item_create
    
    @staticmethod
    async def delete_by_id(id: int):
        data = await ControllerItems.get_by_id(id)
        if not data['status']:
            return data
        data = await ModelItems.delete_by_id(id)
        data['mensaje'] = f'Producto con el id {id} borrado exitosamente'
        data['data'] = None
        return data
    