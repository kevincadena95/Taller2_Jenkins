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
time.sleep(2)        
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
time.sleep(2)
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
time.sleep(1) 

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
time.sleep(1)  

# Eliminar la tarea
drive.execute_script("arguments[0].remove();", new_task)
time.sleep(1)

#Validar estado final: es exitosa si los valores finales coinciden con los valore inicales antes de agregar y elimar la nueva tarea
final_tasks = drive.find_elements(By.XPATH, "//ul//li")
final_vaidation = len(final_tasks)

if final_vaidation == initial_vaidation:
    drive.execute_script("alert('Validación exitosa');")
else:
    drive.execute_script(f"alert('Validación fallida: {initial_vaidation} != {final_vaidation}');")

WebDriverWait(drive, 10).until(EC.alert_is_present())
time.sleep(2)
drive.switch_to.alert.accept()  

#Parte 4-Iframes
#Ir al módulo IFrame
drive.get("https://webdriveruniversity.com/IFrame/index.html")

#Cambiar al iframe
WebDriverWait(drive, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))


#Hacer clic en un elemento dentro (Our products)
our_products_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Our Products']")))
time.sleep(1)
our_products_btn.click()
time.sleep(1)

#Hacer clic en un elemento dentro del Our products
new_laptops_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//p[text()='New Laptops']")))
time.sleep(1)
new_laptops_btn.click()
time.sleep(1)

close_modal_btn = WebDriverWait(drive, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.), 'Close')]")))
time.sleep(1)
close_modal_btn.click()
time.sleep(1)

# Volver al DOM principal
drive.get("https://webdriveruniversity.com/")
time.sleep(1) 

# Ir a Popup & Alerts
drive.get("https://webdriveruniversity.com/Popup-Alerts/index.html")
time.sleep(1) 

# Alert
alert_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.ID, "button1")))
time.sleep(1) 
alert_btn.click()
time.sleep(1) 

WebDriverWait(drive, 10).until(EC.alert_is_present())
alert = drive.switch_to.alert
alert_text = alert.text.strip()
expected_alert_text = "I am an alert box!"
time.sleep(1) 
alert.accept()

if alert_text == expected_alert_text:
    drive.execute_script("alert('Validación de texto exitosa');")
else:
    drive.execute_script("alert('Validación fallida');")

time.sleep(1) 
WebDriverWait(drive, 10).until(EC.alert_is_present())
drive.switch_to.alert.accept()
time.sleep(1) 


# Confirm
confirm_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.ID, "button4")))
time.sleep(1) 
confirm_btn.click()
time.sleep(1) 

WebDriverWait(drive, 10).until(EC.alert_is_present())
confirm_alert = drive.switch_to.alert
confirm_text = confirm_alert.text.strip()
expected_confirm_text = "Press a button!"
time.sleep(1) 
confirm_alert.accept()  

if confirm_text == expected_confirm_text:
    drive.execute_script("alert('Validación de texto exitosa');")
else:
    drive.execute_script("alert('Validación fallida');")

time.sleep(1) 
WebDriverWait(drive, 10).until(EC.alert_is_present())
drive.switch_to.alert.accept()
time.sleep(1) 

# Prompt
prompt_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.ID, "button2")))
time.sleep(1) 
prompt_btn.click()
time.sleep(1) 

modal = WebDriverWait(drive, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
modal_text = modal.text

#Validar Textos
if "We can inject" in modal_text:
    drive.execute_script("alert('Validación exitosa');")
else:
    drive.execute_script("alert('Validación fallida');")

WebDriverWait(drive, 10).until(EC.alert_is_present())
time.sleep(1) 
drive.switch_to.alert.accept()

close_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']")))
time.sleep(1) 
close_btn.click()
time.sleep(1) 


drive.quit()