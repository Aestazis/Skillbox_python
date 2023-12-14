#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['father', 'monther', 'sister']


# список списков приблизителного роста членов вашей семьи
my_family_height = [['father', 180], ['monther', 160], ['sister', 140]]
    # ['имя', рост],
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Рост отца', my_family_height[0][1], 'cm')

father = my_family_height[0][1]
monther = my_family_height[1][1]
sister = my_family_height[2][1]
print('общий рост:', father + monther + sister, 'cm')









