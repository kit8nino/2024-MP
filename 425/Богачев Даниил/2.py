import random
import cmath
import re

def create_and_shuffle_list(size):
    num_list = list(range(size))
    random.shuffle(num_list)
    return num_list

nums = create_and_shuffle_list(1000000)

real_nums = [random.uniform(-1, 1) for _ in range(99999)]

def compute_radius(day, month):
    return day / month

def generate_complex_points(radius):
    points = []
    while len(points) < 42000:
        real_part = random.uniform(-radius, radius)
        imag_part = random.uniform(-radius, radius)
        if abs(real_part + imag_part * 1j) <= radius:
            points.append(real_part + imag_part * 1j)
    return points

rad = compute_radius(24, 11)
complex_pts = generate_complex_points(rad)

def read_file_content(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def extract_words(text):
    return re.findall(r'\w+', text.lower())

words_from_file = extract_words(read_file_content("отрывок из книги.txt"))

def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[len(arr) // 2])
    left = [x for x in arr if key(x) < pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bucket_sort(arr, bucket_size=10):
    if len(arr) == 0:
        return arr
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]
    for num in arr:
        buckets[(num - min_val) // bucket_size].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(selection_sort(bucket))
    return sorted_arr

sorted_complex_pts = quick_sort(complex_pts, key=abs)
print('Отсортированный список комплексных чисел:', sorted_complex_pts[:20])

sorted_real_nums = quick_sort(real_nums)
print('Отсортированный список вещественных чисел:', sorted_real_nums[:20])

sorted_word_list = selection_sort(words_from_file)
print('Отсортированный список слов:', sorted_word_list[:20])

sorted_num_list = bucket_sort(nums)
print('Отсортированный список целых чисел:', sorted_num_list[:20])
