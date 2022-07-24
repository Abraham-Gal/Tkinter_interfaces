import tkinter as tk 
from tkinter import Frame, ttk
from turtle import width

class Aplication(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Interfaz v1")
        #parent.config(width=1024,height=600)
        parent.geometry("1024x600")
        parent.tk.call('wm','iconphoto',ventana._w,tk.PhotoImage(file='Interface/icon_p.png'))

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = Frame(self.notebook, width=1024, height=550)
        self.frame2 = Frame(self.notebook, width=1024, height=550)
        self.frame3 = Frame(self.notebook, width=1024, height=550)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame3.pack(fill='both', expand=True)
        

        #self.home_label = ttk.Label(self.notebook, text="Ventana de inicio man")
        #self.nodo1_label = ttk.Label(self.notebook, text="Ventana de Nodo 1 man")
        #self.nodo2_label = ttk.Label(self.notebook, text="Ventana de Nodo 2 man")

        self.notebook.add(self.frame1, text="Inicio", padding=10)
        self.notebook.add(self.frame2, text="Nodo 1", padding=10)
        self.notebook.add(self.frame3, text="Nodo 2", padding=10)
        
        self.pack()



ventana = tk.Tk()
#ventana.config(width=1024,height=600)
#ventana.tk.call('wm','iconphoto',ventana._w,tk.PhotoImage(file='Interface/icon_p.png'))
app = Aplication(ventana)
ventana.mainloop()

