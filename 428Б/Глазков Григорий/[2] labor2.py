import random
#import numpy as np
import string

#print(random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне

#2, 7, 12, 1

n1 = 100000
n2 = 99999
file = 'literally_text.txt'

#list1 = [i for i in range(0, n)]
list1 = [random.randint(0, 999999) for i in range(n1)]
list2 = [random.uniform(-1, 1) for i in range (n2)]
list3 = []
list4 = []


r = 28/1
for i in range(1, 42000):
    complex_score = complex(random.uniform(-r, r), random.uniform(-r, r))
    if abs(complex_score) < r**2 or abs(complex_score) == r**2:
        list3.append(complex_score)


def complex_convert(list_of_complex, length):
    
    for i in range(length):
        current_value = list_of_complex[i].real
        list_of_complex[i] = current_value
        
    return list_of_complex

list3 = complex_convert(list3, len(list3))

# Открываем файл для чтения
def reader():
    with open('literally_text.txt', 'r') as file:
        # Читаем содержимое файла
        text = file.read()
        # Удаляем знаки препинания из текста
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Разбиваем текст на слова
        words = text.split()
        # Выводим список слов
    return words

list4 = reader()

"""
Пузырьковая сортировка:
    Идем по массиву слева направо,
    если текущий элемент больше
    следующего, меняем их местами
"""

def bubble(a):
    iterations = len(a) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
#print("Первый список: ", list1, "\n")
print("Сортировка 1 списка пузырьком: ", bubble(list1[::100]), "\n")


"""
Гномья сортировка:
    We rich!
    We rich!
    We rich!
    We rich!
    We rich!
    We rich!
    Сравниваем i и i+1 элементы
    массива:
        Меньше или равно - i увеличивается на 1
        в противном случае - i и i+1 меняются местами, а i уменьшается на 1
"""

def dwarf(a):
    N = len(a) - 1
    i = 0
    while i < N:
        if a[i] <= a[i+1]:
            i+=1
        else:
            a[i], a[i+1] = a[i+1], a[i]
            i -= 1 if i > 0 else i
    print("For Rock and Stone! \n")
    return a

#print("Второй список: ", list2, "\n")     
print("Сортировка 2 списка гномами: ", dwarf(list2[::100]), "\n")


"""
Сортировка подсчетом:
    Можно использовать словарь, где ключами будут сами числа, 
    а значениями - их количество. 
    После этого можно собрать отсортированный массив, 
    перебирая элементы словаря по возрастающему ключу.
"""

def counting(a):
    counting_dict = {}

    for value in a:
        counting_dict[value] = counting_dict.get(value, 0) + 1

    sorted_a = []
    for key in sorted(counting_dict):
        sorted_a.extend([key] * counting_dict[key])

    return sorted_a

#print("Третий список: ", list3)     
print("Сортировка 3 списка подсчетом: ", counting(list3[::100]))

"""
Сортировка перемешиванием
"""

def cocktail(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
            if not swapped:
                break
        
        swapped = False
        end = end - 1
        
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        
        start = start + 1
    
    return a

#print("Четвертый список: ", list4)     
print("Сортировка 4 списка перемешиванием: ", cocktail(list4[::100]))
