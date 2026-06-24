import sqlite3

conn = sqlite3.connect("institute_analytics.db")
cursor = conn.cursor()

tables = [
    "students",
    "departments",
    "admissions",
    "attendance",
    "exam_results",
    "placements",
    "faculty",
    "quality_metrics"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

conn.close()