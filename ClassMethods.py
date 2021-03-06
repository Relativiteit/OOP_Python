class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.'+last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):  # self is a instance argument to create the object.
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Corey', 'Goat', 50000)
emp_2 = Employee('Slimy', "Cat", 70000)

Employee.set_raise_amt(1.05)  # is the same as Employee.set_raise_amt = 1.05

""" class methods as alternative constructors """

emp_str_1 = 'John-Doe-20000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Abudulla-Gonzales-90000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
