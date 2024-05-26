# 1.Реализация алогритма comb sort(сортировка расчёской):
    
import random
import numpy as np

#
def comb_sort(A):
    step = len(A) - 1
    while step > 0:
        for i in range(0, len(A)-step):
            if (A[i] > A[i+step]):
                A[i], A[i+step] = A[i+step], A[i]
        step = int(step//1.25)
    return A

#сортировка для комплексных чисел
def comb_sort_complex(A):          
    step = len(A) - 1
    while step > 0:
        for i in range(0, len(A)-step):
            if (abs(A[i]) > abs(A[i+step])):
                A[i], A[i+step] = A[i+step], A[i]
        step = int(step//1.25)
    return A


# 1) Список целых чисел от 0 до 999999
integer_list = list(range(1000000))
random.shuffle(integer_list)  
print("Начальный список целых чисел:", integer_list[:10]) 
sorted_integer_list = comb_sort(integer_list)
print("Отсортированный список целых чисел:", sorted_integer_list[:10])


# 2) Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
import random
float_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Начальный список случайных вещественных чисел:",float_list[:10])
sorted_float_list = comb_sort(float_list)
print("Отсортированный список случайных вещественных чисел:", sorted_float_list[:10])


# 3) 42000 разных точек комплексной плоскости, лежащие внутри окружности радиуса r = 2 (r=24/12)

#Функция для генерации комплексных чисел
def generate_points(num_points):
    points = []
    for _ in range(num_points):
        # Генерируем случайные координаты в диапазоне [-2, 2) для x и y
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        # Проверяем, лежит ли точка внутри окружности радиуса 2
        if x**2 + y**2 <= 4:
            points.append(complex(x, y))
    return points

complex_list = generate_points(42000)
print("Начальный список комплексных чисел:",complex_list[:10])
sorted_complex_list = comb_sort_complex(complex_list)
print("Отсортированный список комплексных чисел:", sorted_complex_list[:10])


# 4) Отрывок из книги «Война и Мир»
with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
    war_and_peace_words = file.read().split()
    print("Не отсортированный отрывок из кникги 'Война и мир':",war_and_peace_words[:10])
sorted_war_and_peace_words = comb_sort(war_and_peace_words)
print("Отсортированный отрывок из 'Войны и Мира':", sorted_war_and_peace_words[:10])











