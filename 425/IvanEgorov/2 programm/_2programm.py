import random
import math

# Comb sort for a list of real numbers
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

# Shell sort for a list of words
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = temp
                j -= gap
            arr[j] = temp
        gap //= 2

# Quicksort function for a list of integers
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Counting Sort for a list of integers (assuming non-negative)
def counting_sort(arr, max_value):
    count = [0] * (max_value + 1)
    for item in arr:
        count[item] += 1
    
    sorted_arr = []
    for value, freq in enumerate(count):
        sorted_arr.extend([value] * freq)
    
    return sorted_arr

# Shaker Sort for a list of real numbers
def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # Bubble sort from left to right
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        # Bubble sort from right to left
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        left += 1

# List of integers from 0 to 999999
integers = list(range(100000))

# List of 10,000 random real numbers in the range [-1, 1]
real_numbers = [random.uniform(-1, 1) for _ in range(10000)]

# Points in the complex plane within a circle with radius r
birth_day = 15
birth_month = 6
max_radius = birth_day / birth_month
complex_points = []

while len(complex_points) != 42000:
    radius = random.uniform(0, max_radius)
    angle = random.uniform(0, 2 * math.pi)
    complex_points.append([radius * math.cos(angle), radius * math.sin(angle)])

# Excerpt from a book split into a list of words
words = []
with open("Book.txt", "r", encoding="utf-8") as book:
    content = book.read()
    words = content.split()
    if len(words) > 10000:
        words = words[:10000]

# Apply sorting algorithms

# Quick sort for integers
integers = quick_sort(integers)

# Counting sort for integers
counting_sorted_integers = counting_sort(integers, 99999)

# Shaker sort for real numbers
shaker_sort(real_numbers)

# Shell sort for words
shell_sort(words)

print("Quick sort for integers:", integers, "\n")
print("Counting sort for integers:", counting_sorted_integers, "\n")
print("Shaker sort for real numbers:", real_numbers, "\n")
print("Shell sort for words:", words[:10], "\n")  # Display the first 10 sorted words
