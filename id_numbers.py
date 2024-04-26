from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC


def get_class_id(driver, wait, class_name):
    driver.get('https://app.masteryconnect.com/home')
    classes_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.classrooms_list')))
    print("classes list: ", classes_list)
    class_links = classes_list.find_elements(By.CSS_SELECTOR, 'a')
    print(class_links)
    class_link = None
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
    class_id = path.strip('/').split('/')[-1]
    print("class_id: ", class_id)
    return class_id


def get_test_id(class_id, driver, wait, test_name):

    class_url = f'https://app.masteryconnect.com/classrooms/{class_id}'
    driver.get(class_url)
    test_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-fullname="' + test_name + '"]')))
    if not test_link:
        return None
    test_url = test_link.get_attribute('href')
    print(test_url)
    parsed_url = urlparse(test_url)
    path = parsed_url.path
    test_id = path.strip('/').split('/')[-1]
    print(test_id)
    return test_id
