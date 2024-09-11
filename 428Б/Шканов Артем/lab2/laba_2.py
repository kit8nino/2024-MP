import random

#sample = random.sample(range(1, 18), 4)
#результат [2, 17, 9, 7]

#1. Bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

random_list = random.sample(range(1000000), 100000)

sorted_list = bubble_sort(random_list)

print("Отсортированный список:")
print(sorted_list)

#2. Bitonic sort

def compare(x, y, direction):
    if (x < y and direction == 1) or (x > y and direction == 0):
        return True
    else:
        return False

def bitonic_merge(arr, start, length, direction):
    if length > 1:
        k = length // 2
        for i in range(start, start + k):
            if compare(arr[i], arr[i + k], direction):
                arr[i], arr[i + k] = arr[i + k], arr[i]
        bitonic_merge(arr, start, k, direction)
        bitonic_merge(arr, start + k, k, direction)

def bitonic_sort(arr, start, length, direction):
    if length > 1:
        k = length // 2
        bitonic_sort(arr, start, k, 1)
        bitonic_sort(arr, start + k, k, 0)
        bitonic_merge(arr, start, length, direction)

# Генерируем список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
random_list = [random.uniform(-1, 1) for _ in range(99999)]

bitonic_sort(random_list, 0, len(random_list), 1)

print("Отсортированный список:")
print(random_list)

#3. Heapsort

birth_day = 10
birth_month = 10
r = birth_day / birth_month

points = [random.uniform(-r, r)+random.uniform(-r, r)*1j for _ in range(42000)]

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and abs(arr[i]) < abs(arr[l]):
        largest = l

    if r < n and abs(arr[largest]) < abs(arr[r]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

heap_sort(points)

print(points)

#4. Gnome sort

def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr

# Чтение содержимого файла "book.txt"
with open("book.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Разбиение текста на список слов
words = text.split()

# Сортировка списка слов с помощью Gnome sort
sorted_words = gnome_sort(words)
print(sorted_words)
