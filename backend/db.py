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
    async def query(query: str):
        try:
            conexion = BaseDeDatos.conexion()
            
            # Verificar si es un query que devuelve datos (SELECT) o no (INSERT, UPDATE, DELETE)
            if query.strip().upper().startswith('SELECT'):
                cursor = conexion.cursor(dictionary=True)  # Para SELECT usar dictionary=True
                cursor.execute(query)
                data = cursor.fetchall()
            else:
                cursor = conexion.cursor(buffered=True)  # Para INSERT/UPDATE/DELETE usar cursor bufferizado
                cursor.execute(query)
                conexion.commit()
                print(f"Filas afectadas: {cursor.rowcount}")
                data = {"rows_affected": cursor.rowcount}
            
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
    