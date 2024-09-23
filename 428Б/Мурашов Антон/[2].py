import random
import numpy as np
import math
import string



#Исходные данные 

#список целых чисел от 0 до 999999;

list_integers=[i for i in range(1000000)]
random.shuffle(list_integers)
#print("Список целых чисел:", list_integers)

#список из 99999 случайных вещественных чисел в диапазоне [-1, 1];

list_of_random_real_numbers=[round(random.uniform(-1,1),3) for x in range(100000)]
#print("Список случайных вещественных чисел:", list_of_random_real_numbers)


#42000 разных точки комплексной плоскости, 
#лежащие внутри окружности радиуса r = birth_day / birth_month 
#(можно случайных, можно равномерно распределённых), сортировать по модулю числа;

birth_day = 25 
birth_month = 10 
r=birth_day/birth_month
#print(r)
n=42000

module_of_a_complex_number=(r**(2)/2)**(0.5) #модуль комплексного числа

complex_list=[]
for i in range(42000):
    Re=np.random.uniform(-module_of_a_complex_number,module_of_a_complex_number)
    Im=np.random.uniform(-module_of_a_complex_number,module_of_a_complex_number)
    complex_list.append(complex(Re,Im))
#print("42000 разных точки комплексной плоскости",complex_list)


#отрывок из книги (любой, на свой выбор) не менее 10000 слов,
# разбитый в список по словам.

with open("2.txt",encoding='utf-8') as textfile:
    text = textfile.read().lower()
textwords = text.split()
#print("Отрывок из книги:",textwords)


#Алгоритмы сортировки

#1-13
#2-10
#3-6
#4-2

print("Bucket sort, блочная (карманная) сортировка")

def bucket_sorting(array):
    max_value = max(array)
    min_value = min(array)
    bucket_size = 5  
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for n in array:
        index = (n - min_value) // bucket_size
        buckets[index].append(n)
    res = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        res.extend(sorted_bucket)
    return res
sorted_sheet_1=bucket_sorting(list_integers)
print(sorted_sheet_1)



print("Quicksort, быстрая сортировка")

def quick_sort(array):
    
    if len(array) <= 1:
        return array
    
    elem = array[0]
    left = list(filter( lambda x: x<elem, array))
    center = [i for i in array if i == elem]
    right = list(filter(lambda x: x>elem, array))

    return quick_sort(left) + center + quick_sort(right)

sorted_sheet_2 = quick_sort(list_of_random_real_numbers)
print(sorted_sheet_2)


# 6.Tree sort, сортировка деревом
print("Tree sort, сортировка деревом")

def insert_node(root, value):
    if root is None:
        return {'value': value, 'left': None, 'right': None}
    if value.real < root['value'].real:
        root['left'] = insert_node(root['left'], value)
    else:
        root['right'] = insert_node(root['right'], value)
    return root


def traverse_tree(root, sorted_list):
    if root is None:
        return
    traverse_tree(root['left'], sorted_list)
    sorted_list.append(root['value'])
    traverse_tree(root['right'], sorted_list)


def binary_tree_sort(numbers_2):
    root = None  # звено
    for value in numbers_2:  # проходится по каждому элементу
        root = insert_node(root, value)
    sorted_list = []
    traverse_tree(root, sorted_list)
    return sorted_list

sorted_sheet_3 = binary_tree_sort(complex_list)
print(sorted_sheet_3)


#2-сортировка пузырьком
print("bubble sort, сортировка пузырьком")

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

sorted_sheet_4=bubble_sort(textwords)
print(sorted_sheet_4)
