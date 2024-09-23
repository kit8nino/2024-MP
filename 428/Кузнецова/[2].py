import numpy as np
import random
import re
'''
a = random.sample(range(1, 18), 4)
print(a)
11 9 2 14
'''

lst1 = []
for i in range(1000000):
    lst1.append(i)

def merge_sort(arr):
    if len(arr) > 1:
        # Разбиваем список на две половины
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        # Рекурсивно сортируем каждую половину
        merge_sort(left_half)
        merge_sort(right_half)
        # Объединяем отсортированные половины
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sort(lst1)
print("otsortirovannii spisok lst1 metodom sliyaniya:")
print(lst1)

    
lst2 = []
for i in range(100000):
    lst2.append(random.uniform(-1, 1))

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
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

sorted_lst2=heapSort(lst2)
print("otsortirovannii spisok lst2 piramidalnim metodom:")
print(sorted_lst2)

r = 5/5 #eto pravda:/
angles = np.linspace(0, 2*np.pi, 42000, endpoint=False)
lst3 = [np.cos(angle) + np.sin(angle)*1j for angle in angles]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        # Флаг, указывающий, были ли произведены обмены на этой итерации
        swapped = False

        for j in range(0, n - i - 1):
            # Сравниваем два соседних элемента
            if arr[j] > arr[j + 1]:
                # Если первый элемент больше второго, меняем их местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Устанавливаем флаг, что был произведен обмен
                swapped = True

        # Если на этой итерации не было произведено ни одного обмена, то список уже отсортирован
        if not swapped:
            break

    return arr

sorted_lst3 = bubbleSort(lst3)
print("otsortirovannii spisok lst3 metodom puzirka:")
print(sorted_lst3)

lst4 = []
f = open("Master_i_Margarita.txt")
for line in f.readlines():
    line = re.sub("[^А-я]"," ", line)
    for word in line.split():
        lst4.append(word)

def radixSort(words):
    # определяем максимальную длину слова в списке
    max_length = len(max(words, key=len))
    # заполняем слова пробелами до максимальной длины
    for i in range(len(words)):
        words[i] = words[i].ljust(max_length)
    # сортируем слова посимвольно, начиная с конца
    for i in range(max_length-1, -1, -1):
        words = sorted(words, key=lambda x: x[i])
    # удаляем пробелы из отсортированных слов
    for i in range(len(words)):
        words[i] = words[i].strip()
    return words

sorted_lst4 = radixSort(lst4)
print("otsortirovannii spisok lst4 porazryadnim metodom:")
print(sorted_lst4)
























      