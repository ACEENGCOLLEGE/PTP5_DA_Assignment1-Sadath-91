# grade_calculator.py
import json

def calculate_grade(json_file):
    with open(json_file) as f:
        data = json.load(f)

    total_tests = len(data["tests"])
    passed_tests = sum(1 for test in data["tests"] if test["outcome"] == "passed")

    points_awarded = passed_tests
    points_available = total_tests

    with open("grade_output.txt", "w") as f:
        f.write(f"Points={points_awarded}\n")
        f.write(f"TotalPoints={points_available}\n")

calculate_grade("test_results.json")
