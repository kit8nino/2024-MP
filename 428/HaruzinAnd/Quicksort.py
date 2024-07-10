import random
import cmath

def quicksort(array, key=lambda x: x):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    less = [x for x in array if key(x) < key(pivot)]
    equal = [x for x in array if key(x) == key(pivot)]
    greater = [x for x in array if key(x) > key(pivot)]
    return quicksort(less, key) + equal + quicksort(greater, key)

integers_list = list(range(1000000))
random.shuffle(integers_list) 
print("Неотсортированные целые числа:", integers_list[:10], "...")
sorted_integers = quicksort(integers_list)
print("Отсортированные целые числа:", sorted_integers[:10], "...")

floats_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Неотсортированные вещественные числа:", floats_list[:10], "...")
sorted_floats = quicksort(floats_list)
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
sorted_complex_points = quicksort(complex_points, key=abs)
print("Отсортированные комплексные числа:", sorted_complex_points[:10], "...")

file_path = 'capitan.txt'  
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
words_list = text.split()
print("Неотсортированные слова:", words_list[:10], "...")
sorted_words = quicksort(words_list)
print("Отсортированные слова:", sorted_words[:10], "...")


