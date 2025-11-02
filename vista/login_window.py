import tkinter as tk
from tkinter import ttk

class LoginWindow:
    def __init__(self, controller):
        self.controller = controller
        self.window = None
        
    def show(self):
        """Muestra la ventana de login"""
        self.window = tk.Tk()
        self.window.title("Sistema de Facturación - Login")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        # Centrar la ventana
        self._center_window()
        
        self._create_widgets()
        return self.window
    
    def _center_window(self):
        """Centra la ventana en la pantalla"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
    def _create_widgets(self):
        """Crea los widgets de la ventana de login"""
        # Frame principal
        main_frame = ttk.Frame(self.window, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="SISTEMA DE FACTURACIÓN",
            font=("Helvetica", 16, "bold"),
            foreground="#2c3e50"  # Color azul oscuro
        )
        title_label.pack(pady=(0, 30))
        
        # Frame del formulario
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Campo de usuario
        ttk.Label(form_frame, text="Usuario:", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        self.username_entry = ttk.Entry(form_frame, width=30, font=("Helvetica", 10))
        self.username_entry.pack(fill=tk.X, pady=(0, 15))
        self.username_entry.focus()
        
        # Campo de contraseña
        ttk.Label(form_frame, text="Contraseña:", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        self.password_entry = ttk.Entry(form_frame, width=30, show="•", font=("Helvetica", 10))
        self.password_entry.pack(fill=tk.X, pady=(0, 20))
        
        # Botón de login
        self.login_button = ttk.Button(
            form_frame,
            text="Iniciar Sesión",
            command=self._on_login,
            width=20
        )
        self.login_button.pack(pady=10)
        
        # Enlace para enter en los campos
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda e: self._on_login())
        
    def _on_login(self):
        """Maneja el evento de login"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.login(username, password)
        
    def close(self):
        """Cierra la ventana de login"""
        if self.window:
            self.window.destroy()