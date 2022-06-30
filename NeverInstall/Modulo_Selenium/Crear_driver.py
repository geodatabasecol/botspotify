from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def crear_driver():
    opt = webdriver.ChromeOptions()

    opt.page_load_strategy = 'normal'        
    opt.add_argument("--disable-xss-auditor")
    opt.add_argument("--disable-web-security")
    opt.add_argument("--allow-running-insecure-content")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-setuid-sandbox")
    opt.add_argument("--disable-webgl")
    opt.add_argument("--enable-popup-blocking")
    opt.add_argument('--ignore-ssl-errors=yes')
    opt.add_argument('--ignore-certificate-errors')  
    opt.add_argument('--start-maximized')
    opt.add_argument('--disable-dev-shm-usage')    
    opt.add_argument('--disable-infobars')    
    opt.add_argument("--incognito")   
    opt.add_argument('--disable-gpu')
    opt.add_experimental_option("excludeSwitches", ["enable-logging",'enable-automation'])
    # prefs = {"profile.managed_default_content_settings.images": 2,
    #          'notifications': 2,
    #          }
    # opt.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(20)
    return driver 



def actualizar_url(driver,url): 
  driver.get(url)