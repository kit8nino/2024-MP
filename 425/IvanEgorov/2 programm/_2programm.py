import random
import math

# list of integers from 0 to 999999
integers = []
for i in range(100000):
    integers.append(i)
# random.shuffle(integers)

# list of 99999 random real numbers in the range [-1, 1]
real_numbers = []
for i in range(10000):
    real_numbers.append(random.uniform(-1, 1))

# 42000 different points in the complex plane, lying inside a circle with radius r = birth_day / birth_month
# (can be random or evenly distributed), sorted by the modulus of the number
birth_day = 15
birth_month = 6
max_module = birth_day / birth_month
complex_points = []
while len(complex_points) != 42000:
    radius = random.uniform(0, max_module)
    angle = random.uniform(0, 2 * math.pi)
    complex_points.append([radius * math.cos(angle),
                           radius * math.sin(angle)])

# excerpt from a book (any book of your choice) of at least 10000 words, split into a list of words
words = []
with open('Book.txt', encoding='utf-8') as book:
    for line in book:
        for word in line.split(" "):
            if word != '\n' and len(words) < 10000:
                words.append(str(word))


# sorting numbers:
# 3.comp sort, comb sort
# 5.Shellsort, shell sort
# 10.Quicksort, quick sort
# 17.bitonic sort, bitonic sort

# Comb sort function
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

# Shell sort function
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

# Quick sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Bitonic sort function
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

# Comb sort for the list of real numbers
comb_sort(real_numbers)
print("Comb sort for real numbers:", real_numbers, "\n")

# Shell sort for the list of words
shell_sort(words)
print("Shell sort for words:", words, "\n")

# Quick sort for the list of integers
integers = quick_sort(integers)
print("Quick sort for integers:", integers, "\n")

# Bitonic sort for the list of complex numbers
complex_points = bitonic_sort(complex_points)
print("Bitonic sort for complex numbers:", complex_points)

