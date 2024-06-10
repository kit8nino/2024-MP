import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Пример использования
random_integers_list = random.sample(range(1000000), 15)
print("Исходный список целых чисел:")
print(random_integers_list)

insertion_sort(random_integers_list)

print("Отсортированный список целых чисел:")
print(random_integers_list)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Пример использования
random_float_numbers = [random.uniform(-1, 1) for _ in range(99999)]
print("Исходный список вещественных чисел:")
print(random_float_numbers[:15])

merge_sort(random_float_numbers)

print("Отсортированный список вещественных чисел:")
print(random_float_numbers[:15])
n = 42000

# Создание списков точек и текста
birth_day = 10
birth_month = 5
r = birth_day / birth_month
points = [complex(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(n)]

with open('your_book.txt', 'r', encoding='utf-8') as file:
    text = file.read().split()
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].isdigit() and right[j].isdigit():  # Проверка, что элементы можно преобразовать в число
            if abs(int(left[i])) < abs(int(right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            # Если элементы не являются числами, просто переходим к следующему элементу
            if not left[i].isdigit():
                i += 1
            if not right[j].isdigit():
                j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Пример использования функции merge
points = ['4', '-2', '5', '7', '-5', '0', '1', '-3']
mid = len(points) // 2

left = points[:mid]
right = points[mid:]

sorted_points = merge(left, right)
print(sorted_points)

# Сортировка списка слов из текста
sorted_text = merge_sort(text)

# Пример вывода отсортированных списков
print("Отсортированный список точек комплексной плоскости:")
print(sorted_points[:10])  # Вывод первых 10 отсортированных точек
print("\nОтсортированный список слов из текста:")
print(sorted_text[:10])  # Вывод первых 10 отсортированных слов из текста
