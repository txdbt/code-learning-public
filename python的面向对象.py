"""class Employee:
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

employer.pay_salary(employee)"""


class Phone:
    def __init__(self,brand:str,color:str,prize:int) -> None:
        self.color = color
        self.prize = prize
        self.turned_on: bool = False

    def turn_on(self) -> None:                                      #創建方法
        if self.turned_on:
            print(f"{self.brand} has already turn on")
        else:
            self.turned_on = True
            print(f"{self.brand} is now turn on")


    def turn_off(self) -> None:                                      #創建方法
        if self.turned_on:
            self.turned_on = False
            print(f"{self.brand} is now turn off")
        else:
            print(f"{self.brand} is already turn off")






samsung: Phone = Phone('samsung','blue',10000)
print(samsung)