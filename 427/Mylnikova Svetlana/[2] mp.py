import random
import math

# ИСХОДНЫЕ ДАННЫЕ

#print (random. sample(range (1, 18), 4) )
# [2,1,3,10] - получившийся выбор сортировок

# список целых чисел от 0 до 999999
int_ciferki = [random. randint(0,
999999) for i in range(1000000) ]

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_ciferki = [random. uniform(-1, 1) for i in range (100000) ]

# 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса г = birth_day / birth_month

complex_points = []
birth_day = 10
birth_month = 7
r = birth_day / birth_month
for i in range (42000) :
    angle = random. uniform(0, 2 * math.pi)
    random_radius = random.uniform(0, r)
    x = random_radius * math. cos(angle)
    y = random_radius * math.sin(angle)
    complex_points.append(complex(x, y) )

# отрывок из книги "Долина страха" из 13068 слов, разбитый в список по словам
with open ("The Valley of Fear.txt", 'r', encoding = "utf-8") as f:
    text = f.read()
book = text.split()


# ДЕЙСТВИЯ

# пункт 1. Сортировка N°2 - сортировка пузырьком

def bubble_sort (lst, key=lambda x: x) :
    n = len(lst)
    for i in range(n) :
        swapped = False
        for j in range(0, n-i-1):
            if key(lst[j]) > key(lst[j+1]) :
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

print("1.1. целые числа до сортировки bubble sort: ", int_ciferki, '\n')
int_ciferki = bubble_sort(int_ciferki)
print ("1.2. целые числа после сортировки bubble sort: ", int_ciferki, '\n')

# пункт 2. Сортировка N°1 - сортировка перемешиванием
def shaker_sort(lst):
    n = len(lst)
    left = 0
    right = n - 1
    while left < right:
        for i in range(left, right):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        right -= 1
        for i in range(right, left, -1):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
        left += 1 
    return lst

print("2.1. вещественные числа до сортировки shaker sort: ", float_ciferki, '\n')
float_ciferki = shaker_sort (float_ciferki)
print("2.2. вещественные числа после сортировки shaker sort:", float_ciferki, '\n')

# пункт 3. Сортировка N°3 - сортировка расческой
def comp_sort(lst):
    gap = len(lst)
    while gap > 1:
        gap = gap // 2
        for i in range(0, len(lst) - gap):
            if abs(complex(lst[i])) > abs(complex(lst[i + gap])) :
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
    return lst

print("3.1. точки комплексной плоскости до сортировки comp sort: ", complex_points, '\n')
complex_points = comp_sort(complex_points)
print("3.2. точки комплексной плоскости после сортировки comp sort: ", complex_points, '\n') 

# пункт 4. Сортировка N°10 - быстрая сортировка
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print("4.1. отрывок из книги до сортировки quicksort: ", book, '\n')
book = quicksort(book)
print("4.2. отрывок из книги после сортировки quicksort: ", book, '\n')