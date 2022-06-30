
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class home:
    def __init__(self,driver,accname) -> None:
            self.driver=driver
            self.clickbotonopenAPP=False
            self.clickbotonresumn=False
            self._accname=accname
            self._regiondelservidor=""

    def verificabotoncreate (self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                        .until(expected_conditions.visibility_of_element_located((By.XPATH, "// a[contains(text(),\'Create an app')]"))) 
                        )    
                        self._botonhomelaunch="Create an app"
                        return True

                    except :
                        
                        return False

    def verificabotonresumenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                            .until(expected_conditions.visibility_of_element_located((By.XPATH, "// span[contains(text(),\'Resume app')]"))) 
                        )
                        self._botonhomelaunch="Resume app"
                        return True
                    except :
                        return False

    def verificabotonresumenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                            .until(expected_conditions.visibility_of_element_located((By.XPATH, f"// div[contains(text(),\'Paused in {self._regiondelservidor}')]"))) 
                        )
                        self._botonhomelaunch="Resume app"
                        return True
                    except :
                        return False       
    def verificabotonbuildingapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                        .until(expected_conditions.visibility_of_element_located((By.XPATH, f"// div[contains(text(),\'Building in {self._regiondelservidor}')]"))) 
                        )
                        self._botonhomelaunch="Building...."
                        return True
                    except :
                        return False                                  

    def verificabotonopenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                        .until(expected_conditions.visibility_of_element_located((By.XPATH, "// span[contains(text(),\'Open in browser')]"))) 
                        )
                        self._botonhomelaunch="Open in browser"                                                                                                                  
                        return True
                    except :
                        return False

    def verificabotonopenapp2(self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                        .until(expected_conditions.visibility_of_element_located((By.XPATH, f"// div[contains(text(),\'Running in {self._regiondelservidor}')]"))) 
                        )
                        self._botonhomelaunch="Open in browser"                                                                                                                  
                        return True
                    except :
                        return None                        



    def accioninicialenhome(self):
        if self.verificabotoncreate()==True:
            print("Boton Create APP..",self._accname)
            self.driver.close()
            return False
        if self.verificabotonresumenapp()==True:
           self.clickbotonresumenapp()
        
        if self.verificabotonbuildingapp()==True:
            
            self.building()
        if self.verificabotonopenapp()==True:
            self.clickboton_openAPP()   
        
                              
        #CLICKS BOTONES
    def clickbotonresumenapp(self):
        try:
            (WebDriverWait(self.driver, 0.1)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, "// span[contains(text(),\'Resume app')]"))) 
            .click()
            )
            self.clickbotonresumn=True
            print("Click botonResumenAPP",self._accname)
        except :
                self.accioninicialenhome()
        if  self.clickbotonresumn==False:
            self.clickbotonresumenapp()                 
   
    def building(self):
        a= self.verificabotonbuildingapp()
        while a==True:
            print("Building....",self._accname)
            time.sleep(7)
            a=self.verificabotonbuildingapp()
        time.sleep(1)
        
     


    def clickboton_openAPP(self):
        try:
            (WebDriverWait(self.driver, 0.1)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, "// span[contains(text(),\'Open in browser')]"))) 
            ).click()
            self.clickbotonopenAPP=True   
            print("Click boton_openAPP",self._accname)
            
        except :
                time.sleep(2)
                self.clickboton_openAPP()  
        
        if  self.clickbotonopenAPP==False:
            self.clickboton_openAPP()
    
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