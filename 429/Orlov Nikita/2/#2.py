import random
import numpy as np

#print(random.sample(range(1, 18), 4))
# [2, 7, 17, 8]

integ = []
for i in range(0, 999999+1):
    integ.append(i)

real = []
for i in range(0, 99999+1):
    real.append(np.random.uniform(-1, 1))

b_day = 6
b_month = 3
r = b_day / b_month
points = []
while len(points) <= 42000:
    point = complex(random.uniform(-r, r), random.uniform(-r, r))
    if abs(point) <= r:
        if point not in points:
            points.append(point)

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
words = text.split()



# Метод сортировки пузырьком (Bubble sort)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

'''
bubble_sort(integ)
print("Отсортированный массив:", integ)
'''

# Метод гномьей сортировки (Gnome sort)

def gnome_sort(arr):
    i = 1
    while i < len(arr):
        # если текущий элемент больше предыдущего, двигаемся вправо
        if arr[i-1] <= arr[i]:
            i += 1
        # если текущий элемент меньше предыдущего, меняем их местами и двигаемся влево
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            if i > 1:
                i -= 1
    return arr

'''
gnome_sort(real)
print(real)
'''

# Метод бетонной сортировки (bitonic sort)

def swap(a, b, c, d):
    if (d == 1 and abs(a[b]) > abs(a[c])) or (d == 0 and abs(a[b]) < abs(a[c])):
        a[b], a[c] = a[c], a[b]

def merge(a, b, cnt, d):
    if abs(cnt) > 1:
        k = int(cnt / 2)
        for i in range(b, b + k):
            swap(a, i, i + k, d)
        merge(a, b, k, d)
        merge(a, b + k, k, d)
 
def bitonic_sort(a, b, cnt, d):
    if abs(cnt) > 1:
        k = int(abs(cnt) / 2)
        bitonic_sort(a, b, k, 1)
        bitonic_sort(a, b + k, k, 0)
        merge(a, b, cnt, d)
'''
bitonic_sort(points, 0, len(points), 1)
print(points)
'''

# Метод сортировки выбором (Selection sort)

def selection_sort(array):
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
    return array

sort_words = selection_sort(words)
print(sort_words)

