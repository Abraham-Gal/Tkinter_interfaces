
Size ={'pantalla':'1024x530'}
Colores = {'fondo':'#96E087','blanco':'#FFFFFF', 'fondo_n1':'#DDF9D7', 'btn_nodo':"#ABFB9A"}
Agua = {'estado':"Sabe we"}
Luz = {'lambientalN1':"last_D", 'lambientalN2':"last_D2"}
Config = {'modo':"Automático"}
Nodo1_LD = {'ha':"1",'hc':"2",'ta':"3",'ls':"4",'uhr':"13:00",'ucl':"15:00",'hl':"6"}

def getUlimoDLuz(nodo):

    if(nodo == 1):
        Luz['lambientalN1'] = "A_g1"
        return Luz['lambientalN1']
    if(nodo == 2):
        Luz['lambientalN2'] = "A_g2"
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

#print (Agua['estado'])