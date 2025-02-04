import json

def calculate_grade(json_file):
    with open(json_file) as f:
        data = json.load(f)

    total_tests = len(data["tests"])
    passed_tests = sum(1 for test in data["tests"] if test["outcome"] == "passed")

    percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    grade = "A" if percentage >= 90 else "B" if percentage >= 80 else "C"

    with open("grade_output.txt", "w") as f:
        f.write(f"FINAL_PERCENTAGE={percentage:.2f}\n")
        f.write(f"FINAL_GRADE={grade}\n")

calculate_grade("test_results.json")
