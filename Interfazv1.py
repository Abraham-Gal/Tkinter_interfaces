import tkinter as tk
from tkinter import Frame, ttk
from tkinter import Canvas
from Nodo1_Interfaz import *
from Nodo2_interfaz import *
from Conf_interfaz import *


class Inicio(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.config(width=1024, height=600,bg='#FFFFFF')
        self.geometry("1024x530")
        self.title("Inicio")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/inicio_b.png'))
        
        

        #-----------------------------------  Fames         ----------------------
        self.info_frame = Frame(self)
        self.info_frame.pack(side="left",pady="10",padx="10")
        self.info_frame.config(bg="#FFFFFF",width="495", height="550",relief="solid", bd=3)

        self.nodo1_frame = Frame(self)
        self.nodo1_frame.pack(anchor="se", pady="10", padx="10")
        self.nodo1_frame.config(bg="#FFFFFF", width="510", height="247",relief="solid", bd=3)

        self.nodo2_frame = Frame(self)
        self.nodo2_frame.pack(anchor="sw", pady="10", padx="10")
        self.nodo2_frame.config(bg="#FFFFFF", width="510", height="247",relief="solid", bd=3)
        #--------------------------------------------------------------------------

        #------------------------------------ Canvas obj --------------------------
        canvas = Canvas(self.info_frame)
        canvas.config(bg="#FFFFFF",width="495", height="550")
        canvas.pack(side="left")
        #--------------------------------------------------------------------------

        #----------------------------------- Objetos de info ----------------------
        self.boton_Config = ttk.Button(self.info_frame, text="Configuracion", command=self.abrir_COnfiguracion)
        self.boton_Config.place(x=100, y=100)

        self.etiqueta_titulo1 = tk.Label(self.info_frame, text="Dispositivo de control inteligente para",bg="#FFFFFF", font=("Times", 20))
        self.etiqueta_titulo1.place(x=33,y=10)
        
        self.etiqueta_titulo2 = tk.Label(self.info_frame, text="microcultivos",bg="#FFFFFF", font=("Times", 20))
        self.etiqueta_titulo2.place(x=33,y=60)

        canvas.create_line(30,100,465,100)
        
        #-------------------------------------------------------------------------
        
        #----------------------------------- Objetos de nodo1 ----------------------
        self.boton_Nodo1 = ttk.Button(self.nodo1_frame, text="Nodo 1", command=self.abrir_Nodo1)
        self.boton_Nodo1.place(x=100, y=100)
        #-------------------------------------------------------------------------

        #----------------------------------- Objetos de nodo2 ----------------------
        self.boton_Nodo2 = ttk.Button(self.nodo2_frame, text="Nodo 2", command=self.abrir_Nodo2)
        self.boton_Nodo2.place(x=100, y=100)
        #-------------------------------------------------------------------------
        
    
    def abrir_Nodo1(self):
        self.ventana_Nodo1 = Nodo1()
    
    def abrir_Nodo2(self):
        self.ventana_Nodo2 = Nodo2()

    def abrir_COnfiguracion(self):
        self.ventana_Configuracion = Configuracion()


ventana_principal = Inicio()
ventana_principal.mainloop()