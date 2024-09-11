import random
import math as mt
import string

#НАДО РАСКОММЕНТИТЬ ПРИНТЫ ЧТОБЫ ПОЛУЧАТЬ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ 
#ДЛЯ КАЖДОГО АЛГОРИТМА !!!!!!!!

#генерирую свой список алгоритмов: 
#print(random.sample(range(1, 18), 4) )
#выпало: [14, 7, 4, 9]

# Генерируем случайный список целых чисел от 0 до 999999
arr = [random.randint(0, 999999) for i in range(1000)]

#print('Неотсортированный список целых чисел', arr)

#Radix sort (разрядная сортировка), номер 14
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

radix_sort(arr)

print(' ')
print(' ')
print(' ')
print(' ')

#print("Отсортированный разрядной сортировкой список целых чисел:", arr)

#генерирую вещественные числа из [-1,1]
arr1 = [random.uniform(-1, 1) for _ in range(99999)]
#print(arr1)

#гномья сортировка (gnome sort), номер 7
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

# Сортируем список arr1 с помощью гномьей сортировки
sorted_arr = gnome_sort(arr1)

print('')
print('')
print('')
print('')

#print('Гномья сортировка в действии', sorted_arr)

#генерирую 42000 точек внутри окружности радиуса r = 3.5
r = 3.5
num_points = 42000
points = []

for i in range(num_points):
    # Генерируем случайный угол в диапазоне [0, 2*pi)
    angle = random.uniform(0, 2*math.pi)
    
    # Генерируем случайное расстояние от центра до точки в диапазоне [0, r)
    radius = math.sqrt(random.uniform(0, r**2))
    
    # Преобразуем полярные координаты в декартовы координаты
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    points.append(complex(x, y))

#print(points)

#получение списка модулей комплексных чисел
moduli_list = [abs(point) for point in points]

#print(moduli_list)

#сортировка вставкой (insertion sort), номер 4 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sort(moduli_list)

#print('Сортировка вставкой в действии:', moduli_list)

#читаем файл 
def read_file_and_split(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().replace('\n', ' ')  #Чтение файла и замена переносов строк на пробелы
            #Удаление знаков препинания и разбиение текста на слова
            words = text.translate(str.maketrans('', '', string.punctuation)).split()
            return words
    except FileNotFoundError:
        print("Файл не найден.")

# Имя файла для чтения
filename = "text.txt"
word_list = read_file_and_split(filename)
#список слов
#print(word_list)


#пирамидальная сортировка, номер 9
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
heap_sort(word_list)

print('Отсортированный пирамидальной сортировкой список слов', word_list)