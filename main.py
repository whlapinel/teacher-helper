import time

from analysis import __get_percent_tested
import download_csv
import find_csv
import users
from find_csv import most_recent_csv_in_downloads
from test_result import get_test_results, Result
import login
from analysis import get_analysis

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load from user config file
    run = True
    while run:
        user = users.User()
        if not user.load_from_config():
            user.construct_from_input()
            user.save_to_config()
        print(user)
        run_input = input("continue? (Y/N): ")
        if run_input == 'N':
            run = False
            continue
        has_ml = input('is there an ML version to your test? Y/N')
        ml_test_name = None
        if has_ml == 'Y':
            ml_test_name = input('Enter name of ML version: ')
        std_test_name = 'Unit 5 Test (Standard) Spring 2024 pdf'
        driver = login.log_in(user)
        class_results = {}
        analyses = {}
        for class_name in user.classroom_names:
            print("getting std/hon test results for class: ", class_name, "test name: ", std_test_name)
            std_test_results = get_test_results(class_name, std_test_name, driver)
            ml_test_results = {}
            if ml_test_name:
                print("getting ML test results for class: ", class_name, "test name: ", ml_test_name)
                ml_test_results = get_test_results(class_name, ml_test_name, driver)
                class_results = {"std": std_test_results, "ml": ml_test_results}
            else:
                class_results = {"std": std_test_results}
            print("class results: ", class_results)
            class_analysis = get_analysis(ml_test_results, std_test_results)
            print("analysis for class " + class_name + ":\n")
            print(class_analysis)
            analyses[class_name] = class_analysis
        print("Analyses: ", analyses)
        driver.quit()
        run = False
