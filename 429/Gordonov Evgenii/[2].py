import random
import math
# Random_Variable=random.sample(range(1, 18), 4)
# print(Random_Variable)
# [7, 6, 11, 8]

print("ГНОМЬЯ СОРТИРОВКА: ")
#мы начинаем с первого элемента и движемся вправо. Если текущий элемент больше или равен предыдущему, мы двигаемся еще правее.
# Если текущий элемент меньше предыдущего, мы меняем их местами и двигаемся на одну позицию влево.
# Мы продолжаем этот процесс до тех пор, пока не пройдем весь список.

def gnome_sort(arr):
    i = 1
    while i < len(arr):
        # если текущий элемент больше предыдущего, двигаемся вправо
        if arr[i-1] <= arr[i]:
            i += 1
        # если текущий элемент меньше предыдущего, меняем их местами и двигаемся влево
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            if i > 1:
                i -= 1
    return arr
numbers = list(range(99))
random.shuffle(numbers)
gnome_sort(numbers)
print(numbers, "\n")

#######################################################################################################################

print("СОРТИРОВКА ДЕРЕВОМ: ")
#универсальный алгоритм сортировки, заключающийся в построении двоичного дерева поиска по ключам массива (списка),
# с последующей сборкой результирующего массива путём обхода узлов построенного дерева в необходимом порядке следования ключей.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)

    return root

def inorder_traversal(root, sorted_list):
    if root:
        inorder_traversal(root.left, sorted_list)
        sorted_list.append(root.val)
        inorder_traversal(root.right, sorted_list)

# Создание случайного списка из 99999 вещественных чисел в диапазоне [-1, 1]
numbers = [random.uniform(-1, 1) for _ in range(99999)]

# Создание корня дерева
root = None

# Вставка чисел в дерево
for num in numbers:
    root = insert_node(root, num)

# Проход в порядке возрастания и заполнение отсортированного списка
sorted_list = []
inorder_traversal(root, sorted_list)

# Вывод отсортированного списка
print(sorted_list)

#######################################################################################################################

print("СОРТИРОВКА СЛИЯНИЕМ: ")
#мы разбиваем массив на две примерно равные части, затем каждая половина сортируется рекурсивно.
# Затем отсортированные половины сливаются в новый массив в отсортированном порядке.

def merge_sort(arr):
    if abs(len(arr)) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if abs(left[i]) <= abs(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Генерация случайных точек внутри окружности радиуса r
birth_day = 16
birth_month = 6
r = birth_day / birth_month
points = []
while len(points) != 42000:
    point = complex(random.uniform(-r, r), random.uniform(-r, r))
    if abs(point) <= r:
        if point not in points:
            points.append(point)

# Сортировка слиянием по модулю числа
sorted_points = merge_sort(points)

# Вывод отсортированных точек
for point in sorted_points:
    print(point)
#######################################################################################################################

print("СОРТИРОВКА ВЫБОРОМ: ")

def selection_sort(array):
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
    return array

with open('SmallQuin.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
sorted_words = selection_sort(words)
print(sorted_words)