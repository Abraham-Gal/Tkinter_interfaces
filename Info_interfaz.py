import tkinter as tk
from tkinter import Label, PhotoImage, ttk, LEFT
from Dicc_variables import *

class Informacion(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(bg=Colores['blanco'])
        self.geometry(Size['pantalla'])
        self.title("Información")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/info.png'))

        #-------------------------  Recursos -----------------------------------------
        self.png_inicio=PhotoImage(file="Interface/btn_inicio.png")
        self.png_planta=PhotoImage(file="Interface/page_info_e.png")
        #-----------------------------------------------------------------------------

        self.img_planta = Label(self, image=self.png_planta, relief="flat", border=0)
        self.img_planta.place(x=10,y=10)

        self.label_titulo = Label(self, text="Dispositivo de control y gestion de microcultivos", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",24))
        self.label_titulo.place(x=120,y=30)

        self.label_UAZ = Label(self, text="Univercidad Autónoma de Zacatecas", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_UAZ.place(x=300,y=90)

        self.label_FGS = Label(self, text="Francisco Garcia Salinas", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_FGS.place(x=370,y=120)

        self.label_tesis = Label(self, text="Tesis de licenciatura", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_tesis.place(x=390,y=150)

        self.label_ING = Label(self, text="Ingeniería en computación", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_ING.place(x=355,y=180)

        self.label_tes = Label(self, text="Tesista", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_tes.place(x=470,y=240)

        self.label_EALG = Label(self, text="Eduardo Abraham Lopez Galvez", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_EALG.place(x=320,y=280)

        self.label_ates = Label(self, text="Asesor de tesis", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_ates.place(x=430,y=330)

        self.label_OO = Label(self, text="Oscar Ordaz", relief="flat", border=0, bg="#FFFFFF", font=("Verdana",18))
        self.label_OO.place(x=445,y=370)

        self.boton_cerrar = ttk.Button(self, text="     Inicio   ", image=self.png_inicio, compound=LEFT ,command=self.destroy)
        self.boton_cerrar.place(x=890, y=455)
        
        self.focus()
        self.grab_set()