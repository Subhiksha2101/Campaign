from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pyshadow.main import Shadow
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Camp:
    driver = webdriver.Chrome()
    shadow = Shadow(driver)
    driver.get("https://qaomni.annalect.com/login")
    driver.maximize_window()
    time.sleep(10)

    # username
    username_parent = shadow.find_element("portal-login")
    username = shadow.get_shadow_element(username_parent, "#username")
    # password
    password_parent2 = shadow.get_shadow_element(username_parent, "portal-password")
    password = shadow.get_shadow_element(password_parent2, "#password")
    # Sign in
    sign_in = shadow.get_shadow_element(username_parent, "#eid-login-btn")


    username.send_keys("campaign.superadmin@test.com")
    sign_in.click()
    time.sleep(10)
    password.send_keys("Nj9=/@M%fUs1KJ")
    sign_in.click()
    time.sleep(30)

    # create tidbits
    tidbit_parent = shadow.find_element("portal-app-container")
    tidbit1 = shadow.get_shadow_element(tidbit_parent, "portal-nav-menu")
    tidbit2 = shadow.get_shadow_element(tidbit1, "omni-nav-menu")
    tidbit3 = shadow.get_shadow_element(tidbit2, "omni-style:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > omni-tooltip:nth-child(1) > div:nth-child(1) > a:nth-child(1) > omni-icon:nth-child(1)")
    tidbit4 = shadow.get_shadow_element(tidbit3, "div")
    tidbit4.click()
    time.sleep(20)
    new_win = driver.get("https://qatidbits.annalect.com/4359f5cc-6569-11e9-bc97-12cc0f0e8006/tidbits?omni=2")
    win_handles = driver.window_handles
    driver.switch_to.window(win_handles[0])
    time.sleep(20)

    # Add a tidbit
    add_parent = shadow.find_element("omni-app-container[component='tidbits-dev']")
    add1 = shadow.get_shadow_element(add_parent, "tidbits-container")
    add2 = shadow.get_shadow_element(add1, "tidbits-layout")
    add3 = shadow.get_shadow_element(add2, "tidbits-header")
    add4 = shadow.get_shadow_element(add3, "omni-icon[role='img']")
    add5 = shadow.get_shadow_element(add4, "div[part='icon']")
    add5.click()
    time.sleep(30)

    # title
    title_parent = shadow.find_element("om2-form-modal[data-gtm-form-interact-field-id='0']")
    title1 = shadow.get_shadow_element(title_parent, "#theform")
    title2 = shadow.get_shadow_element(title1, "input[title='At least one non-whitespace character'][name='title']")
    title2.send_keys("Testing")
    time.sleep(30)

    #dropdown-type
    type_parent = shadow.find_element("om2-form-modal[data-gtm-form-interact-field-id='0']")
    type1 = shadow.get_shadow_element(type_parent, "#theform")
    type2 = shadow.get_shadow_element(type1, " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(1) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    type = shadow.get_shadow_element(type2, "#dropdown-trigger-container")
    type.click()
    time.sleep(30)

    # Reasearch
    research_parent = shadow.find_element("om2-form-modal[data-gtm-form-interact-field-id='0']")
    research1 = shadow.get_shadow_element(research_parent, "#theform")
    research2 = shadow.get_shadow_element(research1, " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(1) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    research = shadow.get_shadow_element(research2, "div[title='Research']")
    research.click()
    time.sleep(30)

    # Tidbit url
    url_parent = shadow.find_element("om2-form-modal[data-gtm-form-interact-field-id='0']")
    url1 = shadow.get_shadow_element(url_parent, "#theform")
    url = shadow.get_shadow_element(url1, "input[title='At least one non-whitespace character'][name='url']")
    url.send_keys("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(30)

    # scroll
    driver.execute_script("arguments[0].scrollIntoView(true);", url)
    time.sleep(30)

    # save
    save_parent = shadow.find_element("om2-form-modal[data-gtm-form-interact-field-id='0']")
    save = shadow.get_shadow_element(save_parent, ".ml-3")
    save.click()
    time.sleep(30)

Camp()


