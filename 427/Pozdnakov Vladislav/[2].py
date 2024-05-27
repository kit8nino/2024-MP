import numpy as np
import random

def get_list1(n=999999):
    list1 = list(range(n+1))
    random.shuffle(list1)
    return list1
list1 = get_list1(99)

def get_list2(n=99999):
    list2 = list([random.uniform(-1, 1) for x in range(n)])
    return list2
list2 = get_list2(99)

def get_list3(n=42000):
    list3 = list()
    rad = 30 / 6
    while len(list3) != n:
        x = random.uniform(-rad, rad)
        y = random.uniform(-rad, rad)
        if x**2 + y**2 < rad**2:
            number = complex(x, y)
            list3.append(number)
    return list3
list3 = get_list3(99)

def get_list4():
    f = open('Metro2033_2.txt', encoding= "UTF-8") # Количество слов = 11071
    list4 = f.read().split()
    f.close()
    return list4
list4 = get_list4()



# Сортировка №12
def counting_sort(list):
    min_val = min(list)
    max_val = max(list)
    count_arr = [0] * (max_val - min_val + 1)
    for num in list:
        count_arr[num - min_val] += 1
    sorted_arr = []
    for i in range(len(count_arr)):
        sorted_arr.extend([i + min_val] * count_arr[i])
    return sorted_arr

# Сортировка №8
def select_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    return list

# Сортировка №7 (для комплексных чисел)
def gnome_sort(A):
    def swap(x, y):
        return y, x
    i = 0
    j = 1
    size = len(A)
    while i < size:
        if abs(A[i-1]) < abs(A[i]):
            i = j
            j += 1
        else:
            A[i-1], A[i] = swap(A[i-1], A[i])
            i -= 1
            if i == 0:
                i = j
                j += 1
    return A

# Сортировка №1
def shaker_sort(list):
    i = 0
    while i != len(list):
        if list[i] < list[i-1]:
            temp1 = list[i]
            list[i] = list[i - 1]
            list[i - 1] = temp1
        i +=1
        j = len(list) - 1
        while j >= i:
            if list[j] < list[j-1]:
                temp2 = list[j]
                list[j] = list[j - 1]
                list[j - 1] = temp2
            j -= 1
    return list


print("12. Counting sort\nИсходный массив:\n", list1, "\n\nПосле сортировки:", counting_sort(list1), "\n\n\n\n\n")

print("8. Quick sort\nИсходный массив:\n", list2, "\n\nПосле сортировки:", select_sort(list2), "\n\n\n\n\n")

print("7. Gnome sort\nИсходный массив:\n", list3, "\n\nПосле сортировки:", gnome_sort(list3), "\n\n\n\n\n")

print("1. Shaker sort\nИсходный массив:\n", list4, "\n\nПосле сортировки:", shaker_sort(list4), "\n\n\n\n\n")
