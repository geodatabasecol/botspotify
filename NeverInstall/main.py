
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
import pyautogui as pyauto
import pygetwindow as gw
lock=Lock()

ventanaactiva=0
numero_multitareas=7
sleep=[1, 3, 5, 7, 9 ,11, 13]

#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.

url_inicial='https://neverinstall.com/signin'


def func(threads,id,emails, password,accname,acc_estado,acc_count,acc_region,sleep,locke,i):
  global ventanaactiva
  
  driver =crear_driver()  #Crea un ombjeto de la clase driver selenium
  
  commandWindows= cWindow(accname) 
  singupneverinstall=singinggoogle(driver, emails,password,accname,barrier,url_inicial,commandWindows) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
  #commandWindows.setActWin()
  
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    estado_home.accioninicialenhome()
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")

  print (len(tabs.count_Tabs))
  print (type(len(tabs.count_Tabs)))
  
  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    break

  
  
  lock.acquire()
  while ventanaactiva ==0:
    try:
      ventanaactiva=id
      commandWindows.setActWin()
      print ("focus ventana", accname)
      pyauto.position(x=305, y=158)
      pyauto.click(x=305, y=158)

      #tessst eeeeeeee
      #test ste 
      
      break
    except:
      print ("Error haciendo focus en la ventana ",accname)
      ventanaactiva=0
      break
  lock.release()

    
  print ("continua condigo....")
  

  
  #Tabs=countTabs(driver)

  time.sleep(10)
  driver.close()
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
