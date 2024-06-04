# 13 - Bucket sort, блочная (карманная) сортировка;
# 7 - Gnome sort, гномья сортировка;
# 10 - Quicksort, быстрая сортировка;
# 8 - selection sort, сортировка выбором;

import random
import math


#список целых чисел от 0 до 999999;

list_integers=[i for i in range(1000000)]
random.shuffle(list_integers)

# Создание списка из 99999 случайных вещественных чисел в диапазоне [-1, 1]
numbers = [random.uniform(-1, 1) for _ in range(99999)]

#42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых);
birth_day = 4
birth_month = 6
r = birth_day/birth_month
n=10000
def picircum(r,n):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
pointsc = picircum(r,n)
random.shuffle (pointsc)
print("Точки на комлексной плоскости:", pointsc)

#отрывок из книги
with open('анекдоты.txt', 'r', encoding='utf-8') as file:
    text = file.read()


punctuation = "\'"+"\”"+'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct_text = ""
for char in text:
    if char not in punctuation:
        no_punct_text += char

words = no_punct_text.split()

#Bucket sort, блочная (карманная) сортировка;
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


print("______________________________________________________________________")
print("Gnome sort:")

def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

# Сортировка списка с помощью гномьей сортировки
sorted_numbers = gnome_sort(numbers)

print(sorted_numbers)



#быстрая сортировака quick sort
print("______________________________________________________________________")
print("Quick sort:")

def quicksort(lst):
   if len(lst) <= 1:
       return lst
   else:
       q = random.choice(lst)
       right = []
       left = []
       middle = []
       for w in lst:
           if w < q:
               left.append(w)
           elif w > q:
               right.append(w)
           else:
               middle.append(w)
       return quicksort(left) + middle + quicksort(right)




print("Отсортированный список слов:",quicksort(words))


print("______________________________________________________________________")
print("selection sort:")
#selection sort, сортировка выбором;
def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selectionsort(pointsc))


