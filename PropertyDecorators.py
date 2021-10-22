"""Property decorator, allows to access attributes without using getters and setters everywhere. But you can still do it with the @property decorator """


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):  # self is a instance argument to create the object.
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):  # self is a instance argument to create the object.
        return '{} {}'.format(self.first, self.last)
# setter

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
# deleter

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee("Johnny", "Cage")

#emp_1.first = 'Jim'

emp_1.fullname = 'Corey Schafer'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print(help(Employee))
print(dev_1.email)
print(dev_2.email)
