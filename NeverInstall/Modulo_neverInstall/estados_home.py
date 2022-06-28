
import time
from Modulo_Selenium.Tabs import countTabs
from Modulo_neverInstall.evaluar import evaluacion1
from Modulo_neverInstall.homeweb import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from Modulo_neverInstall.SingIn.singingoogle import *
from Modulo_Selenium.Crear_driver import *
class home:
        def __init__(self,driver) -> None:
            self.driver=driver
            self.botonhomelaunch=False
        def estadodebotonenhomeNorthAmerica(self):
            try:
                def verificabotoncreate (self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Create an app")))
                        )    
                        return True
                    except :
                        return False


                def verificabotonresumenapp(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Resume app")))
                        )
                        return True
                    except :
                        print ("linea 35 no se encontro el texto: Resume app")
                        return False

                def verificabotonresumenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Paused in North America")))
                        )
                        return True
                    except :
                        print ("linea 47 no se encontro el texto: Paused in North America")
                        return False         
                def verificabotonbuildingapp(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Building in North America")))
                        )
                        return True
                    except :
                        print ("linea 56 no se encontro el texto: Building in North America")
                        return False                                  

                def verificabotonopenapp(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Open in browser")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 56 no se encontro el texto: Open in browser")
                        return False
                def verificabotonopenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Running in North America")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 56 no se encontro el texto: Running in North America")
                        return False                        

            except :
                print ("error homeweb 20-48 ")
                return False

            if verificabotoncreate (self): botonhomelaunch = "boton_createAPP" 
            elif verificabotonresumenapp (self):botonhomelaunch = "boton_resumen"
            elif verificabotonresumenapp2 (self):botonhomelaunch = "boton_resumen"
            elif verificabotonbuildingapp (self): botonhomelaunch = "boton_buildingAPP"
            elif verificabotonopenapp (self): botonhomelaunch = "boton_openAPP"
            elif verificabotonopenapp2 (self):  botonhomelaunch = "boton_openAPP"
            else: botonhomelaunch=False
            return botonhomelaunch

        def estadodebotonenhomeEurope(self):
            try:
                def verificabotoncreate (self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Create an app")))
                        )    
                        return True
                    except :
                        return False


                def verificabotonresumenapp(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Resume app")))
                        )
                        return True
                    except :
                        print ("linea 109 no se encontro el texto: Resume app")
                        return False

                def verificabotonresumenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Paused in Europe")))
                        )
                        return True
                    except :
                        print ("linea 119 no se encontro el texto: Paused in Europe")
                        return False         
                def verificabotonbuildingapp(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Building in Europe")))
                        )
                        return True
                    except :
                        print ("linea 128 no se encontro el texto: Building in Europe")
                        return False                                  

                def verificabotonopenapp(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Open in browser")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 138 no se encontro el texto: Open in browser")
                        return False
                def verificabotonopenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 1)
                        .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Running in Europe")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 147 no se encontro el texto: Running in Europe")
                        return False                        

            except :
                print ("error homeweb 20-48 ")
                return False

            if verificabotoncreate (self): botonhomelaunch = "boton_createAPP" 
            elif verificabotonresumenapp (self):botonhomelaunch = "boton_resumen"
            elif verificabotonresumenapp2 (self):botonhomelaunch = "boton_resumen"
            elif verificabotonbuildingapp (self): botonhomelaunch = "boton_buildingAPP"
            elif verificabotonopenapp (self): botonhomelaunch = "boton_openAPP"
            elif verificabotonopenapp2 (self):  botonhomelaunch = "boton_openAPP"
            else: botonhomelaunch=False
            return botonhomelaunch







        #borrarvisualstudiocode('//*[@id="delete"]/div')


'''

        def estado0 (estadosdelosbotones,Tabs, driver):
        paso1=evaluacion1(estadosdelosbotones,Tabs, driver) 
        REturn,starttime1, starttime2=paso1
            
        while REturn!=True:
            
            Tabs=countTabs(driver)
            estadosdelosbotones=estadodebotonenhome(driver)
            paso1=evaluacion1(estadosdelosbotones,Tabs, driver) 
            REturn,starttime1, starttime2 = paso1
        return REturn,starttime1, starttime2
    '''