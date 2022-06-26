import time

def acction_tinytask ():
    def estatus_ventana_activa():
        with open("ModuloTinyTask/status_ventana.txt") as archivo:
            resul =archivo.read()
        
        if resul== "0":
            return True

        if resul=="1":
            return False

    a= estatus_ventana_activa()
    
    while a==False:
        print ("Estatus ventana activa false")
        time.sleep(0.3)
        a= estatus_ventana_activa()

    archivo= open("ModuloTinyTask/status_ventana.txt", "w") 
    archivo.write("1")  
    archivo.close()
 
    print ("Iniciando realizar  funciones en la ventana ")
    
    print ("Haciendo focus en la ventana")
    a= estatus_ventana_activa()
    print(a)
    time.sleep(30)
    print(a)
    print ("Terminando  funciones en la ventana status ventana ") 
    archivo= open("ModuloTinyTask/status_ventana.txt", "w") 
    archivo.write("0")  
    archivo.close()
    time.sleep(5)
    a= estatus_ventana_activa()
    print(a)

acction_tinytask()
