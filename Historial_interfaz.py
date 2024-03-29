import tkinter as tk
from tkinter import ttk
from Dicc_variables import *

class Historial(tk.Toplevel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1024, height=570)
        self.geometry(Size['pantalla'])
        self.title("Historial")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/historial.png'))

        self.boton_cerrar = ttk.Button(self, text="Inicio", command=self.destroy)
        self.boton_cerrar.place(x=75, y=75)
        
        self.focus()
        self.grab_set()