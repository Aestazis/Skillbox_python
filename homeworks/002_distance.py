#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2


moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[0]) ** 2) ** .5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
moscow_paris = (moscow_london + london_paris)

moscow_box = {'london': moscow_london, 'paris': moscow_paris}
london_box = {'moscow': moscow_london, 'paris': london_paris}
paris_box = {'moscow': moscow_paris, 'london': london_paris}

distances = {'Moscow': moscow_box, 'London': london_box, 'Paris': paris_box}
pprint(distances)




