
import time
from Modulo_Selenium.Tabs import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.homeweb import *


def estadoactualinicial(evaluarstadoinicio,Tabs,driver)  :
    
    if evaluarstadoinicio=="boton_createAPP"and Tabs==1:
        starttime1= None
        starttime2= None
        return None, starttime1, starttime2

    elif evaluarstadoinicio=="boton_resumen" and Tabs==1:
        resul= click_botonresume(driver)
        starttime1 = time.time()
        starttime2 = time.time()
        if resul:
            return True, starttime1,starttime2

    elif evaluarstadoinicio=="boton_openAPP" and Tabs==1:
        resul=click_boton_openAPP(driver)
        starttime1 = time.time()
        starttime2 = time.time()
        if resul:
            return True, starttime1,starttime2
    else :
        return False, starttime1, starttime2
    #lanzar  tinytask
    #el codigo lanzado debe conectar a la base de datos y cambiar el valor de tinitask a 1
def estadoprimerclickboton(evaluarstadoinicio,Tabs,driver)  :
    
    if evaluarstadoinicio=="boton_createAPP"and Tabs==1:
        starttime1= None
        starttime2= None
        return None, starttime1, starttime2

    elif evaluarstadoinicio=="boton_resumen" and Tabs==1:
        resul= click_botonresume(driver)
        starttime1 = time.time()
        starttime2 = time.time()
        if resul:
            return True, starttime1,starttime2

    elif evaluarstadoinicio=="boton_openAPP" and Tabs==1:
        resul=click_boton_openAPP(driver)
        starttime1 = time.time()
        starttime2 = time.time()
        if resul:
            return True, starttime1,starttime2
    else :
        return False, starttime1, starttime2


def evaluacion1(estadosdelosbotones,Tabs, driver):
  resul= estadoactualinicial(estadosdelosbotones,Tabs,driver)
  REturn,starttime1, starttime2=resul

  if REturn== None:
    return None, starttime1 , starttime2
    print (">>>>> ALERT ALERT <<<<<  Boton createAPP")
  if REturn== True:
    
    return True , starttime1 , starttime2
  if REturn== False:
    return False, starttime1 , starttime2


def evaluacion2(driver) :
    evaluarestado=estadodebotonenhome(driver)
    Tabs= Tabs=countTabs(driver)

    if evaluarestado ==  "boton_createAPP" and Tabs==1:
        #print("---> evaluarestado ==  'boton_createAPP'")
        return "boton_createAPP_1" # no va ser necesario porque se deja creada la app solo una vez   
    elif evaluarestado ==  "boton_resumen" and Tabs==1:  
        #print("---> evaluarestado ==  'boton_resumen'")
        return "boton_resumen_1"
    elif evaluarestado ==  "boton_openAPP" and Tabs==1:  
        #print("---> evaluarestado ==  'boton_openAPP'")
        #print("lanzar TYNYTASK")
        return "boton_openAPP_1"
    elif evaluarestado ==  "boton_resumen" and Tabs==2:  
        #print("---> evaluarestado ==  'boton_resumen'")
        #print ("esto pasaria solo si no funciona el codigo para que no se cierre la pagina")
        return "boton_resumen_2"
    elif evaluarestado ==  "boton_openAPP" and Tabs==2:
        #print("---> evaluarestado ==  'boton_openAPP' and Tabs==2 and contador ==0")
        #print("aqui manejar el codigo para que no se cierre")
        return "boton_openAPP_2"
    else:
        return "Else -homeweb 47-77"


def estatus_ventana_activa():
    with open("NeverInstall\status_ventana.txt") as archivo:
        resul =archivo.read()
    if resul== "0":
        return True

    if resul=="1":
        return False