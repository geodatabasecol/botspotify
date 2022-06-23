import time

start = time.time()

end = time.time()

def tiempopararefrecarventana(e,s):
    if e-s >65:
        return True
    if e-s <65:
        return False
print (tiempopararefrecarventana(end,start))

while tiempopararefrecarventana(end,start)==False:
    time.sleep(5)
    estatus= (f"---> Segundos: {end-start} <--- ")
    f = open('holamundo.txt','a')
    f.write('\n' + estatus)
    f.close()
    end = time.time()
    tiempopararefrecarventana(end,start)
tiempopararefrecarventana(end,start)

print("fin")

