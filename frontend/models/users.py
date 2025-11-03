
import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")

class ModelUsers():
    @staticmethod
    def login(username, password):
        try:
            backend_url = os.getenv("API_URL", "http://127.0.0.1:8000")

            login_data = {
                    "username": username,
                    "password": password
                }
            response = requests.post(
                f"{backend_url}/users/login",
                json=login_data,
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
        