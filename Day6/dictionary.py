#словари (dict) Dictionary
#** s распаковка

s = {
    "key": {'value': 12},
    "key1": {'value': 12},
    12: 1.6,
    (13, 56): ["fsg", 123]
}

d = {
    'tr': 345,
    767: 'qwer',

}

d1 = {
    'tr': 345,
    767: 'qwer',
    77: 'kjhg'

}

# for i in d1.keys():
#     print(i)
#
# for i in d1.values():
#     print(i)

for key, value in d1.items():
    print(f'qwerty: {key}, 12345: {value}')



# print(d == d1) # False, True

# f = d.copy()
# f = d.deepcopy()
# print(f)

# del d["tr"]
# d.update(s)
# print(d.pop("tr"))
# s["key1"] = 'New Values'

a = {**s, **d}

# print(s.keys())
# print(s.values())
# print(s.items())
# print(len(s))
# print(s)
# print(s["key"]["value"])
# print(s[13, 56][1])


print(a)
# d.clear()
# print("tr" in d)


