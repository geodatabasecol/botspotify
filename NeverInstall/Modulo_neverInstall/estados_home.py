
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import asyncio

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
                        

    async def verificabotonresumenapp(self):
                    try:
                        (WebDriverWait(self.driver, 0.1)
                            .until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/div/button'))) 
                        )
                        
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



    async def accioninicialenhome(self,ventanaactiva):
        taskverificabotonresumen= asyncio.create_task(self.verificabotonresumenapp())
        task_taskverificabotonresumen= await taskverificabotonresumen
        print(f"Boton resumen{self._accname} : {task_taskverificabotonresumen}")
        if task_taskverificabotonresumen==True:
           task_clickbotonresumen =asyncio.create_task(self.clickbotonresumenapp(ventanaactiva))

           ventanaactiva= await task_clickbotonresumen
        return ventanaactiva

        '''

        task_verificabotonbuildingap=asyncio.create_task(self.verificabotonbuildingapp())
        val_task_verificabotonbuildingap= await task_verificabotonbuildingap
        if val_task_verificabotonbuildingap==True:
            task_build=asyncio.create_task( self.building())
            await task_build
        
        task_verificabotonopenapp = asyncio.create_task(self.verificabotonopenapp())
        val_verificabotonopenapp= await task_verificabotonopenapp
        
        if val_verificabotonopenapp==True:
            task_clickboton_openAPP=asyncio.create_task(self.clickboton_openAPP(ventanaactiva))
            ventanaactiva=await task_clickboton_openAPP
        return ventanaactiva
        '''                                 
        #CLICKS BOTONES
    async def clickbotonresumenapp(self,ventanaactiva):
        ventanaactiva=1
        try:
            (WebDriverWait(self.driver, 0.1)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/div/button'))) 
            .click()
            .minimize_window()
            )
            self.clickbotonresumn=True
            print("Click botonResumenAPP",self._accname)
            await asyncio.sleep(1)
            return ventanaactiva
        except :
                 taskvolverahome=asyncio.create_task(self.accioninicialenhome(ventanaactiva))
                 await taskvolverahome
                 return ventanaactiva
        

    
    async def building(self):
        task_veri_btnbuildingapp= asyncio.create_task(self.verificabotonbuildingapp())
        val= await task_veri_btnbuildingapp
        while val==True:
            print("Building....",self._accname)
            await asyncio.sleep(20)
            task_verificabotonbuilapp= asyncio.create_task(self.verificabotonbuildingapp())
            val= await task_verificabotonbuilapp
        await asyncio.sleep(1)
        
    async def clickboton_openAPP(self,ventanaactiva):
        
        while ventanaactiva==0:
            ventanaactiva=1
            try:
                (WebDriverWait(self.driver, 0.1)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, "// span[contains(text(),\'Open in browser')]"))) 
                ).click()
                self.clickbotonopenAPP=True   
                print("Click boton_openAPP",self._accname)
                self.driver.maximize_window()
                return ventanaactiva
                
            except :
                time.sleep(5)
                self.clickboton_openAPP(ventanaactiva)  
        
        if  self.clickbotonopenAPP==False:
            self.clickboton_openAPP(ventanaactiva)
        
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