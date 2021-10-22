class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.'+last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    # changing the raise amount in Subclass it does not change instances of parent class
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # this will handle copying the code from the init method of Employee
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    # don't pass mutable data types as default argument
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Test', 'Employee', 60000, 'java')

mgr_1 = Manager('Sue', 'Constanza', 90000, [dev_1])


# this will show if a instance is inheriting from the parent
print(isinstance(mgr_1, Manager))
# this will show if a subclass is inheriting from the parent
print(issubclass(Manager, Employee))


# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.add_emp(dev_1)

# mgr_1.print_emps()

# print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
