
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"

import collections
from itertools import starmap
import os
import time
from threading import Thread, Barrier
from Modulo_neverInstall.SingIn.singingoogle import *
from Modulo_Selenium.Crear_driver import *
from Modulo_Selenium.Tabs import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.homeweb.homeweb import *
from Modulo_neverInstall.evaluar import *
from Modulo_DB.DB_conect import *
from Modulo_DB.DB_Never_Install import *
from Modulo_DB.DB_TinyTask import *
#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.
url_inicial='https://neverinstall.com/signin'


def func(threads,id,emails, passwod,accname,acc_estado,acc_count,acc_region):
  driver =crear_driver(url_inicial)
  
  # INICIO A HACER LOGIN con google
  if iniciarcongoogle(driver,emails,passwod) ==False:
    iniciarcongoogle(driver,emails,passwod)
  

  Tabs=countTabs(driver)
  estadosdelosbotones=estadodebotonenhome(driver)
  print (estadosdelosbotones)
  
  paso1=evaluacion1(estadosdelosbotones,Tabs, driver) 
  REturn,starttime1, starttime2=paso1
  while REturn!=True:
    print ("paso1",paso1)
    Tabs=countTabs(driver)
    estadosdelosbotones=estadodebotonenhome(driver)
    paso1=evaluacion1(estadosdelosbotones,Tabs, driver) 
    REturn,starttime1, starttime2=paso1
  
  
  print ("paso estado pass evaluacion 1... dio click en boton")
  
  #paso2 = evaluacion2()
    
    
  #cmd = "test1.exe"
  #os.system(cmd)

  print ("Codigo continua... finalizando..... END... bye bye")

  '''driver.find_element(By.XPATH,"email").send_keys(emails)

  driver.find_element(By.ID,"confirm").send_keys(emails)
  driver.find_element(By.ID,"password").send_keys(passwod)
  driver.find_element(By.ID,"displayname").send_keys(username)
  driver.find_element(By.ID,"month").send_keys(mes)
  driver.find_element(By.ID,"day").send_keys(dia)
  driver.find_element(By.ID,"year").send_keys(year)
  button = driver.find_element(By.XPATH,genero)
  driver.execute_script("arguments[0].click();", button)
  #ingresar = driver.find_element(By.ID,"login-button")
  #ingresar.click()
  print("ok loging  ", emails)
  time.sleep(20)
  
  client = pymongo.MongoClient("mongodb+srv://silklips:!Fps91507856@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority")
  db = client["accounts"]
  client.server_info()
  print("Conexion mongo ok")
  acc_datacollection = db["accountmanager"]
  
  result=acc_datacollection.find( { "acc_estado": 2 } )
  for elem in result: 
    acc_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado":1}})

  result=acc_datacollection.find( { "email":emails } )
  for e in result:print(e)  '''
  
  

  threads.wait()

numero_multitareas=4


acc_data=DB_neverinstall_get_acc (numero_multitareas)

tinytaskreset(acc_data[0])


barrier = Barrier(numero_multitareas)
hiloscerrados = 0
threads = []
for i in range(numero_multitareas):
  #i = Thread(target=func, args=(barrier,emails[i],passwod[i],accname[i],acc_estado[i]))
  i = Thread(target=func, args=(barrier, acc_data[0][i], acc_data[1][i], acc_data[2][i], acc_data[3][i],acc_data[4][i] , acc_data[5][i] , acc_data[6][i]  ))
    
  i.start()
  time.sleep(3)
  print ("sleep 3 seg en threads ")
  threads.append(i)

for i in threads:
  i.join()
