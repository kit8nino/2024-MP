# import random
#
# print(random.sample(range(1, 18), 4))

# Result: [11, 10, 2, 7]

# Modules
import numpy as np
import random
import docx


# Data
# List of integer numbers in interval (0; 999999)
list_1 = [num for num in range(999999)]
random.shuffle(list_1)

# List of float numbers in interval (-1, 1)
list_2 = list(np.arange(-1, 1, 99999))


# List of complex numbers
def get_list_3():
    def get_point():
        r = 26 / 3
        while True:
            x = random.random() * r - r
            y = random.random() * r - r
            if x ** 2 + y ** 2 < r:
                return complex(x, y)

    return [get_point() for _ in range(42000)]


list_3 = get_list_3()


# Excerpt from the book
def get_lest_4():
    document = docx.Document('Master-i-Margarita.docx')
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text

    return text.split()[:1000]


list_4 = get_lest_4()


# Buble sort (2)
def buble_sort(arr: list) -> list:
    result = arr

    for j in range(len(result)):
        swapped = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            return result


# Gnome sort (7)
def gnome_sort(arr: list) -> list:
    result = arr
    i = 0

    while i < len(result):
        if i == 0 or result[i] >= result[i - 1]:
            i += 1
        else:
            result[i], result[i - 1] = result[i - 1], result[i]
            i -= 1
    return result


# Quic sort (10)
def quick_sort(arr: list) -> list:
    result = arr
    if len(result) <= 1:
        return result
    else:
        q = random.choice(result)
        left_nums = []
        right_nums = []
        equal_nums = []
        for number in result:
            if number < q:
                left_nums.append(number)
            elif number > q:
                right_nums.append(number)
            else:
                equal_nums.append(number)
        return quick_sort(left_nums) + equal_nums + quick_sort(right_nums)


# Merge sort (11)
def merge_sort(arr: list) -> list:
    def merge(left_list, right_list):
        result = []
        left_index = right_index = 0

        left_length, right_length = len(left_list), len(right_list)

        for _ in range(left_length + right_length):
            if left_index < left_length and right_index < right_length:
                if left_list[left_index] <= right_list[right_index]:
                    result.append(left_list[left_index])
                    left_index += 1
                else:
                    result.append(right_list[right_index])
                    right_index += 1

            elif left_index == left_length:
                result.append(right_list[right_index])
                right_index += 1

            elif right_index == right_length:
                result.append(left_list[left_index])
                left_index += 1

        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(buble_sort(list_1))
print(gnome_sort(list_2))
print(quick_sort(list_3))
print(merge_sort(list_4))

