# 1. Дан диапазон чисел от 1 до 1000. Вывести все четные числа которые делятся на 7 без
# остатка.

for i in range(1, 1000):
    if i % 2 == 0:
        if i % 7 == 0:
            print(i)

for b in range(1, 1000):
    if b % 2 == 0 and b % 7 == 0:
        print(b)

tb = []
for i in range(1, 1000):
    if i % 2 == 0 and i % 7 == 0:
        tb.append(i)
        print(i)

print(len(tb))