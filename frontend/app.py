import tkinter as tk
from vista.login_window import LoginWindow
from vista.main_window import MainWindow

from models.users import ModelUsers
from models.schemas.customers import CustomerCreate
from models.customers import ModelCustomers
from models.items import ModelItems
from models.schemas.items import ItemCreate
from models.schemas.items import ItemType
from models.schemas.invoices import InvoiceCreate
from models.invoices import ModelInvoices
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


    def delete_client(self): 
        """Elimina el cliente seleccionado en la tabla"""
        # Obtener el ID del cliente seleccionado
        client_id = self.main_window.get_selected_client_from_table()
        
        if client_id is None:
            print("No hay cliente seleccionado para eliminar")
            return
        
        try:
            # Llamar al modelo para eliminar el cliente
            result = ModelCustomers.delete_by_id(client_id)
            
            if result['status']:
                print(f"Cliente eliminado exitosamente: {result}")
                # Recargar la tabla de clientes para mostrar los cambios
                self.main_window.load_clients_to_table(self.user_id)
                # Recargar también el combobox de clientes en facturación
                self.main_window.load_clients_to_combobox()
            else:
                print(f"Error al eliminar cliente: {result['mensaje']}")
                
        except Exception as e:
            print(f"Error al eliminar cliente: {str(e)}") 


    def view_client(self): 
        print("Ver cliente")

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

           

    def create_invoice(self): 
        print("Crear factura")
        datosFactura=[self.main_window.get_invoice_data()]
        print(datosFactura)
        print(self.user_id)
        """
        #?datosFactura recibe una lista con un diccionario 
        tiene los datos de 'client_id', 'article_id' y 'quantity'
        creo que solo necesitas el id cliente para la funcion de create invoice
        mientras que add_invoice necesitaria el id del articulo, la cantidad y la seleccion

        """
        factura = InvoiceCreate(user_id=self.user_id, customer_id=datosFactura[0]['client_id'], item_id=datosFactura[0]['article_id'], amount=int(datosFactura[0]['quantity']))

        factura_creada = ModelInvoices.create(factura)

        if not factura_creada['status']:
            print(f'Error: {factura_creada['mensaje']}')
            return

        print(factura_creada)
        
        # Recargar la tabla de facturas después de crear una nueva factura
        self.main_window.load_invoices_to_table()

    def add_invoice_line(self): 
        print("Agregar línea")
        datosFactura=[self.main_window.get_invoice_data()]
        #usarias esto para obtener la seleccion de factura
        #seleccion=self.main_window.get_invoice_select
        
        """
        me acabo de dar cuenta que no entiendo que pide el documento
        exactamente con nueva factura y nueva linea
        """
    def delete_invoice_line(self): 
        """Elimina la factura seleccionada en la tabla"""
        # Obtener el ID de la factura seleccionada
        invoice_id = self.main_window.get_invoice_select()
        
        if invoice_id is None:
            print("No hay factura seleccionada para eliminar")
            return
        
        try:
            # Llamar al modelo para eliminar la factura
            result = ModelInvoices.delete_by_id(invoice_id)
            
            if result['status']:
                print(f"Factura eliminada exitosamente: {result}")
                # Recargar la tabla de facturas para mostrar los cambios
                self.main_window.load_invoices_to_table()
            else:
                print(f"Error al eliminar factura: {result.get('mensaje', 'Error desconocido')}")
                
        except Exception as e:
            print(f"Error al eliminar factura: {str(e)}")

    def export_invoice(self, format): 
        print(f"Exportar {format}")


controller = Controller()
login_window = LoginWindow(controller)
controller.login_window = login_window
window = login_window.show()
window.mainloop()
