from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from Modulo_neverInstall.SingIn.singingoogle import *
from Modulo_Selenium.Crear_driver import *



def crearappinicial(driver):  #crear app, resuelto no se usa porque la app siempre va estar creada
        
        try:
           (WebDriverWait(driver, 3)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/a')))
            .click()
            )
        except TimeoutException:
            return False

        return True

def click_boton_openAPP(driver):

        try:
            (WebDriverWait(driver, 20)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/button')))
            .click()
            )
            print("click boton_openAPP")
            
           
        except TimeoutException:
            click_boton_openAPP() 
        #CONTINUA AQUI REGISTRAR EN LA BD NEVERINSTAL EL ESTADO 1 PARA EL TYNKTASK ACTIVO
        # SOLO EJECUTA TYNKTASK SI ESTA EN ESTADO 0 (DISPONIBLE)    
        return True        

def click_botonresume(driver):
        try:
            (WebDriverWait(driver, 3)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/div/button')))
            .click()
            )
        except TimeoutException:
            pass

        try:
            (WebDriverWait(driver, 20)
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div[2]/div/div/div/div/div/div[2]/div/div/div[6]/div[1]/div/button')))
            .click()
            )
            print("click click_botonresume")    

        except TimeoutException:
            click_botonresume()
        #CONTINUA AQUI REGISTRAR EN LA BD NEVERINSTAL EL ESTADO 1 PARA EL TYNKTASK ACTIVO
        # SOLO EJECUTA TYNKTASK SI ESTA EN ESTADO 0 (DISPONIBLE)    
        return True

