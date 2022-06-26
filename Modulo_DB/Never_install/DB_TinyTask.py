import pymongo
from Modulo_DB.DB_conect import *

{"_id":{"$oid":"62b4d557cf90690e947997a9"},"tinytask_status":{"$numberInt":"0"}}


def tinytaskreset():
  conexion =abrirconexionmongodb ()
  db=conexion[0]
  client=conexion[1]
  tinytask_data_colection =db["tinytask"]
  try:
      tinytask_data_colection.update_one({"_id":"62b4d557cf90690e947997a9"},{"$set": { "tinytask_status":0}})  
  except pymongo.errors.ConnectionFailure:
      tinytaskreset()
  client.close()
  return 0

def tinytaskactivo():
  conexion =abrirconexionmongodb ()
  db=conexion[0]
  client=conexion[1]
  tinytask_data_colection =db["tinytask"]
  try:
    tinytask_data_colection.update_one({"_id":'62b4d557cf90690e947997a9'},{"$set": { "tinytask_status":1}})  
  except pymongo.errors.ConnectionFailure:
    tinytaskactivo()
  except pymongo.errors.ExecutionTimeout:
    tinytaskactivo()
  client.close()



def tinytaskstatus():
  conexion =abrirconexionmongodb ()
  db=conexion[0]
  client=conexion[1]
  tinytask_data_colection =db["tinytask"]


  try:
    tinystatus =tinytask_data_colection.find()
  except pymongo.errors.ConnectionFailure:
    tinytaskstatus()
  except pymongo.errors.ExecutionTimeout:
    tinytaskstatus()
  for e in tinystatus :
    return (e['tinytask_status'])
  
  client.close()
     