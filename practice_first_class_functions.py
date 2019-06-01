def square(x):
    return x * x


def map_func(squarey, listy):
    result = []
    for i in listy:
        result.append(squarey(i))
    return result


def cube(x):
    return x * x * x


it = map_func(square, [1,2,3,4,5,6,])
print(it)

ity = map_func(cube, [1,2,3,4,5,6,7,])
print(ity)

