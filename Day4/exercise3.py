# 3. У вашего игрового персонажа есть шкала энергии, которая равна 1000 единиц. И у вас есть
# определенные активности, которые забирают у вас энергию. 1 - спорт (100 единиц), 2 -
# домашняя активность (60 единиц), 3 - уроки (180 единиц), 4 - слушать нытье(200 единиц).
# Так же есть активности, которые дают вам энергию: 1 - прослушивание музыки (60 единиц),
# 2 - прием пищи (150 единиц), 3 - сон (500 единиц).
# Задача: пользователь должен сам выбирать активности до тех пор, пока не закончится
# энергия. Вывести на сколько в общем было потрачено энергии и сколько восполнено.

health = 1000
sport = 100
homeactions = 60
homework = 180
swear = 200
eating = 150
sleeping = 500

while health > 0:
    #print("health = 1000, sport = 100, homeactions = 60,homework = 180,swear = 200,eating = 150,sleeping = 500")
    action = input("Choose action...")
    if action == 'sport':
        health -= sport
        print(f'Health: {health}')
    if action == 'homeactions':
        health -= homeactions
        print(f'Health: {health}')
    if action == 'homework':
        health -= homework
        print(f'Health: {health}')
    if action == 'swear':
        health -= swear
        print(f'Health: {health}')
    if action == 'eating':
        health += eating
        print(f'Health: {health}')
    if action == 'sleeping':
        health += sleeping
        print(f'Health: {health}')
    else:
        input("Choose action...") != action
        print('Incorrect!')

else:
    print(f'Fatality! Health: {health}')