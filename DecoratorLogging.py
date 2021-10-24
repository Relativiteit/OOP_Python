import time
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# @decorator_function
# def display():
#     print('display function ran')


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info = my_timer(display_info)  # same as @ my_logger @ my_timer
# display_info = my_logger(my_timer(display_info))  # same as @my_timer

print(display_info.__name__)
#display_info('Juan', 29)
display_info('Tom', 40)
# display()
