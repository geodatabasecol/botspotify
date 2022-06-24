
import time
from Modulo_DB.DB_TinyTask import *
from Modulo_neverInstall.homeweb.homeweb import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from Modulo_neverInstall.SingIn.singingoogle import *
from Modulo_Selenium.Crear_driver import *

def estadodebotonenhome(driver):
    global count1
    try:
        def verificabotoncreate ():
            try:
                (WebDriverWait(driver, 3)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/a')))
                )    
                return True
            except TimeoutException:
                return False

        def verificabotonresumenapp():
            try:
                (WebDriverWait(driver, 3)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/div/button')))
                )    
                return True
            except TimeoutException:
                return False

        def verificabotonopenapp():
            try:
                (WebDriverWait(driver, 3)
                .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/button/div/span')))
                )    
                return True
            except TimeoutException:
                return False
    
    
    except NoSuchElementException:
        print ("error homeweb 10-42 ")
        return False

    if verificabotoncreate ():
        estadoinicialwebneverinstall = "boton_createAPP"
        pass
    elif verificabotonresumenapp ():
        estadoinicialwebneverinstall = "boton_resumen"
        pass
    elif verificabotonopenapp (): 
        estadoinicialwebneverinstall = "boton_openAPP"
        pass
    else: 
        estadoinicialwebneverinstall=False
    return estadoinicialwebneverinstall
  #borrarvisualstudiocode('//*[@id="delete"]/div')


