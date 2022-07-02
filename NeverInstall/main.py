
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"

import time
from ModuloEventosWindows.focus_google import *
from Modulo_Selenium.Crear_driver import *
from Modulo_Selenium.Tabs import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.homeweb import *
from Modulo_neverInstall.evaluar import *
from Modulo_neverInstall.SingIn import *
from Modulo_DB.DB_conect import *
from Modulo_DB.Never_install.DB_Never_Install import *
from Modulo_DB.Never_install.DB_TinyTask import *
from selenium import *
import pyautogui as pyauto
import pygetwindow as gw
import sys
from Modulo_Selenium.mousecontrol import *
import asyncio
from  funciones import *
sys.dont_write_bytecode = True

miclick=mousecontrol()
ventanaactiva=0
numero_multitareas=10
sleep=[1, 3, 5, 7, 9 ,11, 13,15,17,19]

#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.




async def func(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  global ventanaactiva
  ventanaactiva=0
  
   #Crea un ombjeto de la clase driver selenium
  
  url_inicial='https://neverinstall.com/signin' 
  singupneverinstall= singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  
  
  tasksingup =asyncio.create_task(singupneverinstall.primerpasoiniciarlogingoogle())
  await tasksingup
  await asyncio.sleep(1)
  print("Is OK Sing up acount ", accname)
  await asyncio.sleep(1)
  print("Verificando estado inicial en home ", accname)
  #singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
  driver.minimize_window()
 
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
  
  task_home= asyncio.create_task(estado_home.accioninicialenhome(ventanaactiva))
  ventanaactiva = await task_home
  await asyncio.sleep(10)
  driver.minimize_window()
  await asyncio.sleep(1)
  time.sleep(2)
  driver.maximize_window()
  time.sleep(2)
  driver.minimize_window()
  ####voy aqui .... 
  #falta configuar que todas las ventanas se minimizen despues de que cargen ...
  # el problema es que al dar click en resumen  se maximiza sola...
  


  print (ventanaactiva)
  async def click(ventanaactiva):
    driver.maximize_window()
    
    if ventanaactiva==1:
      ventanaactiva=0
      
      
      miclick=mousecontrol()
      miclick.calentando()
      await asyncio.sleep(15)
      miclick.primerclick()
      time.sleep(2)
      miclick.segundoclick()
      time.sleep(2)
      miclick.tercerclick()
      time.sleep(2)
      miclick.pegar()
      time.sleep(5)
      driver.minimize_window()
      
      ventanaactiva=0
      time.sleep(1)
      await asyncio.sleep(15)
  task_click= asyncio.create_task(click(ventanaactiva))
  await task_click


  print (f"{accname} continua condigo....ventana activa {ventanaactiva}")
  

  
  #Tabs=countTabs(driver)



acc_data=DB_neverinstall_get_acc (numero_multitareas)
for e in acc_data:
  print (e)
numero_multitareas=acc_data[7]
print("Numero de funciones",numero_multitareas)

tinytaskreset()

driver0 = driver()
driver1 = driver()
driver2 = driver()
driver3 = driver()
driver4 = driver()
driver5 = driver()
driver6 = driver()
driver7 =driver()
driver8 =driver()
driver9 =driver()
list_drivers=[driver0,driver1, driver2,driver3,driver4,driver5,driver6,driver7,driver8,driver9 ]
#

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
      func ( driver0,acc_data[0][0], acc_data[1][0],acc_data[2][0], acc_data[3][0],acc_data[4][0],acc_data[5][0],acc_data[6][0]),
      func (driver1,acc_data[0][1], acc_data[1][1],acc_data[2][1], acc_data[3][1],acc_data[4][1],acc_data[5][1],acc_data[6][1]),
      func (driver2,acc_data[0][2], acc_data[1][2],acc_data[2][2], acc_data[3][2],acc_data[4][2],acc_data[5][2],acc_data[6][2]),
      func (driver3,acc_data[0][3], acc_data[1][3],acc_data[2][3], acc_data[3][3],acc_data[4][3],acc_data[5][3],acc_data[6][3]),
      func (driver4,acc_data[0][4], acc_data[1][4],acc_data[2][4], acc_data[3][4],acc_data[4][4],acc_data[5][4],acc_data[6][4]),
      func (driver5,acc_data[0][5], acc_data[1][5],acc_data[2][5], acc_data[3][5],acc_data[4][5],acc_data[5][5],acc_data[6][5]),
      func (driver6,acc_data[0][6], acc_data[1][6],acc_data[2][6], acc_data[3][6],acc_data[4][6],acc_data[5][6],acc_data[6][6]),
      func (driver7,acc_data[0][7], acc_data[1][7],acc_data[2][7], acc_data[3][7],acc_data[4][7],acc_data[5][7],acc_data[6][7]),
      func (driver8,acc_data[0][8], acc_data[1][8],acc_data[2][8], acc_data[3][8],acc_data[4][8],acc_data[5][8],acc_data[6][8]),
      func (driver9,acc_data[0][9], acc_data[1][9],acc_data[2][9], acc_data[3][9],acc_data[4][9],acc_data[5][9],acc_data[6][9])

    )
    
asyncio.run(main())
