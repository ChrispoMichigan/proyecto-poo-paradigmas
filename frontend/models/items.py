import requests
import os
from dotenv import load_dotenv

from models.schemas.items import ItemCreate

load_dotenv(".env")

class ModelItems():
    @staticmethod
    def create(item: ItemCreate):
        try:
            backend_url = os.getenv("API_URL", "http://127.0.0.1:8000")

            response = requests.post(
                f"{backend_url}/items",
                json=item.model_dump(mode='json'),
                headers={
                    "Content-Type": "application/json"
                }
            )

            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "status": False,
                    "data": None,
                    "mensaje": f"Error del servidor: {response.status_code}"
                }
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}"
            }
        
    @staticmethod 
    def get_all(user_id: int):
        try:
            backend_url = os.getenv("API_URL", "http://127.0.0.1:8000")

            response = requests.get(
                f"{backend_url}/items/{user_id}",
            )

            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "status": False,
                    "data": None,
                    "mensaje": f"Error del servidor: {response.status_code}"
                }
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "mensaje": f"Error: {str(e)}"
            }