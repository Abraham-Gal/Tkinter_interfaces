from lib2to3.pgen2.token import OP
import tkinter as tk
from tkinter import Label, ttk, Frame
from tkinter import Canvas
from turtle import title
from GraficaN1 import *
from Dicc_variables import *

class Nodo1(tk.Toplevel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1024, height=530,bg=Colores['fondo'])
        self.geometry("1024x530")
        self.title("Nodo de producción 1")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/n1_2.png'))

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
        
        #-----------------------  Configuraciones de gráfica y de datos----------------------
        
        self.label_liquido = Label(self.canvasG1, text="Configuración de gráfica", relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",14))
        self.label_liquido.place(x=30, y=5)

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
        #self.combo2.bind("<<ComboboxSelected>>",self.set_Graf_N1)

        self.btn_vg = ttk.Button(self.canvasG1, text="Grafica", command=self.abrir_grafica)
        self.btn_vg.place(x=200, y=100)

        self.canvasG1.create_rectangle(320,0,330,170, fill="#96E087", outline="#96E087")
        #--------------------------------------------------------------------------
        #-----------------------  Botonera-----------------------------------------
        self.boton_cerrar = ttk.Button(self.infder, text="Inicio", command=self.destroy)
        self.boton_cerrar.place(x=10, y=30)
        #--------------------------------------------------------------------------

        
        self.focus()
        self.grab_set()
    
    def abrir_grafica(self):
        self.ventana_grafica = GrN1()
 
    def set_Graf_N1(self, event):       
        ComboBox_nodo1 = self.combo.get()
        if(ComboBox_nodo1 == "Humedad Ambiental"):
            Conf_gr_N1['xlb'] = "Humedad el ambiente (%)"
            Conf_gr_N1['ylb'] = "Numero de datos"
            Conf_gr_N1['ti'] = "Humedad Ambiental"

        if(ComboBox_nodo1 == "Temperatura"):
            Conf_gr_N1['xlb'] = "Temperatura (C)"
            Conf_gr_N1['ylb'] = "Numero de datos"
            Conf_gr_N1['ti'] = "Temperatura"


  
    
            
