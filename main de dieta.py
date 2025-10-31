import tkinter as tk
from vista.login_window import LoginWindow
from vista.main_window import MainWindow
#este archivo nomas lo hice para hacer pruebas 


class Controller:
    """Controlador temporal para pruebas"""
    def __init__(self):
        self.login_window = None
        self.main_window = None
        
    def login(self, username, password):
        print(f"Intento de login: {username}")
        # login automatico por ahora
        if username and password:
            self.show_main_window()
            
    def show_main_window(self):
        if self.login_window:
            self.login_window.close()
        self.main_window = MainWindow(self)
        window = self.main_window.show()
        window.mainloop()
        
    def quit(self):
        print("salir")
        if self.main_window and self.main_window.window:
            self.main_window.window.quit()
        
    def show_about(self):
        print("Acerca del sistema...")
        
    # metodos para pruebas (solo muestran en consola lo que deben hacer)
    def add_client(self): print("Agregar cliente")
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
