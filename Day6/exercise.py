# 1. В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
#     A, E, I, O, U, L, N, S, T, R – 1 очко;
#     D, G – 2 очка;
#     B, C, M, P – 3 очка;
#     F, H, V, W, Y – 4 очка;
#     K – 5 очков;
#     J, X – 8 очков;
#     Q, Z – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские буквы.

a = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

answer = input("введите буву... ").upper()
coins = 0

for i in answer:
    if i in a[1]:
        coins += 1

    elif i in a[2]:
        coins += 2

    elif i in a[3]:
        coins += 3

    elif i in a[4]:
        coins += 4

    elif i in a[5]:
        coins += 5

    elif i in a[8]:
        coins += 8

    elif i in a[10]:
        coins += 10




print(f'Result is {coins} units')
