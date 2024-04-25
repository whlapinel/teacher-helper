import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def log_in(user, driver, wait):
    username = user.username
    password = user.password
    driver.get('https://launchpad.classlink.com/cmsk12')
    sign_in_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.saml')))
    sign_in_btn.click()
    time.sleep(5)
    usr_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#userNameInput')))
    pwd_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#passwordInput')))
    submit_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span#submitButton')))
    usr_input.send_keys(username)
    pwd_input.send_keys(password)
    submit_btn.click()
    text_me_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#verificationOption0')))
    time.sleep(1)
    text_me_link.click()
    code = input("Please enter the verification code sent to your phone: ")
    code_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#verificationCodeInput')))
    code_input.send_keys(code)
    sign_in_btn2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#signInButton')))
    sign_in_btn2.click()
    selector = 'application[aria-label="MasteryConnect"] > div.cl-clip-img-ctnr.ng-star-inserted'
    canvas_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    original_tab = driver.current_window_handle
    assert len(driver.window_handles) == 1
    canvas_btn.click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_tab:
            driver.switch_to.window(window_handle)
            break
    wait.until(EC.title_is("Mastery Connect :: Home"))
    return driver
