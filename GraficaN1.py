import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from Dicc_variables import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class GrN1(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1024, height=530)
        self.geometry("1024x530")
        self.title("Grafica nodo 1")
        self.tk.call('wm','iconphoto',self._w,tk.PhotoImage(file='Interface/graficas_p.png'))

        #------------------------------ Canvas OBJ -----------------------------------
        self.canvasG1 = Canvas(self)
        self.canvasG1.config(bg=Colores['fondo'],width="1024", height="250")
        self.canvasG1.pack(side="top")
        #-----------------------------------------------------------------------------
        #----------------------------- Gráfica ---------------------------------------
        self.fig = Figure(figsize = (10.2, 2.5), dpi = 100)
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.plot(data_n1)
        
        self.plot1.set(xlabel=Conf_gr_N1['xlb'], ylabel=Conf_gr_N1['ylb'], title=Conf_gr_N1['ti'])
        self.plot1.grid()

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.canvasG1)  
        self.canvas.draw() 
        self.canvas.get_tk_widget().pack() 
  
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.canvasG1) 
        self.toolbar.update() 
  
        self.canvas.get_tk_widget().pack()
        #-----------------------------------------------------------------------------

        self.boton_cerrar = ttk.Button(self, text="Nodo 1", command=self.destroy)
        self.boton_cerrar.place(x=75, y=75)
        
        self.focus()
        self.grab_set()