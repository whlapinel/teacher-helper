import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import id_numbers
import users
import test_scores
import login
from analysis import Analysis, get_analysis, write_to_csv
from test_scores import Score

if __name__ == '__main__':
    run = True
    while run:
        # prompt user to enter passcode
        pin_input = input("Enter pin: ")
        if pin_input != '1234':
            print("Incorrect passcode. Exiting...")
            run = False
            continue
        
        
        # prompt user to enter exact name of test to be analyzed
        
        # prompt user to enter name to give the report
        
        user = users.User()
        if not user.load_from_config():
            user.construct_from_input()
            user.save_to_config()
        print(user)
        run_input = input("continue? (Y/N): ")
        if run_input == 'N':
            run = False
            continue
        has_ml_input: str = input('is there an ML version to your test? (Y/N): ')
        ml_test_name: str = ''
        has_ml = False
        if has_ml_input == 'Y':
            ml_test_name = input('Enter name of ML version: ')
            has_ml = True
        std_test_name = 'Unit 5 Test (Standard) Spring 2024 pdf'
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 30)
        login.log_in(user, driver, wait)
        std_test_id = 0
        ml_test_id = 0
        analyses: [Analysis] = []
        for class_name in user.classroom_names:
            print(f"getting test results for class:{class_name}")
            class_id = id_numbers.get_class_id(driver, wait, class_name)
            std_analysis: Analysis = get_analysis(class_name, class_id, std_test_name, driver, wait)
            analyses.append(std_analysis)
            print(std_analysis)
            if has_ml:
                ml_analysis: Analysis = get_analysis(class_name, class_id, ml_test_name, driver, wait)
                print(ml_analysis)
                analyses.append(ml_analysis)
        for analysis in analyses:
            print(analysis)
        write_to_csv("Unit 5 Test", analyses)
        driver.quit()
        run = False
