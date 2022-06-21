
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"

import collections
import os
import random
import time
from bson import ObjectId
from pip import main
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options
import pymongo
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.
def func(threads,emails, passwod,accname,acc_estado,timesleep):

  options = Options()
  options.page_load_strategy = 'normal'
  driver = webdriver.Chrome(options=options)
  options.page_load_strategy = 'normal'
  options.add_argument('--no-sandbox')
  options.add_argument('--start-maximized')
  #options.add_argument('--start-fullscreen')
  options.add_argument('--single-process')
  options.add_argument('--disable-dev-shm-usage')
  #options.add_argument("--incognito")
  options.add_argument('--disable-gpu')
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_experimental_option('useAutomationExtension', False)
  options.add_experimental_option("excludeSwitches", ["disable-automation"])
  options.add_argument("disable-infobars")
  driver.implicitly_wait(1.5)
  driver.get(singup_spotify)
  driver.maximize_window()
  time.sleep(2)

  print (driver.current_url)
  # INICIO A HACER LOGIN con google
  
  def check_exist_by_XPATH_botton (XPATH):
    global count1
    try:
      driver.find_element(By.XPATH, XPATH)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_XPATH_botton (XPATH)
      else: driver.close(), exit()
    count1=0
    ingresar = driver.find_element(By.XPATH,XPATH)
    return ingresar.click()
  check_exist_by_XPATH_botton ("/html/body/div[1]/div/main/div/div[2]/div/div[3]/button[1]/div/div")
  
  # ingresar el correo 
  def check_exist_by_ID_sendkey (ID_,send_keys_):
    global count1
    try:
      driver.find_element(By.ID, ID_)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_ID_sendkey(ID_,send_keys_)
      else: driver.close(), exit()
    count1=0
    return driver.find_element(By.ID, ID_).send_keys(send_keys_)

  check_exist_by_ID_sendkey("identifierId",emails)      
  
  #click en siguiente 
  def check_exist_by_XPATH_botton (XPATH):
    global count1
    try:
      driver.find_element(By.XPATH, XPATH)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_XPATH_botton (XPATH)
      else: driver.close(), exit()
    count1=0
    ingresar = driver.find_element(By.XPATH,XPATH)
    return ingresar.click()
  check_exist_by_XPATH_botton ('//*[@id="identifierNext"]/div/button/span')

  # ingresar la contraseña  
  def check_exist_by_ID_sendkey (XPATH,send_keys_):
    global count1
    try:
      driver.find_element(By.XPATH, XPATH)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_ID_sendkey(XPATH,send_keys_)
      else: driver.close(), exit()
    count1=0
    return driver.find_element(By.XPATH, XPATH).send_keys(send_keys_)

  check_exist_by_ID_sendkey('//*[@id="password"]/div[1]/div/div[1]/input',passwod)    

  #click en siguiente 
  def check_exist_by_XPATH_botton (XPATH):
    global count1
    try:
      driver.find_element(By.XPATH, XPATH)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_XPATH_botton (XPATH)
      else: driver.close(), exit()
    count1=0
    ingresar = driver.find_element(By.XPATH,XPATH)
    return ingresar.click()
  check_exist_by_XPATH_botton ('//*[@id="passwordNext"]/div/button/span')
  print("ok click google sing in")
  
  def evaluarstadoinicial():
    global count1

    try:
        def verificabotoncreate ():
            try:
                (WebDriverWait(driver, 3)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/a')))
               
                )    
                return True
            except TimeoutException:
                return False

        def verificabotonresumenapp():
            try:
                (WebDriverWait(driver, 3)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/div/button')))
                )    
                return True
            except TimeoutException:
                return False

        def verificabotonopenapp():
            try:
                (WebDriverWait(driver, 3)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/button/div/span')))
                )    
                return True
            except TimeoutException:
                return False
    
    
    except NoSuchElementException:
        print ("error finalevaluar estado inicial never install")
    #  if count1<=3: 
    #    count1+=1
    #    print (count1," no se encontro BOTON CREATE...")
    #    return time.sleep(5), evaluarstadoinicial (XPATH)
    if verificabotoncreate ():
        estadoinicialwebneverinstall="boton_createAPP"
        pass
    elif verificabotonresumenapp ():
        estadoinicialwebneverinstall = "boton_resumen"
        pass
    elif verificabotonopenapp (): 
        estadoinicialwebneverinstall = "boton_openAPP"
        pass
    else: 
        estadoinicialwebneverinstall='NO SE PUDO EVALUAR EL ESTADO INICIAL, BUSQUE OTRO PROGRAMADOR'
    return estadoinicialwebneverinstall
  #borrarvisualstudiocode('//*[@id="delete"]/div')
  

  def crearapp():
        inicio=0
        try:
            (WebDriverWait(driver, 3)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/a')))
            .click()
            )
            print("LANZANDO APP")    
        except TimeoutException:
            return False
        #FALTA TERMINAR EL CODIGO DEBE SELECCIONAR UN SERVIDOR DE FORMA ALEATORIA Y LANZARLO
        #LA PAGINA A CONTINUAR SERIA LA INICIAL DONDE APARECEN LAS APP LANZADAS
        # FINALIZA LLAMANDO A LA FUNCION QUE EVALUA EL ESTADOINICIAL 


        return print("terminando crear app")


  def iniciarbotonresume():
        try:
            (WebDriverWait(driver, 3)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/div/button')))
            .click()
            )
            print("click botonresume")    
        except TimeoutException:
            print("No encontro en 3 seg boton resumen, retorna a iniciarbotonresumen funcion ok")
            print ("Pasa a buscar boton openAPP")

        try:
            (WebDriverWait(driver, 20)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/button')))
            .click()
            )
            print("click boton_openAPP")    
        except TimeoutException:
            print("No encontro boton openAPP, retorna a iniciarbotonresumen funcion ok")
            iniciarbotonresume() 
        #CONTINUA AQUI REGISTRAR EN LA BD NEVERINSTAL EL ESTADO 1 PARA EL TYNKTASK ACTIVO
        # SOLO EJECUTA TYNKTASK SI ESTA EN ESTADO 0 (DISPONIBLE)    
        return True

  def countTabs():
    mainTab=  driver.window_handles
    return len(mainTab)

  def evaluar(evaluarestado,Tabs) :
    countminitos=0
    print ("Entrando a evaluar")  
    contador=0
    if evaluarestado ==  "boton_createAPP" and Tabs==0:
        print("---> Entrando a funcion crearapp()")
        crearapp() # no va ser necesario porque se deja creada la app solo una vez
    elif evaluarestado ==  "boton_resumen":  
        print("---> Entrando a funcion iniciarbotonresume()")
        iniciarbotonresume()
    elif evaluarestado ==  "boton_createAPP" and Tabs==1 and contador ==0:
        print("---> Entrando a lanzar  TINYTASK por primera vez falta codear la funcion")
        contador =1
        crearapp() # no va ser necesario porque se deja creada la app solo una vez
    else:
        print ("entro al Else de evaluar estado .. bye bye")
    time.sleep(60)
    print (f"---> Minuto: {countminitos}Finalizo Evaluar reiniciando evaluar", accname)
    evaluar (evaluarstadoinicial(),countTabs())
    

  
  
  #cmd = "test1.exe"
  #os.system(cmd)

  evaluar (evaluarstadoinicial(),countTabs())

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
  
  client.close()

  threads.wait()

