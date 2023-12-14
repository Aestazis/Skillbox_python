#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamps_col = store[goods['Лампа']][0]['quantity']
print('Лампа -', lamps_col, 'шт, стоимость', lamps_cost, 'руб')

table_col_1 = store[goods['Стол']][0]['quantity']
table_col_2 = store[goods['Стол']][1]['quantity']
general_col = table_col_1 + table_col_2
table_cost = general_col * (store[goods['Стол']][0]['price'] +
                            store[goods['Стол']][1]['price'])
print('Стол -', general_col, 'шт. Стоимость -', table_cost, 'руб.')

couch_col_1 = store[goods['Диван']][0]['quantity']
couch_col_2 = store[goods['Диван']][1]['quantity']
general_col = couch_col_1 + couch_col_2
couch_cost = general_col * (store[goods['Диван']][0]['price'] +
                            store[goods['Диван']][1]['price'])
print('Диван -', general_col, 'шт. Стоимость -', couch_cost, 'руб.')

chair_col_1 = store[goods['Стул']][0]['quantity']
chair_col_2 = store[goods['Стул']][1]['quantity']
chair_col_3 = store[goods['Стул']][2]['quantity']
general_col = chair_col_1 + chair_col_2 + chair_col_3
couch_cost = general_col * (store[goods['Стул']][0]['price'] +
                            store[goods['Стул']][1]['price'] +
                            store[goods['Стул']][2]['price'])
print('Стул -', general_col, 'шт. Стоимость -', couch_cost, 'руб.')


print('----------------------------------------------------------------------------')

# или проще (/сложнее ?)
table_code = goods['Стол']
couch_code = goods['Диван']
chair_code = goods['Стул']
lamp_code = goods['Лампа']

lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_item1 = store[table_code][0]
table_item2 = store[table_code][1]
table_col1 = table_item1['quantity']
table_col2 = table_item2['quantity']
table_price1 = table_item1['price']
table_price2 = table_item2['price']
general_col = table_col1 + table_col2
general_price = table_price1 + table_price2
print('Стол -', general_col, 'шт. Стоимость -', general_col * general_price, 'руб')

couch_item1 = store[couch_code][0]
couch_item2 = store[couch_code][1]
couch_col1 = couch_item1['quantity']
couch_col2 = couch_item2['quantity']
couch_price1 = couch_item1['price']
couch_price2 = couch_item2['price']
general_col = couch_col1 + couch_col2
general_price = couch_price1 + couch_price2
print('Диван -', general_col, 'шт. Стоимость -', general_col * general_price, 'руб')

chair_item1 = store[chair_code][0]
chair_item2 = store[chair_code][1]
chair_item3 = store[chair_code][2]
chair_col1 = chair_item1['quantity']
chair_col2 = chair_item2['quantity']
chair_col3 = chair_item3['quantity']
chair_price1 = chair_item1['price']
chair_price2 = chair_item2['price']
chair_price3 = chair_item3['price']
general_col = chair_col1 + chair_col2 + chair_col3
general_price = chair_price1 + chair_price2 + chair_price3
print('Стул -', general_col, 'шт. Стоимость -', general_col * general_price, 'руб')



# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# здесь ваш код

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################