import pymongo
from Modulo_DB.DB_conect import *


def tinytaskreset(elem):
  conexion =abrirconexionmongodb ()
  db=conexion[0]
  client=conexion[1]
  tinytask_data_colection =db["tinytask"]
  for e in elem: 
    
    try:
      tinytask_data_colection.update_one({"_id":e},{"$set": { "tinytask_status":0}})  
    except pymongo.errors.ConnectionFailure:
      tinytaskreset(elem)
  client.close()
  return 0

def tinytaskactivo(id):
  conexion =abrirconexionmongodb ()
  db=conexion[0]
  client=conexion[1]
  tinytask_data_colection =db["tinytask"]
  try:
    tinytask_data_colection.update_one({"_id":id},{"$set": { "tinytask_status":1}})  
  except pymongo.errors.ConnectionFailure:
    tinytaskactivo(id)
  except pymongo.errors.ExecutionTimeout:
    tinytaskactivo(id)
  client.close()
  return 1


def tinytaskstatus(id):
  conexion =abrirconexionmongodb ()
  db=conexion[0]
  client=conexion[1]
  tinytask_data_colection =db["tinytask"]


  try:
    tinystatus =tinytask_data_colection.find({ "_id": id })
    print (tinystatus)
  except pymongo.errors.ConnectionFailure:
    tinytaskstatus(id)
  except pymongo.errors.ExecutionTimeout:
    tinytaskstatus(id)
  client.close()
  return 1