numero_multitareas=4
#mongodb+srv://silklips:<password>@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority

def obtenerdatosdemongodbparacrearneverinstall ():
    abrirconexionmongodb ()
#db.create_collection("acc_user_info_singup")
#acc_datacollection.insert_many(lista)
#acc_datacollection.drop()
#acc_user_singupcollection.drop()
    global emails
    emails=[]
    global passwod
    passwod=[]
    global accname
    accname=[]
    global acc_estado
    acc_estado=[]
    global datelog
    datelog=[]
    global account
    account=[]
    global timesleep
    timesleep=[20,20,20,10,10,10]
    global numero_multitareas



    acc_neverinstall_data=neverinstall_datacollection.find( { "acc_estado": 0 } )
    acc_porregistrar=(len(list(acc_neverinstall_data)))

#inicio la iteacion entre 0 y el numero de multitareas  
#pendiente cancelar la accion de todo si acc para registrar =0
    if numero_multitareas>=acc_porregistrar:
        numero_multitareas=numero_multitareas

    acc_user_singupdata1=neverinstall_datacollection.find( { "acc_estado": 0 } )

    for elem in acc_user_singupdata1[0:numero_multitareas]:
        neverinstall_loging_log1 = neverinstall_loging_log.find_one( { "_id": elem["_id"]} )
        print (neverinstall_loging_log1)
        emails.append(elem["email"])
        passwod.append(elem["passwod"])
        accname.append(elem["accname"])
        acc_estado.append(elem["acc_estado"])
        neverinstall_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado": 2}})

    print ("email: ",emails)
    print ("passwod: ",passwod)
    print ("accname: ",accname)
    print ("acc_estado: ",acc_estado)
    client.close()

singup_spotify='https://neverinstall.com/signin'

barrier = Barrier(numero_multitareas)


hiloscerrados = 0



def iniciarmutitarea (numero_multitareas):
    global threads
    threads = []
    for i in range(numero_multitareas):
	    #i = Thread(target=func, args=(barrier,emails[i],passwod[i],accname[i],acc_estado[i]))
        i = Thread(target=func, args=(barrier,emails[i],passwod[i],accname[i],acc_estado[i],timesleep[i]))
    
        i.start()
        time.sleep(3)
        print ("sleep 3 seg en threads ")
        threads.append(i)
    for i in threads:
	    i.join()

def abrirconexionmongodb ():
    global client
    global db 
    global acc_datacollection 
    global acc_user_singupcollection
    global neverinstall_datacollection
    global neverinstall_loging_log 
    client = pymongo.MongoClient("mongodb+srv://silklips:!Fps91507856@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority")
    
    db= client["accounts"]
    client.server_info()
    print("Conexion mongo ok")
    
    acc_datacollection = db["accountmanager"]
    acc_user_singupcollection = db["acc_user_info_singup"]
    neverinstall_datacollection =db["neverinstall"]
    neverinstall_loging_log=db["neverinstall_loging_log"]
    return acc_datacollection, acc_user_singupcollection,neverinstall_datacollection, neverinstall_loging_log



obtenerdatosdemongodbparacrearneverinstall()
iniciarmutitarea(numero_multitareas)


