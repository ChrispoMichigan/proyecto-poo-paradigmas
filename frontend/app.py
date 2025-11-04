import tkinter as tk
from vista.login_window import LoginWindow
from vista.main_window import MainWindow

from models.users import ModelUsers
from models.schemas.customers import CustomerCreate
from models.customers import ModelCustomers
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
        
        customer = CustomerCreate(user_id=self.user_id, first_name="Rene", last_name="coca", dni="ASGUW1234")
        data = ModelCustomers.create(customer)
        if not data['status']:
            # En caso de error
            print('Hubo un error')
            print(data['mensaje'])
            return
        
        #user_id: int
        #first_name: str
        #last_name: str
        #dni: str    


    def delete_client(self): print("Eliminar cliente") 
    def view_client(self): print("Ver cliente")
    def add_article(self): print("Agregar artículo")
    def create_invoice(self): print("Crear factura")
    def add_invoice_line(self): print("Agregar línea")
    def delete_invoice_line(self): print("Eliminar línea")
    def export_invoice(self, format): print(f"Exportar {format}")


controller = Controller()
login_window = LoginWindow(controller)
controller.login_window = login_window
window = login_window.show()
window.mainloop()
