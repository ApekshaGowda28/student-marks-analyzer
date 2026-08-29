import csv
import os

name = input("Enter student full name: ")

subjects = ["Python", "Java", "C++", "Databases"]

marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

# Grade
if average >= 90:
    grade = "A+"
    grade_point = 10
elif average >= 80:
    grade = "A"
    grade_point = 9
elif average >= 70:
    grade = "B"
    grade_point = 8
elif average >= 60:
    grade = "B+"
    grade_point = 7
elif average >= 50:
    grade = "D"
    grade_point = 6
else:
    grade = "F"
    grade_point = 0

# CGPA
cgpa = grade_point

# Result
results = "PASS" if average >= 40 else "FAIL"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"CGPA: {cgpa:.2f}")
print(f"Result: {results}")

# Save results to CSV
file_name = "student_results.csv"

file_exists = os.path.exists(file_name)

with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Name",
            "Total Marks",
            "Average Marks",
            "Grade",
            "CGPA",
            "Result"
        ])

    writer.writerow([
        name,
        total,
        round(average, 2),
        grade,
        cgpa,
        results
    ])

print("\nStudent results saved to student_results.csv")