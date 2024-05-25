import random
import numpy as np
import codecs
import re

#print(random.sample(range(1, 18), 4)) #4, 1, 10, 9

#исходные данные
a=random.sample(range(0, 999999), 999999)

b=[]
for j in range(0,99999):
    b.append(random.uniform(-1,1))

birth_day = 18
birth_month = 7
r=birth_day/birth_month
compl=[]

for i in range(42000):
    compl += [random.uniform(0, r) * np.exp(1.j * random.uniform(0, 2 * np.pi))]

file = codecs.open("Мертвые Души.txt", "r", "utf_8_sig" )
text = str(file.read()).split()

# 4 сортировка вставкой (долгая)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


insertion_sort(a)
print("1) ", a, "\n")


# 1 сортировка перемешиванием (долгая)
def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1
    while (swapped == True):
        swapped = False
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if (not(swapped)):
            break
        swapped = False
        end_index = end_index - 1
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start_index = start_index + 1


shaker_sort(b)
print("2) ", b, "\n")


# 10 быстрая сортировка
def quicksort(points):
    if len(points) <= 1:
        return points
    pivot = points[0]
    less = []
    equal = []
    greater = []
    for point in points:
        if abs(point) < abs(pivot):
            less.append(point)
        elif abs(point) == abs(pivot):
            equal.append(point)
        else:
            greater.append(point)
    return quicksort(less) + equal + quicksort(greater)

sorted_points = quicksort(compl)
print("3) ", sorted_points, "\n")


# 9 пирамидальная сортировка
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

heapSort(text)
print("4) ", text)