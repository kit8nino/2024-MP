import numpy as np
import random


# numbers = random.sample(range(1, 18), 4)
# numbers = [11, 10, 7, 4]

def get_list1(n=999999):
    list1 = list(range(n + 1))
    random.shuffle(list1)
    return list1


list1 = get_list1()


def get_list2(n=99999):
    list2 = list([random.uniform(-1, 1) for x in range(n)])
    return list2


list2 = get_list2(99)


def get_list3(n=42000):
    list3 = list()
    rad = 27/4
    while len(list3) != n:
        x = random.uniform(-rad, rad)
        y = random.uniform(-rad, rad)
        if x ** 2 + y ** 2 < rad ** 2:
            number = complex(x, y)
            list3.append(number)
    return list3


list3 = get_list3()


def get_list4():
    f = open('Вий (отрывок).txt')  # Количество слов = 10604
    list4 = f.read().split()
    f.close()
    return list4


list4 = get_list4()


# # #

# Сортировка №11
def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    B = (A[0: n // 2]).copy()
    C = (A[n // 2: n]).copy()
    merge_sort(B)
    merge_sort(C)

    i = j = k = 0
    p = len(B)
    q = len(C)
    while i < p and j < q:
        if B[i] < C[j]:
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
    return A


# Сортировка №10
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        s_arr = []
        m_arr = []
        e_arr = []
        for x in arr:
            if x < q:
                s_arr.append(x)
            elif x > q:
                m_arr.append(x)
            else:
                e_arr.append(x)
        return quicksort(s_arr) + e_arr + quicksort(m_arr)


# Сортировка №7 (для комплексных чисел)
def gnome_sort(A):
    def swap(x, y):
        return y, x

    i = 0
    j = 1
    size = len(A)
    while i < size:
        if abs(A[i - 1]) < abs(A[i]):
            i = j
            j += 1
        else:
            A[i - 1], A[i] = swap(A[i - 1], A[i])
            i -= 1
            if i == 0:
                i = j
                j += 1
    return A


# Сортировка №4
def insertion_sort(A):
    for i in range(len(A)):
        j = i - 1
        key = A[i]
        while A[j] > key and j >= 0:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


# # #

# Результаты

print("11. Merge sort")
print("Исходный массив:")
print(list1)
print("После сортировки:")
print(merge_sort(list1))
print()

print("10. Quick sort")
print("Исходный массив:")
print(list2)
print("После сортировки:")
print(quicksort(list2))
print()

print("7. Gnome sort")
print("Исходный массив:")
print(list3)
print("После сортировки:")
print(gnome_sort(list3))
print()

print("4. Insertion sort")
print("Исходный массив:")
print(list4)
print("После сортировки:")
print(insertion_sort(list4))
print()
