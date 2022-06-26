from Modulo_DB.DB_conect import *
def DB_neverinstall_get_acc (numeromultitareas):
    conexion =abrirconexionmongodb ()
    db=conexion[0]
    client=conexion[1]
    neverinstall_datacollection =db["neverinstall"]

    
    emails=[]
    password=[]
    accname=[]
    acc_estado=[]
    acc_region=[]
    acc_count=[]
    ids=[]
#timesleep=[20,20,20,10,10,10]
    acc_neverinstall_data=neverinstall_datacollection.find( { "acc_estado": 0 } )
    acc_porregistrar=(len(list(acc_neverinstall_data)))

    if numeromultitareas>=acc_porregistrar:
        numeromultitareas=acc_porregistrar
    
    acc_user_singupdata1=neverinstall_datacollection.find( { "acc_estado": 0 } )

    for elem in acc_user_singupdata1[:numeromultitareas]:
        ids.append(elem["_id"])
        emails.append(elem["email"])
        password.append(elem["passwod"])
        accname.append(elem["accname"])
        acc_estado.append(elem["acc_estado"])
        acc_region.append(elem["acc_region"])
        acc_count.append(elem["acc_count"])
        neverinstall_datacollection.update_one({ "_id": elem["_id"] }, {"$set": { "acc_estado": 2}})

    client.close()
    print ("Client close")
    return ids,emails, password, accname, acc_estado,acc_count, acc_region,numeromultitareas

