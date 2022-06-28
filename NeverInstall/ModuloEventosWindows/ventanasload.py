import time

def todaslasventanascargadasok(numero_multitareas, commandWindows):

    while commandWindows.numeroventanascargadas() < numero_multitareas-1:
        time.sleep(2)