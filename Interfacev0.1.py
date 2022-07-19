import tkinter as tk 
from tkinter import ttk

class Aplication(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.etiqueta_inicial = ttk.Label(
            parent, 
            text="Prueba de ejecucion v0.1")
        self.etiqueta_inicial.place(x=20, y=20)

ventana = tk.Tk()
ventana.title("Interfaz v1")
ventana.config(width=1024,height=600)
app = Aplication(ventana)
ventana.mainloop()