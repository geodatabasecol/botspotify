import time
from Modulo_Selenium.Crear_driver import crear_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver =crear_driver()
driver.get("https://www.google.com")
time.sleep(2)
def verificabotoncreate (driver):
    try:
        (WebDriverWait(driver, 0.5)
        .until(EC.visibility_of_element_located((By.CLASS_NAME, "NKcBbd"))) 
        )
        return True
    except :
        return False


print(verificabotoncreate(driver))