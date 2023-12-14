#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# здесь ваш код

print(my_favorite_movies[:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])

# с помощью словарей

box_movies = {'Terminator': 'Терминатор', 'Five': 'Пятый элемент', 'Avatar': 'Аватар', 'Aliens': 'Чужие', 'back': 'Назад в будущее'}
print(box_movies['Terminator'])
print(box_movies['back'])
print(box_movies['Five'])
print(box_movies['Aliens'])

