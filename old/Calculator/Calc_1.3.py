print('                           Noise Fields Company')
print('                             Calculator 1.3')
print('                                 22.10.19')
print('--------------------------------------------------------------------------------')
print('               Добро пожаловать в калькулятор версии 1.3')
print('''                        Что нового в версии 1.3:
#Исправлено отображение результата выражения
#Добавлен повтор действия по желанию
#Добавлены выражения с дробными числами
#Исправлен вылет программы при делении на ноль''')
print('--------------------------------------------------------------------------------')
input('для продолжения нажмите Enter')
print()


def calc():
    global num1
    while True:
        try:
            num1 = float(input("введите первое число:  "))
        except ValueError:
            print("Вы ввели не число. Пожалуйста введите еще раз")
            continue
        else:
            break

    while True:
        try:
            num2 = float(input("введите второе чило:  "))
        except ValueError:
            print('Вы ввели не число. Пожалуйста введите еще раз')

            continue
        else:
            break

    print('''Ведите действие для решения:
+ Для сложения
- Для вычитания
* для умножения
/ для деления
 ''')
    znak = input('Действие: ')
    if znak == '+':
        print('Результат:')
        print('{} + {} ='.format(num1, num2), num1 + num2)
    elif znak == '-':
        print('Результат:')
        print('{} - {} ='.format(num1, num2), num1 - num2)
    elif znak == '*':
        print('Результат:')
        print('{} * {} ='.format(num1, num2), num1 * num2)
    elif znak == '/':
        print('Результат:')
        if num2 == 0:
            print()
            print('Деление на ноль не возможно!')
            print()
            calc()
        print('{} / {} ='.format(num1, num2), num1 / num2)

    else:
        print('не корректный знак!')
    print("--------------------------------------------------------------------------------")
    again()


def again():
    print('''
Хотите повторить вычисление?
Пожалуйста, введите "да" для продолжения, "нет" для выхода из программы''')
    calc_again = input('')
    if calc_again == 'да':
        calc()
    elif calc_again == 'нет':
        print('Всего доброго!')
    else:
        again()


calc()
