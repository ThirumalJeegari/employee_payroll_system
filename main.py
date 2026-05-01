from employee import Employee
from decimal import Decimal
from payroll import Payroll
print()
print("Employee Payroll System")
print()


print("Choose Any below service :")
print("1. Add Employee")
print("2. View Employees")
print("3. Update Salary")
print("4. Delete Employee")
print("5. Generate Payslip")
print("6. Bonus Calculation")
print("7. Attendance")
print()


option = int(input("Choose Any above service :"))


if option == 1:

    employee_id = int(input("Enter Employee ID :"))
    name        = (input("Enter Employee Name :"))
    department  = (input("Enter Employee Department :"))
    base_salary = Decimal(input("Enter Employee Salary :"))

    Employee(employee_id,name,department,base_salary).Add_Employee()
    print("Employee details added Successfully!...")


elif option == 2:
    print("Employee Details.")
    row=Employee().View_Employee()
    for r in row:
        print(r)

elif option == 3:
    Employee.Update_Salary(int(input("Enter Employee ID  to Update :")),Decimal(input("Enter the salary to Update :")))
    print("Updated Salary.")
    
elif option == 4:
    Employee().Delete_Employee(int(input("Enter a Employee ID to Delete :")))
    print("Deleted Employee Details Successfully.")

elif option == 5:
    emp = Employee()
    emp_id = int(input("Enter Employee ID :"))
    data = emp.View_Employee()

    for r in data:
        if r[0] == emp_id:
            base_salary = r[3]
            name = r[1]
            dept = r[2]

            p = Payroll(base_salary)

            attendance = emp.Get_Attendance(emp_id)
            p.Calculate_Bonus(attendance)
            p.Calc_Deductions()
            p.Calculate_Net_Salary()

            emp.Add_Salary(emp_id, p.bonus, p.deductions, p.net_salary)

            p.Genarate_Pay_Slip(emp_id,name,dept)
            break
        else:
            print("Employee not Found!")


elif option == 6:
    emp = Employee()
    emp_id = int(input("Enter Employee ID: "))

    attendance = emp.Get_Attendance(emp_id)

    data = emp.View_Employee()

    for r in data:
        if r[0]==emp_id:
            base_salary = r[3]

    p = Payroll(base_salary)
    bonus = p.Calculate_Bonus(attendance)

    print("Bonus :",bonus)


elif option == 7:
    from datetime import date
    Employee().Set_Attendance(int(input("Enter Employee ID to get Attendance :")),date.today(),input("Enter Status(Present / Absent) :"))
    print("Attendanced Marked!")

else:
    print("You Entered Invalid Option!")

    



