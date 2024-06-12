#this class has relation with the company class file

class Employee:
    def __init__ (self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    #52 weeks of the year
    def calculate_paycheck(self):
        return self.salary/52
        
#sample1 = Employee('Sara', 'Lee', 5000)
#print(sample1.fname)
        
