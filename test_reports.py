import pandas as pd
import find_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CanvasReport:
    def __init__(self):
        self.test_id: int = 0


def get_report(class_number, test_id, driver, wait):
    download_report(class_number, test_id, driver, wait)
    file_path = find_csv.get_latest_csv()
    report = load_report(file_path)
    return report


def download_report(class_number, test_id, driver, wait):
    # fixme: this url is correct but not if you go to the page manually
    # must mouse over the following element a['data-fullname'=test_name] and then click on 
    # a.openBigDialog with href below to get the modal for the test_id. (element text is "Reports")
    reports_url = f'https://app.masteryconnect.com/classrooms/{class_number}/benchmarks/{test_id}/modal?tab=reports'
    driver.get(reports_url)
    download_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#ia-csv-button')))
    download_btn.click()


def load_report(file_path):
    df = pd.read_csv(file_path)
    percentages_dict = df.iloc[7].to_dict()
    trimmed_dict = {k: v for k, v in percentages_dict.items() if not (('Unnamed' in k) or ('question_number' in k))}
    less_than_60 = {k: v for k, v in trimmed_dict.items() if int(v) < 60}
    return list(less_than_60.keys())