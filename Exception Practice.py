c = None
a=(input("enter a num\n"))
b=int(input("enter another num\n"))
try:
    c=b/a
    print("Does it print?")
except SyntaxError:
    print("Oops!")
except ZeroDivisionError as ex:
    print("ZeroDev exception occured:", ex)
except TypeError as ty:
    print("Only input integers: " , ty)
except Exception as exx:
    print()
print(c)