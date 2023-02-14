# 3. Вам даны две строки. Нужно найти есть ли одна строка в другой строке вне
# зависимости от регистра. Если есть вывести "Есть", иначе "Нет"

str1 = input()
str2 = input()

print(str1)

if str1.lower() in str2.lower():
    print("Done")
else:
    print("False")