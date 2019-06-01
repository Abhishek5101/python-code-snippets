try:
    print("Hey! Welcome to the calculator")

    name = input("What is your name?\n")
    a = int(input("Please enter first number, {}\n".format(name)))
    b = int(input("Please enter second number\n"))

    add = a+b
    sub = a-b
    mul = a*b
    div = a/b

    print("1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "")

    option = int(input("What would you like to do with these two numbers\n"))

    if option == 1:
        print(add)
    elif option == 2:
        print(sub)
    elif option == 3:
        print(mul)
    elif option == 4:
        print(div)
except:
    print("Oops! Only Numbers!")