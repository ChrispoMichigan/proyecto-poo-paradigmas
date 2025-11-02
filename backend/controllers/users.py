

from models.users import ModelUsers

class ControllerUsers():
    @staticmethod
    async def get_all():
        data = await ModelUsers.get_all()
        data['mensaje'] = f'{len(data['data'])} usuario obtenidos'
        return data
    
    @staticmethod
    async def get_by_id(id: int):

        data = await ModelUsers.get_by_id(id)
        
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
    async def delete_by_id(id: int):
        data = await ModelUsers.get_by_id(id)
        if not data['status']:
            return data
        data = await ModelUsers.delete_by_id(id)
        data['mensaje'] = f'Usuario con el id {id} borrado exitosamente'
        data['data'] = None
        return data

    @staticmethod
    async def create(user_data: dict):
        
        if not 'username' in user_data.keys():
            return {
                "status": False,
                "data": None,
                "mensaje": "Se requiere el campo username"
            }
        
        if not 'password' in user_data.keys():
            return {
                "status": False,
                "data": None,
                "mensaje": "Se requiere el campo password"
            }

        found_user = await ModelUsers.get_by_username(user_data['username'])
        if not len(found_user['data']) == 0:
            return {
                "status": False,
                "data": None,
                "mensaje": "Nombre de usuario no disponible"
            }
        
        data = await ModelUsers.create(user_data['username'], user_data['password'])
        
        user_create = await ModelUsers.get_by_id(data['data']['last_insert_id'])
        user_create['mensaje'] = 'Usuario creado correctamente'
        return user_create