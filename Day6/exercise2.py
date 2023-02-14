# 2. Вы хотите начать путешествие и с собой можете взять только рюкзак вещей.
# Вы можете нести только n кг. Определите какие вещи от наиболее тяжелых к самым легким
# поместятся в ваш рюкзак. Вот словарь ваших вещей и вес в граммах

things = {
    'зажигалка': 20,
    'компас': 100,
    'фрукты': 500,
    'рубашка': 300,
    'термос': 1000,
    'аптечка': 200,
    'куртка': 600,
    'бинокль': 400,
    'удочка': 1200,
    'салфетки': 40,
    'бутерброды': 820,
    'палатка': 5500,
    'спальный мешок': 2250,
    'жвачка': 10
}

    # all = sorted(things.values())
    # new_dict = {}# for i in all:
    #     for k in things.keys():#         if things[k] == i:
    #             new_dict[k] = things[k]# print(new_dict)

common_weight = int(input()) * 1000
print(type(common_weight))
allowed_things = []
our_weight = 0
for i, v in things.items():
    if our_weight < common_weight:
        allowed_things.append(i)
        our_weight += v
    if our_weight > common_weight:
        allowed_things.append(i)
        our_weight -= v

print(our_weight)
print(allowed_things)