from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qaomni.annalect.com/login")
driver.maximize_window()
time.sleep(3)

# sen = driver.execute_script('return document.querySelector("#portal-login > portal-login").shadowRoot.querySelector("#username")')
# driver.execute_script('arguments[0].value = "test"; arguments[0].dispatchEvent(new Event("input", { bubbles: true }));', sen)

#JS PATH
# document.querySelector("#portal-login > portal-login").shadowRoot.querySelector("#username")
# Both upper and lower methods work
shadow_host = driver.find_element(By.CSS_SELECTOR, "#portal-login > portal-login")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
username_field = shadow_root.find_element(By.CSS_SELECTOR, "#username")
username_field.send_keys("campaign.superadmin@test.com")
time.sleep(4)
# Sign in
sign_in = shadow_root.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
sign_in.click()
time.sleep(10)
# Password
# document.querySelector("#portal-login > portal-login").shadowRoot.querySelector("omni-style > div > div.login-form-container > form > div.password > portal-password").shadowRoot.querySelector("#password")
# shadow_host1 = driver.find_element(By.CSS_SELECTOR, "omni-style > div > div.login-form-container > form > div.password > portal-password")
# shadow_root1 = driver.execute_script("return arguments[0].shadowRoot",shadow_host1)

password = shadow_root.find_element(By.CSS_SELECTOR, "input[type = 'password']")
password.send_keys("Nj9=/@M%fUs1KJ")
time.sleep(5)