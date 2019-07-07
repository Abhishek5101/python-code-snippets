# import time
#
#
# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__ + " took "  + str((end-start)*1000) + "mil sec")
#         return result
#     return wrapper
#
#
# @time_it
# def calc_square(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     return result
#
#
# @time_it
# def calc_cube(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     return result
#
#
# array = range(1,100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)

"""
Decorator is a function which takes some other function as an argument perform some actions and
returns another function as a result.
All of this without altering the code of the function that
you passed in. You use it when adding a 'common functionality' to a lot of other functions without
actually changing their code. A decorator returns function
"""
