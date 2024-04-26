import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import id_numbers
import users
import test_scores
import login
from analysis import Analysis, get_analysis, write_to_csv
from test_scores import Score
from typing import List
from menu import get_choice

def get_analysis_report(user: users.User):
    report_name = input("Enter name for report: ")
    has_std = False
    types = input("Enter test types (e.g.standard, ml, honors): ")
    types = types.split(',')
    for test_type in types:
        
    for i in range (user.classroom_names):
        test_matrix = [{'Classroom': user.classroom_names[i], 'Standard': False, 'ML': False, 'Honors': False}]
        print(f"Classroom: {user.classroom_names[i]}")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)
    login.log_in(user, driver, wait)
    std_test_id = 0
    ml_test_id = 0
    analyses: List[Analysis] = []
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
        if has_hon:
            hon_analysis: Analysis = get_analysis(class_name, class_id, hon_test_name, driver, wait)
            if not hon_analysis:
                print("Honors test not found")
                continue
            print(hon_analysis)
            analyses.append(hon_analysis)
    for analysis in analyses:
        print(analysis)
    write_to_csv("Unit 5 Test", analyses)
    driver.quit()

if __name__ == '__main__':
    # prompt user to enter passcode
    # pin_input = input("Enter pin: ")
    # if pin_input != '1234':
    #     print("Incorrect passcode. Exiting...")
    #     run = False
    #     continue        
    # prompt user to enter exact name of test to be analyzed
    # prompt user to enter name to give the report
    user = users.User()
    if not user.load_from_config():
        user.construct_from_input()
        user.save_to_config()
    run = True
    while run:
        choice = get_choice()
        if choice == '2':
            print("Bye!")
            run = False
            continue
        if choice != '1':
            print("Invalid choice. Exiting...")
            run = False
            continue
        if choice == '1':
            get_analysis_report(user)
            continue