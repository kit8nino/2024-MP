# import random
#
# print(random.sample(range(1, 18), 4))

# Result: [9, 2, 3, 11]

import random
import math

# список целых чисел от 0 до 999999
random_numbers = [random.randint(0, 999999) for i in range(1000000)]

#список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
random_floats = [random.uniform(-1, 1) for i in range(100000)]

#42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю числа;
# др 20.01
random_points = []
radius = 20
for i in range(42000):
    angle = random.uniform(0, 2 * math.pi)
    random_radius = random.uniform(0, radius)
    x = random_radius * math.cos(angle)
    y = random_radius * math.sin(angle)
    random_points.append(complex(x, y))

#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
with open('file_for_[2].txt', 'r', encoding='utf-8') as file:
    book_contents = file.read()
word_list = book_contents.split()

#############################################################################################################
#Реализация алгоритма №2 Метод пузырьком

def bubble_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if key(arr[j]) > key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


random_numbers = bubble_sort(random_numbers)
print (random_numbers)

random_floats = bubble_sort(random_floats)
print(random_floats)

random_points = bubble_sort(random_points, key = abs)
print(random_points)

word_list = bubble_sort(word_list)
print(word_list)

#############################################################################################################

#Реализация алгоритма №3 сортировка расческой;

def comb_sort(arr, key=lambda x: x):
    gap = len(arr)
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        i = 0
        swapped = False
        while i + gap < len(arr):
            if key(arr[i]) > key(arr[i + gap]):
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

    return arr

random_numbers = comb_sort(random_numbers)
print(random_numbers)

random_floats = comb_sort(random_floats)
print(random_floats)

random_points = comb_sort(random_points, key = abs)
print(random_points)

word_list = comb_sort(word_list)
print(word_list)


#############################################################################################################
#Реализация алгоритма №9 Heapsort, пирамидальная сортировка;

def heapify(arr, n, i, key=lambda x: x):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and key(arr[i]) < key(arr[left]):
        largest = left

    if right < n and key(arr[largest]) < key(arr[right]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key=lambda x: x):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

    return arr

random_numbers = heap_sort(random_numbers)
print(random_numbers)

random_floats = heap_sort(random_floats)
print(random_floats)

random_points = heap_sort(random_points, key = abs)
print(random_points)

word_list = heap_sort(word_list)
print(word_list)

#############################################################################################################
#Реализация алгоритма №11 Merge sort, сортировка слиянием;

def merge_sort(arr, key=lambda x: x): 
    if len(arr) <= 1: 
        return arr 
     
    mid = len(arr) // 2 
    left = merge_sort(arr[:mid], key=key) 
    right = merge_sort(arr[mid:], key=key) 
 
    return merge(left, right, key=key) 
 
def merge(left, right, key=lambda x: x): 
    result = [] 
    i = j = 0 
 
    while i < len(left) and j < len(right): 
        if key(left[i]) <= key(right[j]): 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
 
    result.extend(left[i:]) 
    result.extend(right[j:]) 
    return result


random_numbers = merge_sort(random_numbers)
print(random_numbers)

random_floats = merge_sort(random_floats)
print(random_floats)

random_points = merge_sort(random_points, key = abs)
print(random_points)

word_list = merge_sort(word_list)
print(word_list)
