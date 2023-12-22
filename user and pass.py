print('==Регистрация нового пользователя==')
username = 'хуй'
password = 'хуй'
repeat_password = 'пизда'

while username == 'хуй':
    username = input('Введите имя пользователя: ')
    if username == '':
        username = 'хуй'
print()
while password != repeat_password:
    password = input('введите новый пароль: ')
    repeat_password = input('Повторите пароль: ')
    if password != repeat_password:
        print('''==Пароли не совпадают==
                                    ''')
print('==Успешная регистрация==')
print()
repeat_password = password

i_user = 'хуй'
i_pass = 'пизда'
while i_user != username or i_pass != password:
    i_user = input('Введите имя пользователя: ')
    i_pass = input('Введите пароль: ')
    if i_pass != password or i_user != username:
        print('==Неверное имя пользователя или пароль== ')
        print()
print()
print('==Успешная авторизация==')












