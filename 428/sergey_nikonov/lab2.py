import random 
import numpy as np  

list_int = [] 
for i in range(10000): 
    list_int.append(random.randint(0,999999)) 

list_rand_int = [] 
for i in range(9999): 
    list_rand_int.append(random.uniform(-1,1)) 

def generate_points(num_points): 
    points = [] 
    for _ in range(num_points): 
        x = np.random.uniform(-2, 2) 
        y = np.random.uniform(-2, 2) 
        if x**2 + y**2 <= 4: 
            points.append(complex(x, y)) 
    return points 

complex_list = generate_points(42000) 

with open("book.txt", "r", encoding="utf-8") as file: 
    text = file.read().split()

# Функции сортировки

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

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

bubble_sorted_int = bubble_sort(list_int.copy())
sorted_list_rand_int = bubble_sort(list_rand_int.copy())
sorted_complex_list = quicksort_complex(complex_list.copy(), 0, len(complex_list)-1)
sorted_text = bubble_sort(text.copy())

print("Начальный список целых чисел:")
print(list_int[:10])   
print("Отсортированный список целых чисел:")
print(bubble_sorted_int[:10])   
print("\n")

print("Начальный список случайных чисел:")
print(list_rand_int[:10])   
print("Отсортированный список случайных чисел:")
print(sorted_list_rand_int[:10])   
print("\n")

print("Начальный список комплексных чисел:")
print(complex_list[:10])   
print("Отсортированный список комплексных чисел:")
print(sorted_complex_list[:10])   
print("\n")

print("Начальный список слов из текста:")
print(text[:10])   
print("Отсортированный список слов из текста:")
print(sorted_text[:10])