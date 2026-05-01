class Payroll:
    def __init__(self,base_salary):
        self.base_salary = base_salary
        self.bonus = 0
        self.deductions = 0
        self.net_salary = 0

    def Calculate_Bonus(self,attendance):
        present_days = sum(1 for i in attendance if i[0] == "Present")

        if present_days>=25:
            self.bonus = 5000
        elif present_days>=20:
            self.bonus = 3000
        else:
            self.bonus = 1000
        
        return self.bonus
    
    def Calc_Deductions(self):
        self.deductions = 1000

    def Calculate_Net_Salary(self):
        self.net_salary = self.base_salary + self.bonus - self.deductions
        return self.net_salary

    def Genarate_Pay_Slip(self,emp_id,name,depart):
        print()
        print("--------- PAY SLIP ---------")
        print("ID          :",emp_id)
        print("Name        :",name)
        print("Department  :",depart)
        print("Base Salary :",self.base_salary)
        print("Bonus       :",self.bonus)
        print("Deductions  :",self.deductions)
        print("Net Salary  :",self.net_salary)
        print()





    



