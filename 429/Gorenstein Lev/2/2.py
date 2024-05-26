import numpy as np
import re

integers = []
for i in range(0, 999999+1):
    integers.append(i)

reals = []
for i in range(0, 99999+1):
    reals.append(np.random.uniform(-1, 1))

birth_day = 22
birth_month = 5
r = birth_day / birth_month
complex_numbers = []
count = 0
while count < 42000:
    complex_number = complex(np.random.uniform(-r, r), np.random.uniform(-r, r))
    if abs(complex_number) > r:
        continue
    else: 
        complex_numbers.append(complex_number)
        count += 1

file = open("test test.txt") #file = open("Industrial Society and Its Future.txt") - очень много слов
text = file.read()
text = re.sub(r'[^\w\s]', '', text)
words = text.split()
# print(words)
#print(random.sample(range(1, 18), 4)) #1st result: [17, 6, 10, 13]

def bitonic_sort(array):
    def swap(arr, i, j, direction):
        if (arr[i] > arr[j] and direction == 1) or (arr[i] < arr[j] and direction == 0):
            arr[i], arr[j] = arr[j], arr[i]
    def bitonic_merge(arr, lowIndex, amount, direction):
        if amount > 1:
            k = amount // 2
            for i in range(lowIndex, lowIndex + k):
                    swap(arr, i, i + k, direction)
            bitonic_merge(arr, lowIndex, k, direction)
            bitonic_merge(arr, lowIndex + k, k, direction)
            
    def bitonic_sort_main(arr, lowIndex, amount, direction):
        if amount > 1:
            k = amount // 2
            bitonic_sort_main(arr, lowIndex, k, 1)
            bitonic_sort_main(arr, lowIndex + k, k, 0)
            bitonic_merge(arr, lowIndex, amount, direction)
    
    bitonic_sort_main(array, 0, len(array), 1)

""" to get the result """     
# bitonic_sort(#array name)
# print(#array name)
""" ----------------- """

class Tree:
    def __init__(self, parent):
        self.key = parent
        self.right = None
        self.left = None

def insert(root, child):
    if root is None:
        return Tree(child)
    if child < root.key:
        root.left = insert(root.left, child)
    else:
        root.right = insert(root.right, child)
    return root

def traverse(root, res):
    if root:
        traverse(root.left, res)
        res.append(root.key)
        traverse(root.right, res)

def tree_sort(array):
    if not array:
        return []
    root = None
    for key in array:
        root = insert(root, key)
    res = []
    traverse(root, res)
    return res

""" to get the result """     
# array2_sorted = tree_sort(#array name)
# print(array2_sorted)
""" ----------------- """

# "Версия" для комплексных чисел!!!!
# Чтобы работало для целых и действительных и слов: уберите abs!!!!
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        flag = abs(array[-1])
        left_part = [elem for elem in array[:-1] if abs(elem) <= flag]
        right_part = [elem for elem in array[:-1] if abs(elem) > flag]
        return quick_sort(left_part) + [flag] + quick_sort(right_part)
    
""" to get the result """     
# array3_sorted = quick_sort(#array name)
# print(array3_sorted)
""" ----------------- """

# лучше применять эту сортировку для действительных чисел от -1 до 1
# для списка слов не работает.
def bucket_sort(array):
    array2 = [(elem + 1) / 2 for elem in array]
    buckets = [[] for i in range(len(array))]
    
    for elem in array2:
        index = int(elem * len(array))
        buckets[index].append(elem)
        
    for bucket in buckets:
        quick_sort(bucket)
        
    array2_sorted = [elem for bucket in buckets for elem in bucket]
    array_sorted = [(elem * 2) - 1 for elem in array2_sorted]
    
    return array_sorted
    
""" to get the result """     
# array4_sorted = bucket_sort(#array name)
# print(array4_sorted)
""" ----------------- """