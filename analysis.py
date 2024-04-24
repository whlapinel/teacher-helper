import math


# get_analysis will take 2 arguments, ml_results and std_results, and return the following:
# pct_assessed (one percentage), avg_score (tuple of 2 numbers for ml and std), pct_failed (tuple),
# and problem questions (array of numbers) = Questions that less than 60% answered correctly.
class Analysis:
    def __init__(self, percent_tested, avg_scores, pct_failed, problem_questions):
        self.percent_tested = percent_tested
        self.average_scores = avg_scores
        self.pct_failed = pct_failed
        self.problem_questions = problem_questions

    def __repr__(self):
        return (f"Analysis(percent tested: {self.percent_tested},\n avg score (ML, Std/Hon): {self.average_scores},\n "
                f"pct failed (ML, Std/Hon): {self.pct_failed},\n problem questions (ML, St"
                f"d/Hon): {self.problem_questions})\n")


def get_analysis(ml_results, std_results):
    print("running get_analysis...")
    pct_tested = __get_percent_tested(ml_results, std_results)
    avg_scores = __get_avg_scores(ml_results, std_results)
    ml_pct_failed = __get_pct_failed(ml_results)
    std_pct_failed = __get_pct_failed(std_results)
    analysis = Analysis(pct_tested, avg_scores, (ml_pct_failed, std_pct_failed),
                        problem_questions=([1, 2, 3], [1, 2, 3]))
    return analysis


def __get_percent_tested(ml_results, std_results):
    return __calc_percent_tested(ml_results) + __calc_percent_tested(std_results)


def __calc_percent_tested(results):
    if len(results) == 0:
        return 0
    untested_count = 0
    total_results = len(results)
    for result in results:
        if math.isnan(result.percentage):
            print("is nan: ", result.first_name, " ", result.percentage)
            print("percentage nan: ", result)
            untested_count += 1
        print("untested count", untested_count)
    percent_untested = math.floor((untested_count / total_results) * 100)
    print("percent untested: ", percent_untested)
    percent_tested = 100 - percent_untested
    print("percent tested: ", percent_tested)
    return percent_tested


def __get_avg_scores(ml_results, std_results):
    ml_avg = __get_avg_score(ml_results)
    st_avg = __get_avg_score(std_results)
    return ml_avg, st_avg


def __get_avg_score(results):
    total_count = len(results)
    sum_scores = 0
    for result in results:
        if math.isnan(result.percentage):
            total_count -= 1
        else:
            sum_scores += result.percentage
    return math.floor(sum_scores / total_count)


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
    pct_failed = math.floor((fail_count / total_count) * 100)
    return pct_failed
