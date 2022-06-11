import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options
#asdsadsadsadas

def func (threads,emails, passwod,listaartista,itemsagregar):
  
  options = Options()
  options.page_load_strategy = 'normal'
  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(0.5)
  driver.get(login_spotify)
  time.sleep(2)
  print (driver.current_url)
  driver.find_element(By.ID,"login-username").send_keys(emails)
  driver.find_element(By.ID,"login-password").send_keys(passwod)
  ingresar = driver.find_element(By.ID,"login-button")
  ingresar.click()
  print("ok loging  ", emails)
  time.sleep(5)
  print (driver.current_url)
  driver.refresh()
  print ('refresh drive')
  time.sleep(30)
      
      
  threads.wait()


login_spotify = "https://accounts.spotify.com/en/login/?continue=https%3A//open.spotify.com/__noul__%3Fl2l%3D1%26nd%3D1&_locale=en-US"
numero_multitareas = 1

barrier = Barrier(numero_multitareas)
emails=["casadedosportres@gmail.com"]
passwod=['!asdf123456']
threads = []
listartistas=['michael jackson','eminen']

itemsagregar=[
[
],
[

]

]


for i in range(numero_multitareas):
	i = Thread(target=func, args=(barrier,emails[i],passwod[i],listartistas,itemsagregar))
	i.start()
	threads.append(i)

for i in threads:
	i.join()
 
 
