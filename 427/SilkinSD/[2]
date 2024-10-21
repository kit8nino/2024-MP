import numpy as np
import random

# import random
# print(random.sample(range(1, 18), 4))
# Result: [7, 10, 2, 8]

list_1 = [num for num in range(999)]
random.shuffle(list_1)

list_2 = list(np.arange(-1, 1, 999))

def list3():
    def get_point():
        r = 26 / 3
        while True:
            x = random.random() * r - r
            y = random.random() * r - r
            if x ** 2 + y ** 2 < r:
                point = complex(x, y)
                return (point.real ** 2 + point.imag ** 2) ** 0.5
    return [get_point() for _ in range(42000)]
list_3 = list3()

def get_list_4():
    text =(" Рассказ у нас пойдет в особенности о хоббитах, и любознательный читатель многое узнает об их нравах и кое-что из их истории.")
    return text.split()[:71910]

list_4 = get_list_4()


#1.1
def shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr

#1.2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#1.3
def comp_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            sorted = True
            gap = 1
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
    return arr

#1.4
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#1.5
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

#1.6
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = tree_insert(root.left, key)
    else:
        root.right = tree_insert(root.right, key)
    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.key)
        in_order_traversal(root.right, result)

def tree_sort(arr):
    root = None
    for key in arr:
        root = tree_insert(root, key)
    result = []
    in_order_traversal(root, result)
    return result
#1.7
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr

#1.8
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
#1.10
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



print(quick_sort(list_3))
print(selection_sort(list_1))
print(gnome_sort(list_4))
print(bubble_sort(list_1))
