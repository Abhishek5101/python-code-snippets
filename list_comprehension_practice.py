import timeit


def squares(size):
    result = []
    for number in range(size):
        result.append(number * number)
    return result


def squares_comprehension(size):
    return [number * number for number in range(size)]


print(timeit.timeit("squares(50)", "from __main__ import squares", number = 1_000_000))
print(timeit.timeit("squares_comprehension(50)", "from __main__ import squares_comprehension", number = 1_000_000))
