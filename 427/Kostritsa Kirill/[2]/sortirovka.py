import numpy as np
import random

# numbers = random.sample(range(1, 18), 4)
# numbers = [17, 16, 7, 3]

def get_list1(n=999999):
    list1 = list(range(n+1))
    random.shuffle(list1)
    return list1
#print(get_list1(99))

def get_list2(n=99999):
    list2 = list([random.uniform(-1, 1) for x in range(n)])
    return list2
#print(get_list2(99))

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
#print(get_list3())

def get_list4():
    f = open('Крёстный Отец (отрывок).txt') # Количество слов = 11981
    list4 = f.read().split()
    f.close()
    return list4
#print(get_list4())

# Сортировка №17
def bitonic_sort():
    return "В стадии разработки"

# Сортировка №16
def most_significant_digit():
    return "В стадии разработки"

# Сортировка №7
def gnome_sort():
    return "В стадии разработки"

# Сортировка №4
def insertion_sort():
    return "В стадии разработки"

