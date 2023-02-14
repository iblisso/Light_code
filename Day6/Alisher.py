
d = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K',],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

word = input("Введите слово без цифр и спецсимволов: ").upper()
result = 0

for letter in word:
    if letter in d[1]:
        result += 1

    elif letter in d[2]:
        result += 2

    elif letter in d[3]:
        result += 3

    elif letter in d[4]:
        result += 4

    elif letter in d[5]:
        result += 5

    elif letter in d[8]:
        result += 8

    elif letter in d[10]:
        result += 10

print(f"Ваш результат: {result}!")