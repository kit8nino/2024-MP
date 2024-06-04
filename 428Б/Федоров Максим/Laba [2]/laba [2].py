import random
import numpy as np


#1
L = []
for i in range(1000000):
    i = random.randint(0,999999)
    L.append(i)
   
#2
K = []
for i in range(99999):
    i = random.uniform(-1,1)
    K.append(i)
 
#3 
birth_day = 12
birth_month = 1
r = birth_day / birth_month 
kolvo_tochek = 42000
R = r * np.random.rand(kolvo_tochek)
theta = 2 * np.pi * np.random.rand(kolvo_tochek)
x = R * np.cos(theta)
y = R * np.sin(theta)
complex_points = x + 1j * y


#4
def clean_and_split_file(file_path, remove):
    def remove_chars(text, chars):
        for char in chars:
            text = text.replace(char, '')
        return text
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    cleaned_text = remove_chars(text, remove)
    words = cleaned_text.split()
    return words
remove = ['?', '!', '@', '#', '$', ',', '.', '»', '«', '–', '—', '\n', '...', '…', ':', ';', '(', ')', '"', "'", '-', '№']
file_path = "book.txt"
words = clean_and_split_file(file_path, remove)


#D = random.sample(range(1, 18), 4)
#print(D)
# [5,2,7,12]
# Выпали следующие сортировки:
# 1) Shellsort, сортировка Шелла
# 2) bubble sort, сортировка пузырьком
# 3) Gnome sort, гномья сортировка
# 4) Counting sort, сортировка подсчетом;


# Сортировка Шелла
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
    return arr

#сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Гномья Сортировка
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


# сортировка подсчетом
def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]
    return arr


#Проверка сортировок
test_L = L[:100]
test_K = K[:100]
test_complex_points = complex_points[:100]
test_words = words[:100]

counting_sort(test_L)
print(test_L)

shell_sort(test_complex_points)
print(test_complex_points)

gnome_sort(test_K)
print(test_K)

bubble_sort(test_words)
print(test_words)
