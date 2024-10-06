# -- coding: cp1251 --
import math
import random
import string

# Исходные данные
integers = list(range(1000000))
random.shuffle(integers)

floats = [random.uniform(-1, 1) for i in range(99999)]

radius = 25 / 10
i = 0
complex_points = []
while i <= 42000:
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    if x**2 + y**2 < radius:
        complex_points += [(x, y)]
        i += 1
        
file = open("Dostoevskiy.txt", "r", encoding="utf-8").read()
file = file.translate(str.maketrans('', '', string.punctuation))
book = file.split()

# Сортировки
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and len(arr[j - 1]) > len(arr[j]):
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

def shaker_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False
        left += 1

        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swapped = True

        if not swapped:
            break

        right -= 1

        for i in range(right, left - 1, -1):
            if arr[i] < arr[i - 1]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                swapped = True

    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        key = arr[0]
        arr_left = []
        arr_right = []

        for i in range(1, len(arr)):
            if arr[i] < key or arr[i] == key:
                arr_left.append(arr[i])
            else:
                arr_right.append(arr[i])

        return quick_sort(arr_left) + [key] + quick_sort(arr_right)

def selection_sort(arr):
    n = len(arr)
    while n > 2:
        max = 0
        i_max = 0
        for i in range(n):
            if (arr[i - 1][0]**2 + arr[i - 1][1]**2 < arr[i][0]**2 + arr[i][1]**2):
                max = arr[i]
                i_max = i
        arr[i_max], arr[n-1] = arr[n-1], arr[i_max]
        n -= 1
    return arr

# Задания
print(insertion_sort(book))
print(shaker_sort(floats))
print(quick_sort(integers))
print(selection_sort(complex_points))