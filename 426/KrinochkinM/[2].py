# import random
#
# print(random.sample(range(1, 18), 4))

# Result: [9, 2, 3, 11]

import random
import math

# Функция для генерации начальных данных
def generate_data():
    # список целых чисел от 0 до 999999
    random_numbers = [random.randint(0, 999999) for i in range(1000000)]

    # список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
    random_floats = [random.uniform(-1, 1) for i in range(100000)]

    # 42000 разных точек комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month
    #др 20.01
    random_points = []
    radius = 20
    for i in range(42000):
        angle = random.uniform(0, 2 * math.pi)
        random_radius = random.uniform(0, radius)
        x = random_radius * math.cos(angle)
        y = random_radius * math.sin(angle)
        random_points.append(complex(x, y))

    # отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
    with open('file_for_[2].txt', 'r', encoding='utf-8') as file:
        book_contents = file.read()
    word_list = book_contents.split()

    return random_numbers, random_floats, random_points, word_list

#############################################################################################################

# Алгоритм сортировки пузырьком
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

#############################################################################################################

# Алгоритм сортировки расческой
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

#############################################################################################################

# Алгоритм пирамидальной сортировки
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

#############################################################################################################

# Алгоритм сортировки слиянием
def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)

    return merge(left_half, right_half, key)

def merge(left, right, key=lambda x: x):
    result = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if key(left[left_idx]) <= key(right[right_idx]):
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

#############################################################################################################

# Функция для выбора алгоритма сортировки
def choose_sorting_algorithm():
    while True:
        print("Выберите алгоритм сортировки:")
        print("1. Сортировка пузырьком \n2. Сортировка расческой \n3. Пирамидальная сортировка \n4. Сортировка слиянием")
        choice = input("Введите номер алгоритма (1-4): ")

        if choice == "1":
            return bubble_sort
        elif choice == "2":
            return comb_sort
        elif choice == "3":
            return heap_sort
        elif choice == "4":
            return merge_sort
        else:
            print("Неверный выбор. Попробуйте снова.")

# Функция для выбора данных для сортировки
def choose_data_to_sort():
    while True:
        print("Выберите данные для сортировки:")
        print("1. Список целых чисел \n2. Список вещественных чисел \n3. Список комплексных чисел \n4. Список слов из книги ")

        choice = input("Введите номер данных (1-4): ")

        if choice == "1":
            return random_numbers
        elif choice == "2":
            return random_floats
        elif choice == "3":
            return random_points
        elif choice == "4":
            return word_list
        else:
            print("Неверный выбор. Попробуйте снова.")

# Генерация начальных данных
random_numbers, random_floats, random_points, word_list = generate_data()

# Выбор алгоритма сортировки
sorting_algorithm = choose_sorting_algorithm()

# Выбор данных для сортировки
data_to_sort = choose_data_to_sort()

# Сортировка выбранных данных
if data_to_sort == random_points:
    sorted_data = sorting_algorithm(data_to_sort, key = abs)
else:
    sorted_data = sorting_algorithm(data_to_sort)
    
# Вывод отсортированных данных
print("Отсортированные данные:")
print(sorted_data)
