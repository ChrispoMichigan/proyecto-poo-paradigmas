import requests
import os
from dotenv import load_dotenv

from models.schemas.customers import CustomerCreate

load_dotenv(".env")

class ModelCustomers():
    @staticmethod
    def create(customer: CustomerCreate):
        try:
            backend_url = os.getenv("API_URL", "http://127.0.0.1:8000")

            response = requests.post(
                f"{backend_url}/customers",
                json=customer.model_dump(mode="json"),
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
                f"{backend_url}/customers/{user_id}",
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
    def get_by_id(invoice_id: int):
        try:
            backend_url = os.getenv("API_URL", "http://127.0.0.1:8000")

            response = requests.get(
                f"{backend_url}/invoices/{invoice_id}",
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
    def delete_by_id(customer_id: int):
        try:
            backend_url = os.getenv("API_URL", "http://127.0.0.1:8000")

            response = requests.delete(
                f"{backend_url}/customers/{customer_id}",
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