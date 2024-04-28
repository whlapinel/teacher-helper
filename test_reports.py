import pandas as pd
import find_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time



def get_report(class_id, test_id, test_name, driver: webdriver, wait: WebDriverWait):
    download_report(class_id, test_id, test_name, driver, wait)
    file_path = find_csv.get_latest_csv()
    report = load_report(file_path)
    return report


def download_report(class_id, test_id, test_name, driver: webdriver, wait: WebDriverWait):
    # fixme: this url is correct but not if you go to the page manually
    # must mouse over the following element a['data-fullname'=test_name] and then click on 
    # a.openBigDialog with href below to get the modal for the test_id. (element text is "Reports")
    driver.get(f'https://app.masteryconnect.com/classrooms/{class_id}')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"a[data-fullname='{test_name}']")))
    print("found dropdown menu element")
        # move mouse to div#data_scroller
        # hold shift key to scroll right
        # scroll to element
        # hover over dropdown element
        # click on "Reports" element
    action_chains.ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .pause(1)\
        .move_to_element(driver.find_element(By.CSS_SELECTOR, 'div#data_scroller'))\
        .pause(2)\
        .move_to_element(driver.find_element(By.CSS_SELECTOR, f"a[data-fullname='{test_name}']"))\
        .pause(2)\
        .move_to_element(driver.find_element(By.CSS_SELECTOR, f"a.openBigDialog[href='/classrooms/{class_id}/benchmarks/{test_id}/modal?tab=reports']"))\
        .pause(2)\
        .click()\
        .perform()
    download_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#ia-csv-button')))
    download_btn.click()
    time.sleep(5)  # give time for file to download


def load_report(file_path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df
