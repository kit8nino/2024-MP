#2.Реализация сортировки quick sort(быстрая сортировка):

import random
import numpy as np

def quicksort(array, a, b):
    first = a
    last = b
    if array[b] < array[a + int((b - a) / 2)]:
        array[b], array[a + int((b - a) / 2)] = array[a + int((b - a) / 2)], array[b]
    if array[a] > array[a + int((b - a) / 2)]:
        array[a], array[a + int((b - a) / 2)] = array[a + int((b - a) / 2)], array[a]
    if array[b] < array[a + int((b - a) / 2)]:
        array[b], array[a + int((b - a) / 2)] = array[a + int((b - a) / 2)], array[b]
    pivot = array[a + int((b - a) / 2)]
    #index = a + int((b - a) / 2)
    
    while a < b:
        if array[a] != pivot:
            a += 1
        elif array[b] != pivot:
            b -= 1
        else:
            a += 1
            b -= 1

        while array[a] < pivot:
            a += 1

        while array[b] > pivot:
            b -= 1

        array[a], array[b] = array[b], array[a]

    if a - 1 - first > 2:
        quicksort(array, first, a - 1)
    if last - a - 1 > 0:
        quicksort(array, a + 1, last)
    return array
  
#сортировка для комплексных чисел  
def quicksort_complex(array, a, b):
    first = a
    last = b
    pivot = array[a + int((b - a) / 2)]

    while a <= b:
        while abs(array[a]) < abs(pivot):
            a += 1
        while abs(array[b]) > abs(pivot):
            b -= 1
        if a <= b:
            array[a], array[b] = array[b], array[a]
            a += 1
            b -= 1

    if a - 1 > first:
        quicksort_complex(array, first, a - 1)
    if last > a:
        quicksort_complex(array, a, last)
    return array
    
#1) Список целых чисел от 0 до 999999
integers_list = list(range(1000000))
random.shuffle(integers_list)  # перемешиваем список
print("Начальный список целых чисел:", integers_list[:10])
sorted_integers = quicksort(integers_list ,0, len(integers_list) - 1)
print("Отсортированный список целых чисел:", integers_list[:10])

#2) Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
floats_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Начальный список случайных вещественных чисел:",floats_list[:10])
sorted_floats = quicksort(floats_list ,0, len(floats_list) - 1)
print("Отсортированный список случайных вещественных чисел:", floats_list[:10])


#3) 42000 разных точек комплексной плоскости, лежащие внутри окружности радиуса r = 2 (r=24/12)

#Функция для генерации комплексных чисел
def generate_points(num_points):
    points = []
    for _ in range(num_points):
        # Генерируем случайные координаты в диапазоне [-2, 2) для x и y
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        # Проверяем, лежит ли точка внутри окружности радиуса 2
        if x**2 + y**2 <= 4:
            points.append(complex(x, y))
    return points

complex_list = generate_points(42000)
print("Начальный список комплексных чисел:",complex_list[:10])
sorted_points = quicksort_complex(complex_list ,0, len(complex_list) - 1)
print("Отсортированный список комплексных чисел:", complex_list[:10])


#4) Отрывок из книги «Война и Мир»
with open("war_and_peace.txt", "r", encoding='utf-8') as file:
    war_and_peace_words = file.read().split()
    print("Не отсортированный отрывок из кникги 'Война и мир':",war_and_peace_words[:10])
sorted_excerpt = quicksort(war_and_peace_words ,0, len(war_and_peace_words) - 1)
print("Отсортированный отрывок из 'Войны и Мира':", sorted_excerpt[:10])


