import sqlite3

conn = sqlite3.connect("institute_analytics.db")
cursor = conn.cursor()

print("\n===== QUERY 1 =====")
cursor.execute("""
SELECT department_id, COUNT(*) AS total_students
FROM students
GROUP BY department_id
""")
for row in cursor.fetchall():
    print(row)

print("\n===== QUERY 2 =====")
cursor.execute("""
SELECT AVG(attendance_percentage)
FROM attendance
""")
print(cursor.fetchone())

print("\n===== QUERY 3 =====")
cursor.execute("""
SELECT result,
COUNT(*) AS total_students
FROM exam_results
GROUP BY result
""")
for row in cursor.fetchall():
    print(row)

print("\n===== QUERY 4 =====")
cursor.execute("""
SELECT company_name,
COUNT(*) AS hired_students
FROM placements
GROUP BY company_name
ORDER BY hired_students DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n===== QUERY 5 =====")
cursor.execute("""
SELECT ROUND(AVG(package_lpa),2)
FROM placements
""")
print(cursor.fetchone())

print("\n===== QUERY 6 =====")

cursor.execute("""
SELECT s.department_id,
ROUND(AVG(a.attendance_percentage),2)
FROM students s
JOIN attendance a
ON s.student_id = a.student_id
GROUP BY s.department_id
""")

for row in cursor.fetchall():
    print(row)

print("\n===== QUERY 7 =====")

cursor.execute("""
SELECT s.department_id,
ROUND(AVG(e.marks),2)
FROM students s
JOIN exam_results e
ON s.student_id = e.student_id
GROUP BY s.department_id
""")

for row in cursor.fetchall():
    print(row)

print("\n===== QUERY 8 =====")

cursor.execute("""
SELECT s.department_id,
COUNT(p.placement_id)
FROM students s
JOIN placements p
ON s.student_id = p.student_id
GROUP BY s.department_id
""")

for row in cursor.fetchall():
    print(row)
    
conn.close()