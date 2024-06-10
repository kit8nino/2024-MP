import random
import math
import timeit
import codecs

def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
def bubble_sort(items):
    for i in range(len(items) - 1):
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

def selection_sort(words):
    n = len(words) 
    for i in range(0, n-1): 
        min_idx = i 
        for j in range(i + 1, n): 
            if words[j] < words[min_idx]: 
                min_idx = j 
        words[i], words[min_idx] = words[min_idx], words[i]
    return words
def tree_sort(arr, key=None):
    
    tree = BinaryTree(arr)

    sorted_list = []
    tree.inorder(lambda x: sorted_list.append(x))

    return sorted_list

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, func):
        if self.left is not None:
            self.left.inorder(func)

        func(self.data)

        if self.right is not None:
            self.right.inorder(func)

def create_string_list():
    with codecs.open("book_excerpt.txt", "r", "utf_8_sig") as fileObj:
        text = fileObj.read()
    text = text.replace("–", "").replace(",", "").replace("!", "").replace("?", "").replace(".", "").replace(":", "").replace("-", "")
    return text.split()

# Исходные данные
birth_day = 13
birth_month = 3
r = birth_day / birth_month

integers = []
for i in range(10000):
    integers.append(random.randint(0,999999))


floats = [random.uniform(-1, 1) for _ in range(99999)]
complex_numbers = [complex(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(42000)]
book_excerpt = create_string_list()


# Сортировка
#shell_sort
#bubble_sort
#tree_sort
#selection_sort
bubble_sort(integers)
shell_sort(floats)
tree_sort(complex_numbers, key=lambda x:abs(x))
selection_sort(book_excerpt)

print(integers)
print(floats)
print([abs(x) for x in complex_numbers])  # Выводим модули комплексных чисел
print(book_excerpt)
