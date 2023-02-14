# 1. Напишите скрипт, который принимает в себя два пароля. Если пароли совпдают,
# вывести "Успех", иначе "Пароли не совпадают". (Пароль не должен быть короче 8
# символов, но не длиннее 16).

password = input("Enter Password ")
confirmpassword = input("Confirm Password ")

if len(password) >= 8 and len(password) <= 16:
    if password == confirmpassword:
        print("Access Granted")

    else:
        print("Password not Valid")

