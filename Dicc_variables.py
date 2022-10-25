
from msilib.schema import ComboBox


Size ={'pantalla':'1024x530'}
Colores = {'fondo':'#96E087','blanco':'#FFFFFF', 'fondo_n1':'#DDF9D7', 'btn_nodo':"#ABFB9A"}
Agua = {'estado':"Sabe we"}
Luz = {'lambientalN1':"last_D", 'lambientalN2':"last_D2"}
Config = {'modo':"Automático"}
Nodo1_LD = {'ha':"1",'hc':"2",'ta':"3",'ls':"4",'uhr':"13:00",'ucl':"15:00",'hl':"6",'dp':"7",'hc1':"8",'hc2':"9",'hc3':"10",'lc1':"11",'lc2':"12",'lc3':"13", 'cultivo':"Frijoles"}
Nodo2_LD = {'ha':"1",'hc':"2",'ta':"3",'ls':"4",'uhr':"13:00",'ucl':"15:00",'hl':"6",'dp':"7"}
Op_graficas = ["Humedad Ambiental", "Temperatura","Humedad de cultivo", "Humedad de charola 1", "Humedad de charola 2", "Humedad de charola 3", "Luz del cultivo", "Luz charola 1", "Luz charola 2", "Luz charola 3"]
Intervalo_g = ["Todos", "Ultimo dia", "Ultimos dos dias", "Utimos tres dias"]
Int_g1 = "Todos"
Conf_gr_N1 = {'xlb': "Numero de datos",'ylb': "Humedad del ambiente %", 'ti': "Humedad ambietnal"}
Conf_gr_N2 = {'xlb': "Numero de datos",'ylb': "Humedad del ambiente %", 'ti': "Humedad ambietnal"}
data_n1 = [i**2 for i in range(101)] 
data_n2 = [i+2 for i in range(101)]


def getUlimoDLuz(nodo):

    if(nodo == 1):
        return Luz['lambientalN1']
    if(nodo == 2):
        return Luz['lambientalN2'] 

def getModoFuncion():
    return Config['modo']

def setModoFuncion(modo):
    if(modo == 1):
        Config['modo'] = "Automático"
        return Config['modo']
    if(modo == 2):
        Config['modo'] = "Manual"
        return Config['modo']

def setNodo1_LD(elemento, valor):
    if(elemento == 1):
        Nodo1_LD['ha'] = valor
    if(elemento == 2):
        Nodo1_LD['hc'] = valor
    if(elemento == 3):
        Nodo1_LD['ta'] = valor
    if(elemento == 4):
        Nodo1_LD['ls'] = valor
    if(elemento == 5):
        Nodo1_LD['uhr'] = valor
    if(elemento == 6):
        Nodo1_LD['ucl'] = valor
    if(elemento == 7):
        Nodo1_LD['hl'] = valor
    if(elemento == 8):
        Nodo1_LD['dp'] = valor

def getNodo1_LD(elemento):
    if(elemento == 1):
        return Nodo1_LD['ha'] 
    if(elemento == 2):
        return Nodo1_LD['hc'] 
    if(elemento == 3):
        return Nodo1_LD['ta'] 
    if(elemento == 4):
        return Nodo1_LD['ls'] 
    if(elemento == 5):
        return Nodo1_LD['uhr'] 
    if(elemento == 6):
        return Nodo1_LD['ucl'] 
    if(elemento == 7):
        return Nodo1_LD['hl']
    if(elemento == 8):
        return Nodo1_LD['dp']

def setNodo2_LD(elemento, valor):
    if(elemento == 1):
        Nodo2_LD['ha'] = valor
    if(elemento == 2):
        Nodo2_LD['hc'] = valor
    if(elemento == 3):
        Nodo2_LD['ta'] = valor
    if(elemento == 4):
        Nodo2_LD['ls'] = valor
    if(elemento == 5):
        Nodo2_LD['uhr'] = valor
    if(elemento == 6):
        Nodo2_LD['ucl'] = valor
    if(elemento == 7):
        Nodo2_LD['hl'] = valor
    if(elemento == 8):
        Nodo2_LD['dp'] = valor

def getNodo2_LD(elemento):
    if(elemento == 1):
        return Nodo2_LD['ha'] 
    if(elemento == 2):
        return Nodo2_LD['hc'] 
    if(elemento == 3):
        return Nodo2_LD['ta'] 
    if(elemento == 4):
        return Nodo2_LD['ls'] 
    if(elemento == 5):
        return Nodo2_LD['uhr'] 
    if(elemento == 6):
        return Nodo2_LD['ucl'] 
    if(elemento == 7):
        return Nodo2_LD['hl']
    if(elemento == 8):
        return Nodo2_LD['dp']

def set_Graf_N1(event):       
    if(event == "Humedad Ambiental"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Humedad el ambiente (%)"
        Conf_gr_N1['ti'] = "Humedad Ambiental"
    if(event == "Temperatura"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Temperatura (C)"
        Conf_gr_N1['ti'] = "Temperatura"
    if(event == "Humedad de cultivo"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Humedad de cultivo (niveles)"
        Conf_gr_N1['ti'] = "Humedad de Cultivo"
    if(event == "Humedad de charola 1"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Humedad de charola 1 (niveles)"
        Conf_gr_N1['ti'] = "Humedad de charola 1"
    if(event == "Humedad de charola 2"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Humedad de charola 2 (niveles)"
        Conf_gr_N1['ti'] = "Humedad de charola 2"
    if(event == "Humedad de charola 3"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Humedad de charola 3 (niveles)"
        Conf_gr_N1['ti'] = "Humedad de charola 3"
    if(event == "Luz del cultivo"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Luz de cultivo (niveles)"
        Conf_gr_N1['ti'] = "Luz del cultivo"
    if(event == "Luz charola 1"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Luz de charola 1 (niveles)"
        Conf_gr_N1['ti'] = "Luz de charola 1"
    if(event == "Luz charola 2"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Luz de charola 2 (niveles)"
        Conf_gr_N1['ti'] = "Luz de charola 2"
    if(event == "Luz charola 3"):
        Conf_gr_N1['xlb'] = "Numero de datos"
        Conf_gr_N1['ylb'] = "Luz de charola 3 (niveles)"
        Conf_gr_N1['ti'] = "Luz de charola 3"

def set_Graf_int_N1(event):
    if(event == "Todos"):
        Int_g1 = "Todos"
        print("Todos")
    if(event == "Ultimo dia"):
        Int_g1 = "Ultimo dia"
    if(event == "Ultimos dos dias"):
        Int_g1 = "Ultimos dos dias"
    if(event == "Ultimos tres dias"):
        Int_g1 = "Ultimos tres dias"
