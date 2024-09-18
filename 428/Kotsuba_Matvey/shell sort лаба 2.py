#3.Реализация сортировки Shellsort (сортировка Шелла):

import random
import numpy as np

def shellsort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
        

#сортировка для комплексных чисел
def shellsort_complex(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and abs(array[j - gap]) > abs(temp):
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2


# 1) Список целых чисел от 0 до 999999
integer_list = list(range(1000000))
random.shuffle(integer_list)
print("Начальный список целых чисел:", integer_list[:10])
shellsort(integer_list)
print("Отсортированный список целых чисел:", integer_list[:10])


# 2) Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Начальный список случайных вещественных чисел:",float_list[:10])
shellsort(float_list)
print("Отсортированный список случайных вещественных чисел:", float_list[:10])

# 3) 42000 разных точек комплексной плоскости, лежащие внутри окружности радиуса r = 2 (r=24/12)

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
shellsort_complex(complex_list)
print("Отсортированный список комплексных чисел:", complex_list[:10])


# 4) Отрывок из книги «Война и Мир»
with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
    war_and_peace_words = file.read().split()
    print("Не отсортированный отрывок из кникги 'Война и мир':",war_and_peace_words[:10])
shellsort(war_and_peace_words)
print("Отсортированный отрывок из 'Войны и Мира':", war_and_peace_words[:10])
