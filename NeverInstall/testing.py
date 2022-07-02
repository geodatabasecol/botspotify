import time
from ModuloEventosWindows.focus_google import *
from Modulo_Selenium.Crear_driver import *
from Modulo_Selenium.Tabs import *
from Modulo_neverInstall.estados_home import *
from Modulo_neverInstall.homeweb import *
from Modulo_neverInstall.evaluar import *
from Modulo_neverInstall.SingIn import *
from Modulo_DB.DB_conect import *
from Modulo_DB.Never_install.DB_Never_Install import *
from Modulo_DB.Never_install.DB_TinyTask import *
from selenium import *
import pyautogui as pyauto
import pygetwindow as gw
import sys
from Modulo_Selenium.mousecontrol import *
import asyncio
from  funciones import *

class test:
    def __init__(self,driver):
        self.driver= driver
    def verificabotonresumenapp(self):
        try:
            (WebDriverWait(self.driver, 0.1)
                .until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"))) 
            )
            
            return True
        except :
            
            return False

drivera =driver()
drivera.get("https://www.google.com")

mitest=test(drivera)

print(mitest.verificabotonresumenapp())