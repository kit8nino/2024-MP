import random
import math

# список целых чисел от 0 до 999999
integers = []
for i in range(100000):
    integers.append(i)
# random.shuffle(integers)

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
with open('Арни.txt', encoding='utf-8') as book:
    for line in book:
        for i in (line.split(" ")):
            if i != '\n' and len(words) < 10000:
                words.append(str(i))


# номера выпавшие для сортировки:
# 3.comp sort, сортировка расческой
# 5.Shellsort, сортировка Шелла
# 10.Quicksort, быстрая сортировка
# 17.bitonic sort, битонная сортировка

# Функция сортировки расческой
def comb_sort(arr):
    shrink_factor = 1.3
    gap = len(arr)
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink_factor)
        swapped = False
        i = 0
        while gap + i < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

# Функция сортировки Шелла
def shell_sort(arr):
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

# Функция быстрой сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Функция битонной сортировки
def bitonic_sort(arr):
    def bitonic_merge(arr, up):
        if len(arr) <= 1:
            return arr
        else:
            bitonic_compare(arr, up)
            mid = len(arr) // 2
            return bitonic_merge(arr[:mid], up) + bitonic_merge(arr[mid:], up)

    def bitonic_compare(arr, up):
        dist = len(arr) // 2
        for i in range(dist):
            if (arr[i] > arr[i + dist]) == up:
                arr[i], arr[i + dist] = arr[i + dist], arr[i]

    def bitonic_sort_rec(arr, up):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            return bitonic_sort_rec(bitonic_merge(arr[:mid], up), up) + bitonic_sort_rec(bitonic_merge(arr[mid:], up), not up)

    return bitonic_sort_rec(arr, True)

# Сортировка расческой для списка вещественных чисел
comb_sort(real_numbers)
print("Сортировка расческой для вещественных чисел:", real_numbers, "\n")

# Сортировка Шелла для списка слов
shell_sort(words)
print("Сортировка Шелла для списка слов:", words, "\n")

# Быстрая сортировка для списка целых чисел
integers = quick_sort(integers)
print("Быстрая сортировка для списка целых чисел:", integers, "\n")

# Битонная сортировка для списка комплексных чисел
complex_points = bitonic_sort(complex_points)
print("Битонная сортировка для комплексных чисел:", complex_points)