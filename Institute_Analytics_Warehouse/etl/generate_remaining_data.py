from faker import Faker
import pandas as pd
import random

fake = Faker()

# =========================
# Admissions
# =========================

admissions = []

for i in range(1, 501):
    admissions.append([
        i,
        i,
        random.choice([2023, 2024, 2025])
    ])

admissions_df = pd.DataFrame(
    admissions,
    columns=[
        "admission_id",
        "student_id",
        "admission_year"
    ]
)

admissions_df.to_csv("../data/admissions.csv", index=False)

# =========================
# Attendance
# =========================

attendance = []

for i in range(1, 501):
    attendance.append([
        i,
        i,
        round(random.uniform(55, 98), 2)
    ])

attendance_df = pd.DataFrame(
    attendance,
    columns=[
        "attendance_id",
        "student_id",
        "attendance_percentage"
    ]
)

attendance_df.to_csv("../data/attendance.csv", index=False)

# =========================
# Exam Results
# =========================

results = []

for i in range(1, 501):

    marks = random.randint(35, 100)

    result = "Pass"

    if marks < 40:
        result = "Fail"

    results.append([
        i,
        i,
        random.randint(1, 8),
        marks,
        result
    ])

results_df = pd.DataFrame(
    results,
    columns=[
        "result_id",
        "student_id",
        "semester",
        "marks",
        "result"
    ]
)

results_df.to_csv("../data/exam_results.csv", index=False)

# =========================
# Placements
# =========================

companies = [
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Capgemini",
    "HCL"
]

placements = []

for i in range(1, 301):

    placements.append([
        i,
        random.randint(1, 500),
        random.choice(companies),
        round(random.uniform(3.5, 12.0), 2)
    ])

placements_df = pd.DataFrame(
    placements,
    columns=[
        "placement_id",
        "student_id",
        "company_name",
        "package_lpa"
    ]
)

placements_df.to_csv("../data/placements.csv", index=False)

# =========================
# Faculty
# =========================

faculty = []

for i in range(1, 51):

    faculty.append([
        i,
        fake.name(),
        random.randint(1, 5),
        random.choice([
            "Assistant Professor",
            "Associate Professor",
            "Professor"
        ])
    ])

faculty_df = pd.DataFrame(
    faculty,
    columns=[
        "faculty_id",
        "faculty_name",
        "department_id",
        "designation"
    ]
)

faculty_df.to_csv("../data/faculty.csv", index=False)

# =========================
# Quality Metrics
# =========================

quality_df = pd.DataFrame({
    "metric_name": [
        "Student Faculty Ratio",
        "Placement Percentage",
        "Graduation Outcome",
        "Research Publications",
        "Quality Initiatives"
    ],
    "metric_value": [
        10,
        82,
        90,
        45,
        12
    ]
})

quality_df.to_csv("../data/quality_metrics.csv", index=False)

print("All CSV Files Created Successfully")