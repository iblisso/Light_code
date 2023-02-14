a = 7
b = 6

try:
    if a > b:
        print(c / 0)
except NameError:
    print("Error")
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")

print('Hello World')