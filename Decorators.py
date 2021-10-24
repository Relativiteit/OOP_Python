# Decorators

def decorator_function(orginal_function):
    def wrapper_function(*args, **kwargs):  # any arguments, any keywords or functions
        print('wrapper executed this before {}'.format(orginal_function.__name__))
        return orginal_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('disp[lay function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)

display()
