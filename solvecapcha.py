
import os
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'normal'
browser = webdriver.Chrome(options=options)
browser.get('https://www.google.com/recaptcha/api2/demo')




def solveRecaptcha(sitekey, url):
    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result

result = solveRecaptcha(
    "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    "https://www.google.com/recaptcha/api2/demo"
)

code = result['code']

print(code)

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
)

browser.execute_script(
    "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

browser.find_element(By.ID, "recaptcha-demo-submit").click()

time.sleep(120)

