a = 7
b = 6

# print(a
# SyntaxError: '(' was never closed

# print(a / 0)
# ZeroDivisionError: division by zero

try:
    if a > b:
        print(c / 0)
except NameError:
    print("Error")
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")

print('Hello World')

