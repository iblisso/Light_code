# Задание №7:
# Как в Linux выглядит полный путь до Desktop Директории для пользователя 'developer'.
# /Users/developer/desktop

# # Задача 9
# # Есть набор чисел
#
# # # # Поделить каждое число из digits на 9 и вывести на экран.
# #
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for number in digits:
#     print(number / 9)


# Задача 10
# Здесь замешаны разные типы данных.
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
#
#
#
# for i in spisok_2:
#     if not i in spisok_1:
#         print("Unique list from spisok_2: ", i)


# # Задание 13:
# # Вам дан список:

# # # # # Определите количество четных и не четных.
# # #

# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# countable = 0
# uncountable = 0
#
# for i in numbers:
#     if int(i) % 2 == 0:
#             countable += 1
#
#     else:
#         uncountable += 1
# print("Countable: ", countable, ", and uncountable: ", uncountable)
# print(f"Countable: {countable} uncountable: {uncountable}")




 # Задание 14:
# # Дан список  целых чисел:

# # # # Создайте новый лист и замените отрицательные числа на -1, положительные на число 1,
# # # # ноль оставить без изменения.
# # # #

# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# numbers2 = 0
# for i in numbers:
#     if int(i) > 0:
#        numbers2 = 1
#
#     elif i < 0:
#         numbers2 = -1
#
#     else:
#         i == 0
#         numbers2 = 0
#     print(numbers2)
# #

