f = open('text.txt', 'r')
d = 'qwerty'
g = f.read()
if d in g:
    print(True)


f.close()