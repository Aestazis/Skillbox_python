
print('                           Noise Fields Company')
print('                             Calculator 1.1')
print('                                 21.10.19')
print('--------------------------------------------------------------------------------')
print('               Добро пожаловать в калькулятор версии 1.1')
print('''                        В данной версии добавлено:
#Отображение выражения. Теперь можно видеть как происходит решение
#Добавлено описание символов, которые можно вводить''')
input('для продолжения нажмите Enter')
print('--------------------------------------------------------------------------------')

num1 = int (input ("введите первое число:  "))
num2 = int (input ("введите второе чило:  "))
znak = (input ('''Ведите действие для решения:
+ Для сложения
- Для вычитания
* для умножения
/ для деления
 '''))
#при вводе не верного числа или букв должно писать "не верное число" и возвращать обратно
if znak == '+':
    print('Результат:')
    print('{} + {} = '.format(num1,num2))
    print(num1 + num2)
elif znak == '-':
    print('Результат:')
    print('{} - {} = '.format(num1,num2))
    print(num1 - num2)
elif znak == '*':
    print('Результат:')
    print('{} * {} = '.format(num1,num2))
    print(num1 * num2)
elif znak == '/':
    print('Результат:')
    print('{} / {} = '.format(num1,num2))
    print(num1 / num2)
else:
    print('введен не верный знак')
    input('Для выхода из программы нажмите Enter')
input('Для выхода из программы нажмите Enter')
#При вводе не верного знака, должно возвращать к первому вопросу "введите действие"