# тест коммитов
# print('test')
# print('test2')
# print('jopa')

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

# print('щас чето сложим и получится вот это:', 2 + 2, batat)
# выводится 4 150

# x, y = map(int, input().split())
# print(type(x))
# print(x, y)

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

# Сиски являются изменяемыми объектыми и создаются в квадратных скобках
spisok = []  # или spisok = list()
spisok2 = [1, 2, 3, 4, 5, batat, 'Джигурда']
spisok3 = []  # сюда будем добавлять объекты
spisok4 = list([1, 2, 3, 4, 5])
spisok5 = [1, 6, 4, 8, 10, 5]
# Квадратные скобки позволяют создать список

print(spisok2[5])
print(spisok2[-1])
print(spisok2[:5])
print(spisok2[::2])  # от начала до коцнца с шагом 2
print(spisok2[1:5:2])  # от 1 до 5 с шагом 2
print(spisok5[::-1])  # от конца до начала. Только цифры или строки. Переменные вертеть нельзя
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

spisok4[1] = 300
# меняет второй объект на 300

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
print(matrix[2][1])  # 2 - список, 1 - объект. Объекты считаются 0(1об.), 1(2об.), 2(3об.), 3(4об.) и т.д.
# выводит первый объект из первого списка и второй объект из третьего списка

# [123, 2, 'лалалей', 3, 4] - что сейчас находится в переменной spisok3
print(123 in spisok3)
print(5 in spisok3)
# выводит находится ли объект в списке. True или False

gen = list(range(20))  # выводит список с последовательными числами от 0 до 19
gen2 = list(range(5, 10))  # выводит список с 5 по 9
gen3 = list(range(5, 10, 2))  # выводит список с по 9 с шагом 2

print(gen.count(5))  # выводит сколько пятерок у нас в списке
print(min(gen))  # выводит минимальное число в списке
print(max(gen))  # выводит максимальное число в списке

spisok5.sort()  # сортирует список
print(spisok5)

# списки в квадратных скобках изменяемые а в круглый не изменяемые
my_tuple = (1, 2, 3)
# если попробовать добавить цифру в список - будет ошибка
print(my_tuple + (5, 6))
# но можно их складывать. Создатся новый объект со своим id

# В фигурных скобках создаются словари или кортежи.
my_box = {}
my_box['овощ'] = batat
my_box['машина'] = 'car'
print(my_box)
# выводит словарь. Мы сказали что переменная batat это овощ, а машина car (ключ : значение)

my_box = {'овощ': batat, 'машина': 'car'}
# или можно так

print(my_box['овощ'])
# выводит значение по ключу

print(my_box.get('кот', 'Murzik'))
# Если в словаре нет ключа кот, то при его запросе вывести Муризка
print(my_box.setdefault('кот', 'Murzik'))
print(my_box)
# Если в словаре нет ключа кот, то добавляет его в словарь

# множества
my_set = {1, 5, 6, 7, 2, 6, 5, 4, 4, 1}
my_set2 = set([1, 5, 6, 7, 2, 6, 5, 4, 4, 1])
# создает множество, в котором может быть только один уникальный объект. Выдает {1, 2, 4, 5, 6, 7}

other_set = {25, 46, 55, 145, 1, 5, 4}
print(my_set | other_set)  # объединяет оба множества в одно
print(my_set & other_set)  # выводит пересекающиеся числа во множестве (какие есть там и там)
print(my_set - other_set)  # попали только те элементы из первого списка, которых нет во втором спике
# .add() - добавление во множество
# .pop() discard() - удаление из множества
# .update() - обновление

# from pprint import pprint - pprint пишет в строку в словаре

# вычисление общего роста на примере домашки
family = [['father', 180],
          ['monther', 160]]
height = family[0][1]
height = height + family[1][1]
# или можно записать
height += family[1][1]
print(height)

# break
my_pets = ['cat', 'dog', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('вытащили', pet)
    if pet == 'cat':
        print('это кот')
        break
    i = i + 1
print('конец')
# Если в списке есть кот, выводит что нашли и заканчивает цикл

my_pets = ['dog', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('вытащили', pet)
    if pet == 'cat':
        print('это кот')
        break
    i = i + 1
else:
    print('не нашли...')
print('конец')
# Если кота нет, выводит через else что не нашли.

# continue
my_pets = ['dog', 'lion', 'skunk', 'hamster', 'cat', 'monkey']
i = -1
while i < len(my_pets):
    i = i + 1
    if i == 2:
        continue
    pet = my_pets[i]
    print('вытащили', pet)
    if pet == 'cat':
        print('это кот')
        break
else:
    print('не нашли...')
print('конец')
# когда i становится 2, то цикл начинается заново, не проходя дальше continue

my_pets = ['lion', 'cat', 'dog', 'horse', 'elephant']
for pets in my_pets:
    print('берем', pets)
    if pets == 'dog':
        print('мы нашли собаку, всё хорошо')
        break
    print('нет')
else:
    print('собака в списке не найдена')  # если убрать 'dog' из списка
# Пример с циклом for in
