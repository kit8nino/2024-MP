import random

random.sample(range(1, 18), 4) # вернет список из 4 случайных значений в заданном диапазоне
print(random.sample(range(1, 18), 4))

#мне выпало [7, 2, 10, 5]
#Gnome sort, гномья сортировка
#bubble sort, сортировка пузырьком
#Quicksort, быстрая сортировка
#Shellsort, сортировка Шелла

# 1) список целых чисел от 0 до 999999 с гномьей сортировкой:
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

# Список целых чисел
list1 = list(range(1000000))

# Применение гномьей сортировки
sorted_list1 = gnome_sort(list1.copy())
print("Список отсортированный с помощью Гномьей сортировки",sorted_list1[:100])# Печать первых 100 элементов

#2) список из 99999 случайных вещественных чисел в диапазоне [-1,1] с сортировкой пузырьком:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Список случайных вещественных чисел
list2 = [random.uniform(-1, 1) for _ in range(99999)]

# Применение сортировки пузырьком
sorted_list2 = bubble_sort(list2.copy())
print("Список отсортированный с помощью сортировки пузырьком",sorted_list2[:100])# Печать первых 100 элементов
#долго считает (~ минут 10, может чуть поменьше)

# 3) 42000 точек комплексной плоскости внутри окружности, отсортированные по модулю числа с использованием быстрой сортировки:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    opora = arr[len(arr) // 2]
    left = [x for x in arr if abs(x) < abs(opora)]
    middle = [x for x in arr if abs(x) == abs(opora)]
    right = [x for x in arr if abs(x) > abs(opora)]
    return quicksort(left) + middle + quicksort(right)

# Генерация точек на комплексной плоскости
radius = 24 / 8
list3 = []
while len(list3) < 42000:
    real = random.uniform(-radius, radius)
    imag = random.uniform(-radius, radius)
    if real**2 + imag**2 <= radius**2:
        list3.append(complex(real, imag))

# Применение быстрой сортировки
sorted_list3 = quicksort(list3.copy())
print("Список отсортированный с помощью быстрой сортировки", sorted_list3[:100])  # Печать первых 100 элементов

# 4) Отрывок книги, разбитый в список по словам, с сортировкой Шелла:
def Shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Чтение текста из файла
with open('text1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Разделение текста на слова
list4 = text.split()

# Применение сортировки Шелла
sorted_list4 = Shell_sort(list4.copy())
print("Список отсортированный с помощью сортировки Шелла",sorted_list4[:100])  # Печать первых 100 слов