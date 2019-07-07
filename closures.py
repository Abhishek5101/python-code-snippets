"""
Understanding the concept of closures in python
"""


def outer():
    message = "Sup?"

    def inner():
        print(message)
    return inner


a = outer()
a()
a()
"""
Above illustrates the concept of a closure. The var 'a' holds
a function which is waiting to be executed- a calls outer() which 
in turn refers to but does not call  inner. But when you call a()
inner() gets called
"""