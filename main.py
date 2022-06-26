
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"

from itertools import starmap
import time
from threading import Thread, Barrier
from types import NoneType
from ModuloEventosWindows.activar_tinytask import *
from ModuloEventosWindows.focus_google import *
from Modulo_neverInstall.SingIn.singingoogle import *
from Modulo_Selenium.Crear_driver import *
from Modulo_Selenium.Tabs import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.homeweb import *
from Modulo_neverInstall.evaluar import *
from Modulo_DB.DB_conect import *
from Modulo_DB.Never_install.DB_Never_Install import *
from Modulo_DB.Never_install.DB_TinyTask import *
from selenium import *



import win32gui, win32con, win32com.client
#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.

url_inicial='https://neverinstall.com/signin'

def func(threads,id,emails, passwod,accname,acc_estado,acc_count,acc_region,sleep):
  url =f"https://"+accname+".com"

  driver =crear_driver()

  try:
      driver.get(url)
  #driver =crear_driver(url_inicial)
  except :

      pass
  nombreventa= (str.lower(accname)+'.com')
  
  ventana=main2(nombreventa)
   
  driver.get(url_inicial)

  # INICIO A HACER LOGIN con google
  if iniciarcongoogle(driver,emails,passwod) ==False:
    iniciarcongoogle(driver,emails,passwod)
  
  Tabs=countTabs(driver)
  estadosdelosbotones=estadodebotonenhome(driver)
  

  resul0=estado0 (estadosdelosbotones,Tabs, driver)
  REturn,starttime1, starttime2=resul0

  print ("Return resul0",REturn )
  
  activar_tinitask=acction_tinytask (driver,ventana,accname)
  
  print ("paso estado pass evaluacion 1... dio click en boton")
  
  #paso2 = evaluacion2(driver,starttime1,starttime2)
  #Tabs=countTabs(driver)
  #estadosdelosbotones=estadodebotonenhome(driver)
    
  #cmd = "test1.exe"
  #os.system(cmd)

  print ("Codigo continua... finalizando..... END... bye bye")

  driver.close()
  threads.wait()

numero_multitareas=7
sleep=[1, 4, 6, 8, 10 ,12, 14]

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
                   acc_data[5][i] , acc_data[6][i], sleep[i]  ))
    
  i.start()
  
  #time.sleep(sleep[i])
  print ("sleep 0.2 seg en threads ")
  time.sleep(5)
  threads.append(i)

for i in threads:
  i.join()
