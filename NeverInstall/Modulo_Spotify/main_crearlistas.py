from fileinput import close
from subprocess import IDLE_PRIORITY_CLASS
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from threading import Thread, Barrier
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import requests

count1=0

def func (threads,emails, passwod,listaartista,itemsagregar):

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
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_argument('--disable-blink-features=AutomationControlled')
  options.add_experimental_option('useAutomationExtension', False)
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-infobars")
  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(1.5)
  driver.get(login_spotify)
  time.sleep(2)
  print (driver.current_url)
  
  def check_exist_by_ID_sendkey (ID_,send_keys_):
    global count1
    try:
      driver.find_element(By.ID, ID_)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_ID_sendkey(ID_,send_keys_)
      else: driver.close(), exit()
    count1=0
    return driver.find_element(By.ID, ID_).send_keys(send_keys_)
  
  def check_exist_by_ID_botton (ID_):
    global count1
    try:
      driver.find_element(By.ID, ID_)
    except NoSuchElementException:
      if count1<=3: 
        count1+=1
        print (count1)
        return time.sleep(5), check_exist_by_ID_botton(ID_)
      else: driver.close(), exit()
    count1=0
    ingresar = driver.find_element(By.ID,"login-button")
    return ingresar.click()
  
  
  check_exist_by_ID_sendkey("login-username",emails)
  check_exist_by_ID_sendkey("login-password",passwod)
  check_exist_by_ID_botton("login-button")
  
  #driver.find_element(By.ID,"login-username").send_keys(emails)
  #driver.find_element(By.ID,"login-password").send_keys(passwod)
  #ingresar = driver.find_element(By.ID,"login-button")
  #ingresar.click()
  print("ok loging  ", emails)
  time.sleep(5)
  print (driver.current_url)
  driver.refresh()
  print ('refresh drive')
  time.sleep(5)
  nuevalista= driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/nav/div[1]/div[2]/div/div[1]/button")
  nuevalista.click()
  print ('nueva lista click')
  time.sleep(5)
  
  time.sleep(5)
  print ('driver buscar lista ok')
  
  for  artista in listaartista:
    buscar= driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/section/div/div/input')
    buscar.clear()
    buscar.send_keys(artista)
    time.sleep(5)
    it=0
    for item in itemsagregar[it]:
      agregarcancion = driver.find_element(By.XPATH,item )
      agregarcancion.click()
      print("cancion agregada")
      time.sleep(5)
      it+=1



  threads.wait()
  


login_spotify = "https://accounts.spotify.com/en/login/?continue=https%3A//open.spotify.com/__noul__%3Fl2l%3D1%26nd%3D1&_locale=en-US"
numero_multitareas = 1

barrier = Barrier(numero_multitareas)
emails=["casadedosportres@gmail.com","sinlerest12@gmail.com", "fredysiyle33@gmail.com"]
passwod=['!asdf123456', '!asdf123456','!asdf123456']
threads = []
listartistas=['michael jackson','eminen']

itemsagregar=[
[
'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[2]/div/div[3]/button',
'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[3]/div/div[3]/button',
'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/div[3]/button'
],
[
'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div/div[3]/button',
'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[3]/div/div[3]/button',
'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/div[3]/button'
]

]


for i in range(numero_multitareas):
	i = Thread(target=func, args=(barrier,emails[i],passwod[i],listartistas,itemsagregar))
	i.start()
	threads.append(i)

for i in threads:
	i.join()
 
 
