
Size ={'pantalla':'1024x530'}
Colores = {'fondo':'#96E087','blanco':'#FFFFFF', 'fondo_n1':'#DDF9D7'}
Agua = {'estado':"Sabe we"}
Luz = {'lambientalN1':"last_D", 'lambientalN2':"last_D2"}
Config = {'modo':"Automático"}


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

#print (Agua['estado'])