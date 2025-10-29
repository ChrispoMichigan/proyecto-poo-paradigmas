from abc import ABC, abstractmethod


class ControllerUsers(ABC):
    @abstractmethod
    async def get_users():
        return {
            "status": True,
            "id": 1,
            "username": "Juan"
        }