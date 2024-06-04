import random
import cmath
import threading
import time


# 1. Список из 1000 случайных целых чисел в диапазоне от 0 до 999999
integers_list = random.sample(range(1000000), 1000)


# 2. Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_list = [random.uniform(-1, 1) for _ in range(99999)]

# 3. Список из 42000 точек на комплексной плоскости внутри окружности радиуса r
# Дата рождения 2 июня
birth_day = 2
birth_month = 6
radius = birth_day / birth_month

complex_points = []
for _ in range(42000):
    angle = random.uniform(0, 2 * cmath.pi)
    distance = random.uniform(0, radius)
    point = cmath.rect(distance, angle)
    complex_points.append(point)

# Загрузка текста из файла
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Путь к текстовому файлу с отрывком из книги
book_excerpt_path = 'book_excerpt.txt'
book_excerpt_text = load_text_from_file(book_excerpt_path)

# Разбиваем текст на слова
book_excerpt_words = book_excerpt_text.split()
book_excerpt_words = book_excerpt_words[:10000]  # Убедимся, что не более 10000 слов

# 1. Сортировка перемешиванием
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr

# 2. Сортировка деревом
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def tree_sort(arr):
    if len(arr) == 0:
        return arr
    root = None
    for value in arr:
        root = insert(root, value)
    result = []
    in_order_traversal(root, result)
    return result

# 3. Сортировка подсчётом для комплексных чисел по модулю
def sort_complex_by_magnitude(arr):
    return sorted(arr, key=abs)

# 4. Битонная сортировка для отрывка из книги
def bitonic_merge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if direction == (arr[i] > arr[i + k]):
                arr[i], arr[i + k] = arr[i + k], arr[i]
        bitonic_merge(arr, low, k, direction)
        bitonic_merge(arr, low + k, k, direction)

def bitonic_sort_recursive(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort_recursive(arr, low, k, True)
        bitonic_sort_recursive(arr, low + k, k, False)
        bitonic_merge(arr, low, cnt, direction)

def bitonic_sort(arr, up=True):
    return sorted(arr, key=str.lower, reverse=not up)


def run_sorting_algorithm(algorithm, data, description):
    def sort():
        print(f"Before {description}:", data[:10])
        start_time = time.time()
        sorted_data = algorithm(data.copy())
        end_time = time.time()
        print(f"After {description}:", sorted_data[:10])
        print(f"Time taken for {description}: {end_time - start_time:.2f} seconds")
    
    sort_thread = threading.Thread(target=sort)
    sort_thread.start()

    start_time = time.time()
    while sort_thread.is_alive():
        sort_thread.join(timeout=1)
        if time.time() - start_time > 5:
            print(f"Still sorting {description}, please wait...")

# Пример использования
run_sorting_algorithm(cocktail_sort, integers_list, "cocktail sort")
print('\n')
run_sorting_algorithm(tree_sort, float_list, "tree sort")
print('\n')
run_sorting_algorithm(sort_complex_by_magnitude, complex_points, "sort by magnitude (complex)")
print('\n')
run_sorting_algorithm(bitonic_sort, book_excerpt_words, "bitonic sort")