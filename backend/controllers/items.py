
from models.items import ModelItems
from controllers.users import ControllerUsers

class ControllerItems():
    @staticmethod
    async def get_all(user_id: int):

        found_user = await ControllerUsers.get_by_id(user_id)

        if not found_user['status']:
            return found_user

        data = await ModelItems.get_all(user_id)
        data['mensaje'] = f'{len(data['data'])} productos obtenidos'
        return data