import tkinter as tk
from vista.login_window import LoginWindow
from vista.main_window import MainWindow

from models.users import ModelUsers
from models.schemas.customers import CustomerCreate
from models.customers import ModelCustomers
from models.items import ModelItems
from models.schemas.items import ItemCreate
from models.schemas.items import ItemType
#este archivo nomas lo hice para hacer pruebas 


class Controller:
    """Controlador temporal para pruebas"""
    def __init__(self):
        self.login_window : LoginWindow
        self.main_window : MainWindow 
        
    def login(self, username, password):

        self.login_window.estado_label.config(text="Verificando credenciales...", foreground="blue")
        self.login_window.window.update()  # Forzar actualización de la UI

        data = ModelUsers.login(username, password)
        
        # login automatico por ahora
        if not data['status']:
            # Mostrar error
            self.login_window.estado_label.config(text=data['mensaje'], foreground="red")
            return
            
        # Mostrar éxito
        self.user_id = data['data'][0]['id']
        
        #self.main_window.user_id = self.user_id
        self.login_window.estado_label.config(text="Login exitoso", foreground="green")
        self.login_window.window.update()
        
        # Esperar un momento antes de cambiar de ventana
        self.login_window.window.after(1000, self.show_main_window)  # Esperar 1 segundo
            
    def show_main_window(self):
        if self.login_window:
            self.login_window.close()
        self.main_window = MainWindow(self)
        self.main_window.user_id = self.user_id
        window = self.main_window.show()
        window.mainloop()
        
    def quit(self):
        print("salir")
        if self.main_window and self.main_window.window:
            self.main_window.window.quit()
        
    def show_about(self):
        print("Acerca del sistema...")
        
    # metodos para pruebas (solo muestran en consola lo que deben hacer)
    def add_client(self): 
        print("Agregar cliente")
        print(self.user_id)
        temp_firstname=self.main_window.client_name_entry.get()
        temp_lastname=self.main_window.client_lastname_entry.get()
        temp_dni=self.main_window.client_dni_entry.get()
        #print(temp_firstname,temp_lastname,temp_dni)
        
        customer = CustomerCreate(user_id=self.user_id, first_name=temp_firstname, last_name=temp_lastname, dni=temp_dni)
        data = ModelCustomers.create(customer)
        #print(data)
        if not data['status']:
            # En caso de error
            print('Hubo un error')
            print(data['mensaje'])
            return
        self.main_window.load_clients_to_table(self.user_id)
        

        #user_id: int
        #first_name: str
        #last_name: str
        #dni: str    


    def delete_client(self): print("Eliminar cliente") 
    def view_client(self): print("Ver cliente")
    def add_article(self): 
        print("Agregar artículo")
        #?when se te olvida que ya tenias funciones para sacar los datos del frontend
    
        datosArticulo=[self.main_window.get_article_data()]
        print(datosArticulo)
        print("nombre del articulo:",datosArticulo[0][2])
        print(self.user_id)
        #- Crear un producto de tipo físico
        if datosArticulo[0][0] == "fisico":
            item = ItemCreate(
                user_id=self.user_id, 
                code=datosArticulo[0][1], 
                type=ItemType.fisico, 
                denomination=datosArticulo[0][2], 
                price=datosArticulo[0][3], 
                weight=datosArticulo[0][4]
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
        elif datosArticulo[0][0] == "digital":

           
            print('='* 10 + "Producto de tipo digital" + '='* 10)
           

            
            #- Crear un producto de tipo digital
            item = ItemCreate(
                user_id=self.user_id, 
                code=datosArticulo[0][1], 
                type=ItemType.digital, 
                denomination=datosArticulo[0][2], 
                price=datosArticulo[0][3], 
                license=datosArticulo[0][4] 
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
        else:
            print("chingao")
        self.main_window.load_articles_to_table(self.user_id)

           

    def create_invoice(self): print("Crear factura")
    def add_invoice_line(self): print("Agregar línea")
    def delete_invoice_line(self): print("Eliminar línea")
    def export_invoice(self, format): print(f"Exportar {format}")


controller = Controller()
login_window = LoginWindow(controller)
controller.login_window = login_window
window = login_window.show()
window.mainloop()
