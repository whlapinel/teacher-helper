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



def view_classes(user: users.User) -> None:
    print("Classes:")
    for classroom in user.classrooms:
        print(classroom['name'])
        print(classroom['type'])
    return

def get_analysis_report(user: users.User):
    report_name = input("Enter name for report: ")
    test_names = []
    checked_types: List[str] = []
    for classroom in user.classrooms:
        if classroom['type'] not in checked_types:
            checked_types.append(classroom['type'])
            test_name = input(f"Enter name of {classroom['type']} test: ")
            test_names.append({"type": classroom['type'], "name": test_name})
    ml_test_name = input("Enter name of ML version: ")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)
    login.log_in(user, driver, wait)
    analyses: List[Analysis] = []
    for classroom in user.classrooms:
        print(f"getting test results for class:{classroom['name']} type:{classroom['type']}")
        test_name_filter = filter((lambda x: x["type"] == classroom['type']), test_names)
        test_name = list(test_name_filter)[0]["name"]
        class_id = id_numbers.get_class_id(driver, wait, classroom['name'])
        analysis: Analysis = get_analysis(classroom['name'], class_id, test_name, driver, wait)
        analyses.append(analysis)
        ml_analysis: Analysis = get_analysis(classroom['name'], class_id, ml_test_name, driver, wait)
        analyses.append(ml_analysis)
    for analysis in analyses:
        print(analysis)
    write_to_csv(report_name, analyses)
    driver.quit()

if __name__ == '__main__':
    # prompt user to enter passcode
    run = True
    user = users.User()
    if not user.load_from_config():
        user.construct_from_input()
        user.save_to_config()
    pin_input = input("Enter pin: ")
    if pin_input != user.pin:
        print("Incorrect passcode. Exiting...")
        run = False
    while run:
        choice = get_choice()
        if choice == '3':
            view_classes(user)
            continue
        if choice == '2':
            print("Bye!")
            run = False
            continue
        if choice != '1':
            print("Invalid choice. Please choose from the menu.")
            continue
        if choice == '1':
            get_analysis_report(user)
            continue