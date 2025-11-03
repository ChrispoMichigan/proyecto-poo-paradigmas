import mariadb
import os
from dotenv import load_dotenv

load_dotenv(".env")

class BaseDeDatos():
    @staticmethod
    async def conexion():
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
    async def query(query: str, params=None):
        conexion = None
        try:
            conexion = await BaseDeDatos.conexion()
            cursor = conexion.cursor(dictionary=True)
            
            if params is not None:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Verificar si es un query que devuelve datos (SELECT) o no (INSERT, UPDATE, DELETE)
            if query.strip().upper().startswith('SELECT'):
                data = cursor.fetchall()
            else:
                # Para INSERT, UPDATE, DELETE obtener información útil
                conexion.commit()
                
                # Obtener el ID del último registro insertado (útil para INSERT)
                last_insert_id = cursor.lastrowid if cursor.lastrowid else None
                
                # Obtener el número de filas afectadas
                rows_affected = cursor.rowcount
                
                data = {
                    "last_insert_id": last_insert_id,
                    "rows_affected": rows_affected
                }
            
            cursor.close()
            
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
    