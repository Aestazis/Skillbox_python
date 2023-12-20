print('                           Noise Fields Company')
print('                             Calculator 1.2')
print('                                 21.10.19')
print('--------------------------------------------------------------------------------')
print('               Добро пожаловать в калькулятор версии 1.2')
print('''                        Что нового в версии 1.2:
#Исправлено отображение вводимых знаков для действия 
#Исправлен вылет программы при вводе символа, отличного от числа''')
print('--------------------------------------------------------------------------------')
input('для продолжения нажмите Enter')
print()
num1 = 0
while True:
    try:
        num1 = int(input("введите первое число:  "))
    except ValueError:
        print("Вы ввели не число")
        continue
    else:
        break
num2 = 0
while True:
    try:
        num2 = int(input("введите второе чило:  "))
    except ValueError:
        print('Вы ввели не число')
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
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
elif znak == '-':
    print('Результат:')
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)
elif znak == '*':
    print('Результат:')
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)
elif znak == '/':
    print('Результат:')
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)
else:
    print('не корректный знак')

input('Для выхода из программы нажмите Enter')
# При вводе не верного знака, должно возвращать к первому вопросу "введите действие"