import tkinter as tk 
from tkinter import Frame, ttk
from tkinter.tix import NoteBook
from turtle import width

class InicioFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Prueba de etiqueta en inicio")
        self.label.pack()
    
class Nodo1Frame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Prueba de etiqueta en nodo 1")
        self.label.pack()

class Nodo2Frame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Prueba de etiqueta en nodo 2")
        self.label.pack()


class Aplication(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Interfaz v1")
        #parent.config(width=1024,height=600)
        parent.geometry("1024x600")
        parent.tk.call('wm','iconphoto',ventana._w,tk.PhotoImage(file='Interface/icon_p.png'))

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        #self.FrameInicio = Frame(self.notebook, width=1024, height=550)
        #self.FrameInicio.pack(fill='both', expand=True)
        
        self.inicioframe = InicioFrame(self.notebook, width=1024, height=550)
        self.inicioframe.pack(fill='both', expand=True)
        
        self.nodo1frame = Nodo1Frame(self.notebook)
        self.nodo1frame.pack(fill='both', expand=True)
        
        self.nodo2frame = Nodo2Frame(self.notebook)
        self.nodo2frame.pack(fill='both', expand=True)


        self.notebook.add(self.inicioframe, text="Inicio", padding=10)
        self.notebook.add(self.nodo1frame, text="Nodo 1", padding=10)
        self.notebook.add(self.nodo2frame, text="Nodo 2", padding=10)
        
        self.pack()



ventana = tk.Tk()
#ventana.config(width=1024,height=600)
#ventana.tk.call('wm','iconphoto',ventana._w,tk.PhotoImage(file='Interface/icon_p.png'))
app = Aplication(ventana)
ventana.mainloop()

