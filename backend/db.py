import mariadb
import os
from dotenv import load_dotenv

load_dotenv(".env")

class BaseDeDatos():
    @staticmethod
    def conexion():
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST", "localhost")
        port = int(os.getenv("DB_PORT", "3306"))
        database = os.getenv("DB_NAME")
        
        if not all([user, password, database]):
            raise RuntimeError("Faltan variables de entorno: DB_USER, DB_PASSWORD o DB_NAME")

        return mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
    @staticmethod
    async def query(query:str):
        try:
            conexion = BaseDeDatos.conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(query)
            data = cursor.fetchall()
            return {
                "status": True,
                "data": data
            }
        except Exception as e:
            return {
                "status": False,
                "data": None,
                "message": f"Error: {str(e)}"
            }
        finally:
            if conexion:
                conexion.close()
    