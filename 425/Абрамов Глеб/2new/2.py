import random
import cmath
import re 

def generate_and_shuffle_list(size):
    integer_list = list(range(size))
    random.shuffle(integer_list)
    return integer_list

integer_list = generate_and_shuffle_list(1000000)


real_numbers_list = [random.uniform(-1, 1) for _ in range(99999)]

def calculate_radius(birth_day, birth_month):
    radius = birth_day / birth_month
    return radius

def generate_complex_numbers(radius):
    points = []
    while len(points) < 42000:
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if abs(cmath.rect(1, 0) * cmath.rect(x, y)) <= radius:
            points.append(x + y * 1j)

    return points

radius = calculate_radius(24, 11)
complex_points = generate_complex_numbers(radius)

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    return text

def split_into_words(text):
    words = re.findall(r'\w+', text.lower())

    return words

word_list = split_into_words(read_file("отрывок из книги.txt"))

def bubble_sort(sorting_list):
    size = len(sorting_list)

    for i in range(size - 1):
        swapped = False
        for j in range(0, size - i - 1):
            if abs(sorting_list[j]) > abs(sorting_list[j + 1]):
                swap(sorting_list, j, j + 1)
                swapped = True
        if not swapped:
            break

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]



def shell_sort(sorting_list):
    size = len(sorting_list)
    gap = size // 2
    while gap > 0:
        for i in range(size - gap):
            j = i
            while j >= 0 and sorting_list[j] > sorting_list[j + gap]:
                swap(sorting_list, j, j + gap)
                j -= 1
        gap //= 2

def merge_sort(sorting_list):
    if len(sorting_list) > 1:
        middle = len(sorting_list) // 2
        left_list = sorting_list[:middle]
        right_list = sorting_list[middle:]
        merge_sort(left_list)
        merge_sort(right_list)
        merge(left_list, right_list, sorting_list)
    return sorting_list

def merge(left_list, right_list, merged_list):
    left_index, right_index, current_index = 0, 0, 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            merged_list[current_index] = left_list[left_index]
            left_index += 1
        else:
            merged_list[current_index] = right_list[right_index]
            right_index += 1
        current_index += 1

    while left_index < len(left_list):
        merged_list[current_index] = left_list[left_index]
        left_index += 1
        current_index += 1

    while right_index < len(right_list):
        merged_list[current_index] = right_list[right_index]
        right_index += 1
        current_index += 1

def bucket_sort(sorting_list, bucket_size=10):
    min_value = min(sorting_list)
    max_value = max(sorting_list)

    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]  

    for num in sorting_list:
        index = int((num - min_value) // bucket_size) 
        buckets[index].append(num)
    for bucket in buckets:
       shell_sort(bucket)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(bucket)

    return sorted_list


bubble_sort(complex_points[:20])
print('Отсортированный список комплексных чисел:', complex_points[:20])

shell_sort(real_numbers_list[:20])
print('Отсортированный список вещественных чисел :', real_numbers_list[:20])

sorted_words = merge_sort(word_list[:20])
print('Отсортированный список слов:', sorted_words[:20])

sorted_integer_list = bucket_sort(integer_list[:20])
print('Отсортированный список целых чисел:', sorted_integer_list[:20])
