#printrandom.sample(range(1, 18), 4) 
#[11, 2, 5, 13]

#2.bubble sort, сортировка пузырьком;
#5.Shellsort, сортировка Шелла;
#11.Merge sort, сортировка слиянием;
#13.Bucket sort, блочная (карманная) сортировка;

import random
import cmath
import re 



def generate_and_shuffle_list(size):
    list_of_integer = list(range(size))
    random.shuffle(list_of_integer)
    return list_of_integer

list_of_integer = generate_and_shuffle_list(1000000)


list_of_random_real_numbers = [random.uniform(-1, 1) for _ in range(99999)]

def the_radius_of_the_circle(birth_day, birth_month):
    radius = birth_day / birth_month
    return radius

def generating_complex_numbers (the_radius_of_the_circle):
    radius = the_radius_of_the_circle

    points = []
    while len(points) < 42000:
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if abs(cmath.rect(1, 0) * cmath.rect(x, y)) <= radius:
            points.append(x + y * 1j)

    return points

points_of_the_complex_plane = generating_complex_numbers(the_radius_of_the_circle(24, 11))

def read_file(filename):
    with open(filename, "r") as file:
        text = file.read()

    return text

def split_into_words(text):
    words = re.findall(r'\w+', text.lower())

    return words

list_of_words = split_into_words(read_file("harry_potter.txt"))

def bubble_sort(list_of_sorting):
    size = len(list_of_sorting)

    for i in range(size - 1):
        swapped = False
        for j in range(0, size - i - 1):
            if abs(list_of_sorting[j]) > abs(list_of_sorting[j + 1]):
                swap(list_of_sorting, j, j + 1)
                swapped = True
        if not swapped:
            break


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]



def shell_sort(list_of_sorting):
    size = len(list_of_sorting)
    gap = size // 2
    while gap > 0:
        for i in range(size - gap):
            j = i
            while j >= 0 and list_of_sorting[j] > list_of_sorting[j + gap]:
                swap(list_of_sorting, j, j + gap)
                j -= 1
        gap //= 2



def merge_sort(list_of_sorting):
    if len(list_of_sorting) > 1:
        middle = len(list_of_sorting) // 2
        left_part_of_list = list_of_sorting[:middle]
        right_part_of_list = list_of_sorting[middle:]
        merge_sort(left_part_of_list)
        merge_sort(right_part_of_list)
        merge(left_part_of_list, right_part_of_list, list_of_sorting)
    return list_of_sorting

def merge(left_part_of_list, right_part_of_list, merged_list):
    left_index, right_index, current_index = 0, 0, 0

    while left_index < len(left_part_of_list) and right_index < len(right_part_of_list):
        if left_part_of_list[left_index] <= right_part_of_list[right_index]:
            merged_list[current_index] = left_part_of_list[left_index]
            left_index += 1
        else:
            merged_list[current_index] = right_part_of_list[right_index]
            right_index += 1
        current_index += 1

    while left_index < len(left_part_of_list):
        merged_list[current_index] = left_part_of_list[left_index]
        left_index += 1
        current_index += 1

    while right_index < len(right_part_of_list):
        merged_list[current_index] = right_part_of_list[right_index]
        right_index += 1
        current_index += 1



def bucket_sort(list_of_sorting, bucket_size=10):
    min_value = min(list_of_sorting)
    max_value = max(list_of_sorting)

    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]  

    for num in list_of_sorting:
        index = int((num - min_value) // bucket_size) 
        buckets[index].append(num)
    # прочитала, что данные внутри корманов можно отсортировать любой из сортировок, поэтому выбрала ту, которую уже реализовала
    for bucket in buckets:
       shell_sort(bucket)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(bucket)

    return sorted_list


# из-за большого количесва элементов в списках код работает долго, но работает!)
#чтобы не терять время, я сделала срез

bubble_sort(points_of_the_complex_plane[:20])
print('Отсортированный список комплексных чисел :',points_of_the_complex_plane)

shell_sort(list_of_random_real_numbers[:20])
print('Отсортированный список вещественных чисел :',list_of_random_real_numbers)

words_of_sorted=merge_sort(list_of_words[:20])
print('Отсортированный список слов',words_of_sorted)

integer_of_sorted = bucket_sort(list_of_integer[:20])
print('Отсортированный список целых чисел', integer_of_sorted)