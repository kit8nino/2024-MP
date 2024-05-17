#4.Реализация сортировки Heapsort (пирамидальная сортировка):

import random
import numpy as np

def heapify(arr, n, i, key=lambda x: x):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left

    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)


#сортировка для комплексных чисел
def heap_sort(arr, key=lambda x: x):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)
        
def heap_sort_complex(arr, key=lambda x: abs(x)):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

# 1) Список целых чисел от 0 до 999999
integer_list = list(range(1000000))
random.shuffle(integer_list)
print("Начальный список целых чисел:", integer_list[:10]) 
heap_sort(integer_list)
print("Отсортированный список целых чисел:", integer_list[:10])

# 2) Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Начальный список случайных вещественных чисел:",float_list[:10])
heap_sort(float_list)
print("Отсортированный список случайных вещественных чисел:", float_list[:10])

# 3) 42000 разных точек комплексной плоскости, лежащие внутри окружности радиуса r = 2
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
heap_sort_complex(complex_list)
print("Отсортированный список комплексных чисел по модулю:", complex_list[:10])

# 4) Отрывок из книги "Война и Мир"
with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
    war_and_peace_words = file.read().split()
    print("Не отсортированный отрывок из кникги 'Война и мир':",war_and_peace_words[:10])
    heap_sort(war_and_peace_words)
print("Отсортированный отрывок из 'Войны и Мира':", war_and_peace_words[:10])