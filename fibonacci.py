def fibonacci():
    high = 1
    fibonacci_list = [0, 1]
    keepgoing = True
    while keepgoing:
        high += fibonacci_list[-2]
        fibonacci_list.append(high)
        if len(fibonacci_list) > 50:
            keepgoing = False
    print(fibonacci_list)


fibonacci()
