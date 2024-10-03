import random
import math

def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i-1] <= arr[i]:
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr
arr = list(range(1000000))
arr = gnome_sort(arr)
print(arr)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = [random.uniform(-1, 1) for _ in range(99999)]
arr = shell_sort(arr)
print(arr)

def sift_down(arr, start, end):
    root = start
    while (root * 2 + 1) <= end:
        child = root * 2 + 1
        if child < end and abs(arr[child]) < abs(arr[child + 1]):
            child += 1
        if abs(arr[root]) < abs(arr[child]):
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

def build_heap(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        sift_down(arr, i, len(arr) - 1)

def heapsort(arr):
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sift_down(arr, 0, i - 1)

def generate_points_in_circle(r, n):
    points = []
    while len(points) < n:
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            points.append(complex(x, y))
    return points

# параметры задания
birth_day = 15
birth_month = 5
r = birth_day / birth_month
n = 42000

# генерация списка точек
points = generate_points_in_circle(r, n)

# сортировка списка точек по модулю числа
heapsort(points)

# вывод первых 10 точек из отсортированного списка
print(points[:10])

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def get_words_from_text(text):
    words = text.split()
    return words

# текст для сортировки
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eget dui et nisl vestibulum auctor. Cras porttitor metus justo, ut fringilla purus vulputate eget. In hac habitasse platea dictumst. Sed bibendum ultrices ante, eget rhoncus nisi ornare in. Donec ullamcorper semper mauris, a interdum justo tincidunt a. Proin vitae pulvinar purus. Aliquam erat volutpat.

Suspendisse eget lectus a libero imperdiet malesuada. Phasellus at urna eget erat dapibus porta. Ut bibendum, purus a pharetra tempus, urna quam consectetur odio, ut ullamcorper nibh nisi eget orci. Integer euismod, nisi ut aliquam tincidunt, nunc nisl aliquet nisl, eget aliquam nunc nisi et nisl. Sed nec lectus nec orci fringilla facilisis. Donec fringilla imperdiet lacus, ac malesuada velit lacinia eget.

Curabitur suscipit, velit vitae bibendum lacinia, odio nisi ullamcorper nisl, eget lacinia nisi nisl eget nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed congue, magna in vehicula tincidunt, purus nisi lacinia velit, vitae venenatis ante odio eget risus.

Nullam a orci ut lectus pharetra pellentesque. Aliquam erat volutpat. Sed at eros augue. Nullam id magna at libero vulputate tincidunt. Aenean a orci et nisl consequat auctor. Suspendisse potenti. Donec facilisis magna nec sapien venenatis vestibulum. Nam interdum, eros non egestas bibendum, nisl orci bibendum lectus, ac blandit justo odio ut nisi.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed congue, magna in vehicula tincidunt, purus nisi lacinia velit, vitae venenatis ante odio eget risus.
"""

# получение списка слов из текста
words = get_words_from_text(text)

# добавление слов в список до тех пор, пока его длина не достигнет 10000
while len(words) < 10000:
    words.extend(words)

# сортировка списка слов по алфавиту
words = merge_sort(words)

# вывод первых 10 слов из отсортированного списка
print(words[:10])

