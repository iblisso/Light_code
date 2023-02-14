# Alexey Bogomolov, [13 февр. 2023 г., 20:24:49]:
# with open('out.txt', 'w') as f:
#     Log = input('Login: ')
#     Pass = input('Password: ')
#     a = { "login": Log, "password": Pass}
#     if Log and Pass:
#         f.write(str(a), )

with open('out.txt', 'a') as f:
    Log = input('Login: ')
    Pass = input('Password: ')
    a = { "login": Log, "password": Pass}
    if Log and Pass:
        f.write(str(a)+'\n')
with open("out.txt", "r") as f:
    print(len(f.readlines()))