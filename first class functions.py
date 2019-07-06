"""
understanding first class functions in python.
They can be passed on as an argument, returned
 as a value or assigned to a variable
"""


def square(x):
    return x*x


f = square
print(f)