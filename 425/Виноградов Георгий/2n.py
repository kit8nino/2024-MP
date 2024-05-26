import random
import math

# список целых чисел от 0 до 999999
integers = []
for i in range(100000):
    integers.append(i)

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
real_numbers = []
for i in range(10000):
    real_numbers.append(random.uniform(-1, 1))

# 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month
# (можно случайных, можно равномерно распределённых), сортировать по модулю числа
birth_day = 15
birth_month = 6
max_module = birth_day / birth_month
complex_points = []
while len(complex_points) != 42000:
    radius = random.uniform(0, max_module)
    angle = random.uniform(0, 2 * math.pi)
    complex_points.append([radius * math.cos(angle),
                           radius * math.sin(angle)])

# отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
words = []
with open('1984.txt', encoding='utf-8') as book:
    for line in book:
        for i in (line.split(" ")):
            if i != '\n' and len(words) < 10000:
                words.append(str(i))

# Гномья сортировка
def gnome_sort(list):
    index = 1
    i = 0
    n = len(list)
    while i < n - 1:
        if len(list[i]) <= len(list[i + 1]):
            i = index
            index = index + 1
        else:
            list[i], list[i + 1] = list[i + 1], list[i]
            i = i - 1
            if i < 0:
                i = index
                index = index + 1

gnome_sort(words)
print("Гномья сортировка для списка слов:")
print(words)

# Сортировка подсчетом для списка целых чисел
def counting_sort(list):
    list_count = [0] * len(list)
    for i in list:
        list_count[i] += 1
    list.clear()
    for i in range(len(list_count)):
        for a in range(list_count[i]):
            list.append(i)

counting_sort(integers)
print("\nСортировка подсчетом для списка целых чисел:")
print(integers)

# Пирамидальная сортировка для вещественных чисел
def heap_sort(list):
    def heapify(list, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and list[i] < list[left]:
            largest = left
        if right < n and list[largest] < list[right]:
            largest = right
        if largest != i:
            list[i], list[largest] = list[largest], list[i]
            heapify(list, n, largest)

    n = len(list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)

heap_sort(real_numbers)
print("\nПирамидальная сортировка для списка вещественных чисел:")
print(real_numbers)

# Поразрядная сортировка для комплексных чисел
def radix_sort(list):
    def counting_sort_radix(arr, exp1):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = (arr[i] / exp1)
            count[int((index) % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] / exp1)
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def radix_sort_helper(arr):
        max1 = max(arr)
        exp = 1
        while max1 / exp > 0:
            counting_sort_radix(arr, exp)
            exp *= 10

    arr = [abs(complex_num[0]) for complex_num in list]  # Вычисляем модуль комплексного числа
    radix_sort_helper(arr)
    for i in range(len(list)):
        list[i][0] = arr[i]

radix_sort(complex_points)
print("\nПоразрядная сортировка для списка комплексных чисел:")
print(complex_points)
