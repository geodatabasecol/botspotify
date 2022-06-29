from Modulo_Selenium.Crear_driver import crear_driver


driver =crear_driver()
from selenium.webdriver.support.ui import WebDriverWait
def document_initialised(driver):
    return driver.execute_script("return initialised")

driver.navigate("file:///race_condition.html")
WebDriverWait(driver, timeout=10).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"