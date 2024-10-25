# -*- coding: utf-8 -*-
"""
Created on Mon May 27 06:23:54 2024

@author: vs890
"""

import random
import math
import re
#список целых чисел от 0 до 999999
integers = [random.randint(0, 999999) for _ in range(1000000)]
#список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
real_numbers = [random.uniform(-1, 1) for _ in range(99999)]
# 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = 9 / 3
points = []
while len(points) < 42000:
    x = random.uniform(-3, 3)
    y = random.uniform(-3, 3)
    if math.sqrt(x**2 + y**2) <= 3:
        points.append(complex(x, y))
#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
with open('text.txt', 'r') as file:
    text = file.read()
words_list = re.findall(r'\b\w+\b', text.lower())

#4 insertion sort, сортировка вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
            
        arr[position] = current_value

insertion_sort(integers)
print("Отсортированный список целых чисел: ", integers)

#1 shaker sort, сортировка перемешиванием
def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
shaker_sort(real_numbers)
print("Отсортированный список вещественных чисел: ", real_numbers)

#15 least significant digit
def lsd_sort(arr):
    digits = 10

    for d in range(digits):
        arr = sorted(arr, key=lambda x: int(x.real * 10**d) % 10)

    return arr

points_sorted = lsd_sort(points)
print("Отсортированный список комплексных чисел: ", points_sorted)

#3 comp sort, сортировка расческой
def comb_sort(words):
    gap = len(words)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(words):
            if words[i] > words[i + gap]:
                words[i], words[i + gap] = words[i + gap], words[i]
                sorted = False
            i += 1

    return words
sorted_words = comb_sort(words_list)
print("Отсортированный список слов: ", sorted_words)