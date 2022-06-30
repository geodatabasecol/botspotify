import time
from Modulo_Selenium.Crear_driver import crear_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver =crear_driver()
driver.get("http://bit.ly/vinayakgfg")
time.sleep(2)
def verificabotoncreate (driver):
    try:
        (WebDriverWait(driver, 0.5)
        .until(EC.visibility_of_element_located((By.XPATH,"// a[contains(text(),\'5 CHEAP HOLIDAY')]"))) 
        )
        return True
    except :
        return False

print(verificabotoncreate(driver))

