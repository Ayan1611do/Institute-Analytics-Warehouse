# Institute Analytics Data Warehouse

## Project Overview

The Institute Analytics Data Warehouse is a data warehousing and analytics project developed to support institutional decision-making and performance monitoring. The project integrates data from multiple academic and administrative domains, stores them in a centralized database, and provides analytical insights through SQL queries and Power BI dashboards.

The system simulates real-world institutional data and demonstrates the complete data warehousing lifecycle, including data generation, ETL processing, database creation, analytical querying, and dashboard visualization.

---

## Objectives

* Build a centralized data warehouse for institutional analytics.
* Integrate data from multiple academic and administrative sources.
* Perform ETL (Extract, Transform, Load) operations using Python.
* Execute analytical SQL queries for business insights.
* Develop interactive Power BI dashboards for visualization.
* Support decision-making through data-driven reporting.

---

## Technologies Used

### Programming Language

* Python 3.x

### Database

* SQLite

### Data Processing Libraries

* Pandas
* SQLite3

### Visualization Tool

* Microsoft Power BI

### Development Environment

* Visual Studio Code

---

## Project Structure

```text
Institute_Analytics_Warehouse/
│
├── backend/
│   └── backend_info.txt
│
├── dashboard/
│   └── Institute_Analytics_Dashboard.pbix
│
├── Data/
│   ├── students.csv
│   ├── departments.csv
│   ├── admissions.csv
│   ├── attendance.csv
│   ├── exam_results.csv
│   ├── placements.csv
│   ├── faculty.csv
│   └── quality_metrics.csv
│
├── Database/
│   ├── create_database.py
│   ├── load_data.py
│   ├── analytics_queries.py
│   ├── check_database.py
│   ├── check_tables.py
│   └── institute_analytics.db
│
├── docs/
│   └── README.md
│
├── etl/
│   ├── generate_data.py
│   └── generate_remaining_data.py
│
├── presentation/
│   └── Institute_Analytics_Data_Warehouse.pptx
│
└── institute_analytics.db
```

---

## Dataset Description

### Students

Stores student information including:

* Student ID
* Student Name
* Gender
* Department ID

### Departments

Stores department details:

* Department ID
* Department Name

### Admissions

Stores admission-related information.

### Attendance

Stores student attendance percentages.

### Exam Results

Stores:

* Semester
* Marks
* Result Status (Pass/Fail)

### Placements

Stores:

* Company Name
* Package (LPA)
* Student Placement Details

### Faculty

Stores faculty information across departments.

### Quality Metrics

Stores institutional quality indicators used for analytics.

---

## ETL Process

### Extract

Data is generated and collected from CSV files.

### Transform

Data is cleaned, validated, and prepared using Python scripts.

### Load

Processed data is loaded into the SQLite data warehouse.

---

## Database Statistics

| Table           | Records |
| --------------- | ------- |
| Students        | 500     |
| Departments     | 5       |
| Admissions      | 500     |
| Attendance      | 500     |
| Exam Results    | 500     |
| Placements      | 300     |
| Faculty         | 50      |
| Quality Metrics | 5       |

---

## Analytical SQL Queries

The project includes multiple analytical SQL queries such as:

### Query 1

Student count by department.

### Query 2

Average attendance percentage.

### Query 3

Pass vs Fail analysis.

### Query 4

Placement count by company.

### Query 5

Average placement package.

### Query 6

Average attendance by department.

### Query 7

Average marks by department.

### Query 8

Department-wise placement count.

---

## Dashboard Features

The Power BI dashboard includes:

### KPI Cards

* Total Students
* Total Departments
* Placement Records
* Average Package (LPA)

### Visualizations

* Students by Department
* Placements by Company
* Pass vs Fail Analysis

### Filters

* Department Selection Slicer

---

## Key Insights

* Information Technology department has the highest student count.
* Overall attendance is above 75%.
* Pass percentage is above 90%.
* Multiple companies participate in campus placements.
* Average package is approximately 7.66 LPA.
* Placement distribution varies across departments.

---

## Business Benefits

* Improves institutional performance monitoring.
* Supports accreditation and quality assessment.
* Enables data-driven decision making.
* Provides centralized reporting and analytics.
* Simplifies institutional data management.

---

## Future Enhancements

* Integration with MySQL or PostgreSQL.
* Real-time dashboard updates.
* Student performance prediction using Machine Learning.
* Faculty performance analytics.
* Web-based analytics portal.
* Automated ETL scheduling.

---

## Conclusion

The Institute Analytics Data Warehouse successfully demonstrates the implementation of a complete data warehousing solution. The project integrates institutional datasets, performs ETL operations, stores data in a centralized warehouse, executes analytical queries, and presents meaningful insights through Power BI dashboards. The solution provides a strong foundation for institutional analytics and decision support systems.
