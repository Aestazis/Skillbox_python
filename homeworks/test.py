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
