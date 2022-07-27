import tkinter as tk
from tkinter import ttk

class Configuracion(tk.Toplevel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1024, height=600)
        self.title("Configuración de cultivos")

        self.boton_cerrar = ttk.Button(self, text="Inicio", command=self.destroy)
        self.boton_cerrar.place(x=75, y=75)
        
        self.focus()
        self.grab_set()