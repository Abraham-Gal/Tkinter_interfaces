import tkinter as tk
from tkinter import Label, ttk, Frame, PhotoImage, LEFT
from tkinter import Canvas
from Dicc_variables import *

class Conf_n1(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1024, height=530,bg=Colores['fondo'])
        self.geometry("1024x530")
        self.title("Configuración nodo 1")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/n1_2.png'))

        #------------------- Canvas Objects --------------------------------
        self.canvas = Canvas(self)
        self.canvas.config(bg=Colores['blanco'],width="1024", height="530")
        self.canvas.pack(anchor="w")
        #-------------------------------------------------------------------

        #-------------------- Recursos --------------------------------------
        self.png_menos=PhotoImage(file="Interface/btn_menos.png")
        self.png_mas=PhotoImage(file="Interface/btn_mas.png")
        #---------------------------------------------------------------------
        
        #--------------------- Configuración de luz -------------------------
        
        self.label_Chl = Label(self.canvas, text="Horas de luz por dia: "+ Nodo1_LD['hl'], relief="flat", border=0, bg=Colores['blanco'], font=("Verdana",14))
        self.label_Chl.place(x=20, y=10)

        self.boton_mL = ttk.Button(self.canvas, text="    Más", image=self.png_menos, compound=LEFT, command=self.aumento_luz)
        self.boton_mL.place(x=75, y=75)

        #-----------------------------------------------------------------
        self.boton_cerrar = ttk.Button(self.canvas, text="Nodo 1", command=self.destroy)
        self.boton_cerrar.place(x=900, y=400)
        
        self.focus()
        self.grab_set()
    #-----------------------  Metodos ------------------------------------
    def aumento_luz(self):
        h_luz = int(Nodo1_LD['hl'])
        h_luz = h_luz + 1
        Nodo1_LD['hl'] = str(h_luz)
        self.label_Chl.place(x=20, y=10)
        print(Nodo1_LD['hl'])

    #---------------------------------------------------------------------


        