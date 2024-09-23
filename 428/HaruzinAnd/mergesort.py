import random
import cmath

def merge_sort(array, key=lambda x: x):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if key(left_half[i]) < key(right_half[j]):
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

integers_list = list(range(1000000))
random.shuffle(integers_list) 
print("Неотсортированные целые числа:", integers_list[:10], "...")
sorted_integers = merge_sort(integers_list)
print("Отсортированные целые числа:", sorted_integers[:10], "...")

floats_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Неотсортированные вещественные числа:", floats_list[:10], "...")
sorted_floats = merge_sort(floats_list)
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
sorted_complex_points = merge_sort(complex_points, key=abs)
print("Отсортированные комплексные числа:", sorted_complex_points[:10], "...")

file_path = 'capitan.txt'  
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
words_list = text.split()
print("Неотсортированные слова:", words_list[:10], "...")
sorted_words = merge_sort(words_list, key=lambda x: x.lower())
print("Отсортированные слова:", sorted_words[:10], "...")