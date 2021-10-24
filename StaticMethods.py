import datetime


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
    def from_string(cls, emp_str):  # from.. naming convention class methods
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))


emp_1 = Employee('Corey', 'Goat', 50000)
emp_2 = Employee('Slimy', "Cat", 70000)
