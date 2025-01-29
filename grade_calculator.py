import json
import sys

def compute_grade(results_file):
    with open(results_file, "r") as file:
        data = json.load(file)

    total_tests = data.get("summary", {}).get("total", 0)
    passed_tests = data.get("summary", {}).get("passed", 0)

    if total_tests == 0:
        percentage = 0
    else:
        percentage = (passed_tests / total_tests) * 100

    # Define grade thresholds
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    # Print output for GitHub Actions
    print(f"Percentage={percentage:.2f}")
    print(f"Grade={grade}")

    # Save to a file for GitHub Actions to read
    with open("grade_output.txt", "w") as output_file:
        output_file.write(f"Percentage={percentage:.2f}\n")
        output_file.write(f"Grade={grade}\n")

if __name__ == "__main__":
    compute_grade(sys.argv[1])
