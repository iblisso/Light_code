# 2. Вам дана строка: "hELlo woRLd". Выведите первое слово в нижнем регистре (Но
# первая буква должна быть заглавной), а второе в вверхнем.

name = "hELlo woRLd"
name = name[0:5].title() + ' ' + name[6:].upper()

print(name)

name = "heLlo woRLd"
print(str.title(name[0:5]), str.upper(name[6:]))

print(name[0:5].title(), name[6:].upper())