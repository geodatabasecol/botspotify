
from concurrent.futures import thread
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

 # INICIO A HACER LOGIN con google
class singinggoogle:
    def __init__ (self,driver,emails,password):
        self.driver=driver
        self.email=emails
        self.password= password
   
# ingresando con GOOGLE           
    def iniciarcongoogle(self):
        def check_exist_by_XPATH_botton (XPATH):
            global count1
            try:
                self.driver.find_element(By.XPATH, XPATH)
            except NoSuchElementException:
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
            print ("No existe botton iniciar con google 9-24")
            return False
   


     # ingresar el correo 
    def ingresandocorreo(self):
        def check_exist_by_ID_sendkey (ID_,send_keys_):
            global count1
            try:
                self.driver.find_element(By.ID, ID_)
            except NoSuchElementException:
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
            except NoSuchElementException:
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
    def ingresandocontrasena(self):
        def check_exist_by_ID_sendkey (XPATH,send_keys_):
            global count1
            try:
                self.driver.find_element(By.XPATH, XPATH)
            except NoSuchElementException:
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
            except NoSuchElementException:
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
    