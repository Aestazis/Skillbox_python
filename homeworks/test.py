codes = {
    'calimb': '1234',
    'pen': '5678'
}

store = {
    '1234': [{'kol': 20, 'price': 550}],
    '5678': [{'kol': 50, 'price': 235},
             {'kol': 30, 'price': 250}]
}

calimb_code = codes['calimb']
pen_code = codes['pen']

calimb_kol = store[calimb_code][0]
calimb_kol2 = calimb_kol['kol']
calimb_price = calimb_kol['price']
print('Калимба - ', calimb_kol2, 'шт.', 'Стоимость - ', calimb_kol2 * calimb_price)

pen_item = store[pen_code]
pen_string1 = pen_item[0]
pen_string2 = pen_item[1]
pen_col1 = pen_string1['kol']
pen_col2 = pen_string2['kol']
pen_price1 = pen_string1['price']
pen_price2 = pen_string2['price']
general_col_pen = pen_col1 + pen_col2
general_price_pen = pen_price1 + pen_price2
print(general_price_pen)
print('Ручка -', general_col_pen, 'шт. Стоимость -', general_price_pen * general_col_pen, 'руб')


