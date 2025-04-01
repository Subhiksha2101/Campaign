from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pyshadow.main import Shadow
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Camp:
    # Initialize the driver
    driver = webdriver.Chrome()
    shadow = Shadow(driver)
    driver.get("https://qaomni.annalect.com/login")
    driver.maximize_window()
    time.sleep(10)

    # Handle username and password inputs
    username_parent = shadow.find_element("portal-login")
    username = shadow.get_shadow_element(username_parent, "#username")
    password_parent = shadow.get_shadow_element(username_parent, "portal-password")
    password = shadow.get_shadow_element(password_parent, "#password")
    sign_in = shadow.get_shadow_element(username_parent, "#eid-login-btn")

    username.send_keys("campaign.superadmin@test.com")
    sign_in.click()
    time.sleep(10)
    password.send_keys("Nj9=/@M%fUs1KJ")
    sign_in.click()
    time.sleep(30)

    # Navigate to "Create Tidbits"
    tidbit_parent = shadow.find_element("portal-app-container")
    tidbit1 = shadow.get_shadow_element(tidbit_parent, "portal-nav-menu")
    tidbit2 = shadow.get_shadow_element(tidbit1, "omni-nav-menu")
    tidbit3 = shadow.get_shadow_element(
        tidbit2,
        "omni-style:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > omni-tooltip:nth-child(1) > div:nth-child(1) > a:nth-child(1) > omni-icon:nth-child(1)",
    )
    tidbit4 = shadow.get_shadow_element(tidbit3, "div")

    tidbit4.click()
    time.sleep(20)

    # Switch to iframe
    iframe = shadow.get_shadow_element(tidbit_parent, "portal-iframe-container")
    iframe1 = shadow.get_shadow_element(iframe, "portal-iframe-element[class='  ']")
    iframe2 = shadow.get_shadow_element(iframe1, "#iframe-861358633")

    # Wait for iframe to be available and switch
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe2))

    # Locate and click the "Add" button
    try:
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )
        add_button.click()
    except Exception as e:
        print(f"Error locating button: {e}")

    time.sleep(30)
    driver.switch_to.default_content()


Camp()
