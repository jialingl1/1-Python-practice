#import the class Employee from employee. Imported child classes as well
from employee import Employee, SalaryEmployee, HourlyEmployee

#class
class Company:
    #instance of a class (aka object)
    def __init__(self):
        self.employees = []

    #method:
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    #method 2 to display the actual employee names
    def display_employees(self):
        print('Current employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------')
    
    #method 3:
    def pay_employees(self):
        print('Paying Employees: ')
        for i in self.employees:
            print('Paycheck for: ', i.fname, i.lname)
            #special syntax for displaying dollar amount with decimals
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('-------')


#where the main program start - we add employees here to test.
def main():
    #define my_company by calling the Company constructor
    my_company = Company()

    employee1 = SalaryEmployee('Carla', 'Giraldo', 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Samuel', 'Jackson', 25, 50)
    my_company.add_employee(employee2)
    employee3 = HourlyEmployee('Frodo', 'Bolson', 40, 15)
    my_company.add_employee(employee3)

    #calling of the methods in the Company class for them to work
    my_company.display_employees()
    my_company.pay_employees()

#call the main method to execute all
main()

