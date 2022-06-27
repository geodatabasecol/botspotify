import time

def todaslasventanascargadasok(numero_multitareas, i):
    i=i+1
    archivo=open(f"NeverInstall/tareasencascada.txt","r") 
    resul = archivo.read() 
    archivo.close()
    time.sleep(1)
  
    archivo=open (f"NeverInstall/tareasencascada.txt","w")
    archivo.write(resul+str(i))
    archivo.close()
    
    time.sleep(1)  
    
    archivo= open(f"NeverInstall/tareasencascada.txt","r") 
    resul=archivo.read()
     
    print (len(resul))
    while len(resul) < numero_multitareas-1:
        time.sleep(1)
        resul =archivo.read() 
    archivo.close()
    return True