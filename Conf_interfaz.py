import tkinter as tk
from tkinter import ttk
from Dicc_variables import *

class Configuracion(tk.Toplevel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(bg=Colores['blanco'])
        self.geometry(Size['pantalla'])
        self.title("Configuración de cultivos")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/conf.png'))

        self.boton_cerrar = ttk.Button(self, text="Inicio", command=self.destroy)
        self.boton_cerrar.place(x=75, y=75)
        
        self.focus()
        self.grab_set()