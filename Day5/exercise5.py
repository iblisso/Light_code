# 5. У вас есть список из строк.
# Ваша задача найти самую длинную,
# затем привести каждую остальную строку к такой же длине
# заполняя их символом "_".['Something', 'in', 'the', 'way', 'mmmmmmm', 'btw', 'python', 'is', 'better', 'than', 'js']

s = ['Something', 'in', 'the', 'way', 'mmmmmmm', 'btw', 'python', 'is', 'better', 'than', 'js']


smax = max(s, key=len)
for i in range(len(s)):
    while len(s[i]) < len(smax):
        s[i] += '_'

print(s)