import random 
import numpy as np
import math

def gnomeSort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i-1] <= arr[i]:
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr

def bubbleSort(arr):
    for i in range(len(arr)-1):
        done = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
                done = False
        if done:
            break

#Для значений по модулю (костыли)
def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and abs(arr[j-gap]) > abs(temp):
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def shakerSort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        swapped = False
        for i in range (start, end):
            if (arr[i] > arr[i+1]) :
                arr[i], arr[i+1]= arr[i+1], arr[i]
                swapped=True
        if (swapped==False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1,-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start = start+1


#1.Cписок целых чисел от 0 до 999999
intList = []
for i in range(1000):
    intList.append(random.randint(0,999999))
print(f"Cписок целых чисел: {intList[:50]}\n")
gnomeSort(intList)
print(f"Отсортированный список целых чисел: {intList[:50]}\n")

#2.Список случайных вещественных чисел в диапазоне [-1, 1]
floatList = [random.uniform(-1, 1) for _ in range(1000)]
print(f"Список вещественных чисел: {floatList[:50]}\n")
bubbleSort(floatList)
print(f"Отсортированный список вещественных чисел: {floatList[:50]}\n")

#3. Точки комплексной плоскости
birthDay = 13
birthMonth = 6
r = birthDay / birthMonth

pointList = [complex(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(1000)]
print(f"Cписок точек: {pointList[:50]}\n")
shellSort(pointList)
print(f"Отсортированный список точек: {pointList[:50]}\n")

#4. Отрывок из книги
with open("underTheDome.txt", "r", encoding='utf-8') as file:
    bookFragWords = file.read().split()
print(f"Список слов из отрывка: {bookFragWords[:50]}\n")
shakerSort(bookFragWords)
print(f"Отсортированный список слов из отрывка: {bookFragWords[:50]}\n")
