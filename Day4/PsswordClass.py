incorrect_symbols = '!@#$%^&*()_+'
password1 = "QWERty12345"
password2 = input('Confirm Password!')

digits - "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz1234567890"
isvalid = ''

while True:
    for i in password1:
        if i in digits:
            isvalid += i
    if password1 == password2:
        if len(password1) == len(isvalid):
            print('Done!')
            break

        else:
            print('Fail!')

    else:
        print('Password Didnt match!')