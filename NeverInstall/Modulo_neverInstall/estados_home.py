
import time



from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class home:
        def __init__(self,driver) -> None:
            self.driver=driver
            self._botonhomelaunch=""
        def estadodebotonenhomeNorthAmerica(self):
            try:
                def verificabotoncreate (self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.XPATH, ''))) 
                        )    
                        print ("true boton create app")
                        return True

                    except :
                        print ("falseeeeeeeeeee")
                        return False


                def verificabotonresumenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                            .until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[6]/div[1]/div/div/button'))) 
                        
                        )
                        print ("true texto resumen app")
                        return True
                    except :
                        print ("linea 35 no se encontro el texto: Resume app")
                        return False

                def verificabotonresumenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]')))
                        )
                        return True
                    except :
                        print ("linea 47 no se encontro el texto: Paused in North America")
                        return False         
                def verificabotonbuildingapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Building in North America")))
                        )
                        return True
                    except :
                        print ("linea 56 no se encontro el texto: Building in North America")
                        return False                                  

                def verificabotonopenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Open in browser")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 56 no se encontro el texto: Open in browser")
                        return False
                def verificabotonopenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Running in North America")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 56 no se encontro el texto: Running in North America")
                        return False                        

            except :
                print ("error homeweb 20-48 ")
                return False

            if verificabotoncreate (self): self._botonhomelaunch = "boton_createAPP" 
            elif verificabotonresumenapp (self):self._botonhomelaunch = "boton_resumen"
            elif verificabotonresumenapp2 (self):self._botonhomelaunch = "boton_resumen"
            elif verificabotonbuildingapp (self): self._botonhomelaunch = "boton_buildingAPP"
            elif verificabotonopenapp (self): self._botonhomelaunch = "boton_openAPP"
            elif verificabotonopenapp2 (self):  self._botonhomelaunch = "boton_openAPP"
            else: self._botonhomelaunch=False
            return self._botonhomelaunch

        def estadodebotonenhomeEurope(self):
            try:
                def verificabotoncreate (self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Create an app")))
                        )    
                        return True
                    except :
                        return False


                def verificabotonresumenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Resume app")))
                        )
                        return True
                    except :
                        print ("linea 109 no se encontro el texto: Resume app")
                        return False

                def verificabotonresumenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Paused in Europe")))
                        )
                        return True
                    except :
                        print ("linea 119 no se encontro el texto: Paused in Europe")
                        return False         
                def verificabotonbuildingapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Building in Europe")))
                        )
                        return True
                    except :
                        print ("linea 128 no se encontro el texto: Building in Europe")
                        return False                                  

                def verificabotonopenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Open in browser")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 138 no se encontro el texto: Open in browser")
                        return False
                def verificabotonopenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 0.5)
                        .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Running in Europe")))   
                        )                                                                                                                  
                        return True
                    except :
                        print ("linea 147 no se encontro el texto: Running in Europe")
                        return False                        

            except :
                print ("error homeweb 20-48 ")
                return False

            if verificabotoncreate (self): self._botonhomelaunch = "boton_createAPP" 
            elif verificabotonresumenapp (self):self._botonhomelaunch = "boton_resumen"
            elif verificabotonresumenapp2 (self):self._botonhomelaunch = "boton_resumen"
            elif verificabotonbuildingapp (self): self._botonhomelaunch = "boton_buildingAPP"
            elif verificabotonopenapp (self): self._botonhomelaunch = "boton_openAPP"
            elif verificabotonopenapp2 (self):  self._botonhomelaunch = "boton_openAPP"
            else: self._botonhomelaunch=False
            return self._botonhomelaunch







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