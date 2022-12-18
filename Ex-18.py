# Реализуйте алгоритм перемешивания списка.

import random

n = 20
spisok = []                     # Сформируем изначальный список
for i in range(n):
    spisok.append(i)

print(spisok)

# Берем элемент списка со случайным индексом, удаляем его из списка и заново добавляем в конец
for i in range(len(spisok)):
    temp = random.choice(spisok)
    spisok.remove(temp)
    spisok.append(temp)

print(spisok)