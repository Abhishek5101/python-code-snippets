"""
understanding first class functions in python.
They can be passed on as an argument, returned
 as a value or assigned to a variable
"""


def square(x):
    return x*x


f = square(4)
print(f)

var = map(square, [i for i in range(6)])
print(var)