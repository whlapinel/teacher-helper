import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

import login


def download_csv(class_name, test_name, driver):
    # driver should already be on the MC home page
    time.sleep(10)
    driver.get('https://app.masteryconnect.com/home')
    classes_list = driver.find_element(By.CSS_SELECTOR, 'ul.classrooms_list')
    print("classes list: ", classes_list)
    class_links = classes_list.find_elements(By.CSS_SELECTOR, 'a')
    print(class_links)
    class_link = ''
    for link in class_links:
        print("link.text: ", link.text)
        if link.text == class_name:
            class_link = link
            print("matching class_link.text:", class_link.text)
    if not class_link:
        return None
    class_url = class_link.get_attribute('href')
    print("class_url:", class_url)
    parsed_url = urlparse(class_url)
    path = parsed_url.path
    class_number = path.strip('/').split('/')[-1]
    print("class_number: ", class_number)
    if not class_url:
        print("No match found for class name.")
        return None
    driver.get(class_url)
    time.sleep(15)
    test_link = driver.find_element(By.CSS_SELECTOR, 'a[data-fullname="' + test_name + '"]')
    test_url = test_link.get_attribute('href')
    print(test_url)
    parsed_url = urlparse(test_url)
    path = parsed_url.path
    test_id = path.strip('/').split('/')[-1]
    print(test_id)
    # below url should download the test scores in Excel
    download_url = 'https://app.masteryconnect.com/classrooms/' + class_number + '/export/' + test_id + '/options?b=1'
    print(download_url)
    driver.get(download_url)
    time.sleep(10)
    checkbox = driver.find_element(By.NAME, "export_options[show_percentages]")
    checkbox.click()
    time.sleep(2)
    checkbox2 = driver.find_element(By.NAME, "export_options[show_answers]")
    checkbox2.click()
    time.sleep(2)
    export_btn = driver.find_element(By.CSS_SELECTOR, 'button.no-disable')
    export_btn.click()
    time.sleep(10)
    return
