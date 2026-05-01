import mysql.connector
from decimal import Decimal

db_con_obj =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Thirumal@2004",
    database = "Employee_Payroll_System"
)


cursor_obj = db_con_obj.cursor()



queryCreatingEmpTable ="""
    Create table if not exists Employee(
    employee_id int primary key auto_increment,
    name varchar(50) not null,
    department varchar(50) not null,
    base_salary decimal(10,2)
    )
    """
cursor_obj.execute(queryCreatingEmpTable)


queryCreatingSalTable ="""
    Create table if not exists salary(
    salary_id int primary key auto_increment,
    employee_id int,
    bonus decimal(10,2),
    deductions decimal(10,2),
    net_salary decimal(10,2)
    )
    """
cursor_obj.execute(queryCreatingSalTable)


queryCreatingAttTable ="""
    Create table if not exists attendance(
    attendance_id int primary key auto_increment,
    employee_id int,
    date DATE,
    status varchar(10)
    )
    """
cursor_obj.execute(queryCreatingAttTable)

db_con_obj.commit()


