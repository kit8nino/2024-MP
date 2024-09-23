import random
import cmath
import requests

# Список из 1 000 000 случайных целых чисел в диапазоне от 0 до 9 999 999
int_list = [random.randint(0, 9999999) for _ in range(100000)]

# 2. Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_list = [random.uniform(-1, 1) for _ in range(99999)]

# 3. 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month
birth_day = 15
birth_month = 5
r = birth_day / birth_month

complex_points = [r * cmath.rect(random.uniform(0, 1), random.uniform(0, 2*cmath.pi)) for _ in range(42000)]

# 4. Отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
response = requests.get('https://www.gutenberg.org/files/1342/1342-0.txt')
book_text = response.text

words = book_text.split()[:10000]

# Реализация функции сортировки пузырьком
def bubble_sort(arr, key=None):
    n = len(arr)
    if n <= 1:
        return arr

    while True:
        swapped = False
        for i in range(n - 1):
            if key:
                if key(arr[i]) > key(arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            else:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
        if not swapped:
            break
        n -= 1

    return arr

# Сортировка списка целых чисел
sorted_int_list = bubble_sort(int_list.copy())
#print(int_list)
#print(sorted_int_list)
print("Сортировка списка целых чисел завершена.")

# Сортировка списка случайных вещественных чисел
sorted_float_list = bubble_sort(float_list.copy())
#print(float_list)
#print(sorted_float_list)
print("Сортировка списка случайных вещественных чисел завершена.")

# Сортировка точек на комплексной плоскости по модулю
sorted_complex_points = bubble_sort(complex_points.copy(), key=abs)
#print(complex_points)
#print(sorted_complex_points)
print("Сортировка точек на комплексной плоскости завершена.")

# Сортировка списка слов из отрывка книги
sorted_words = bubble_sort(words.copy())
#print(words)
#print(sorted_words)
print("Сортировка списка слов завершена.")



# Реализация алгоритмов сортировки на Python
def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        n -= 1

    return arr

def shaker_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    left = 0
    right = n - 1
    while left < right:
        new_right = right
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                new_right = i
        right = new_right

        new_left = left
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                new_left = i
        left = new_left

    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quickinssort(arr, left=0, right=None, threshold=32):
    if right is None:
        right = len(arr) - 1

    if right - left <= threshold:
        insertion_sort(arr, left, right)
        return

    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if left < j:
        quickinssort(arr, left, j, threshold)
    if i < right:
        quickinssort(arr, i, right, threshold)

# Создание копий исходного списка
int_list_copy_for_bubble = int_list.copy()
int_list_copy_for_shaker = int_list.copy()
int_list_copy_for_selection = int_list.copy()
int_list_copy_for_quick = int_list.copy()
int_list_copy_for_quickins = int_list.copy()

# Вызов сортировки
# Bubble Sort
sorted_int_list_bubble = bubble_sort(int_list_copy_for_bubble)
print("Сортировка списка целых чисел пузырьком завершена.")

# Shaker Sort
sorted_int_list_shaker = shaker_sort(int_list_copy_for_shaker)
print("Сортировка списка целых чисел шейкерной сортировкой завершена.")

# Selection Sort
sorted_int_list_selection = selection_sort(int_list_copy_for_selection)
print("Сортировка списка целых чисел сортировкой выбором завершена.")

# Quick Sort
sorted_int_list_quick = quick_sort(int_list_copy_for_quick)
print("Сортировка списка целых чисел быстрой сортировкой завершена.")

# Quick Sort with Insertion Sort
quickinssort(int_list_copy_for_quickins)
sorted_int_list_quickins = int_list_copy_for_quickins
print("Сортировка списка целых чисел гибридной сортировкой завершена.")

