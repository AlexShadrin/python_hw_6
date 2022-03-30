# Python 3.8
# Windows 64-bit

import random
import sys

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

print('Размер массива', sys.getsizeof(r))
print('Размер элемента массива', sys.getsizeof(r[0]))
print('Размер кортежа', sys.getsizeof(tuple(r)))
print('Размер элемента кортежа', sys.getsizeof(tuple(r)[0]))
sum = 0
for size in r:
    sum += sys.getsizeof(size)
print('Размер всех элементов в массиве', sum)

'''
Размер массива 904
Размер элемента массива 28
Размер кортежа 840
Размер элемента кортежа 28
Размер всех элементов в массиве 2800
'''