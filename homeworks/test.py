my_pets = ['lion', 'cat', 'dog', 'horse', 'elephant']
for pets in my_pets:
    print('берем', pets)
    if pets == 'dog':
        print('мы нашли собаку, всё хорошо')
        break
    print('нет')
else:
    print('собака в списке не найдена')



