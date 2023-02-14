# Функция filter() в Python применяет другую функцию
# к заданному итерируемому объекту
# (список, строка, словарь и так далее), проверяя,
# нужно ли сохранить конкретный элемент или нет.
#  Простыми словами, она отфильтровывает то,
#  что не проходит и возвращает все остальное.
# """

# a = [i for i in range(1, 11)]
# b = filter(lambda x: x % 2 == 0, a)
# # f = list(b)
# # print(f)
# for i in b:
#     print(i)


# city = ('Bishkek', "Osh", "Batken", "Kara-Balta")
# # b = filter(str.isalpha, city)
# b = filter(lambda x: len(x) % 2 ==0,filter(str.isalpha, city))
# print(list(b))