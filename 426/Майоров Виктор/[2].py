from random import randint
import random
import math
#print(random.sample(range(1, 18), 4) )   --→  [1, 7, 3, 11]


# 1 список целых чисел от 0 до 999999
spisok1 = [random.randint(0, 999999) for i in range(999999)]

# 2 список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
spisok2 = [random.uniform(-1, 1) for i in range(999999)]

# 3 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса radius=20/2=10
param = 2 * math.pi / 42000
plane_of_points = []
for i in range(42000):
    r1 = 10 * math.cos(i * param)
    r2 = 10 * math.sin(i * param)
    plane_of_points.append((r1, r2))


# 4 книга
with open('elegance.txt', 'r', encoding = 'utf-8') as doc:
  book = doc.read().lower()
list_of_text = book.split()

# 1 сортировка перемешиванием
def shaker_sort(arr):

    for i in range(1, len(arr)):
        shake = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > shake):
                arr[j + 1] = arr[j]
                j = j - 1
        arr[j + 1] = shake
    return arr
#print(shaker_sort(spisok1))

# 7 гномья сортировка
def gnom(arr):
            i, size = 1, len(arr)
            while i < size:
                if arr[i - 1] <= arr[i]:
                    i += 1
                else:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    if i > 1:
                        i -= 1
            return arr
#print(gnom(spisok2))

# 3 сортировка расчесткой
def rascheska(arr):
    first = len(arr) - 1
    while first > 0:
        for i in range(0, len(arr) - first):
            if (arr[i] > arr[i + first]):
                arr[i], arr[i + first] = arr[i + first], arr[i]
        step = int(first // 1.25)
    return arr
#print(rascheska(plane_of_points))


# 11 сортировка слиянием
def merge_sort (arr):
    if len(arr) < 2:
        return arr
    result = []
    midlle = int(len(arr) / 2)
    one = merge_sort(arr[:midlle])
    two = merge_sort(arr[midlle:])
    i = 0
    j = 0
    while i < len(one) and j < len(two):
        if one[i] > two[j]:
            result.append(two[j])
            j += 1
        else:
            result.append(one[i])
            i += 1
    result += one[i:]
    result += two[j:]
    return result
#print(merge_sort(list_of_text))

while True:
    index = input("Введите номер списка для проверки сортировок (для завершения введите exit):")
    if index == "1":
        print(shaker_sort(spisok1))
    elif index == "2":
        print(gnom(spisok2))
    elif index == "3":
        print(rascheska(plane_of_points))
    elif index == "4":
        print(merge_sort(list_of_text))
    elif index == "exit":
        break
    else:
        print("Введено неверное значение!")
