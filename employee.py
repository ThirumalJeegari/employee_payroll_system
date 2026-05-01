class Employee:
    def __init__(self,emp_id = None,name = None,depart =None,sal = None):
        self.emp_id = emp_id
        self.name = name
        self.depart = depart
        self.sal = sal


    def  Add_Employee(self):
        from db_Connection import cursor_obj,db_con_obj
        InsertingEmpDetails = "Insert into Employee(name,department,base_salary) values(%s,%s,%s)"
        data = (self.name,self.depart,self.sal)
        cursor_obj.execute(InsertingEmpDetails,data)
        db_con_obj.commit()

    def View_Employee(self):
        FetchqueryDetails ="Select * from Employee"
        from db_Connection import cursor_obj
        cursor_obj.execute(FetchqueryDetails)
        row = cursor_obj.fetchall()
        return row
    
    @staticmethod
    def Update_Salary(emp_id,sal):
        UpdatequeryDetails ="Update Employee set base_salary = %s where employee_id=%s"
        data = (sal,emp_id)
        from db_Connection import cursor_obj,db_con_obj
        cursor_obj.execute(UpdatequeryDetails,data)
        db_con_obj.commit()

    def Delete_Employee(self,emp_id):
        DeletequeryDetails = "Delete from Employee where employee_id =%s"
        data=(emp_id,)  # , is used Tuple
        from db_Connection import cursor_obj,db_con_obj
        cursor_obj.execute(DeletequeryDetails,data)
        db_con_obj.commit()

    def Set_Attendance(self,employee_id,date,status):
        Set_Att_query = "insert into attendance(employee_id,date,status) values(%s,%s,%s)"
        data =(employee_id,date,status)
        from db_Connection import cursor_obj,db_con_obj
        cursor_obj.execute(Set_Att_query,data)
        db_con_obj.commit()

    def Get_Attendance(self,employee_id):
        Get_Att_query = "select status from attendance where employee_id =%s"
        data =(employee_id,) # , is used for Tuple
        from db_Connection import cursor_obj
        cursor_obj.execute(Get_Att_query,data)
        return cursor_obj.fetchall()
    
    def Add_Salary(self,employee_id,bouns,deductions,salary):
        AddSalaryQuery="insert into salary(employee_id, bonus, deductions, net_salary) values(%s,%s,%s,%s)"
        data=(employee_id,bouns,deductions,salary)
        from db_Connection import cursor_obj,db_con_obj
        cursor_obj.execute(AddSalaryQuery,data)
        db_con_obj.commit()


    


        


        
        