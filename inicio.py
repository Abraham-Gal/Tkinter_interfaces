import tkinter as tk
from tkinter import ttk 

ventana = tk.Tk()
ventana.title("Aca la primera muestra")
ventana.config(width=400, height=300)  

etiqueta_lectura = ttk.Label(text="Lectura nativa: ")
etiqueta_lectura.place(x=20, y=20)

caja_lectura = ttk.Entry()
caja_lectura.place(x=110, y=20, width=130)

ventana.mainloop()