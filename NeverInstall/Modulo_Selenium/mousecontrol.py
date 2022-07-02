import time

import pyautogui as mouse
class mousecontrol:

    def calentando(self):
        mouse.moveTo(x=360, y=181)
        mouse.click(x=360, y=181)
        mouse.moveTo(x=361, y=183)
        mouse.click(x=361, y=183)
        mouse.moveTo(x=362, y=182)
        mouse.click(x=362, y=182)

    def primerclick(self):
        mouse.moveTo(x=315, y=161)
        mouse.click(x=315, y=161)
        time.sleep(1)
        mouse.moveTo(x=315, y=161)
        mouse.click(x=315, y=161)
        time.sleep(1)
        mouse.moveTo(x=315, y=161)
        mouse.click(x=315, y=161)
    def segundoclick(self):
        time.sleep(1)
        mouse.click(button='right')
        time.sleep(1)
    def tercerclick(self):
        time.sleep(1)
        mouse.click(x=386, y=316)   
        time.sleep(1)
    
    def pegar(self):
        time.sleep(2)
        mouse.write("lscpu")
        mouse.press('enter')

    def posicion(self):
        
        return mouse.position()
        
        
#    def tercerclick(self):
#        mouse.moveTo(x=307, y=148)
#        mouse.click(x=307, y=148)
#    
#    def cuartoclick(self):
#        mouse.moveTo(x=1362, y=645)
#        mouse.click()   
#
#    def quintoclick(self):
#        mouse.moveTo(x=647, y=349)
#        mouse.click()    

#time.sleep(8)
#miclick=mousecontrol()
#miclick.calentando()
#time.sleep(1)
#miclick.primerclick()
#time.sleep(1)
#miclick.segundoclick()
#time.sleep(1)
#miclick.tercerclick()
#while miclick.posicion():
#    print(miclick.posicion())

#time.sleep(3)
#miclick.pegar()
#miclick.tercerclick()
#time.sleep(3)  
#miclick.cuartoclick()
#time.sleep(3)
#miclick.quintoclick()
#time.sleep(3)