import sqlite3

conn = sqlite3.connect("institute_analytics.db")
cursor = conn.cursor()

tables = [
    "students",
    "attendance",
    "exam_results",
    "placements"
]

for table in tables:
    print(f"\n===== {table.upper()} =====")

    cursor.execute(f"PRAGMA table_info({table})")

    for column in cursor.fetchall():
        print(column)

conn.close()