import sqlite3
import pandas as pd

conn = sqlite3.connect("institute_analytics.db")

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
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df.to_csv(f"../powerbi/{table}.csv", index=False)

print("Power BI files exported successfully")

conn.close()