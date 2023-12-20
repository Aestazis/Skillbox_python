print('                           Noise Fields Company')
print('                             Calculator 1.0')
print('                                 18.10.19')
print('--------------------------------------------------------------------------------')
input('для продолжения нажмите Enter')

num1 = int (input ("введите первое число:  "))
num2 = int (input ("введите второе чило:  "))
znak = input('Введите знак: ')

if znak == "+":
    print(num1 + num2)
elif znak == "-":
    print(num1 - num2)
elif znak == "*":
    print(num1 * num2)
elif znak == "/":
    print(num1 + num2)
else:
    print("Введен не верный знак")
input('Для выхода из программы нажмите Enter')