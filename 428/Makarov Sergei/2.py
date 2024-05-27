#Сортировка пузырьком
import random
import math
L = []
for x in range(1, 1000):
    ch = random.randint(1, 999999)
    L.append(ch)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort(L))

#Сортировка расческой
random_list = [random.uniform(-1, 1) for _ in range(99999)]
def comb_sort(arr):
    n = len(arr)
    gap = n
    while gap > 1 or False:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            i += 1
    return arr
print(comb_sort(random_list))

#Гномья сортировка 
import random
with open('alice_in_wonderland.txt', 'r') as f:
    words = f.read().split()

def gnome_sort(words):
    n = len(words)
    i = 0
    while i < n:
        if i > 0 and words[i] < words[i-1]:
            words[i], words[i-1] = words[i-1], words[i]
            i -= 1
        else:
            i += 1
    return words
sorted_words = gnome_sort(words)

#Поразрядная сортировка

r = 31 / 8  
points = []
for _ in range(42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    while x*2 + y*2 > r*2:
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
    points.append(complex(x, y))
def radix_sort(points):
    num_digits = int(math.log10(max(abs(p.real) for p in points))) + 1
    for digit in range(num_digits):
        counting_sort(points, digit)
    return points
def counting_sort(points, digit):
    counts = [0] * 10
    for point in points:
        index = get_digit(point, digit)
        counts[index] += 1
    for i in range(1, 10):
        counts[i] += counts[i-1]
    sorted_points = [None] * len(points)
    
    for point in reversed(points):
        index = get_digit(point, digit)
        sorted_points[counts[index] - 1] = point
        counts[index] -= 1
    for i in range(len(points)):
        points[i] = sorted_points[i]

def get_digit(point, digit):
    num_str = f"{abs(point):.0f}"
   
    if len(num_str) >= digit + 1:
        return int(num_str[-digit - 1])
    else:
        return 0
sorted_points = radix_sort(points)
print(sorted_points)
