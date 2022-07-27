import tkinter as tk
from tkinter import ttk
from Nodo1_Interfaz import *
from Nodo2_interfaz import *
from Conf_interfaz import *


class Inicio(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.config(width=1024, height=600)
        self.title("Inicio")

        self.boton_Nodo1 = ttk.Button(self, text="Nodo 1", command=self.abrir_Nodo1)
        self.boton_Nodo1.place(x=100, y=100)

        self.boton_Nodo2 = ttk.Button(self, text="Nodo 2", command=self.abrir_Nodo2)
        self.boton_Nodo2.place(x=100, y=150)
        
        self.boton_Config = ttk.Button(self, text="Configuracion", command=self.abrir_COnfiguracion)
        self.boton_Config.place(x=100, y=200)
    
    def abrir_Nodo1(self):
        self.ventana_Nodo1 = Nodo1()
    
    def abrir_Nodo2(self):
        self.ventana_Nodo2 = Nodo2()

    def abrir_COnfiguracion(self):
        self.ventana_Configuracion = Configuracion()


ventana_principal = Inicio()
ventana_principal.mainloop()