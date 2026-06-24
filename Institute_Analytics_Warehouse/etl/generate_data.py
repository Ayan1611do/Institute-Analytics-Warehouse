from faker import Faker
import pandas as pd
import random

fake = Faker()

departments = [
    "Computer Engineering",
    "Information Technology",
    "Artificial Intelligence & Data Science",
    "Electronics Engineering",
    "Mechanical Engineering"
]

# Students
students = []

for i in range(1, 501):
    students.append([
        i,
        fake.name(),
        random.choice(["Male", "Female"]),
        random.randint(1, 5)
    ])

students_df = pd.DataFrame(
    students,
    columns=[
        "student_id",
        "student_name",
        "gender",
        "department_id"
    ]
)

students_df.to_csv("../data/students.csv", index=False)

print("Students CSV Created")

# Departments

dept_data = {
    "department_id": [1, 2, 3, 4, 5],
    "department_name": [
        "Computer Engineering",
        "Information Technology",
        "Artificial Intelligence & Data Science",
        "Electronics Engineering",
        "Mechanical Engineering"
    ]
}

dept_df = pd.DataFrame(dept_data)

print(dept_df)

dept_df.to_csv("../data/departments.csv", index=False)
print("Done")