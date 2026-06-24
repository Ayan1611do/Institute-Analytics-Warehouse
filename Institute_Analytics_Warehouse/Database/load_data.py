import sqlite3
import pandas as pd

conn = sqlite3.connect("institute_analytics.db")

# Paths to CSV files
students = pd.read_csv("../data/students.csv")
departments = pd.read_csv("../data/departments.csv")
admissions = pd.read_csv("../data/admissions.csv")
attendance = pd.read_csv("../data/attendance.csv")
exam_results = pd.read_csv("../data/exam_results.csv")
placements = pd.read_csv("../data/placements.csv")
faculty = pd.read_csv("../data/faculty.csv")
quality_metrics = pd.read_csv("../data/quality_metrics.csv")

# Load into SQLite tables
students.to_sql("students", conn, if_exists="replace", index=False)
departments.to_sql("departments", conn, if_exists="replace", index=False)
admissions.to_sql("admissions", conn, if_exists="replace", index=False)
attendance.to_sql("attendance", conn, if_exists="replace", index=False)
exam_results.to_sql("exam_results", conn, if_exists="replace", index=False)
placements.to_sql("placements", conn, if_exists="replace", index=False)
faculty.to_sql("faculty", conn, if_exists="replace", index=False)
quality_metrics.to_sql("quality_metrics", conn, if_exists="replace", index=False)

print("All Tables Loaded Successfully!")

conn.close()