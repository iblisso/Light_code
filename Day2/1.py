
#Дано число, вывести его если оно четное, иначе возвести его в квадрат.

numbers = int(input("symbol "))
if numbers % 2 == 0:
    print("я прав")
else:
    print(numbers ** 2)