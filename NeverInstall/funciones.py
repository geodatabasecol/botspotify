import time

from Modulo_Selenium.Tabs import tabcontrol
from Modulo_neverInstall.SingIn.singingoogle import singinggoogle
from Modulo_neverInstall.estados_home import home
import asyncio

url_inicial='https://neverinstall.com/signin'

############################### 0 #######################################
async def func0(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()
  


############################### 1 #######################################

async def func1(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()

############################### 2 #######################################
async def func2(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
    driver=driver
    id=id
    emails=emails
    password=password
    accname=accname
    acc_estado=acc_estado
    acc_count=acc_count
    acc_region=acc_region
     #Crea un ombjeto de la clase driver selenium
    singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
    singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
      
    print("Verificando estado inicial de home", accname)
    #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
    #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
    estado_home = home(driver,accname)  
      
    tabs=tabcontrol(driver)
    tabs.countTabs() 
    while len(tabs.count_Tabs)==1:
      print ("No se cargo VS CODE",accname)
      ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
      time.sleep(1)
      if len(tabs.countTabs())==2:
        break
        print ("Primer paso OK... verificando numero de TABS")
    while len(tabs.count_Tabs)==2:
        tabs.switch_to_vscodeTab()
        print ("Tab actual VS CODE",accname)
        driver.maximize_window()
        break
    driver.maximize_window()
  


############################### 3 #######################################

async def func3(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()


############################### 4 #######################################

async def func4(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()


############################### 5 #######################################
async def func5(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()


############################### 6 #######################################

async def func6(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()

############################### 7 #######################################
async def func7(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()

############################### 8 #######################################
async def func8(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()

############################### 9 #######################################
async def func9(driver,id,emails, password,accname,acc_estado,acc_count,acc_region):
  driver=driver
  id=id
  emails=emails
  password=password
  accname=accname
  acc_estado=acc_estado
  acc_count=acc_count
  acc_region=acc_region
   #Crea un ombjeto de la clase driver selenium
  
   
  singupneverinstall=singinggoogle(driver,emails,password,accname,url_inicial) #Crea un objeto para loging google
  
  singupneverinstall.primerpasoiniciarlogingoogle() #Llama a la funcion que hace loging en neverinstall 
    
  print("Verificando estado inicial de home", accname)
  #La clase home verifica el estado de los botones en home de neverinstall.com para Nort America, Europe
  #Funcion que retorna el estado de los botones ("boton_createAPP", "boton_resumen", "boton_openAPP", "boton_buildingAPP")
  estado_home = home(driver,accname)  
    
  tabs=tabcontrol(driver)
  tabs.countTabs() 
  while len(tabs.count_Tabs)==1:
    print ("No se cargo VS CODE",accname)
    ventanaactiva =estado_home.accioninicialenhome(ventanaactiva)
    time.sleep(1)
    if len(tabs.countTabs())==2:
      break

  
  print ("Primer paso OK... verificando numero de TABS")


  while len(tabs.count_Tabs)==2:
    tabs.switch_to_vscodeTab()
    print ("Tab actual VS CODE",accname)
    driver.maximize_window()
    break

  driver.maximize_window()