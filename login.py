import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

def log_in(user):
    username = user.username
    password = user.password
    class_number = '5137260'
    test_name = 'Unit 5 Test (Standard) Spring 2024 pdf'
    # username = input("Enter your username: ")
    # password = input("Enter your password: ")
    driver = webdriver.Chrome()
    driver.get('https://launchpad.classlink.com/cmsk12')
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.saml.UseTMS')
    sign_in_btn.click()
    time.sleep(5)
    usr_input = driver.find_element(By.CSS_SELECTOR, 'input#userNameInput')
    pwd_input = driver.find_element(By.CSS_SELECTOR, 'input#passwordInput')
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'span#submitButton')
    usr_input.send_keys(username)
    pwd_input.send_keys(password)
    submit_btn.click()
    time.sleep(5)
    text_me_link = driver.find_element(By.CSS_SELECTOR, 'a#verificationOption0')
    text_me_link.click()
    code = input("Please enter the verification code sent to your phone: ")
    code_input = driver.find_element(By.CSS_SELECTOR, 'input#verificationCodeInput')
    code_input.send_keys(code)
    sign_in_btn2 = driver.find_element(By.CSS_SELECTOR, 'input#signInButton')
    sign_in_btn2.click()
    # next line is the problem line... not very surprised. let's try waiting
    time.sleep(15)
    # click on MasteryConnect app from LaunchPad
    selector = 'application[aria-label="MasteryConnect"] > div.cl-clip-img-ctnr.ng-star-inserted'
    canvas_btn = driver.find_element(By.CSS_SELECTOR, selector)
    canvas_btn.click()
    time.sleep(15)
    return driver
