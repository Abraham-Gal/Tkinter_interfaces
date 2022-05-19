import tkinter as tk
from tkinter import ttk 

def calcular_diferencia():
    lectura = float(caja_lectura.get())
    diferencia = lectura - 776.55
    lectura_nativa = 152.75

    etiqueta_diferencia.config(text=f"Diferencia de lectura: {diferencia}")
    etiqueta_lectura_nativa.config(text=f"porcentaje de erro: {lectura_nativa}")


ventana = tk.Tk()
ventana.title("Aca la primera muestra")
ventana.config(width=400, height=300)  

etiqueta_lectura = ttk.Label(text="Lectura nativa: ")
etiqueta_lectura.place(x=20, y=20)

caja_lectura = ttk.Entry()
caja_lectura.place(x=110, y=20, width=130)

boton_lectura = ttk.Button(text="Calculo", command=calcular_diferencia)
boton_lectura.place(x=20, y=60)

etiqueta_diferencia = ttk.Label(text="Diferencia de lectura: n/a")
etiqueta_diferencia.place(x=20, y=100)

etiqueta_lectura_nativa = ttk.Label(text="porcentaje de erro: n/a")
etiqueta_lectura_nativa.place(x=20, y=140)

ventana.mainloop()