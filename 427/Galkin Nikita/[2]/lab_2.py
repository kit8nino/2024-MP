
import numpy as np
import random

# Исходные данные:
def f_list1(n=999999):
    list1 = list(range(n+1))
    random.shuffle(list1)
    return list1
list1 = f_list1()

list2 = [random.uniform(-1, 1) for i in range(99999)]

list_3 = []
def get_complex():
    r = 13 / 5
    x = np.random.uniform(-r, r)
    y = np.random.uniform(-r, r)
    while x ** 2 + y ** 2 >= r ** 2:
        x = np.random.uniform(-r, r)
        y = np.random.uniform(-r, r)
    return complex(x, y)
for i in range(42000):
    list_3.append(get_complex())

def get_module(complex_list):
    modules = []
    for c in complex_list:
        modules.append(abs(c))
    return modules

def f_list4():
    f = open('Идиот.txt', encoding='utf-8')
    list4 = f.read().split()
    f.close()
    return list4
list4 = f_list4()

def get_module(list3):
    modules = []
    for c in list3:
        modules.append(abs(c))
    return modules


# Действия:

def shaker_sort(lst): # Реализация сортировки перемешиванием 
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        start += 1
    return lst


def bubble_sort(lst): # Реализация сортировки пузырьком
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def select_sort(list): # Реализация сортировки выбором
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    return list
    

def tree_sort(lst):  # Реализация сортировки деревом
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def insert(root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

    def in_order_traversal(root, result):
        if root:
            in_order_traversal(root.left, result)
            result.append(root.val)
            in_order_traversal(root.right, result)

    root = None
    for item in lst:
        root = insert(root, item)

    result = []
    in_order_traversal(root, result)
    for i in range(len(lst)):
        lst[i] = result[i]
    return lst




# Выходные данные:

print("Исходный массив:")
print(list1)
print("После сортировки:")
print(shaker_sort(list1))
print()
print()
print("Исходный массив:")
print(list2)
print("После сортировки:")
print(bubble_sort(list2))
print()
print()
print("Исходный массив:")
print(list_3)
print("После сортировки:")
print(select_sort(get_module(list_3)))
print()
print()
print("Исходный массив:")
print(list4)
print("После сортировки:")
print(tree_sort(list4))

