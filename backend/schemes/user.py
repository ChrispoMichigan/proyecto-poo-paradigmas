from pydantic import BaseModel

# Definimos el esquema 
class UserData(BaseModel):
    username: str
    password: str