import random
import math

def bubble_sort(lst):
n = len(lst)
# Проходим по всем элементам списка
for i in range(n):
# Флаг, указывающий на то, была ли выполнена перестановка
swapped = False
# Проходим по элементам списка от i до n - 1 чтоб не съебало далеко
for j in range(i, n - 1):
# Если текущий элемент больше следующего, меняем их местами
if abs(lst[j]) > abs(lst[j + 1]):
lst[j], lst[j + 1] = lst[j + 1], lst[j]
swapped = True
# Если модули текущего и следующего элементов равны, сравниваем их по аргументу
elif abs(lst[j]) == abs(lst[j + 1]) and lst[j].imag > lst[j + 1].imag:
lst[j], lst[j + 1] = lst[j + 1], lst[j]
swapped = True
# Если за проход по внутреннему циклу перестановок не было, выходим из внешнего цикла
if not swapped:
break
return lst
def Counting_sort(word_list): #эта параша для целых чисел но можно для слов
max_length = 0
for word in word_list:
if len(word) > max_length:
max_length = len(word)
count = [0] * (max_length + 1) #для подсчета количества слов каждой длины
for word in word_list:
count[len(word)] += 1

for i in range(1, max_length + 1):
count[i] += count[i - 1]

result = [None] * len(word_list) # создание ничего в кол-ве слов Выходной список
# переносим слова из входного списка в выходной список в правильном порядке
for word in reversed(word_list):
index = count[len(word)] - 1
result[index] = word
count[len(word)] -= 1

return result
def Radix_sort(int_lst): #Эта тема тоже подойдет для целых чисел
max_num = max(int_lst) # Макс число, можно было фором но и так все медленно
max_digit = len(str(abs(max_num))) # Кол-во разрядов

# Сортировка по разрядам
for digit in range(max_digit):
# 10 корзин 0-9
baskets = [[] for _ in range(10)]
# Расфосовка
for num in int_lst:
digit_num = num // 10 ** digit % 10
baskets[digit_num].append(num)
# Собираем элементы из корзин в новый список
integer_list = [num for basket in baskets for num in basket]

return int_lst
def merge_sort(fl_lst):
if len(fl_lst) <= 1:
return fl_lst
#Разделяем список на две части
mid = len(fl_lst) // 2
left = fl_lst[:mid]
right = fl_lst[mid☺

#Танцы с бубном и рекурсия
left = merge_sort(left)
right = merge_sort(right)

#Объединяем два отсортированных списка
return merge(left, right)


def merge(left, right):
result = []
i = j = 0

#Сравниваем элементы двух списков и добавляем меньший элемент в результат
while i < len(left) and j < len(right):
if left[i] < right[j]:
result.append(left[i])
i += 1
else:
result.append(right[j])
j += 1

#Добавляем остатки
result += left[i☺

#Добавляем остатки
result += right[j☺

#Возвращаем объединенный и отсортированный список
return result

# список целых чисел не панимаю штук или че ну пусть будет так!
integer_list = [random.randint(0, 999999) for _ in range(999999)]

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_list = [random.uniform(-1, 1) for _ in range(99999)]

# 42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = 17 / 2 (можно случайных, можно равномерно распределённых)
circle_points = []
for i in range(42000):
angle = random.uniform(0, 2*math.pi) #0 до 360
x = (17/2) * math.cos(angle)
y = (17/2) * math.sin(angle)
circle_points.append(complex(x, y))
with open('book.txt', 'r', encoding='UTF-8') as file: #глупый шиндовс глупая кодировка
text = file.read()
# отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
book_words = [word.strip(".,!?;:-–—\"\'()\ufeff") for word in text.split() if word.strip(".,!?;:-–—\"\'()\ufeff")] #Хз как оно работает но без ифа есть '' в мас Магия не иначе

IntegerARR = 'Int.txt'
FloatARR = 'Float.txt'
ComplexARR = 'Circle_complex.txt'
StringARR = 'Str.txt'



with open(IntegerARR, 'w') as f:
f.write(','.join(map(str,Radix_sort(integer_list))))
with open(FloatARR, 'w') as f:
f.write(','.join(map(str,merge_sort(float_list))))
with open(ComplexARR, 'w') as f:
f.write(','.join(map(str,
bubble_sort(circle_points))))
with open(StringARR, 'w', encoding='UTF-8') as f:
f.write(','.join(map(str, Counting_sort(book_words))))
