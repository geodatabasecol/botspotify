
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"


import time
from threading import Thread, Barrier
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

from ModuloEventosWindows.ventanasload import todaslasventanascargadasok

archivo=open (f"NeverInstall/tareasencascada.txt","w")
archivo.write("")
archivo.close()
print('Estado inicial tareasencascada = ""')

#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.

url_inicial='https://neverinstall.com/signin'


def func(threads,id,emails, passwod,accname,acc_estado,acc_count,acc_region,sleep,i):
  
  
  url =f"https://"+accname+".com"

  driver =crear_driver()
  try:
      driver.get(url)
      
  #driver =crear_driver(url_inicial)
  except :

      pass
  time.sleep(3)

  nombreventana= (str.lower(accname)+'.com')

  commandWindows= cWindow()    
  commandWindows.find_window_wildcard(nombreventana)
  commandWindows.ventanacargadaok()
  print(accname ,commandWindows.valorhwnd())

  todaslasventanascargadasok(numero_multitareas,commandWindows)

  print("Todas las ventanas cargadas... \nIniciando Loging NeverInstall...") 
  
  try:
      driver.get(url_inicial)
      time.sleep(2)
  #
  except :

      pass
  print("Cargando NeverInstall OK")

  commandWindows.hacerfocusenlaventana(accname)
  time.sleep(5)    
  exit()
  
  # INICIO A HACER LOGIN con google
  if iniciarcongoogle(driver,emails,passwod) ==False:
    iniciarcongoogle(driver,emails,passwod)
  
  Tabs=countTabs(driver)
  estadosdelosbotones=estadodebotonenhome(driver)
  
  exit()
  driver.close()
  threads.wait()

  
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

numero_multitareas=2
sleep=[1, 3, 5, 7, 9 ,11, 13]

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
                   acc_data[5][i] , acc_data[6][i], sleep[i],i  ))
    
  i.start()
 
  #time.sleep(sleep[i])
  print ("sleep 0.2 seg en threads ")
  time.sleep(3)
  threads.append(i)

for i in threads:
  i.join()
