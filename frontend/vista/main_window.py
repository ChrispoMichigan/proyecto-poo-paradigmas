import tkinter as tk
from tkinter import ttk

from models.customers import ModelCustomers
from models.items import ModelItems
from models.invoices import ModelInvoices

class MainWindow:
    def __init__(self, controller):
        self.controller = controller
        self.window = None
        self.notebook = None
        self.user_id: int = 0
        
    def show(self):
        #Muestra la ventana principal
        self.window = tk.Tk()
        self.window.title("Sistema de Facturacion")
        self.window.geometry("1000x700")
        
        self._create_menu()
        self._create_widgets()
        self.load_clients_to_table(self.user_id)
        self.load_articles_to_table(self.user_id)
        self.load_articles_to_combobox()
        self.load_clients_to_combobox()
        return self.window
        
    def _create_menu(self):
        #Crea la barra de menu
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
    def _create_widgets(self):
        #creacion de widgets
        # Frame principal
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Crear las pestañas
        self._create_client_tab()
        self._create_articles_tab()
        self._create_invoices_tab()
        
    def _create_client_tab(self):
        #pestaña de clientes
        client_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(client_frame, text="Clientes")
        
        # seccion de formulario
        form_frame = ttk.LabelFrame(client_frame, text="Registrar Cliente", padding=10)
        form_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Grid para formulario
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        self.client_name_entry = ttk.Entry(form_frame, width=20)
        self.client_name_entry.grid(row=0, column=1, padx=(0, 15), pady=5, sticky=tk.EW)
        
        ttk.Label(form_frame, text="Apellidos:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5), pady=5)
        self.client_lastname_entry = ttk.Entry(form_frame, width=20)
        self.client_lastname_entry.grid(row=0, column=3, padx=(0, 15), pady=5, sticky=tk.EW)
        
        ttk.Label(form_frame, text="DNI:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        self.client_dni_entry = ttk.Entry(form_frame, width=20)
        self.client_dni_entry.grid(row=1, column=1, padx=(0, 15), pady=5, sticky=tk.EW)
        
        # Botones del formulario
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=tk.E)
        
        self.add_client_button = ttk.Button(button_frame, text="Agregar Cliente",command=self.controller.add_client)
        self.add_client_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.clear_client_button = ttk.Button(button_frame,text="Limpiar",command=self.clear_client_form)
        self.clear_client_button.pack(side=tk.LEFT)
        
        # Frame de la tabla
        table_frame = ttk.LabelFrame(client_frame, text="Lista de Clientes", padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview para clientes
        columns = ("ID", "Nombre", "Apellidos", "DNI")
        self.clients_tree = ttk.Treeview(table_frame, columns=columns,show="headings")
        
        # Configurar columnas
        self.clients_tree.heading("ID", text="ID")
        self.clients_tree.heading("Nombre", text="Nombre")
        self.clients_tree.heading("Apellidos", text="Apellidos")
        self.clients_tree.heading("DNI", text="DNI")
        self.clients_tree.column("ID", width=50)
        self.clients_tree.column("Nombre", width=150)
        self.clients_tree.column("Apellidos", width=150)
        self.clients_tree.column("DNI", width=100)
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.clients_tree.yview)
        self.clients_tree.configure(yscrollcommand=scrollbar.set)
        
        self.clients_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Frame de botones 
        action_frame = ttk.Frame(client_frame)
        action_frame.pack(fill=tk.X, pady=(10, 0))
        
        #llamada borrar cliente
        self.delete_client_button = ttk.Button(action_frame,text="Eliminar Cliente Seleccionado",command=self.controller.delete_client)
        self.delete_client_button.pack(side=tk.LEFT)
        #!Borrar consultar cliente si no hace nada
        #self.view_client_button = ttk.Button(action_frame,text="Consultar Cliente",command=self.controller.view_client)
        #self.view_client_button.pack(side=tk.LEFT, padx=(10, 0))
        
    
    def clear_clients_table(self):
        """Limpia todas las filas de la tabla de clientes"""
        for item in self.clients_tree.get_children():
            self.clients_tree.delete(item)

    def load_clients_to_table(self, clients_list):
        """Carga una lista de clientes en la tabla"""
        # Limpiar tabla primero
        self.clear_clients_table()
        #print(self.user_id)
        data = ModelCustomers.get_all(self.user_id)
        if not data['status']:
            #! Aqui hacer algo en caso de error
            print('Error')
            print(data['mensaje'])
            return
        #print(data['data'])

        # Agregar cada cliente
        for client in data['data']:
            self.clients_tree.insert("", "end", values=(
                client['id'],
                client['first_name'],
                client['last_name'], 
                client['dni']
            ))

    def _create_articles_tab(self):
        #pestaña de articulos
        articles_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(articles_frame, text="Articulos")
        
        # Frame para tipo de articulo
        type_frame = ttk.LabelFrame(articles_frame, text="Tipo de Articulo", padding=10)
        type_frame.pack(fill=tk.X, pady=(0, 10))
        
        #elegir entre fisico y digital
        self.article_type = tk.StringVar(value="fisico")
        #fisico
        ttk.Radiobutton(type_frame, text="Articulo Fisico", variable=self.article_type, value="fisico",command=self._toggle_article_fields).pack(side=tk.LEFT, padx=(0, 20))
        #digital
        ttk.Radiobutton(type_frame, text="Articulo Digital", variable=self.article_type, value="digital",command=self._toggle_article_fields).pack(side=tk.LEFT)
        
        # Frame del formulario
        form_frame = ttk.LabelFrame(articles_frame, text="Registrar Articulo", padding=10)
        form_frame.pack(fill=tk.X, pady=(0, 10))
        
        # tomar datos de los articulos
        ttk.Label(form_frame, text="Codigo:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        self.article_code_entry = ttk.Entry(form_frame, width=20)
        self.article_code_entry.grid(row=0, column=1, padx=(0, 15), pady=5, sticky=tk.EW)
        
        ttk.Label(form_frame, text="Denominacion:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5), pady=5)
        self.article_name_entry = ttk.Entry(form_frame, width=20)
        self.article_name_entry.grid(row=0, column=3, padx=(0, 15), pady=5, sticky=tk.EW)
        
        ttk.Label(form_frame, text="Precio:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        self.article_price_entry = ttk.Entry(form_frame, width=20)
        self.article_price_entry.grid(row=1, column=1, padx=(0, 15), pady=5, sticky=tk.EW)
        """
        como nota por ahora los atributos de peso son solo para fisicos
        mientras que licencias es solo para digitales 
        """
        
        self.weight_frame = ttk.Frame(form_frame)
        self.weight_frame.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(self.weight_frame, text="Peso (kg):").pack(side=tk.LEFT, padx=(0, 5))
        self.article_weight_entry = ttk.Entry(self.weight_frame, width=15)
        self.article_weight_entry.pack(side=tk.LEFT)
        
        self.license_frame = ttk.Frame(form_frame)
        self.license_frame.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(self.license_frame, text="Licencia:").pack(side=tk.LEFT, padx=(0, 5))
        self.article_license_entry = ttk.Entry(self.license_frame, width=15)
        self.article_license_entry.pack(side=tk.LEFT)
        
        # Botones del formulario
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        #llamada a funcion de añadir articulo
        self.add_article_button = ttk.Button(button_frame,text="Agregar Articulo",command=self.controller.add_article)
        self.add_article_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.clear_article_button = ttk.Button(button_frame,text="Limpiar",command=self.clear_article_form)
        self.clear_article_button.pack(side=tk.LEFT)
        
        # Frame de la tabla
        table_frame = ttk.LabelFrame(articles_frame, text="Lista de Articulos", padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview para articulos
        columns = ("ID", "Codigo", "Denominacion", "Precio", "Tipo", "Detalle")
        self.articles_tree = ttk.Treeview(table_frame,columns=columns,show="headings")
        
        # Configurar columnas
        for col in columns:
            self.articles_tree.heading(col, text=col)
            self.articles_tree.column(col, width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.articles_tree.yview)
        self.articles_tree.configure(yscrollcommand=scrollbar.set)
        
        self.articles_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Mostrar campos iniciales
        self._toggle_article_fields()

    def clear_articles_table(self):
        """Limpia todas las filas de la tabla de clientes"""
        for item in self.articles_tree.get_children():
            self.articles_tree.delete(item)

    def load_articles_to_table(self, articles_list):
        """Carga una lista de clientes en la tabla"""
        # Limpiar tabla primero
        self.clear_articles_table()
        #print(self.user_id)
        data = ModelItems.get_all(self.user_id)
        if not data['status']:
            #! Aqui hacer algo en caso de error
            print('Error')
            print(data['mensaje'])
            return
        #print(data['data'])

        # Agregar cada articulo
        for article in data['data']:
            if article['type'] == 'fisico':
                details = ("Peso:",article['weight'])  # Si es fisico, mostrar el peso
            elif article['type'] == 'digital':
                details = ("licencia:",article['license'])  # Si es digital, mostrar la licencia
            else:
                details = 'N/A'  # Si no es ni fisico ni digital, dejar un valor por defecto

            self.articles_tree.insert("", "end", values=(
                article['id'],
                article['code'],
                article['denomination'], 
                article['price'],
                article['type'],
                details     
            ))

    def load_invoices_to_table(self):
        """Cargar facturas del usuario actual a la tabla"""
        try:
            # Limpiar tabla actual
            for item in self.lines_tree.get_children():
                self.lines_tree.delete(item)
            
            # Obtener facturas del backend
            data = ModelInvoices.get_all(self.user_id)
            
            if not data['status']:
                print(f"Error al cargar facturas: {data.get('mensaje', 'Error desconocido')}")
                return
            
            total_general = 0.0
            
            # Agregar cada factura a la tabla
            for invoice in data['data']:
                # Extraer información del cliente (primer elemento de la lista)
                customer_name = f"{invoice['customer'][0]['first_name']} {invoice['customer'][0]['last_name']}"
                
                # Extraer información del item (primer elemento de la lista)
                item_info = invoice['item'][0]
                item_name = item_info['denomination']
                item_price = float(item_info['price']) if item_info['price'] else 0.0
                
                # Calcular subtotal
                subtotal = item_price * invoice['amount']
                total_general += subtotal
                
                # Insertar fila en la tabla
                self.lines_tree.insert("", "end", values=(
                    invoice['id'],
                    f"{customer_name} - {item_name}",
                    invoice['amount'],
                    f"${item_price:.2f}",
                    f"${subtotal:.2f}"
                ))
            
            # Actualizar total
            self.total_label.config(text=f"${total_general:.2f}")
            
        except Exception as e:
            print(f"Error al cargar facturas: {str(e)}")

    def _create_invoices_tab(self):
        #pestaña de facturacion
        invoices_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(invoices_frame, text="Facturacion")
        
        # Frame superior (seleccion de cliente)
        client_frame = ttk.LabelFrame(invoices_frame, text="Seleccionar Cliente", padding=10)
        client_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(client_frame, text="Cliente:").pack(side=tk.LEFT, padx=(0, 10))
        #combo box donde van los clientes
        self.invoice_client_combo = ttk.Combobox(client_frame, width=40, state="readonly")
        self.invoice_client_combo.pack(side=tk.LEFT, padx=(0, 10))
        
        #llamada a funcion de crear factura
        self.new_invoice_button = ttk.Button(client_frame,text="Nueva Factura",command=self.controller.create_invoice)
        self.new_invoice_button.pack(side=tk.LEFT)
        
        # Frame para agregar lineas
        line_frame = ttk.LabelFrame(invoices_frame, text="Agregar Linea a Factura", padding=10)
        line_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(line_frame, text="Articulo:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        #combobox que lee los articulos guardados
        self.line_article_combo = ttk.Combobox(line_frame, width=30, state="readonly")
        self.line_article_combo.grid(row=0, column=1, padx=(0, 15), pady=5, sticky=tk.EW)
        
        ttk.Label(line_frame, text="Cantidad:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5), pady=5)
        self.line_quantity_entry = ttk.Entry(line_frame, width=10)
        self.line_quantity_entry.grid(row=0, column=3, padx=(0, 15), pady=5)
        
        # Frame de lineas de factura
        lines_frame = ttk.LabelFrame(invoices_frame, text="Lineas de Factura", padding=10)
        lines_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Treeview para lineas
        columns = ("ID", "Articulo", "Cantidad", "Precio Unit.", "Subtotal")
        self.lines_tree = ttk.Treeview(lines_frame,columns=columns,show="headings")
        
        for col in columns:
            self.lines_tree.heading(col, text=col)
            self.lines_tree.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(lines_frame, orient=tk.VERTICAL, command=self.lines_tree.yview)
        self.lines_tree.configure(yscrollcommand=scrollbar.set)
        
        self.lines_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Frame de totales y acciones
        total_frame = ttk.Frame(invoices_frame)
        total_frame.pack(fill=tk.X)
        
        # Total
        ttk.Label(total_frame, text="TOTAL:", font=("Helvetica", 12, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        self.total_label = ttk.Label(total_frame, text="$0.00", font=("Helvetica", 12, "bold"))
        self.total_label.pack(side=tk.LEFT, padx=(0, 20))
        
        # Botones de accion
        #llamada para borrar una linea de la factura
        self.delete_line_button = ttk.Button(
            total_frame,
            text="Eliminar Linea",
            command=self.controller.delete_invoice_line
        )
        self.delete_line_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # llamada para exportar el json
        self.export_json_button = ttk.Button(
            total_frame,
            text="Exportar JSON",
            command=lambda: self.controller.export_invoice('json')
        )
        self.export_json_button.pack(side=tk.LEFT, padx=(0, 5))
         # llamada para exportar el csv
        self.export_csv_button = ttk.Button(
            total_frame,
            text="Exportar CSV",
            command=lambda: self.controller.export_invoice('csv')
        )
        self.export_csv_button.pack(side=tk.LEFT)

        # Cargar facturas al inicio
        self.load_invoices_to_table()


    def load_clients_to_combobox(self):
        #cargar los clientes a la combobox
        clients_data = ModelCustomers.get_all(self.user_id)
        if not clients_data['status']:
            print('Error al cargar los clientes')
            print(clients_data['mensaje'])
            return

        # Limpiar la ComboBox antes de llenarla
        self.invoice_client_combo.set('')  # Resetear el valor seleccionado
        self.invoice_client_combo['values'] = []  # Limpiar los valores actuales

        # Crear una lista de tuplas (ID, Nombre Completo)
        clients = [(client['id'], f"{client['first_name']} {client['last_name']}") for client in clients_data['data']]
        
        # Establecer los valores en la ComboBox (solo nombres para el usuario )
        self.invoice_client_combo['values'] = [client[1] for client in clients]
        
       
        if clients:
            self.invoice_client_combo.set(clients[0][1])  # primer cliente por defecto

        # Guardar la lista completa de clientes para poder obtener el id despues
        self.clients_list = clients

    def load_articles_to_combobox(self):
        #cargar articulos a la combobox
        articles_data = ModelItems.get_all(self.user_id)
        if not articles_data['status']:
            print('Error al cargar los artículos')
            print(articles_data['mensaje'])
            return

        # Limpiar la ComboBox antes de llenarla
        self.line_article_combo.set('')  # Resetear el valor seleccionado
        self.line_article_combo['values'] = []  # Limpiar los valores actuales

        # Crear una lista de tuplas (ID, Denominacion y  Codigo)
        articles = [(article['id'], f"{article['denomination']} ({article['code']})") for article in articles_data['data']]
        
        # Establecer los valores en la ComboBox (solo nombres para el usuario )
        self.line_article_combo['values'] = [article[1] for article in articles]
        
        if articles:
            self.line_article_combo.set(articles[0][1])  # primer articulo por defecto

        # Guardar la lista completa de articulos para poder acceder al id
        self.articles_list = articles


    def get_selected_client_id(self):
        #saca el id del cliente de la combobox en facturas
        selected_client_name = self.invoice_client_combo.get()
        # Buscar el ID correspondiente en la lista de clientes
        selected_client = next((client for client in self.clients_list if client[1] == selected_client_name), None)
        return selected_client[0] if selected_client else None
    def get_selected_article_id(self):
    #Sacar el id del articulo en la combobox de facturas
        selected_article_name = self.line_article_combo.get()
        # Buscar el ID correspondiente en la lista de artículos
        selected_article = next((article for article in self.articles_list if article[1] == selected_article_name), None)
        return selected_article[0] if selected_article else None


    """seccion de funciones que usa el frontend waos"""   
    def _toggle_article_fields(self):
        #esta es la cosa que muestra cosas distintas si es fisico o digital
        article_type = self.article_type.get()
        
        if article_type == "fisico":
            self.weight_frame.grid()
            self.license_frame.grid_remove()
        else:
            self.weight_frame.grid_remove()
            self.license_frame.grid()
            
    def clear_client_form(self):
        #limpiar el formulario de clientes
        self.client_name_entry.delete(0, tk.END)
        self.client_lastname_entry.delete(0, tk.END)
        self.client_dni_entry.delete(0, tk.END)
        
    def clear_article_form(self):
        #limpiar el formulario de articulos
        self.article_code_entry.delete(0, tk.END)
        self.article_name_entry.delete(0, tk.END)
        self.article_price_entry.delete(0, tk.END)
        self.article_weight_entry.delete(0, tk.END)
        self.article_license_entry.delete(0, tk.END)
        
    def get_client_data(self):
        #obtener datos del cliente (los que escribio el usuario)
        return {
            'nombre': self.client_name_entry.get(),
            'apellidos': self.client_lastname_entry.get(),
            'dni': self.client_dni_entry.get()
        }
        
    def get_article_data(self):
        #obtener datos del formulario de articulos (los que escribio el usuario)
        if self.article_type.get() == "fisico":
            distiction=self.article_weight_entry.get()
        else:
            distiction=self.article_license_entry.get()
        return [
            self.article_type.get(),
            self.article_code_entry.get(),
            self.article_name_entry.get(),
            self.article_price_entry.get(),
            distiction
        ]
        
    def get_invoice_data(self):
        #obtiene los datos para crear una factura
        client_id = self.get_selected_client_id()  # Obtén el ID del cliente seleccionado
        article_id = self.get_selected_article_id()  # Obtén el ID del artículo seleccionado
        quantity = self.line_quantity_entry.get()  # Obtén la cantidad del artículo ingresada

        # Devuelve todos los datos de la factura 
        return {
            'client_id': client_id,
            'article_id': article_id,
            'quantity': quantity
        }
    
    def get_invoice_select(self):
        """Obtiene el ID de la factura seleccionada en la tabla de facturas"""
        selected_items = self.lines_tree.selection()
        
        if selected_items:
            # Obtener el primer item seleccionado
            selected_item = selected_items[0]
            # Obtener los valores de la fila seleccionada
            invoice_data = self.lines_tree.item(selected_item, 'values')
            # El ID está en la primera columna (índice 0)
            return int(invoice_data[0]) if invoice_data else None
        else:
            print("No hay factura seleccionada")
            return None
    
    def get_selected_client_from_table(self):
        """Obtiene el ID del cliente seleccionado en la tabla de clientes"""
        selected_items = self.clients_tree.selection()
        
        if selected_items:
            # Obtener el primer item seleccionado
            selected_item = selected_items[0]
            # Obtener los valores de la fila seleccionada
            client_data = self.clients_tree.item(selected_item, 'values')
            # El ID está en la primera columna (índice 0)
            return int(client_data[0]) if client_data else None
        else:
            print("No hay cliente seleccionado")
            return None
            
    def update_total(self, total: float):
        #actualiza el total
        self.total_label.config(text=f"${total:.2f}")