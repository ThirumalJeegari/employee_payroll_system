# employee_payroll_system

📌 Project Overview

The Employee Payroll System is a Python-based application developed using Object-Oriented Programming (OOP) principles and integrated with a MySQL database.
It helps manage employee records, track attendance, calculate bonuses, and generate payslips efficiently.

🚀 Features

👤 Add Employee Details

📋 View All Employees

💰 Update Employee Salary

❌ Delete Employee Records

📅 Track Attendance (Present / Absent)

🎯 Bonus Calculation based on attendance

🧾 Generate Payslip

🗄️ Store salary records in database


🛠️ Tech Stack

Programming Language: Python

Database: MySQL

Concepts Used:

Object-Oriented Programming (OOP)

File Handling (basic)


Database Connectivity (mysql-connector)

📂 Project Structure
Employee Payroll System/
│
├── db_Connection.py   # Database connection and table creation
├── employee.py        # Employee operations (CRUD, attendance, salary)
├── payroll.py         # Payroll calculations (bonus, deductions, payslip)
├── main.py            # Main driver program (user interface)
├── README.md          # Project documentation

⚙️ Installation & Setup

1. Clone the Repository
git clone https://github.com/your-username/employee_payroll_system.git
cd employee_payroll_system

3. Install Required Package
pip install mysql-connector-python

5. Setup MySQL Database
   
Create a database:
CREATE DATABASE Employee_Payroll_System;
Update your database credentials in:
db_Connection.py

▶️ How to Run
python main.py

📊 Example Workflow

Add employee details
Mark attendance
Calculate bonus based on attendance
Generate payslip
Store salary in database

🧠 Key Concepts Demonstrated

Class & Object Design
Static Methods
Database CRUD Operations
Real-world business logic implementation

🔥 Future Enhancements

GUI version using Tkinter
Web version using Flask/Django
Login Authentication System
Export Payslip as PDF
Monthly Salary Tracking

👨‍💻 Author
Thirumal Jeegari
B.Tech (Final Year) | Data Scientist Aspirant

⭐ Support

If you like this project, give it a ⭐ on GitHub!
