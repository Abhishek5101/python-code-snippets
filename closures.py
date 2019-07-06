"""
Understanding the concept of closures in python
"""


def outer():
    message = "Sup?"

    def inner():
        print(message)
    return inner()


a = outer()
a()
a()