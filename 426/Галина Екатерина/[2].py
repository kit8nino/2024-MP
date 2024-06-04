### Действия
# путем использования random.sample(range(1, 18), 4) были получены следующие алгоритмы сортировки:
# Gnome sort(7), Counting sort(12), Shellsort(5), Bubble sort(2)

#1)Сортировка Gnome sort
# алгоритм сортировки, похожий на сортировку вставками, но в отличие от последней перед вставкой на нужное место происходит серия обменов.Алгоритм находит первое место, где два соседних элемента стоят в неправильном порядке, и меняет их местами. 
import random

# Генерация исходного списка целых чисел от 0 до 999999
random.seed(42)
original_list = random.sample(range(1000000), 1000)

def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

sorted_list = gnome_sort(original_list)

print("Исходный список:")
print(original_list)
print("\nОтсортированный список:")
print(sorted_list)

#2)Сортировка Counting sort
#алгоритм сортировки, в котором используется диапазон чисел сортируемого массива (списка) для подсчёта совпадающих элементов. 
import random

def counting_sort(arr):
    n = len(arr)
    max_val = 200000  # Максимальное значение после преобразования в целые числа
    count = [0] * max_val
    sorted_arr = [0] * n

    for num in arr:
        index = int((num + 1) * 100000)  # Преобразуем вещественное число в целое в диапазоне [0, 200000]
        count[index] += 1

    for i in range(1, max_val):
        count[i] += count[i - 1]

    for num in reversed(arr):
        index = int((num + 1) * 100000)
        sorted_arr[count[index] - 1] = num
        count[index] -= 1

    return sorted_arr

# Генерируем список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
input_list = [random.uniform(-1, 1) for _ in range(99999)]
sorted_list = counting_sort(input_list)
print(sorted_list)

#3)Сортировка Shellsort
#Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом, но и на определённом расстоянии друг от друга. 
import random
import math

def generate_points(n, r):
    points = []
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        point = complex(x, y)
        if abs(point) <= r:
            points.append(point)
    return points

def shellsort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and abs(arr[j - gap]) > abs(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr
#42000 разных точки комплексной плоскости, лежащие внутри окружности 
birth_day = 17
birth_month = 3
r = birth_day / birth_month

points = generate_points(42000, r)
sorted_points = shellsort(points)

for point in sorted_points:
    print(point, "Модуль:", abs(point))

#4)Сортировка Bubble sort
## алгоритм сортировки, который многократно перебирает входной список элемент за элементом, сравнивая текущий элемент с последующим, при необходимости меняя местами их значения.
# Функция для сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Считывание отрывка из книги и разбиение на слова
with open('текс.txt', 'r', encoding='utf-8') as file:
    book_excerpt = file.read().lower()  
    words = book_excerpt.split()

# Сортировка списка слов с помощью сортировки пузырьком
bubble_sort(words)

print("Первые 20 отсортированных слов:")
print(words[:20])
