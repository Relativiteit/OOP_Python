class Employee:
    #pass  you can have a empty class then you put in pass so it won't error.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self): # self is a instance argument to create the object.
        return '{} {}'.format(self.first, self.last) 

emp_1 = Employee('Corey', "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

#print(emp_1)
#print(emp_2)

# instance variables manually

"""emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000 """

print(emp_1.email)
print(emp_2.email) 

print(emp_1.fullname()) # instance and call the method, dont need to give self

Employee.fullname(emp_1) # does not know instance so need to give self.
