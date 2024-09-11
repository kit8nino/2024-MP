import random
import math as mt
import string

import functions_2.py

# НАДО РАСКОММЕНТИТЬ ПРИНТЫ ЧТОБЫ ПОЛУЧАТЬ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ 
# ДЛЯ КАЖДОГО АЛГОРИТМА !!!!!!!!

# генерирую свой список алгоритмов: 
# print(random.sample(range(1, 18), 4) )
# выпало: [14, 7, 4, 9]


#  Генерируем случайный список целых чисел от 0 до 999999
arr_1 = [random.randint(0, 999999) for i in range(100000)]
# print(arr_1)


# генерирую вещественные числа из [-1,1]
arr_2 = [random.uniform(-1, 1) for _ in range(99999)]
# print(arr_2)


# генерирую 42000 точек внутри окружности радиуса r = 3.5
r = 3.5
num_points = 42000
arr_3 = []
for i in range(num_points):
    #  Генерируем случайный угол в диапазоне [0, 2*pi)
    angle = random.uniform(0, 2*math.pi)
    #  Генерируем случайное расстояние от центра до точки в диапазоне [0, r)
    radius = math.sqrt(random.uniform(0, r**2))
    #  Преобразуем полярные координаты в декартовы координаты
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    arr_3.append(complex(x, y))
# print(arr_3)

# считываю текст из файла
file = open("text.txt", 'r', encoding="utf-8")
arr_4 = []
to_remove_symbols = ['"', "'", '.', '«', '»', '!']
for line in file:
    for word in line.split(' '):
        if (word != '' and word != '\n' and word != '-'):
            for symbol in to_remove_symbols:
                word.replace(symbol, '')
            arr_4.append(word.replace('\n', ''))
# print(len(arr_4))
# print(arr_4)

radix_sort(arr_1)
print("Сортировка 1 закончена")
print('\n')


sorted_arr_2 = gnome_sort(arr_2)
print("Сортировка 2 закончена")
print('\n')

insertion_sort(arr_3)
print("Сортировка 3 закончена")
print('\n')

heap_sort(arr_4)
print("Сортировка 4 закончена")
print('\n')
