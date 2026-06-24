import sqlite3

conn = sqlite3.connect("institute_analytics.db")

print("Database Created Successfully")

conn.close()