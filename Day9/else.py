a = 7
b = 6

try:
    if a > b:
        print(a - 0)
except NameError:
    print("Error")
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")
else:
    print('ZBS')
print('Hello World')