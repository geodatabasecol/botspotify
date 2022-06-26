import pymongo

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
    print("Conexion MongoDB ok")

    return db,client