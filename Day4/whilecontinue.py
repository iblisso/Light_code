i = 10

while True:
    i += 1
    if i == 1000:
        break
    if i % 2 == 0:
        continue
    print(i)