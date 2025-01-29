import json
import sys

def compute_grade(test_results_file):
    with open(test_results_file, 'r') as file:
        results = json.load(file)

    # Ensure JSON format is correct
    if "tests" not in results:
        print("Error: Invalid test results format")
        return

    total_tests = len(results["tests"])
    passed_tests = sum(1 for test in results["tests"] if test["outcome"] == "passed")

    pass_percentage = (passed_tests / total_tests) * 100

    if pass_percentage >= 80:
        grade = "A"
    elif pass_percentage >= 60:
        grade = "B"
    else:
        grade = "C"

    print(f"Grade={grade}")  # Required for GitHub Actions
    print(f"::set-output name=result::{grade}")  # GitHub Actions syntax for output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python grade_calculator.py <test_results.json>")
        sys.exit(1)

    compute_grade(sys.argv[1])
