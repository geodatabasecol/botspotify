import collections
import random
import time
from bson import ObjectId
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options
import pymongo

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
  time.sleep(2)
  print (driver.current_url)
  driver.find_element(By.ID,"email").send_keys(emails)
  driver.find_element(By.ID,"confirm").send_keys(emails)
  driver.find_element(By.ID,"password").send_keys(passwod)
  driver.find_element(By.ID,"displayname").send_keys(username)
  driver.find_element(By.ID,"month").send_keys(mes)
  driver.find_element(By.ID,"day").send_keys(dia)
  driver.find_element(By.ID,"year").send_keys(year)
  driver.find_element(By.ID,genero).click()

  

  #ingresar = driver.find_element(By.ID,"login-button")
  #ingresar.click()
  print("ok loging  ", emails)
  time.sleep(50)
  threads.wait()


#mongodb+srv://silklips:<password>@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://silklips:!Fps91507856@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority")
db = client["accounts"]
client.server_info()
print("Conexion mongo ok")
acc_datacollection = db["accountmanager"]
acc_user_singupcollection = db["acc_user_info_singup"]

post1={ "acc_estado":0,"email": "emailadd@gmail.com", "pass":"pass003","username":"emailadd" }
post2={ "acc_estado":0,"email": "regvcdnd@gmail.com", "pass":"pass001","username":"regvcdnd" }
post3={ "acc_estado":0,"email": "5rteyfy4@gmail.com", "pass":"pass001","username":"5rteyfy4" }
post4={ "acc_estado":0,"email": "dhtrghfd@gmail.com", "pass":"pass001","username":"dhtrghfd" }
post5={ "acc_estado":0,"email": "vbxcvbvc@gmail.com", "pass":"pass001","username":"vbxcvbvc" }

#db.create_collection("acc_user_info_singup")

lista=[post1, post2,post3, post4, post5]

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

for elem in acc_user_singupdata1[0:numero_multitareas]:
  itir=0
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
 
 