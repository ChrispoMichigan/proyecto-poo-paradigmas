
#! Importar las funciones para los datos
from models.items import ModelItems
from models.schemas.items import ItemCreate
from models.schemas.items import ItemType
#* Pasarle el id del usuario logeado
data = ModelItems.get_all(user_id=1)
print('='* 10 + "DATA" + '='* 10)
print(data)
print('='* 25)


print('='* 10 + "Producto de tipo físico" + '='* 10)
print('='* 25)
#- Crear un producto de tipo físico
item = ItemCreate(
    user_id=1, 
    code="AUC1224", 
    type=ItemType.fisico, 
    denomination="Es una caja", 
    price=120, 
    weight=10
)
#? Imprimir información a mandar 
print(item.model_dump(mode='json'))
#? Mandar información
data = ModelItems.create(item)
#? Manejar respuesta
if data['status']:
    print('Item creado correctamente')
    print(data['mensaje'])
else:
    print('Error')
    print(data['mensaje'])
print('='* 25)
print('='* 25)

print('='* 10 + "Producto de tipo digital" + '='* 10)
print('='* 25)
#- Crear un producto de tipo digital
item = ItemCreate(
    user_id=1, 
    code="AUC1224", 
    type=ItemType.digital, 
    denomination="Es una caja", 
    price=120, 
    license="IMT"
)

#? Imprimir información a mandar 
print(item.model_dump(mode='json'))
#? Mandar información
data = ModelItems.create(item)
#? Manejar respuesta
if data['status']:
    print('Item creado correctamente')
    print(data['mensaje'])
else:
    print('Error')
    print(data['mensaje'])

print('='* 25)
print('='* 25)