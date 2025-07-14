class Employee:
    def __init__(self,emp_id,name,age,monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary

class Employer:
    def __init__(self,funds):
        self.funds = funds
    

    def pay_salary(self,employee):
        if self.funds >=employee.monthly_salary:
            self.funds -= employee.monthly_salary
            print(f"为{employee.name}发放月薪{employee.monthly_salary},雇主剩余资金{self.funds}")
        else:
            print("雇主资金不足，无法发放工资")
        

employee = Employee("E001","mike",30,8000)

employer = Employer(5000)

employer.pay_salary(employee)