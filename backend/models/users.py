
from db import BaseDeDatos

class ModelUsers():
    @staticmethod
    async def get_all():
        data = await BaseDeDatos.query("SELECT id, username, created_at FROM users")
        if not data['status']:
            return data
        data['mensaje'] = f'Se encontraron {len(data['data'])} usuarios'
        return data
    
    @staticmethod
    async def get_by_id(id: int):

        data = await BaseDeDatos.query("SELECT id, username, created_at FROM users WHERE id = ?", (id,))
        
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
        data = await BaseDeDatos.query("DELETE FROM users WHERE id = ?", (id,))
        data['mensaje'] = f'Usuario con el id {id} borrado exitosamente'
        data['data'] = None
        return data

    @staticmethod
    async def create(user_data: dict):

        found_user = await BaseDeDatos.query('SELECT username FROM users WHERE username = ?', (user_data['username'],))
        if not len(found_user['data']) == 0:
            return {
                "status": False,
                "data": None,
                "mensaje": "Nombre de usuario no disponible"
            }
        
        user_create = await BaseDeDatos.query('INSERT INTO users(username, password) values(?, ?)', (user_data['username'], user_data['password'],))

        data = await BaseDeDatos.query('SELECT username, created_at FROM users WHERE id = ?', (user_create['data']['last_insert_id'],))
        data['mensaje'] = 'Usuario creado correctamente'
        return data