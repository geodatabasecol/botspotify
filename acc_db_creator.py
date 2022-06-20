import collections
from datetime import date, datetime
from logging import exception
import random
import time
from bson import ObjectId
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options
import pymongo



client = pymongo.MongoClient("mongodb+srv://silklips:!Fps91507856@mycrypta.ugxec.mongodb.net/?retryWrites=true&w=majority")
db = client["accounts"]
client.server_info()
print("Conexion mongo ok")
acc_datacollection = db["accountmanager"]
acc_user_singupcollection = db["acc_user_info_singup"]
neverinstall_datacollection =db["neverinstall"]
neverinstall_loging_log =db["neverinstall_loging_log"]
post1={ "acc_estado":1,"email": "regvcdnd@gmail.com", "pass":"!asdf2021","username":"regvcdnd" } 
post2={ "acc_estado":1,"email": "5rteyfy4@gmail.com", "pass":"!asdf2021","username":"5rteyfy4" } 
post3={ "acc_estado":1,"email": "dhtrghfd@gmail.com", "pass":"!asdf2021","username":"dhtrghfd" } 
post4={ "acc_estado":0,"email": "vbxcvbvc@gmail.com", "pass":"!asdf2021","username":"vbxcvbvc" }
post5={ "acc_estado":0,"email": "xmulsika@gmail.com", "pass":"!asdf2021","username":"xmulsika" }

acc_new_add=[post1, post2,post3, post4, post5]


neverinstal1={ "email": "azuresilk01@gmail.com","passwod":"fps91507856","accname":"neverinstal1","acc_estado":0 ,"acc_count": 0  } 
neverinstal2={ "email": "azuresilk02@gmail.com","passwod":"fps91507856","accname":"neverinstal2","acc_estado":0 ,"acc_count": 0  } 

neverinstall_new_add=[neverinstal1, neverinstal2]

def db_acc_neverinstall (neverinstall_acc_nuevas):
  #neverinstall_datacollection.insert_many(neverinstall_acc_nuevas)

  result=neverinstall_datacollection.find( { "acc_estado": 0 } )
  for elem in result: 
    try:
      time = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
      print(elem["_id"]," ", elem["accname"], " ",datetime.now()  )
      neverinstall_loging_log.insert_one({"_id":elem["_id"],"accname":elem["accname"], "datalog":("%s/%s/%s  %s:%s" % (time.day, time.month, time.year, time.hour, time.minute))})
    except pymongo.errors.DuplicateKeyError:
      continue


def db_add_accounts (acc_nuevas):
  acc_datacollection.insert_many(acc_nuevas)
  

def db_acc_datosusuariosingup():
  mesesingles=["January","February","March","April","May","June","July","August","September","October","November","December"]
  mesesespanol=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  genderid=['//*[@id="gender_option_male"]','//*[@id="gender_option_female"]', '//*[@id="gender_option_nonbinary"]']
  result=acc_datacollection.find( { "acc_estado": 0 } )
  for elem in result: 
    try:
      acc_user_singupcollection.insert_one({"_id":elem["_id"],"day":random.sample(range(1,28), 1)[0],"month": random.choice(mesesespanol),"year":random.sample(range(1990,2004),1)[0],"genero":random.choice(genderid)})
    except pymongo.errors.DuplicateKeyError:
      continue

def db_acc_neverinstallestado2_to_0():
  result=neverinstall_datacollection.find( { "acc_estado": 2 } )
  for elem in result: 
    neverinstall_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado":0}})

def db_acc_estado2_to_0():
  result=acc_datacollection.find( { "acc_estado": 2 } )
  for elem in result: 
    acc_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado":0}})



#db_add_accounts (acc_new_add)
#db_acc_datosusuariosingup()
#db_acc_estado2_to_0()

#db_acc_neverinstall(neverinstall_new_add)  #agregar nuevas cuentas a la bd
db_acc_neverinstallestado2_to_0()



#lista=[post1, post2,post3, post4, post5]
#db.create_collection("acc_user_info_singup")
#db.create_collection("acc_datacollection")
#acc_datacollection.insert_many(lista)
#acc_datacollection.drop()
#acc_user_singupcollection.drop()

nombres_listas_reproduccion=['nombre_listareproduccion1','nombre_listareproduccion2','nombre_listareproduccion3','nombre_listareproduccion4',
                            'nombre_listareproduccion5', 'nombre_listareproduccion6','nombre_listareproduccion7', 'nombre_listareproduccion8',
                            'nombre_listareproduccion9', 'nombre_listareproduccion10'  ]
nombres_artistas_a_buscar=['artista1','artista2','artista3','artista4','artista3','artista5','artista6','artista7', 'artista8' ]

artistas_a_monetizar=['MI_ARTISTA1','MI_ARTISTA2']

listafinalrandom=[]


client.close()
print("cliente closed")