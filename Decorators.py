# Decorators

def decorator_function(orginal_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(orginal_function.__name__))
        return orginal_function()
    return wrapper_function


def display():
    print('disp[lay function ran')


decorated_display = decorator_function(display)

decorated_display()
