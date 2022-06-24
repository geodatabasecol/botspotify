import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options



def crear_driver(url_inicial):  
 
  options = Options()
  options.page_load_strategy = 'normal'
  driver = webdriver.Chrome(options=options)
  options.page_load_strategy = 'normal'
  options.add_argument('--no-sandbox')
  options.add_argument('--start-maximized')
  #options.add_argument('--start-fullscreen')
  options.add_argument('--single-process')
  options.add_argument('--disable-dev-shm-usage')
  #options.add_argument("--incognito")
  options.add_argument('--enable-gpu')
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_experimental_option('useAutomationExtension', False)
  options.add_experimental_option("excludeSwitches", ["disable-automation"])
  options.add_argument("disable-infobars")
  driver.implicitly_wait(1.5)
  driver.get(url_inicial) #pasa la URL inicial 
  driver.maximize_window()
  return driver
