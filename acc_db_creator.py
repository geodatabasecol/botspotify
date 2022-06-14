import collections
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

post1={ "acc_estado":1,"email": "emailadd@gmail.com", "pass":"!asdf2021","username":"emailadd" }
post2={ "acc_estado":0,"email": "regvcdnd@gmail.com", "pass":"!asdf2021","username":"regvcdnd" }
post3={ "acc_estado":0,"email": "5rteyfy4@gmail.com", "pass":"!asdf2021","username":"5rteyfy4" }
post4={ "acc_estado":0,"email": "dhtrghfd@gmail.com", "pass":"!asdf2021","username":"dhtrghfd" }
post5={ "acc_estado":0,"email": "vbxcvbvc@gmail.com", "pass":"!asdf2021","username":"vbxcvbvc" }




lista=[post1, post2,post3, post4, post5]
#db.create_collection("acc_user_info_singup")
#acc_datacollection.insert_many(lista)
#acc_datacollection.drop()
#acc_user_singupcollection.drop()



result=acc_datacollection.find( { "acc_estado": 0 } )
for elem in result: 
  acc_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "pass":"!asdf2021"}})

  #acc_user_singupcollection.insert_one({"_id":elem["_id"],"day":random.sample(range(1,28), 1)[0], "month":random.sample(range(1,12), 1)[0],"year":random.sample(range(1990,2004), 1)[0], "genero":random.sample(range(1,3), 1)[0]})
  
#for elem in result:  print (elem)



client.close()