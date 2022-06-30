import time
from turtle import position
import pyautogui as pyauto 

class mousecontrol:
    def __init__(self) -> None:
        pass
    def primerclick(self):
        pyauto.position(x=305, y=158)
        pyauto.click(x=305, y=158)

    def segundoclick(self):
        pyauto.position(x=305, y=148)
        pyauto.click(x=305, y=148)   
    
    def tercerclick(self):
        pyauto.position(x=1365, y=645)
        pyauto.click(x=1365, y=645)      
    
    def obtener(self):
        while pyauto.position():
            print(pyauto.position())
mitest= mousecontrol()


time.sleep(15)
mitest.primerclick()
mitest.primerclick()
time.sleep(3)
mitest.segundoclick()
mitest.segundoclick()
time.sleep(3)
mitest.tercerclick()
mitest.tercerclick()
time.sleep(3)  