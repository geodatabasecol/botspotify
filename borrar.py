import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options


def func(threads):
  options = Options()
  options.page_load_strategy = 'normal'
  options.add_argument('--no-sandbox')
  options.add_argument('--start-maximized')
  #options.add_argument('--start-fullscreen')
  options.add_argument('--single-process')
  options.add_argument('--disable-dev-shm-usage')
  options.add_argument("--incognito")
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_experimental_option('useAutomationExtension', False)
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-infobars")
  driver = webdriver.Chrome(options=options)
  driver.get(url)
  time.sleep(20)
  

  threads.wait()


url='https://nordvpn.com/es/what-is-my-ip/'

numero_multitareas = 20

barrier = Barrier(numero_multitareas)

threads = []

for _ in range(numero_multitareas):
	i = Thread(target=func, args=(barrier,))
	i.start()
	threads.append(i)

for i in threads:
	i.join()