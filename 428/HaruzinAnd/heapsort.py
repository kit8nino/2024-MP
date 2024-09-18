import random
import cmath

def heapify(array, n, i, key=lambda x: x):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and key(array[l]) > key(array[largest]):
        largest = l

    if r < n and key(array[r]) > key(array[largest]):
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest, key)

def heap_sort(array, key=lambda x: x):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, key)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0, key)

    return array

integers_list = list(range(1000000))
random.shuffle(integers_list) 
print("Неотсортированные целые числа:", integers_list[:10], "...")
sorted_integers = heap_sort(integers_list)
print("Отсортированные целые числа:", sorted_integers[:10], "...")

floats_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Неотсортированные вещественные числа:", floats_list[:10], "...")
sorted_floats = heap_sort(floats_list)
print("Отсортированные вещественные числа:", sorted_floats[:10], "...")

birth_day = 27  
birth_month = 1  
r = birth_day / birth_month
complex_points = []
for _ in range(42000):
    angle = random.uniform(0, 2 * cmath.pi)
    radius = random.uniform(0, r)
    complex_points.append(cmath.rect(radius, angle))
print("Неотсортированные комплексные числа:", complex_points[:10], "...")
sorted_complex_points = heap_sort(complex_points, key=abs)
print("Отсортированные комплексные числа:", sorted_complex_points[:10], "...")

file_path = 'capitan.txt'  
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
words_list = text.split()
print("Неотсортированные слова:", words_list[:10], "...")
sorted_words = heap_sort(words_list)
print("Отсортированные слова:", sorted_words[:10], "...")
