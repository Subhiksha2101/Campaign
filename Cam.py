from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pyshadow.main import Shadow

class Camp():
    driver = webdriver.Chrome()
    shadow = Shadow(driver)
    driver.get("https://qaomni.annalect.com/login")
    driver.maximize_window()
    time.sleep(10)

    # username
    username_parent = shadow.find_element("portal-login")
    username = shadow.get_shadow_element(username_parent, "#username")
    # username.send_keys("campaign.superadmin@test.com")
    # sign_in.click()
    # time.sleep(10)

    # password
    password_parent2 = shadow.get_shadow_element(username_parent, "portal-password")
    password = shadow.get_shadow_element(password_parent2, "#password")
    # Sign in
    sign_in = shadow.get_shadow_element(username_parent, "#eid-login-btn")
    # create

    username.send_keys("campaign.superadmin@test.com")
    sign_in.click()
    time.sleep(10)
    password.send_keys("Nj9=/@M%fUs1KJ")
    sign_in.click()
    time.sleep(30)

    # create_icon1 = shadow.find_elements("portal-app-container")
    # create_icon2 = shadow.get_shadow_element(create_icon1, "portal-nav-menu")
    # create_icon3 = shadow.get_shadow_element(create_icon2, "omni-nav-menu")
    # create_icon4 = shadow.get_shadow_element(create_icon3,
    #                                          "  omni-style:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > div:nth-child(3) > portal-create-menu:nth-child(1) > li:nth-child(1) > omni-tooltip:nth-child(1) > div:nth-child(1) > a:nth-child(1) > omni-icon:nth-child(1)")
    # create_icon = shadow.get_shadow_element(create_icon4, "div")
    # create_icon.click()
    # time.sleep(10)

Camp()
# camp()








