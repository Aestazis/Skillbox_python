print('--------------------------------------------------------------------------------')
print('''В версии 1.0.1 добавлено:
# Новые формы для ответов
# Улучшенные алгоритмы ответов
# Новые вопросы и ответы, а так же факты
# Улучшенный интерфейс
''')
print('--------------------------------------------------------------------------------')
input('Для продолжения нажмите Enter')
print('Как тебя зовут?')
name = input("Ваш ответ: ")
print('Привет', name,"!")
print('===================================')
#Вопрос Как дела?
print('Как твои дела?')
vopros_dela = (input("Ваш ответ: "))
if vopros_dela == 'хорошо':
    print("отлично, когда дела хорошо")
elif vopros_dela == "Хорошо":
    print("Отлично, когда дела хоршо")
elif vopros_dela == 'отлично':
    print("Хорошо, когда всё отлично")
elif vopros_dela == 'Отлично':
    print("Хорошо, когда всё отлично")
elif vopros_dela == 'замечательно':
    print('Хорошо, когда всё замечатльно')
elif vopros_dela == 'Замечательно':
    print('Хорошо, когда всё замечательно')
elif vopros_dela == 'нормально':
    print('Хорошо, когда всё нормально')
elif vopros_dela == 'Нормально':
    print('Хорошо, когда всё нормально')
else:
    print("бывает... что уж тут поделать")

#Конец вопроса Как дела?

#Вопрос про бегемота
print('===================================')
print('раз с делами разобрались, давай поговорим о чем нибудь отвлеченном.')
print('Например, ты знаешь что вес беременного бегемота равен 800 килограмм?')
vopros_begemot = input('Ваш ответ: (да\нет) ')
if vopros_begemot == 'да':
    print('ничесе какой ты умный...')
elif vopros_begemot == 'нет':
    print('ну вот теперь знаешь, что беременный бегемот весит 800 кг, пользуйся этим')
    print("===================================")
#Конец вопроса про бегемота

#Заключительный вопрос или выход из программы
#Medved - функция с ответом про медведя
def medved():
    print('Все белые медведи - левши. Теперь ты это знаешь!')
    print('===================================')

input('Для выхода из программы нажмите Enter')