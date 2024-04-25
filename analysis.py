import datetime
import math
import csv
from typing import List
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import id_numbers
import test_scores
from test_reports import get_report, CanvasReport


class Analysis:
    def __init__(self, test_name: str, test_id: int, class_name: str, class_id: int, percent_tested: float,
                 avg_score: float, pct_failed: float, problem_questions: [int]) -> None:
        self.test_name: str = test_name
        self.test_id: int = test_id
        self.class_name: str = class_name
        self.class_id: int = class_id
        self.percent_tested: float = percent_tested
        self.avg_score: float = avg_score
        self.pct_failed: float = pct_failed
        self.problem_questions: [int] = problem_questions

    def __repr__(self):
        return (f"Analysis:\n"
                f"class name: {self.class_name}\n "
                f"test name: {self.test_name}\n"
                f"percent tested: {self.percent_tested}\n "
                f"avg score: {self.avg_score}\n"
                f"pct failed: {self.pct_failed}\n"
                f"\n")


def get_analysis(class_name, class_id, test_name, driver, wait):
    print("running get_analysis...")
    test_id = id_numbers.get_test_id(class_id, driver, wait, test_name)
    report = get_report(class_id, test_id, driver, wait)
    scores = test_scores.get_scores(class_id, class_name, test_id, test_name, driver, wait)
    pct_tested = __calc_percent_tested(scores)
    avg_scores = __get_avg_score(scores)
    pct_failed = __get_pct_failed(scores)
    problem_questions = __get_problem_questions(report)
    analysis = Analysis(test_name, test_id, class_name, class_id, pct_tested, avg_scores, pct_failed, problem_questions)
    return analysis


def __calc_percent_tested(results):
    if len(results) == 0:
        return 0
    untested_count = 0
    total_count = len(results)
    for result in results:
        if math.isnan(result.percentage):
            print("is nan: ", result.first_name, " ", result.percentage)
            print("percentage nan: ", result)
            untested_count += 1
        print("untested count", untested_count)
    tested_count = total_count - untested_count
    print(f"tested: {tested_count}")
    print(f"out of: {total_count}")
    percent_tested = round((tested_count / total_count) * 100, 1)
    print("percent tested: ", percent_tested)
    return percent_tested


def __get_avg_score(results):
    total_count = len(results)
    sum_scores = 0
    for result in results:
        if math.isnan(result.percentage):
            total_count -= 1
        else:
            sum_scores += result.percentage
    return round(sum_scores / total_count, 1)


def __get_pct_failed(results):
    total_count = len(results)
    fail_count = 0
    for result in results:
        if math.isnan(result.percentage):
            total_count -= 1
        else:
            if result.percentage < 60:
                fail_count += 1
        print("fail count: ", fail_count)
    pct_failed = round((fail_count / total_count) * 100, 1)
    return pct_failed


def __get_problem_questions(report: CanvasReport) -> [int]:
    return [1, 2, 3, 4, 5, 6, 7, 8]


def write_to_csv(report_name: str, analyses: [Analysis]) -> None:
    filename: str = f"{report_name} {datetime.date.today()}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["", "", f"{report_name}", "", ""])
        writer.writerow(["class name", "test name", "pct tested", "avg score", "pct failed"])
        for analysis in analyses:
            writer.writerow([analysis.class_name, analysis.test_name, analysis.percent_tested, analysis.avg_score,
                             analysis.pct_failed])
