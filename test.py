# тест коммитов
#print('test')
#print('test2')
#print('jopa')

print(4 > 1)
# выводится True или False

print("""jopa\npizda""")
# выводятся две строки. 1 jopa. 2 pizda

kabachok = "шляпа, вторая шляпа, третья шляпа"
print(kabachok[:5])
print(kabachok[7:19])
# выводятся последовательно символы из кабачка

# int - целое число
# float - число с плавающей точкой
# str - строка
batat = 150
tvorog = 150.4
pirozhok = 'хлебобулочное изделие'
print(type(batat))
print(type(tvorog))
print(type(pirozhok))
# выводится тип переменной

print(isinstance(batat, int))
print(isinstance(batat, str))
# выводится True или False в зависимости от типа переменной

print(id(batat))
# выводится id объекта за переменной в оперативной памяти

#print('щас чето сложим и получится вот это:', 2 + 2, batat)
# выводится 4 150

#x, y = map(int, input().split())
#print(type(x))
#print(x, y)

# Поиск символа в строке
print(pirozhok.find('о'))
# Выводится номер символа в строке
print(pirozhok.rfind('и'))
# Выводится номер символа с права налево

print(pirozhok.replace('и', 'ё'))
# Заменяет букву в строке

print(pirozhok.lower())
print(pirozhok.upper())
# Выводит всё в нижнем регистре или в верхнем

bukvocifra = "заебротрон 3000"
bukva = 'abc'
cifra = '123'
ebala = '*********huy@@l'
ebala2 = '       huy     '
print(bukvocifra.isalpha())
print(bukva.isalpha())
# выводит состоит ли строка только из букв или нет. Возвращает True или False

print(bukvocifra.isnumeric())
print(cifra.isnumeric())
# выводит состоит ли строка только из цифр или нет

print(ebala.strip('*@l'))
print(ebala2.strip())
# Удаляет из строки указанные символы. Если не указан аргумент, обрежет строку с обеих концов, пробелы например
































