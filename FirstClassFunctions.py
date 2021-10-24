def square(x):
    return x * x


f = square

print(square)
print(f(5))  # firstclass function


def cube(x):
    return x * x * x


# custom map function
def my_map(func, arg_list):  # function argument, array argument
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)
