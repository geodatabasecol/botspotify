
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"


from multiprocessing.connection import wait
import time
from threading import Thread, Barrier, Lock

from ModuloEventosWindows.focus_google import *
from Modulo_Selenium.Crear_driver import *
from Modulo_Selenium.Tabs import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.homeweb import *
from Modulo_neverInstall.evaluar import *
from Modulo_DB.DB_conect import *
from Modulo_DB.Never_install.DB_Never_Install import *
from Modulo_DB.Never_install.DB_TinyTask import *
from selenium import *

lock=Lock()

ventanaactiva=0
numero_multitareas=3
sleep=[1, 3, 5, 7, 9 ,11, 13]

#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.

url_inicial='https://neverinstall.com/signin'


def func(threads,id,emails, password,accname,acc_estado,acc_count,acc_region,sleep,locke,i):
  global ventanaactiva
  
  driver =crear_driver()  #Crea un ombjeto de la clase driver selenium
  commandWindows= cWindow() 
  singupneverinstall=singinggoogle(driver, emails,password,accname,barrier,url_inicial,commandWindows) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
  barrier.reset()
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
 
  estado_home.accioninicialenhome()

  print ("Primer paso OK... verificando numero de TABS")
  tabs=tabcontrol(driver)
  tabs.countTabs()
  print (len(tabs.count_Tabs))
  print (type(len(tabs.count_Tabs)))
  if len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE")
  else:
    print ("No se cargo VS CODE")
    estado_home.clickboton_openAPP()
  
  
  
  while ventanaactiva ==0:
    lock.acquire()
    ventanaactiva=id
    commandWindows.hacerfocusenlaventana()
    print ("focus ventana", accname)
    #tessst eeeeeeee
    #test ste 
    lock.release()


    break
  print ("continua condigo....")
  

  
  #Tabs=countTabs(driver)

  time.sleep(40)
  threads.wait()

'''

  
  resul0=estado0 (estadosdelosbotones,Tabs, driver)
  REturn,starttime1, starttime2=resul0

  print ("Return resul0",REturn )
  
  
  
  print ("paso estado pass evaluacion 1... dio click en boton")
  
  #paso2 = evaluacion2(driver,starttime1,starttime2)
  #Tabs=countTabs(driver)
  #estadosdelosbotones=estadodebotonenhome(driver)
    
  #cmd = "test1.exe"
  #os.system(cmd)

  print ("Codigo continua... finalizando..... END... bye bye")

  driver.close()
  threads.wait()
'''


acc_data=DB_neverinstall_get_acc (numero_multitareas)
for e in acc_data:
  print (e)
numero_multitareas=acc_data[7]
print("hilos",numero_multitareas)

tinytaskreset()


barrier = Barrier(numero_multitareas)
hiloscerrados = 0
threads = []
for i in range(numero_multitareas):
  #i = Thread(target=func, args=(barrier,emails[i],passwod[i],accname[i],acc_estado[i]))
  i = Thread(target=func, args=(barrier, acc_data[0][i], acc_data[1][i],
                   acc_data[2][i], acc_data[3][i],acc_data[4][i] , 
                   acc_data[5][i] , acc_data[6][i], sleep[i],lock,i ))
    
  i.start()
 
  #time.sleep(sleep[i])
  print ("sleep 0.2 seg en threads ")
  time.sleep(1)
  threads.append(i)

for i in threads:
  i.join()
