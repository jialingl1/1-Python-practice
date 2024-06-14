#this class has relation with the company class file

#general employee class so that all types of employees can inherit its properties and not just the salaried ones.
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
#this class became the child class and now it derives/inherit from the Employee class.
class SalaryEmployee(Employee):
    def __init__ (self, fname, lname, salary):
        #self.fname = fname -NO longer needed since now it inherit these from elsewhere.
        #self.lname = lname
        super().__init__(fname, lname) #--use super method to pass in properties from parent class
        self.salary = salary

    #52 weeks of the year
    def calculate_paycheck(self):
        return self.salary/52
        
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate

#this class inherit from the salary employee class instead of the general employee class.
#b/c they receive a regular salary plus comission.
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, comission_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.comission_rate = comission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_comission = self.sales_num*self.comission_rate
        return regular_salary + total_comission
        
