# Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  # any arguments, any keywords or functions
        print('wrapper executed this before {}'.format(
            original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(
            self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('disp[lay function ran')


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)

display()
