from lib2to3.pgen2.token import OP
import tkinter as tk
from tkinter import Label, ttk, Frame, PhotoImage, LEFT
from tkinter import Canvas
from turtle import title
from GraficaN1 import *
from DataN1 import *
from Conf_n1 import *
from Dicc_variables import *

class Nodo1(tk.Toplevel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1024, height=530,bg=Colores['fondo'])
        self.geometry("1024x530")
        self.title("Nodo de producción 1")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/n1_2.png'))

        #------------------------------------ Recursos ----------------------------
        self.png_inicio=PhotoImage(file="Interface/btn_inicio.png")
        self.png_refresh=PhotoImage(file="Interface/btn_ref.png")
        #--------------------------------------------------------------------------

        #------------------------------------ Frames-------------------------------
        self.izq = Frame(self)
        self.izq.pack(side="left",pady="10",padx="10")
        self.izq.config(bg=Colores['blanco'],width="350", height="510",relief="flat", bd=3)

        self.supder = Frame(self)
        self.supder.pack(anchor="nw",padx="10", pady="10")
        self.supder.config(bg=Colores['blanco'],width="650",height="150", relief="flat", bd=3)

        self.medder = Frame(self)
        self.medder.pack(anchor="w",padx="10", pady="10")
        self.medder.config(bg=Colores['blanco'],width="650",height="150", relief="flat", bd=3)

        self.infder = Frame(self)
        self.infder.pack(anchor="s",padx="10", pady="10")
        self.infder.config(bg=Colores['blanco'],width="650",height="150", relief="flat", bd=3)
        #--------------------------------------------------------------------------

        #------------------------------------ Canvas obj --------------------------
        self.canvasData = Canvas(self.izq)
        self.canvasData.config(bg=Colores['blanco'],width="350", height="510")
        self.canvasData.pack(anchor="w")

        self.canvasG1 = Canvas(self.supder)
        self.canvasG1.config(bg=Colores['blanco'],width="650", height="150")
        self.canvasG1.pack(anchor="ne")
        #--------------------------------------------------------------------------
        
        #-----------------------  Configuraciones de gráfica----------------------
        
        self.label_Graf = Label(self.canvasG1, text="Configuración de gráfica", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",14))
        self.label_Graf.place(x=30, y=5)

        self.canvasG1.create_rectangle(0,40,650,42, fill="#96E087", outline="#96E087")

        self.label_datag =Label(self.canvasG1, text="Dato a graficar: ", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",10))
        self.label_datag.place(x=10, y=50)

        self.combo = ttk.Combobox(self.canvasG1, state="readonly", values=Op_graficas)
        self.combo.place(x=10, y=70)
        self.combo.set(Op_graficas[0])
        self.combo.bind("<<ComboboxSelected>>",self.set_Graf_N1)

        self.label_intg =Label(self.canvasG1, text="Intervalo a graficar: ", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",10))
        self.label_intg.place(x=10, y=100)

        self.combo2 = ttk.Combobox(self.canvasG1, state="readonly", values=Intervalo_g)
        self.combo2.place(x=10, y=120)
        self.combo2.set(Intervalo_g[0])
        self.combo2.bind("<<ComboboxSelected>>",self.set_Graf_int_N1)

        self.btn_vg = ttk.Button(self.canvasG1, text="Grafica", command=self.abrir_grafica)
        self.btn_vg.place(x=200, y=100)

        self.canvasG1.create_rectangle(320,0,330,170, fill="#96E087", outline="#96E087")
        
        #--------------------------------------------------------------------------

        #---------------------- Configuración de datos -----------------------------------

        self.label_Data = Label(self.canvasG1, text="Configuración de datos", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",14))
        self.label_Data.place(x=360, y=5)

        self.label_dataD =Label(self.canvasG1, text="Grupo de datos: ", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",10))
        self.label_dataD.place(x=350, y=50)

        self.combo3 = ttk.Combobox(self.canvasG1, state="readonly", values=Op_graficas)
        self.combo3.place(x=350, y=70)
        self.combo3.set(Op_graficas[0])
        #self.combo3.bind("<<ComboboxSelected>>",self.set_Graf_N1)
        
        self.label_ind =Label(self.canvasG1, text="Intervalo de datos: ", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",10))
        self.label_ind.place(x=350, y=100)

        self.combo4 = ttk.Combobox(self.canvasG1, state="readonly", values=Intervalo_g)
        self.combo4.place(x=350, y=120)
        self.combo4.set(Intervalo_g[0])
        #self.combo4.bind("<<ComboboxSelected>>",self.set_Graf_N1)

        self.btn_vd = ttk.Button(self.canvasG1, text="Datos", command=self.abrir_datos)
        self.btn_vd.place(x=525, y=100)
        
        #--------------------------------------------------------------------------
        

        #----------------------- Ultimas lecturas ---------------------------------
        self.label_ultdat = Label(self.canvasData, text="Ultimas lecturas", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",19))
        self.label_ultdat.place(x=70, y=5)

        self.canvasData.create_rectangle(20,40,310,42, fill="#96E087", outline="#96E087")

        self.label_ultdath = Label(self.canvasData, text="Humedad ambiental:    "+ Nodo1_LD['ha'] + "%", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdath.place(x=10, y=70)

        self.canvasData.create_rectangle(0,100,350,102, fill="#96E087", outline="#96E087")

        self.label_ultdathcg = Label(self.canvasData, text="Humedad Del cultivo:    "+ Nodo1_LD['hc'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdathcg.place(x=10, y=110)

        self.label_ultdathc1 = Label(self.canvasData, text="Humedad De charola 1:    "+ Nodo1_LD['hc1'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdathc1.place(x=30, y=140)

        self.label_ultdathc2 = Label(self.canvasData, text="Humedad De charola 2:    "+ Nodo1_LD['hc2'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdathc2.place(x=30, y=170)

        self.label_ultdathc3 = Label(self.canvasData, text="Humedad De charola 3:    "+ Nodo1_LD['hc3'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdathc3.place(x=30, y=200)

        self.canvasData.create_rectangle(0,230,350,232, fill="#96E087", outline="#96E087")

        self.label_ultdatls = Label(self.canvasData, text="Luz del sistema:    "+ Nodo1_LD['ls'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdatls.place(x=10, y=240)

        self.label_ultdatls1 = Label(self.canvasData, text="Luz de charola 1:    "+ Nodo1_LD['lc1'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdatls1.place(x=30, y=270)

        self.label_ultdatls2 = Label(self.canvasData, text="luz de charola 2:    "+ Nodo1_LD['lc2'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdatls2.place(x=30, y=300)

        self.label_ultdatls3 = Label(self.canvasData, text="Luz de charola 3:    "+ Nodo1_LD['lc3'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdatls3.place(x=30, y=330)

        self.canvasData.create_rectangle(0,360,350,362, fill="#96E087", outline="#96E087")

        self.label_ultdatt = Label(self.canvasData, text="Temperatura 3:    "+ Nodo1_LD['ta'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",12))
        self.label_ultdatt.place(x=10, y=370)

        self.canvasData.create_rectangle(0,400,350,402, fill="#96E087", outline="#96E087")

        self.boton_refresh = ttk.Button(self.canvasData, text="Sensar ahora", image=self.png_refresh, compound=LEFT)
        self.boton_refresh.place(x=120, y=430)
        
        #--------------------------------------------------------------------------

        #---------------------------- Información del nodo-------------------------
        self.label_infnode = Label(self.medder, text="Información del nodo", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",14))
        self.label_infnode.place(x=210, y=5)

        self.label_dias = Label(self.medder, text="Dias de cultivo:   "+ Nodo1_LD['dp'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",11))
        self.label_dias.place(x=10, y=40)

        self.label_cultivo = Label(self.medder, text="Cultivo:   "+ Nodo1_LD['cultivo'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",11))
        self.label_cultivo.place(x=10, y=70)

        self.label_hr = Label(self.medder, text="Horas de luz:   "+ Nodo1_LD['hl'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",11))
        self.label_hr.place(x=10, y=100)

        self.boton_confn1 = ttk.Button(self.medder, text="Configuración de nodo", command=self.abrir_conf)
        self.boton_confn1.place(x=300, y=70)
        #-------------------------------------------------------------------------- 

        #-----------------------  Botonera-----------------------------------------
        self.boton_cerrar = ttk.Button(self.infder, text="      Inicio", image=self.png_inicio, compound=LEFT , command=self.destroy)
        self.boton_cerrar.place(x=10, y=30)
        #--------------------------------------------------------------------------

        
        self.focus()
        self.grab_set()
    
    #----------------------------métodos de acción----------------------------------
    def abrir_grafica(self):
        self.ventana_grafica = GrN1()

    def abrir_datos(self):
        self.ventana_datos = DataN1()
 
    def abrir_conf(self):
        self.ventana_conn1 = Conf_n1()

    def set_Graf_N1(self, event):       
        ComboBox_nodo1 = self.combo.get()
        set_Graf_N1(ComboBox_nodo1)
    
    def set_Graf_int_N1(self, event):
        ComboBox2_nodo1 = self.combo2.get()
        set_Graf_int_N1(ComboBox2_nodo1)
    
    #-------------------------------------------------------------------------------
  
    
            
