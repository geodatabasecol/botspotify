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
tinytask=db["tinytask"]


neverinstall_loging_log =db["neverinstall_loging_log"]
post1={ "acc_estado":1,"email": "regvcdnd@gmail.com", "pass":"!asdf2021","username":"regvcdnd" } 
post2={ "acc_estado":1,"email": "5rteyfy4@gmail.com", "pass":"!asdf2021","username":"5rteyfy4" } 
post3={ "acc_estado":1,"email": "dhtrghfd@gmail.com", "pass":"!asdf2021","username":"dhtrghfd" } 
post4={ "acc_estado":0,"email": "vbxcvbvc@gmail.com", "pass":"!asdf2021","username":"vbxcvbvc" }
post5={ "acc_estado":0,"email": "xmulsika@gmail.com", "pass":"!asdf2021","username":"xmulsika" }

acc_new_add=[post1, post2,post3, post4, post5]

#neverinstal1={ "email": "azuresilk01@gmail.com","passwod":"fps91507856","accname":"azuresilk01","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
#neverinstal2={ "email": "azuresilk02@gmail.com","passwod":"Fps91507856","accname":"azuresilk02","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
#neverinstal3={ "email": "azuresilk03@gmail.com","passwod":"Fps91507856","accname":"azuresilk03","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
#neverinstal4={ "email": "azuresilk04@gmail.com","passwod":"fps91507856","accname":"azuresilk04","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
#neverinstal5={ "email": "azuresilk05@gmail.com","passwod":"fps91507856","accname":"azuresilk01","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
#neverinstal6={ "email": "azuresilk06@gmail.com","passwod":"fps91507856","accname":"azuresilk06","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal7={ "email": "azuresilk07@gmail.com","passwod":"fps91507856","accname":"azuresilk07","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal8={ "email": "azuresilk08@gmail.com","passwod":"fps91507856","accname":"azuresilk08","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal9={ "email": "azuresilk09@gmail.com","passwod":"fps91507856","accname":"azuresilk09","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal10={ "email": "azuresilk10@gmail.com","passwod":"fps91507856","accname":"azuresilk10","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal11={ "email": "azuresilk11@gmail.com","passwod":"fps91507856","accname":"azuresilk11","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal12={ "email": "azuresilk12@gmail.com","passwod":"fps91507856","accname":"azuresilk12","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal13={ "email": "azuresilk13@gmail.com","passwod":"fps91507856","accname":"azuresilk13","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal14={ "email": "azuresilk14@gmail.com","passwod":"fps91507856","accname":"azuresilk14","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal15={ "email": "azuresilk15@gmail.com","passwod":"fps91507856","accname":"azuresilk15","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal16={ "email": "azuresilk16@gmail.com","passwod":"fps91507856","accname":"azuresilk16","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal17={ "email": "azuresilk17@gmail.com","passwod":"fps91507856","accname":"azuresilk17","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal18={ "email": "azuresilk18@gmail.com","passwod":"fps91507856","accname":"azuresilk18","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal19={ "email": "azuresilk19@gmail.com","passwod":"fps91507856","accname":"azuresilk19","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
#neverinstal20={ "email": "azuresilk20@gmail.com","passwod":"fps91507856","accname":"azuresilk20","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 


