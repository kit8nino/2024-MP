import random
import numpy as np

#1
list1 = []   
N=1000000
for i in range(N): #создание городов
    list1.append(i)
random.shuffle(list1)
print("Начальный список:\n", list1)

#Сортировка пузырьком
def bubble_sort(arr):
    for i in range(N):
        swap = False
        for j in range(0, N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        
        if swap == False:
            break

bubble_sort(list1)
print("Отсортированный список:\n",list1)

#2
list2 = []
for i in range(99999):
    list2.append(np.random.uniform(-1, 1))
N = len(list2)
print("\nНачальный список:\n", list2)

#Гномья сортировка
def gnom_sort(arr):
    i = 1
    while i != N:
        if i == 0 or arr[i] >=arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

gnom_sort(list2)
print("Отсортированный список:\n",list2)

#3
list3 = []
r =  19 /2
N = 42000
while len(list3) != N:
    x = np.random.uniform(-r, r)
    y = np.random.uniform(-r, r)
    if x**2 + y**2 <= r**2:
        z = complex(x, y)
        list3.append(z)
print("\nНачальный список:\n", list3)


#Быстрая сортировка
def quick_sort(arr): 
    if len(arr)<=1:
        return arr
    else:
        q = random.choice(arr)
        L = []
        M = []
        R = []
        for compl in arr:
            if abs(compl) < abs(q):
                L.append(compl)
            elif abs(compl) > abs(q):
                R.append(compl)
            else:
                M.append(compl)
        return quick_sort(L) + M + quick_sort(R)

        
    
res = quick_sort(list3)
print("Отсортированный список:\n",res) 

#4
fun = open('prestuplenie-i-nakazanie.txt') 
list4 = fun.read().split()
fun.close()

# Количество слов = 11485
z = 0
for i in range(len(list4)):
    z += 1
print("\nКоличество слов:", z)

print("\nНачальный список:\n", list4)


#Функции для использования отдельных сортировок
def alphabet(val):
    return ord(val[0])

def dlina_slova(val):
    return len(val)


#Сортировка слиянием
def merge_sort(arr, func):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], func)
    right = merge_sort(arr[mid:], func)
    
    return merge(left, right, func)

def merge(left, right, func):
    resultat = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if func(left[i]) < func(right[j]):
            resultat.append(left[i])
            i += 1
        else:
            resultat.append(right[j])
            j += 1
    
    resultat.extend(left[i:])
    resultat.extend(right[j:])
    
    return resultat

sort_alphabet = merge_sort(list4[:], alphabet)
sort_dlina_slova = merge_sort(list4[:], dlina_slova)
print("\nОтсортированный список по алфавиту:\n", sort_alphabet)
print("\nОтсортированный список по длине слова:\n", sort_dlina_slova)
