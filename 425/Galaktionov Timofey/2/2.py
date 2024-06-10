import random
import numpy as np
import codecs

# Создание списка целых чисел от 0 до 999999
list_int = [random.randint(0, 999999) for _ in range(10000)]

# Создание списка случайных вещественных чисел в диапазоне [-1, 1]
list_rand_int = [random.uniform(-1, 1) for _ in range(9999)]

# Создание списка комплексных чисел внутри окружности радиуса r = 0.5
def create_comlex_list(radius):
    A = []
    B = []
    while len(A) < 42000:
        a = random.uniform(-radius, radius)
        b = random.uniform(-radius, radius)
        if np.sqrt(a**2 + b**2) < radius:
            A.append(a)
            B.append(b)
    Z = [complex(A[i], B[i]) for i in range(len(A))]
    return Z

# Чтение текста из файла и преобразование его в список слов
def create_string_list():
    file_path = "2.txt"
    with codecs.open(file_path, "r", "utf_8_sig") as fileObj:
        text = fileObj.read()
    text = text.replace('–', '').replace(',', '').replace('!', '').replace('?', '')
    text = text.replace('.', '').replace(':', '').replace('-', '')
    list_of_string = text.split()
    return list_of_string

complex_list = create_comlex_list(0.5)
list_string = create_string_list()

# Алгоритмы сортировки

# Сортировка выбором
def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

# Пузырьковая сортировка
def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]

# Вспомогательная функция для вычисления модуля комплексного числа
def complex_module(z):
    return np.sqrt(z.real**2 + z.imag**2)

# Сортировка слиянием
def merge_sort(A):
    n = len(A)
    if n > 1:
        mid = n // 2
        B = A[:mid]
        C = A[mid:]
        merge_sort(B)
        merge_sort(C)
        merge(B, C, A)

def merge(B, C, A):
    p = len(B)
    q = len(C)
    i = 0
    j = 0
    k = 0
    while i < p and j < q:
        if complex_module(B[i]) <= complex_module(C[j]):
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    while i < p:
        A[k] = B[i]
        i += 1
        k += 1
    while j < q:
        A[k] = C[j]
        j += 1
        k += 1

# Быстрая сортировка
def quick_sort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s - 1)
        quick_sort(A, s + 1, r)

def partition(A, l, r):
    p = len(A[l])
    i = l + 1
    j = r
    while True:
        while i <= j and len(A[j]) >= p:
            j -= 1
        while i <= j and len(A[i]) <= p:
            i += 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[l], A[j] = A[j], A[l]
    return j

# Сортировка списка целых чисел
selection_sort(list_int)

# Сортировка списка случайных вещественных чисел
bubble_sort(list_rand_int)

# Сортировка списка комплексных чисел
merge_sort(complex_list)

# Сортировка списка строк
quick_sort(list_string, 0, len(list_string) - 1)

# Вывод отсортированных списков
print("Отсортированный список целых чисел:\n", list_int)
print("\nОтсортированный список случайных вещественных чисел:\n", list_rand_int)
print("\nОтсортированный список комплексных чисел:\n", complex_list)
print("\nОтсортированный список строк:\n", list_string)
