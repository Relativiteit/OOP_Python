class Employee:
    # class variable 
    num_of_emps = 0 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1 


    def fullname(self): # self is a instance argument to create the object.
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount = self.raise_amount

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Goat', 50000)
emp_2 = Employee('Slimy', "Cat", 70000)

print(Employee.num_of_emps)

"""print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""


