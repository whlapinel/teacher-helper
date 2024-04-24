import pandas as pd
from download_csv import download_csv
from find_csv import most_recent_csv_in_downloads

class Result:
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
        return (f"Result({self.first_name} {self.last_name}, ID: {self.student_id}, "
                f"Score: {self.score}/{self.points_possible}, "
                f"Percentage: {self.percentage}%)\n")


def get_test_results(class_name, test_name, driver):
    download_csv(class_name, test_name, driver)
    results_file_path = most_recent_csv_in_downloads()
    results = load_results(results_file_path)
    return results


def load_results(file_path):
    data = pd.read_csv(file_path)
    results = []
    for _, row in data.iterrows():
        result = Result(
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