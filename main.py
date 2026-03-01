from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys   
import time

service = Service("msedgedriver.exe")
drive = webdriver.Edge(service=service)

#Parte 1-Login
drive.get("https://webdriveruniversity.com/Login-Portal/index.html?")
drive.maximize_window()

WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='text']"))
)

#Combinación-1
username_input = drive.find_element(By.XPATH, "//input[@id='text']")
username_input.clear()
username_input.send_keys("kevin")

password_input = drive.find_element(By.XPATH, "//input[@id='password']")
password_input.clear()
password_input.send_keys("12345")

login_btn = drive.find_element(By.XPATH, "//button[@id='login-button']")
login_btn.click()

WebDriverWait(drive, 5).until(EC.alert_is_present())
alert = drive.switch_to.alert
time.sleep(1)        
alert.accept()
time.sleep(1)

#Combinación-2
username_input = drive.find_element(By.XPATH, "//input[@id='text']")
username_input.clear()
username_input.send_keys("Gonzalo")

password_input = drive.find_element(By.XPATH, "//input[@id='password']")
password_input.clear()
password_input.send_keys("Ark34")

login_btn = drive.find_element(By.XPATH, "//button[@id='login-button']")
login_btn.click()

WebDriverWait(drive, 5).until(EC.alert_is_present())
alert = drive.switch_to.alert
time.sleep(1)
alert.accept()
time.sleep(1)

#Combinación-3
username_input = drive.find_element(By.XPATH, "//input[@id='text']")
username_input.clear()
username_input.send_keys("webdriver")

password_input = drive.find_element(By.XPATH, "//input[@id='password']")
password_input.clear()
password_input.send_keys("webdriver123")

login_btn = drive.find_element(By.XPATH, "//button[@id='login-button']")
login_btn.click()

WebDriverWait(drive, 5).until(EC.alert_is_present())
alert = drive.switch_to.alert
time.sleep(2)
alert.accept()
time.sleep(1)


#Parte 2-To Do List 
drive.get("https://webdriveruniversity.com/To-Do-List/index.html")

WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'], input"))
)
#Contar los elementos iniciales para la validacion final
initial_items = drive.find_elements(By.CSS_SELECTOR, "ul li, li")
initial_count = len(initial_items)
time.sleep(2) 

#Agregar tarea
task_input = drive.find_element(By.CSS_SELECTOR, "input[type='text'], input")
task_input.clear()
task_input.send_keys("Hacer Taller 2")
task_input.send_keys(Keys.ENTER)

# esperar hasta que aparezca un nuevo item en la lista
WebDriverWait(drive, 5).until(
    lambda d: len(d.find_elements(By.CSS_SELECTOR, "ul li, li")) > initial_count
)
time.sleep(2) 

# Marcar la tarea como completada
new_item = drive.find_element(By.XPATH, "//li[normalize-space() = 'Hacer Taller 2']")
new_item.click()
time.sleep(2)  

# Eliminar la tarea
drive.execute_script("arguments[0].remove();", new_item)
time.sleep(2)

#Validar estado final
final_items = drive.find_elements(By.CSS_SELECTOR, "ul li, li")
final_count = len(final_items)

if final_count != initial_count:
    raise Exception(f"Validación fallida: items iniciales {initial_count}, items finales {final_count}")


time.sleep(1)
drive.quit()