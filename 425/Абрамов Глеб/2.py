import random
import math

# список целых чисел от 0 до 999999
integers = []
for i in range(100000):
    integers.append(i)
# random.shuffle(integers)

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
real_numbers = []
for i in range(10000):
    real_numbers.append(random.uniform(-1, 1))

# 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month
# (можно случайных, можно равномерно распределённых), сортировать по модулю числа


birth_day = 15
birth_month = 6
max_module = birth_day / birth_month
complex_points = []
while len(complex_points) != 42000:
    radius = random.uniform(0, max_module)
    angle = random.uniform(0, 2 * math.pi)
    complex_points.append([radius * math.cos(angle),
                           radius * math.sin(angle)])

# отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
words = []
with open('отрывок из книги.txt', encoding='utf-8') as book:
    for line in book:
        for i in (line.split(" ")):
            if i != '\n' and len(words) < 10000:
                words.append(str(i))


# номера выпавшие для сортировки:
# 4 сортировка вставкой
# 7 гномья сортировка
# 12 сортировка подсчетом
# 13 блочная (карманная) сортировка


# функция сортировки вставкой для действительных чисел

def insertion(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        # будем передвигать элемент пока он не встанет на нужное место
        while ((j >= 0) and (list[j] > value)):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = value


# функция для нахождения модуля комплексного числа
def module(complex):
    return math.sqrt((complex[0] * complex[0]) + (complex[1] * complex[1]))


# функция сортировки вставкой для комлексных чисел(будет использоваться позже)
def complex_insertion(list):
    for i in range(1, len(list)):
        value = module(list[i])
        j = i - 1
        while ((j >= 0) and (module(list[j]) > value)):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = list[j]


insertion(real_numbers)
print("сортировка вставкой для действительных чисел", "\n")


# print(real_numbers)

# гномья сортировка для списка слов
def Gnome_sort(list):
    index = 1
    i = 0
    n = len(list)
    while i < n - 1:
        # если следующий элемент больше то идем дальше
        if len(list[i]) <= len(list[i + 1]):
            i = index
            index = index + 1
        # если следующий меньше то меняем местами и сдвигаемся назад
        else:
            list[i], list[i + 1] = list[i + 1], list[i]
            i = i - 1
            if i < 0:
                i = index
                index = index + 1


Gnome_sort(words)
print("гномья сортировка")
print("отсортированный список слов", words)


# сортировка подсчетом для списка целых чисел


def counting_sort(list):
    list_count = [0] * len(list)
    for i in list:
        list_count[i] += 1
    list.clear()
    for i in range(len(list_count)):
        for a in range(list_count[i]):
            list.append(i)


counting_sort(integers)
print("сортировка подсчетом для списка целых чисел", "\n")
print(integers)


# print(integers)


# карманная сортировка для комплексных чисел

def Bucket_sort(list):
    buckets = []
    # создадим пустых корзин столько же сколько и переменных в сортируемом списке
    for i in range(len(list)):
        buckets.append([])
    # каждую переменную из сортируемого списка положим в свою корзину
    for i in list:
        buckets[int((module(i)) // (max_module / 42000))].append(i)
    # каждую корзину отсортируем вставкой
    for i in buckets:
        complex_insertion(i)
    # очистим список и заполним его значениями из корзин
    list.clear()
    for i in buckets:
        for number in i:
            list.append(number)


Bucket_sort(complex_points)
print("карманная сортировка для комплексных чисел", "\n")
print(complex_points)
