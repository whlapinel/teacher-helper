import pandas as pd
from find_csv import get_latest_csv
import time
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Score:
    def __init__(self, school, teacher, tracker, assessment_name, student_id, last_name, first_name, points_possible, score, percentage):
        self.school = school
        self.teacher = teacher
        self.tracker = tracker
        self.assessment_name = assessment_name
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.points_possible = points_possible
        self.score = score
        self.percentage = percentage

    def __repr__(self):
        return (f"Score({self.first_name} {self.last_name}, ID: {self.student_id}, "
                f"Score: {self.score}/{self.points_possible}, "
                f"Percentage: {self.percentage}%)\n")


def get_scores(class_id, class_name, test_id, test_name, driver, wait):
    download_scores(class_id, test_id, driver, wait)
    results_file_path = get_latest_csv()
    results = load_scores(results_file_path)
    # check to make sure test name matches first row
    if (results[0].assessment_name != test_name or
            results[0].tracker != class_name):
        print("loaded scores test name: ", results[0].assessment_name)
        print("analyzing test name: ", test_name)
        raise Exception("Wrong test scores loaded!!")
    return results


def download_scores(class_id, test_id, driver, wait):
    # driver should already be on the MC home page
    # below url should download the test scores in Excel
    download_url = 'https://app.masteryconnect.com/classrooms/' + class_id + '/export/' + test_id + '/options?b=1'
    print(download_url)
    driver.get(download_url)
    checkbox = wait.until(EC.presence_of_element_located((By.NAME, "export_options[show_percentages]")))
    checkbox.click()
    checkbox2 = wait.until(EC.presence_of_element_located((By.NAME, "export_options[show_answers]")))
    checkbox2.click()
    export_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.no-disable')))
    export_btn.click()
    time.sleep(5)
    return


def load_scores(file_path):
    data = pd.read_csv(file_path)
    results = []
    for _, row in data.iterrows():
        result = Score(
            school=row['school'],
            teacher=row['teacher'],
            tracker=row['tracker'],
            assessment_name=row['assessment_name'],
            student_id=row['student_id'],
            last_name=row['last_name'],
            first_name=row['first_name'],
            points_possible=row['points_possible'],
            score=row['score'],
            percentage=row['percentage']
        )
        results.append(result)
    return results
