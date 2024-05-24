# -- coding: cp1251 --
import math
import random
import string

# Список целых чисел
integers = list(range(1000000))
random.shuffle(integers)

# Список случайных вещественных чисел
random_floats = [random.uniform(-1, 1) for i in range(99999)]

# Список комплексных чисел
radius = 14 / 11
i = 0
complex_points = []
while i <= 42000:
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    if x**2 + y**2 < radius:
        complex_points += [(x, y)]
        i += 1

# Отрывок из книги
file = open("book.txt", "r").read()
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

def comb_sort(arr):
    n = len(arr)
    gap = n
    swap = True
    k = 1.247

    while gap > 1 or swap:
        gap = max(1, int(gap / k))
        swap = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                temp = arr[i + gap]
                arr[i + gap] = arr[i]
                arr[i] = temp
                swap = True

    return arr

def gnome_sort(arr):
    i = 0
    n = len(arr)
    
    while i < n:
        if i == 0 or (arr[i - 1][0]**2 + arr[i - 1][1]**2 < arr[i][0]**2 + arr[i][1]**2):
            i += 1
        else:
            temp = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = temp
            i -= 1
            
    return arr

print(insertion_sort(book))
print(shaker_sort(random_floats))
print(comb_sort(integers))
print(gnome_sort(complex_points))
