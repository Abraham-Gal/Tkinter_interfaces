from cgi import test
import tkinter as tk
from tkinter import LEFT, Frame, Label, PhotoImage, ttk
from tkinter import Canvas
from Nodo1_Interfaz import *
from Nodo2_interfaz import *
from Conf_interfaz import *
from Info_interfaz import *
from Historial_interfaz import *
from Dicc_variables import *


class Inicio(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.config(width=1024, height=530,bg=Colores['fondo'])
        self.geometry(Size['pantalla'])
        self.title("Inicio")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/inicio_b.png'))  

        #-----------------------------------  Frames         ----------------------
        self.info_frame = Frame(self)
        self.info_frame.pack(side="left",pady="10",padx="10")
        self.info_frame.config(bg=Colores['blanco'],width="495", height="550",relief="flat", bd=3)

        self.nodo1_frame = Frame(self)
        self.nodo1_frame.pack(anchor="se", pady="10", padx="10")
        self.nodo1_frame.config(bg=Colores['fondo_n1'], width="510", height="247",relief="flat", bd=3)

        self.nodo2_frame = Frame(self)
        self.nodo2_frame.pack(anchor="sw", pady="10", padx="10")
        self.nodo2_frame.config(bg=Colores['fondo_n1'], width="510", height="247",relief="flat", bd=3)
        #--------------------------------------------------------------------------

        #------------------------------------ Recursos   ---------------------------
        self.png_agua=PhotoImage(file="Interface/agua_e.png")
        self.png_luz=PhotoImage(file="Interface/luz_e.png")
        self.png_conf=PhotoImage(file="Interface/btn_conf.png")
        self.png_his=PhotoImage(file="Interface/btn_his.png")
        self.png_inf=PhotoImage(file="Interface/btn_info.png")
        self.png_nodo=PhotoImage(file="Interface/btn_nodo.png")
        #---------------------------------------------------------------------------
        
        #------------------------------------ Canvas obj --------------------------
        canvas = Canvas(self.info_frame)
        canvas.config(bg="#FFFFFF",width="495", height="550")
        canvas.pack(side="left")

        canvas_n1 = Canvas(self.nodo1_frame)
        canvas_n1.config(bg=Colores['fondo_n1'],width="510", height="247")
        canvas_n1.pack(side="left")
        #--------------------------------------------------------------------------

        #----------------------------------- Objetos de info ----------------------
        #========> Agua
        self.img_agua = Label(self.info_frame, image=self.png_agua, relief="flat", border=0)
        self.img_agua.place(x=370, y=20)

        self.label_liquido = Label(self.info_frame, text="Liquido", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",24))
        self.label_liquido.place(x=30, y=20)

        self.label_estado = Label(self.info_frame, text="Estado:", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",14))
        self.label_estado.place(x=30, y=70)

        self.label_DatoL = Label(self.info_frame, text=Agua['estado'], relief="flat", border=0, bg="#FFFFFF", font=("Verdana",14))
        self.label_DatoL.place(x=105, y=70)

        canvas.create_rectangle(30,120,465,115, fill="#96E087", outline="#96E087")

        #========> Luz ambiental
        self.img_luz = Label(self.info_frame, image=self.png_luz, relief="flat", border=0)
        self.img_luz.place(x=370, y=175)
        
        self.label_lambiental = Label(self.info_frame, text="Luz ambiental", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",24))
        self.label_lambiental.place(x=30, y=155)

        self.label_laN1 = Label(self.info_frame, text="Nodo 1:", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",14))
        self.label_laN1.place(x=30, y=205)

        self.label_laN1D = Label(self.info_frame, text=getUlimoDLuz(1),relief="flat", border=0, bg="#FFFFFF", font=("Verdana",14))
        self.label_laN1D.place(x=120, y=205)
    
        self.label_laN2 = Label(self.info_frame, text="Nodo 2:", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",14))
        self.label_laN2.place(x=30, y=235)

        self.label_laN2D = Label(self.info_frame, text=getUlimoDLuz(2),relief="flat", border=0, bg="#FFFFFF", font=("Verdana",14))
        self.label_laN2D.place(x=120, y=235)

        canvas.create_rectangle(30,300,465,295, fill="#96E087", outline="#96E087")

        #========> Modo

        self.label_modo = Label(self.info_frame, text="Modo de operación:", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",16))
        self.label_modo.place(x=60, y=330)

        self.label_modo = Label(self.info_frame, text=getModoFuncion(), relief="flat", border=0, bg="#FFFFFF", font=("Verdana",16))
        self.label_modo.place(x=290, y=330)

        canvas.create_rectangle(30,400,465,395, fill="#96E087", outline="#96E087")

        #========> Botonera

        self.boton_Config = ttk.Button(self.info_frame, text="Configuracion", image=self.png_conf, compound=LEFT, command=self.abrir_Configuracion)
        self.boton_Config.place(x=30, y=425)

        self.boton_Info = ttk.Button(self.info_frame, text="Información", image=self.png_inf, compound=LEFT, command=self.abrir_info)
        self.boton_Info.place(x=190, y=425)

        self.boton_Historial = ttk.Button(self.info_frame, text="  Historial", image=self.png_his, compound=LEFT, command=self.abrir_Historial)
        self.boton_Historial.place(x=340,y=425)
        
        #-----------------------------------------------------------------------------
        
        #----------------------------------- Objetos de nodo1 ------------------------
        self.label_NP1 = Label(self.nodo1_frame, text="Nodo de producción 1", relief="flat", border=0, bg=Colores['fondo_n1'], font=("Verdana",15))
        self.label_NP1.place(x=125, y=10)

        canvas_n1.create_rectangle(30,50,445,45, fill="#96E087", outline="#96E087")

        self.boton_Nodo1 = tk.Button(self.nodo1_frame, text="  Nodo 1   ", image=self.png_nodo, compound=LEFT, command=self.abrir_Nodo1 , bg=Colores['btn_nodo'], activebackground=Colores['blanco'])
        self.boton_Nodo1.place(x=370, y=200)
        #----------------------------------------------------------------------------

        #----------------------------------- Objetos de nodo2 -----------------------
        self.boton_Nodo2 = ttk.Button(self.nodo2_frame, text="Nodo 2", command=self.abrir_Nodo2)
        self.boton_Nodo2.place(x=100, y=100)
        #-------------------------------------------------------------------------
        
    
    #--------------------------------------- metodos de accion -------------------------
    def abrir_Nodo1(self):
        self.ventana_Nodo1 = Nodo1()
    
    def abrir_Nodo2(self):
        self.ventana_Nodo2 = Nodo2()

    def abrir_Configuracion(self):
        self.ventana_Configuracion = Configuracion()
    
    def abrir_info(self):
        self.ventana_info = Informacion()
    
    def abrir_Historial(self):
        self.ventana_historial = Historial()
    #-----------------------------------------------------------------------------------

ventana_principal = Inicio()
ventana_principal.mainloop()