
from concurrent.futures import thread
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import asyncio
# INICIO A HACER LOGIN con google
class singinggoogle:
    def __init__ (self,driver,emails,password,accname,url_inicial):
        self.driver=driver
        self.email=emails
        self.password= password
        self.accname=accname
        
        self.url_inicial=url_inicial


    async def iniciarcongoogle(self):
        def check_exist_by_XPATH_botton (XPATH):
            global count1
            try:
                self.driver.find_element(By.XPATH, XPATH)
            except :
                if count1<=3: 
                    count1+=1
                    print (count1)
                    return time.sleep(1), check_exist_by_XPATH_botton (XPATH)
                else: 
                    
                    return False
            count1=0
            try:
                ingresar = self.driver.find_element(By.XPATH,XPATH)
                ingresar.click()
                return True
            except:
                return False

        if check_exist_by_XPATH_botton ("/html/body/div[1]/div/main/div/div[2]/div/div[3]/button[1]/div/div")==False:
            print ("No existe botton iniciar con google 9-24",self.accname)
            return False
   


     # ingresar el correo 
    async def ingresandocorreo(self):
        def check_exist_by_ID_sendkey (ID_,send_keys_):
            global count1
            try:
                self.driver.find_element(By.ID, ID_)
            except :
                if count1<=3: 
                    count1+=1
                    return time.sleep(1), check_exist_by_ID_sendkey(ID_,send_keys_)
                else: 
                    
                    return False
            count1=0
            try:
                self.driver.find_element(By.ID, ID_).send_keys(send_keys_)
                return True
            except:
                return False
            

        if check_exist_by_ID_sendkey("identifierId",self.email)==False:
            print ("No se pudo dar click en boton singingoogle Line 32-45")
            self.driver.close()
            
            return False
    #click en siguiente 
        def check_exist_by_XPATH_botton (XPATH):
            global count1
            try:
                self.driver.find_element(By.XPATH, XPATH)
            except :
                if count1<=3: 
                    count1+=1
                    print (count1)
                    return time.sleep(1), check_exist_by_XPATH_botton (XPATH)
                else:
                    return False
                
            count1=0
            try:
                ingresar = self.driver.find_element(By.XPATH,XPATH)
                ingresar.click()
                return True
            except:
                return False
        if check_exist_by_XPATH_botton ('//*[@id="identifierNext"]/div/button/span')== False:
            print ("No se pudo dar click en boton singingoogle Line 51-66")
            return False


  # ingresar la contraseña  
    async def ingresandocontrasena(self):
        def check_exist_by_ID_sendkey (XPATH,send_keys_):
            global count1
            try:
                self.driver.find_element(By.XPATH, XPATH)
            except :
                if count1<=3: 
                    count1+=1
                    print (count1)
                    return time.sleep(1), check_exist_by_ID_sendkey(XPATH,send_keys_)
                else:
                    return False
            count1=0
            self.driver.find_element(By.XPATH, XPATH).send_keys(send_keys_)
            return True
            

        if check_exist_by_ID_sendkey('//*[@id="password"]/div[1]/div/div[1]/input',self.password)==False:
            print ("No se pudo dar click en boton singingoogle Line 72-85")
            return False


    #click en siguiente 
        def check_exist_by_XPATH_botton (XPATH):
            global count1
            try:
                self.driver.find_element(By.XPATH, XPATH)
            except :
                if count1<=3: 
                    count1+=1
                    print (count1)
                    return time.sleep(1), check_exist_by_XPATH_botton (XPATH)
                else: self.driver.close(), exit()
            count1=0
            try:
                ingresar = self.driver.find_element(By.XPATH,XPATH)
                ingresar.click()
                return True
            except:
                return False
        if check_exist_by_XPATH_botton ('//*[@id="passwordNext"]/div/button/span')==False:
            print ("No se pudo dar click en boton singingoogle Line 94-107")
            return False
        
        return True
    
    async def primerpasoiniciarlogingoogle(self):

        
        try:
             task_loadurl=self.driver.get(self.url_inicial)
             await task_loadurl
  #
        except :
        
            pass
        
        print("Load NeverInstall.com ",self.accname)

        #commandWindows.hacerfocusenlaventana(accname)
           
        task_ingresacongoogle= asyncio.create_task(self.iniciarcongoogle())
        await task_ingresacongoogle

        print("Singup con google account ", self.accname)
        task_ingresarcorreo= asyncio.create_task(self.ingresandocorreo())
        await task_ingresarcorreo
        
        print ("Ingresando correo el correo ", self.accname)
        task_contrasena= asyncio.create_task(self.ingresandocontrasena())
        await task_contrasena
        print ("Ingresando contraseña ", self.accname)