
# MODULO PARA REGISTRAR ACCOUNTS SINGUP ACC
#pip install webdriver-manager
#pip install pymongo
#pip install selenium
#pip install "pymongo[srv]"

import collections
import random
import time
from bson import ObjectId
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options
import pymongo
#funcion que lanza los multihilos y actualiza el estado de la acc a 1 si finaliza todo ok.
def func(threads,emails, passwod,username,dia,mes,year,genero):
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
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_experimental_option('useAutomationExtension', False)
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-infobars")
  driver.implicitly_wait(1.5)
  driver.get(singup_spotify)
  driver.maximize_window()
  time.sleep(2)
  print (driver.current_url)
  driver.find_element(By.ID,"email").send_keys(emails)
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
  for e in result:print(e)  
  client.close()

  threads.wait()


#mongodb+srv://silklips:<password>@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://silklips:!Fps91507856@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority")
db = client["accounts"]
client.server_info()
print("Conexion mongo ok")
acc_datacollection = db["accountmanager"]
acc_user_singupcollection = db["acc_user_info_singup"]


#db.create_collection("acc_user_info_singup")

#acc_datacollection.insert_many(lista)
#acc_datacollection.drop()
#acc_user_singupcollection.drop()

numero_multitareas = 3

emails=[]
passwod=[]
username=[]
dia=[]
mes=[]
year=[]
genero=[]

acc_user_singupdata1=acc_datacollection.find( { "acc_estado": 0 } )
acc_porregistrar=(len(list(acc_user_singupdata1)))

#inicio la iteacion entre 0 y el numero de multitareas  
#pendiente cancelar la accion de todo si acc para registrar =0
if numero_multitareas>=acc_porregistrar:
  numero_multitareas=numero_multitareas
acc_user_singupdata1=acc_datacollection.find( { "acc_estado": 0 } )

for elem in acc_user_singupdata1[0:numero_multitareas]:
  acc_user_singupdata2=acc_user_singupcollection.find_one( { "_id": elem["_id"]} )
  print (acc_user_singupdata2)
  
  acc_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado": 2}})

  emails.append(elem["email"])
  passwod.append(elem["pass"])
  username.append(elem["username"])
  dia.append(acc_user_singupdata2["day"])
  mes.append(acc_user_singupdata2["month"])
  year.append(acc_user_singupdata2["year"])
  genero.append(acc_user_singupdata2["genero"])


print ("email: ",emails)
print ("passwod: ",passwod)
print ("username: ",username)
print ("dia: ",dia)
print ("mes: ",mes)
print ("year: ",year)
print ("genero: ",genero)

client.close()

singup_spotify='https://www.spotify.com/us/signup'

barrier = Barrier(numero_multitareas)

threads = []

for i in range(numero_multitareas):
	i = Thread(target=func, args=(barrier,emails[i],passwod[i],username[i],dia[i],mes[i],year[i],genero[i]))
	i.start()
	threads.append(i)

for i in threads:
	i.join()
 
