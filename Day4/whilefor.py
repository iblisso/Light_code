#цикл while for


i = 10
while i <= 100:
    print(i)
    print('First')
    #i = i + 5
    i += 5
    while i < 100:
        print(i)
        print('Second')
        i += 10
print(i)