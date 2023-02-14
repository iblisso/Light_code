# 4. Напишите скрипт для валидации паролей. Пользователь должен вводить два пароля и в
# случае, если они одинаковы вывести "Успех", иначе "Повторите попытку". Пароль должен:
#   1) Быть больше или равному 8 символам или меньше или равным 16 символам.
#   2) Содержать заглавные буквы.
#   3) числа.
#   4) не содержать в себе символы "*-№#?!@$%^()="
# В случае если пароль не соответствует хотя бы одному условию, вывести соответствующую
# надпись.


password = input("Enter Password ")
confirm_password = input("Confirm Password ")
password_attempt = 1
wrong_password = False

while password != confirm_password and  not(wrong_password) :
    if len(password) >= 8 and len(password) <= 16 and password_attempt <= 3:
        print(password)
    else:
        wrong_password = True
    password_attempt = password_attempt + 1

if wrong_password:
    print("ACCESS IS DENIED!")

else:
    print("Access Granted")