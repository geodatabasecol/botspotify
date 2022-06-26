
import time
from ModuloTinyTask.focus_google import *
from Modulo_DB.Never_install.DB_TinyTask import *
from Modulo_Selenium.Tabs import countTabs
from Modulo_Selenium.focus_windows import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.evaluar import estatus_ventana_activa



def acction_tinytask (driver,ventana,accname):
    
    status=tinytaskstatus()
    Tabs=countTabs(driver)
    estadosdelosbotones=estadodebotonenhome(driver)
    a= estatus_ventana_activa()

    while a==False:
        print ("Estatus ventana activa false",accname)
        time.sleep(2)
        a= estatus_ventana_activa()

    archivo= open("status_ventana.txt", "w") 
    archivo.write("1")  
    archivo.close()
    a= estatus_ventana_activa()
    print(a," ",accname)
    print ("Haciendo focus en la ventana",accname)
    main3(ventana)

    print ("Iniciando realizar  funciones en la ventana ")
    print ("aqui ejecutar las acciones en la ventana ", accname) 
    a= estatus_ventana_activa()
    print(a," ",accname)
    print ("Haciendo focus en la ventana",accname)
    
    time.sleep(10)
    print(a," ",accname)
    print ("Terminando  funciones en la ventana status ventana ",accname) 
    archivo= open("status_ventana.txt", "w") 
    archivo.write("0")  
    archivo.close()
    time.sleep(2)
    a= estatus_ventana_activa()
    print(a," ",accname)
    
    print (status,estadosdelosbotones, Tabs )
    perro loco


