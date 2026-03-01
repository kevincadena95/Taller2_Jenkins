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
    EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
)
#Contar los elementos iniciales para la validacion final
initial_tasks = drive.find_elements(By.XPATH, "//ul//li")
initial_vaidation = len(initial_tasks)
time.sleep(2) 

#Agregar tarea
task_input = drive.find_element(By.XPATH, "//input[@type='text']")
task_input.clear()
task_input.send_keys("Hacer Taller 2")
task_input.send_keys(Keys.ENTER)


#esperar hasta que aparezca un nuevo item en la lista 
WebDriverWait(drive, 5).until( 
    lambda d: len(d.find_elements(By.XPATH, "//ul//li")) > initial_vaidation )
time.sleep(1) 

# Marcar la tarea como completada
new_task = drive.find_element(By.XPATH, "//li[normalize-space() = 'Hacer Taller 2']")
new_task.click()
time.sleep(2)  

# Eliminar la tarea
drive.execute_script("arguments[0].remove();", new_task)
time.sleep(2)

#Validar estado final: es exitosa si los valores finales coinciden con los valore inicales antes de agregar y elimar la nueva tarea
final_tasks = drive.find_elements(By.XPATH, "//ul//li")
final_vaidation = len(final_tasks)

if final_vaidation == initial_vaidation:
    drive.execute_script("alert('Validación exitosa');")
else:
    drive.execute_script(f"alert('Validación fallida: {initial_vaidation} != {final_vaidation}');")

WebDriverWait(drive, 10).until(EC.alert_is_present())
time.sleep(3)
drive.switch_to.alert.accept()

drive.quit()