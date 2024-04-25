
import find_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CanvasReport:
    def __init__(self):
        self.test_id: int = 0


def get_report(class_number, test_id, driver, wait):
    return "hello"


def download_report(class_number, test_id, driver, wait):
    reports_url = f'https://app.masteryconnect.com/classrooms/{class_number}/benchmarks/{test_id}/modal?tab=reports'
    driver.get(reports_url)
    download_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#ia-csv-button')))
    download_btn.click()


def load_report():
    file_path = find_csv.get_latest_csv()