neverinstal21={ "email": "azuresilk21@gmail.com","passwod":"fps91507856","accname":"azuresilk21","acc_estado":0 ,"acc_count": 0, "acc_region": "USA" } 
neverinstal22={ "email": "azuresilk22@gmail.com","passwod":"fps91507856","accname":"azuresilk22","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal23={ "email": "axuredilk23@gmail.com","passwod":"fps91507856","accname":"axuredilk23","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
#neverinstal24={ "email": "azuresilk24@gmail.com","passwod":"fps91507856","accname":"azuresilk24","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
#neverinstal25={ "email": "azuresilk25@gmail.com","passwod":"fps91507856","accname":"azuresilk25","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
#neverinstal26={ "email": "azuresilk26@gmail.com","passwod":"fps91507856","accname":"azuresilk26","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
#neverinstal27={ "email": "azuresilk27@gmail.com","passwod":"fps91507856","accname":"azuresilk27","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
#neverinstal28={ "email": "azuresilk28@gmail.com","passwod":"fps91507856","accname":"azuresilk28","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
#neverinstal29={ "email": "azuresilk29@gmail.com","passwod":"fps91507856","accname":"azuresilk29","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
#neverinstal30={ "email": "azuresilk30@gmail.com","passwod":"fps91507856","accname":"azuresilk30","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal31={ "email": "azuresilk31@gmail.com","passwod":"fps91507856","accname":"azuresilk31","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal32={ "email": "azuresilk32@gmail.com","passwod":"fps91507856","accname":"azuresilk32","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal33={ "email": "azuresilk33@gmail.com","passwod":"fps91507856","accname":"azuresilk33","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal34={ "email": "azuresilk34@gmail.com","passwod":"fps91507856","accname":"azuresilk34","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal35={ "email": "azuresilk35@gmail.com","passwod":"fps91507856","accname":"azuresilk35","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal36={ "email": "azuresilk36@gmail.com","passwod":"fps91507856","accname":"azuresilk36","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal37={ "email": "azuresilk37@gmail.com","passwod":"fps91507856","accname":"azuresilk37","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal38={ "email": "azuresilk38@gmail.com","passwod":"fps91507856","accname":"azuresilk38","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal39={ "email": "azuresilk39@gmail.com","passwod":"fps91507856","accname":"azuresilk39","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal40={ "email": "azuresilk40@gmail.com","passwod":"fps91507856","accname":"azuresilk40","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal41={ "email": "azuresilk41@gmail.com","passwod":"fps91507856","accname":"azuresilk41","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal42={ "email": "azuresilk42@gmail.com","passwod":"fps91507856","accname":"azuresilk42","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal43={ "email": "azuresilk43@gmail.com","passwod":"fps91507856","accname":"azuresilk43","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal44={ "email": "azuresilk44@gmail.com","passwod":"fps91507856","accname":"azuresilk44","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal45={ "email": "azuresilk45@gmail.com","passwod":"fps91507856","accname":"azuresilk45","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal46={ "email": "azuresilk46@gmail.com","passwod":"fps91507856","accname":"azuresilk46","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal47={ "email": "azuresilk47@gmail.com","passwod":"fps91507856","accname":"azuresilk47","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal48={ "email": "azuresilk48@gmail.com","passwod":"fps91507856","accname":"azuresilk48","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
#neverinstal49={ "email": "azuresilk49@gmail.com","passwod":"fps91507856","accname":"azuresilk49","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal50={ "email": "azuresilk50@gmail.com","passwod":"fps91507856","accname":"azuresilk50","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal51={ "email": "azuresilk51@gmail.com","passwod":"fps91507856","accname":"azuresilk51","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal52={ "email": "azuresilk52@gmail.com","passwod":"fps91507856","accname":"azuresilk52","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal53={ "email": "azuresilk53@gmail.com","passwod":"fps91507856","accname":"azuresilk53","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal54={ "email": "azuresilk54@gmail.com","passwod":"fps91507856","accname":"azuresilk54","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal55={ "email": "azuresilk55@gmail.com","passwod":"fps91507856","accname":"azuresilk55","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal56={ "email": "azuresilk56@gmail.com","passwod":"fps91507856","accname":"azuresilk56","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal57={ "email": "azuresilk57@gmail.com","passwod":"fps91507856","accname":"azuresilk57","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal58={ "email": "azuresilk58@gmail.com","passwod":"fps91507856","accname":"azuresilk58","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal59={ "email": "azuresilk59@gmail.com","passwod":"fps91507856","accname":"azuresilk59","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal60={ "email": "azuresilk60@gmail.com","passwod":"fps91507856","accname":"azuresilk60","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal61={ "email": "azuresilk61@gmail.com","passwod":"fps91507856","accname":"azuresilk61","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal62={ "email": "azuresilk62@gmail.com","passwod":"fps91507856","accname":"azuresilk62","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal63={ "email": "azuresilk63@gmail.com","passwod":"fps91507856","accname":"azuresilk63","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal64={ "email": "azuresilk64@gmail.com","passwod":"fps91507856","accname":"azuresilk64","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal65={ "email": "azuresilk65@gmail.com","passwod":"fps91507856","accname":"azuresilk65","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal66={ "email": "azuresilk66@gmail.com","passwod":"fps91507856","accname":"azuresilk66","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal67={ "email": "azuresilk67@gmail.com","passwod":"fps91507856","accname":"azuresilk67","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal68={ "email": "azuresilk68@gmail.com","passwod":"fps91507856","accname":"azuresilk68","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal69={ "email": "azuresilk69@gmail.com","passwod":"fps91507856","accname":"azuresilk69","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal70={ "email": "azuresilk70@gmail.com","passwod":"fps91507856","accname":"azuresilk70","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal71={ "email": "azuresilk71@gmail.com","passwod":"fps91507856","accname":"azuresilk71","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal72={ "email": "azuresilk72@gmail.com","passwod":"fps91507856","accname":"azuresilk72","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal73={ "email": "azuresilk73@gmail.com","passwod":"fps91507856","accname":"azuresilk73","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal74={ "email": "azuresilk74@gmail.com","passwod":"fps91507856","accname":"azuresilk74","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal75={ "email": "azuresilk75@gmail.com","passwod":"fps91507856","accname":"azuresilk75","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal76={ "email": "azuresilk76@gmail.com","passwod":"fps91507856","accname":"azuresilk76","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal77={ "email": "azuresilk77@gmail.com","passwod":"fps91507856","accname":"azuresilk77","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal78={ "email": "azuresilk78@gmail.com","passwod":"fps91507856","accname":"azuresilk78","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal79={ "email": "azuresilk79@gmail.com","passwod":"fps91507856","accname":"azuresilk79","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal80={ "email": "azuresilk80@gmail.com","passwod":"fps91507856","accname":"azuresilk80","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 

neverinstal81={ "email": "azuresilk81@gmail.com","passwod":"fps91507856","accname":"azuresilk81","acc_estado":0 ,"acc_count": 0,"acc_region": "USA" } 
neverinstal82={ "email": "azuresilk82@gmail.com","passwod":"fps91507856","accname":"azuresilk82","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal83={ "email": "azuresilk83@gmail.com","passwod":"fps91507856","accname":"azuresilk83","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal84={ "email": "azuresilk84@gmail.com","passwod":"fps91507856","accname":"azuresilk84","acc_estado":0 ,"acc_count": 0, "acc_region": "USA"  } 
neverinstal85={ "email": "azuresilk85@gmail.com","passwod":"fps91507856","accname":"azuresilk85","acc_estado":0 ,"acc_count": 0 , "acc_region": "USA" } 
neverinstal86={ "email": "azuresilk86@gmail.com","passwod":"fps91507856","accname":"azuresilk86","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" }  
neverinstal87={ "email": "azuresilk87@gmail.com","passwod":"fps91507856","accname":"azuresilk87","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal88={ "email": "azuresilk88@gmail.com","passwod":"fps91507856","accname":"azuresilk88","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal89={ "email": "azuresilk89@gmail.com","passwod":"fps91507856","accname":"azuresilk89","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 
neverinstal90={ "email": "azuresilk90@gmail.com","passwod":"fps91507856","accname":"azuresilk90","acc_estado":0 ,"acc_count": 0 ,"acc_region": "USA" } 




neverinstall_new_add=[neverinstal7,neverinstal8,neverinstal9,neverinstal10,neverinstal11,neverinstal12,neverinstal13, neverinstal14,neverinstal15,neverinstal16,neverinstal17,neverinstal18,neverinstal19, neverinstal21,neverinstal22,neverinstal23,
                      neverinstal31,neverinstal32,neverinstal33, neverinstal34,neverinstal35,neverinstal36,neverinstal37,neverinstal38,neverinstal39,neverinstal40,neverinstal41,neverinstal42,neverinstal43, neverinstal44,neverinstal45,neverinstal46,neverinstal47,neverinstal48,neverinstal50, neverinstal51,neverinstal52,neverinstal53,neverinstal54,neverinstal55,neverinstal56,neverinstal57,neverinstal58,neverinstal59,neverinstal60,
                      neverinstal61,neverinstal62,neverinstal63, neverinstal64,neverinstal65,neverinstal66,neverinstal67,neverinstal68,neverinstal69,neverinstal70,neverinstal71,neverinstal72,neverinstal73, neverinstal74,neverinstal75,neverinstal76,neverinstal77,neverinstal78,neverinstal79,neverinstal80, neverinstal81,neverinstal82,neverinstal83,neverinstal84,neverinstal85,neverinstal86,neverinstal87,neverinstal88,neverinstal89,neverinstal90]

#'''neverinstal24,neverinstal25,neverinstal26,neverinstal27,neverinstal28,neverinstal29,neverinstal30'''

def db_acc_neverinstall (neverinstall_acc_nuevas):
  neverinstall_datacollection.insert_many(neverinstall_acc_nuevas)

  result=neverinstall_datacollection.find( { "acc_estado": 0 } )
  for elem in result: 
    try:
      time = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
      print(elem["_id"]," ", elem["accname"], " ",datetime.now()  )
      neverinstall_loging_log.insert_one({"_id":elem["_id"],"accname":elem["accname"], "datalog":("%s/%s/%s  %s:%s" % (time.day, time.month, time.year, time.hour, time.minute))})
      tinytask.insert_one({"_id":elem["_id"],"tinytask_status":0})
    except pymongo.errors.DuplicateKeyError:
      continue
    

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

def db_acc_neverinstallestado1_to_0():
  result=neverinstall_datacollection.find( { "acc_estado": 1 } )
  for elem in result: 
    neverinstall_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado":0}})
  
    #tinytask.update_one({ "_id": elem["_id"] }, {"$set": { "tinytask_status":0}})
  result=neverinstall_datacollection.find( { "acc_estado": 0 } )
  for elem in result: 
      print(elem)
  
def db_acc_estado2_to_0():
  result=acc_datacollection.find( { "acc_estado": 9 } )
  i=0
  for elem in result: 
    acc_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado":0}})
    i+=1
    print(i)

def accounsspotyficheckpass():
  result=acc_datacollection.find( { "acc_estado": 5} )
  i=0
  print ("{:<20} {:<20} {:<20} {:<20} ".format("#",'EMAIL','PASSW', "USER" ))
  for elem in result: 
    acc=elem["email"]
    passw=elem["pass"]
    user=elem["username"]

    i+=1
    print ("{:<20} {:<20} {:<20} {:<20}".format( i, acc, passw,user))

  result=acc_datacollection.find( { "acc_estado": 1} )
  i=0
  print ("{:<20} {:<20} {:<20} {:<20} ".format("#",'EMAIL','PASSW', "USER" ))
  for elem in result: 
    acc=elem["email"]
    passw=elem["pass"]
    user=elem["username"]

    i+=1
    print ("{:<20} {:<20} {:<20} {:<20}".format( i, acc, passw,user))





def limpiaraccmanager():
  result=neverinstall_datacollection.find( {"acc_estado":0 } )
  
  i=0
  print ("{:<20} {:<40} {:<20}".format('EMAIL','PAIS', "#"))
  a=0
  for elem in result: 
    a+=1
    acc_region=elem["acc_region"]
    acc=elem["email"]
    #LEN=int(len(elem["email"]))
    print ("{:<20} {:<40} {:<20}".format(acc,acc_region, a))
  


#-----ACCOUNS SPOTIFY DATA ----
accounsspotyficheckpass()
#db_add_accounts (acc_new_add)
#db_acc_datosusuariosingup()
#db_acc_estado2_to_0()

#-----NEVERINSTAL DATA ----
#db_acc_neverinstall(neverinstall_new_add)  #agregar nuevas cuentas a la bd
#neverinstall_datacollection.drop()
#neverinstall_loging_log.drop()
#neverinstalloginglog()
#db_acc_neverinstallestado1_to_0()
#limpiaraccmanager()



#limpiaraccmanager()

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