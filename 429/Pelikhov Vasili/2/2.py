import numpy as np
import re

integers = []
for i in range(0, 999999+1):
    integers.append(i)

reals = []
for i in range(0, 99999+1):
    reals.append(np.random.uniform(-1, 1))

birth_day = 28
birth_month = 10
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

file = open("Le_Petit_Prince.txt") 
text = file.read()
text = re.sub(r'[^\w\s]', '', text)
words = text.split()
#print(random.sample(range(1, 18), 4)) #1st result: [17, 11, 10, 13]

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

bitonic_sort(words)
print(words)


def merge_sort(array):
    loc_array = array
    n = len(loc_array)
    if n > 1:
        mid = n//2
        left = loc_array[:mid]
        right = loc_array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                loc_array[k] = left[i]
                i+=1
            else:
                loc_array[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            loc_array[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            loc_array[k] = right[j]
            j+=1
            k+=1
    return  loc_array

array2_sorted = merge_sort(integers)
print(array2_sorted)


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        flag = abs(array[-1])
        left_part = [elem for elem in array[:-1] if abs(elem) <= flag]
        right_part = [elem for elem in array[:-1] if abs(elem) > flag]
        return quick_sort(left_part) + [flag] + quick_sort(right_part)

array3_sorted = quick_sort(complex_numbers)
print(array3_sorted)


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

array4_sorted = bucket_sort(reals)
print(array4_sorted)
