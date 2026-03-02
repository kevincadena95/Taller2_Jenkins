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


#Parte 4-Iframes
drive.get("https://webdriveruniversity.com/IFrame/index.html")

WebDriverWait(drive, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
)

find_out_more_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Find Out More!')]"))
)
find_out_more_btn.click()

modal_title = WebDriverWait(drive, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-title"))
)

if "webdriveruniversity" not in modal_title.text.lower():
    raise Exception(f"No se encontró el texto esperado en el modal del iframe: '{modal_title.text}'")

close_modal_btn = drive.find_element(By.XPATH, "//button[contains(., 'Close')]")
close_modal_btn.click()

WebDriverWait(drive, 10).until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal.show"))
)

# Volver al DOM principal
drive.switch_to.default_content()

# Ir a Popup & Alerts
drive.get("https://webdriveruniversity.com/Popup-Alerts/index.html")

# Alert
alert_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.ID, "button1"))
)
alert_btn.click()

WebDriverWait(drive, 10).until(EC.alert_is_present())
alert = drive.switch_to.alert

if "alert" not in alert.text.lower():
    raise Exception(f"Texto inesperado en Alert: '{alert.text}'")

alert.accept()

# Confirm
confirm_btn = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.ID, "button4"))
)
confirm_btn.click()

WebDriverWait(drive, 10).until(EC.alert_is_present())
confirm_alert = drive.switch_to.alert

if "press a button" not in confirm_alert.text.lower():
    raise Exception(f"Texto inesperado en Confirm: '{confirm_alert.text}'")

confirm_alert.accept()

confirm_result = WebDriverWait(drive, 10).until(
    EC.visibility_of_element_located((By.ID, "confirm-alert-text"))
)

if "ok" not in confirm_result.text.lower():
    raise Exception(f"No se reflejó OK en el resultado del Confirm: '{confirm_result.text}'")

# Prompt
drive.execute_script(
    "window.__prompt_result = null;"
    "setTimeout(function(){ window.__prompt_result = prompt('Escribe tu nombre'); }, 100);"
)

WebDriverWait(drive, 10).until(EC.alert_is_present())
prompt_alert = drive.switch_to.alert

if "nombre" not in prompt_alert.text.lower():
    raise Exception(f"Texto inesperado en Prompt: '{prompt_alert.text}'")

prompt_alert.send_keys("Mateo")
prompt_alert.accept()

WebDriverWait(drive, 10).until(
    lambda d: d.execute_script("return window.__prompt_result;") is not None
)

prompt_result = drive.execute_script("return window.__prompt_result;")

if prompt_result != "Mateo":
    raise Exception(f"Resultado inesperado en Prompt. Esperado 'Mateo' y se obtuvo '{prompt_result}'")



time.sleep(1)
drive.quit()