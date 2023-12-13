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
# выводится True или False в зависимости от типа переменной (является ли числом или строкой переменная)

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

spisok = []
spisok2 = [1, 2, 3, 4, 5, batat, 'Джигурда']
spisok3 = [] # сюда будем добавлять объекты
print(spisok2)
# Квадратные скобки позволяют создать список

print(spisok2[5])
print(spisok2[-1])
print(spisok2[:5])
print(spisok2[::2]) # от начала до коцнца с шагом 2
print(spisok2[1:5:2]) # от 1 до 5 с шагом 2
# Выводит объект по счету

spisok3.append(123)
print(spisok3)
# добовляет в конец списка один объект

spisok3.extend([1, 2, 3, 4, 5])
print(spisok3)
# расширяет список. Добавляет в конец много объектов

spisok3.insert(3, 'лалалей')
print(spisok3)
# добавляет в третью строку объект 'лалалей'

del spisok3[6]
print(spisok3)
# удаляет объект из списка

spisok3.remove(1)
print(spisok3)
# удаляет первый попавшийся объект, указанный в скобках (1)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
# создает список списоков

print(matrix[0][0])
print(matrix[2][1]) # 2 - список, 1 - объект. Объекты считаются 0(1об.), 1(2об.), 2(3об.), 3(4об.) и т.д.
# выводит первый объект из первого списка и второй объект из третьего списка

# [123, 2, 'лалалей', 3, 4] - что сейчас находится в переменной spisok3
print(123 in spisok3)
print(5 in spisok3)
# выводит находится ли объект в списке. True или False











































