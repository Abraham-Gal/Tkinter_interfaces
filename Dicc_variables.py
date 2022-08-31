
from msilib.schema import ComboBox


Size ={'pantalla':'1024x530'}
Colores = {'fondo':'#96E087','blanco':'#FFFFFF', 'fondo_n1':'#DDF9D7', 'btn_nodo':"#ABFB9A"}
Agua = {'estado':"Sabe we"}
Luz = {'lambientalN1':"last_D", 'lambientalN2':"last_D2"}
Config = {'modo':"Automático"}
Nodo1_LD = {'ha':"1",'hc':"2",'ta':"3",'ls':"4",'uhr':"13:00",'ucl':"15:00",'hl':"6",'dp':"7"}
Nodo2_LD = {'ha':"1",'hc':"2",'ta':"3",'ls':"4",'uhr':"13:00",'ucl':"15:00",'hl':"6",'dp':"7"}
Op_graficas = ["Humedad Ambiental", "Temperatura","Humedad de cultivo", "Humedad De charola 1", "Humedad De charola 2", "Humedad de charola 3", "Lud del cultivo", "Luz Charola 1", "Luz Charola 2", "Luz charola 3"]
Intervalo_g = ["Todos", "Ultimo dia", "Ultimos dos dias", "Utimos tres dias"]
Conf_gr_N1 = {'xlb': "n/a",'ylb': "n/a", 'ti': "n/a" }
Conf_gr_N2 = {'xlb': "n/a",'ylb': "n/a", 'ti': "n/a" }
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
            Conf_gr_N1['xlb'] = "Humedad el ambiente (%)"
            Conf_gr_N1['ylb'] = "Numero de datos"
            Conf_gr_N1['ti'] = "Humedad Ambiental"

        if(event == "Temperatura"):
            Conf_gr_N1['xlb'] = "Temperatura (C)"
            Conf_gr_N1['ylb'] = "Numero de datos"
            Conf_gr_N1['ti'] = "Temperatura"

#print (Agua['estado'])