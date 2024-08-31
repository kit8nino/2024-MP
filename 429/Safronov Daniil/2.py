# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:07:51 2024

@author: Даниил
"""

import random

arr1 = list(range(1000000))
arr2 = [random.uniform(-1, 1) for _ in range(99999)]
points = [complex(random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(42000)]
with open('Text.txt', 'r') as file:
    text = file.read()
words = text.split()
words = [word.strip('.,!?;:()[]{}\'"') for word in words]
word_list = []
for word in words:
    word_list.append(word)



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


sorted_arr1 = quicksort(arr1)
print("1) ",sorted_arr1)
print("\n \n \n \n")
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result



sorted_arr2 = merge_sort(arr2)
print("2) ",sorted_arr2)
print("\n \n \n \n")
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i].real // exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i].real // exp)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr, key=lambda x: x.real)
    exp = 1
    while max_val.real // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
radix_sort(points)
for point in points:
    print(point)        

print("\n \n \n \n")
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]



selection_sort(words)
print("4) ",words)