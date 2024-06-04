import random
import math

# random.sample(range(1, 18), 4)
# [12, 14, 15, 1]

# создание списка целых чисел от 0 до 999999
integer_list = list(range(100000))

# создание списка из 99999 случайных вещественных чисел в диапазоне [-1, 1]
float_list = [random.uniform(-1, 1) for _ in range(99999)]

# создание 42000 разных точек комплексной плоскости внутри окружности радиуса r = birth_day / birth_month
birth_day = 9
birth_month = 7
r = birth_day / birth_month
complex_list = []
while len(complex_list) < 42000:
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if math.sqrt(x ** 2 + y ** 2) <= r:
        complex_list.append(complex(x, y))
complex_list.sort(key=abs)

# отрывок из книги
with open('Миллион мелких осколков.txt', 'r') as f:
    lines = f.readlines()


# сортировка перемешиванием для списка целых чисел
def shuffle_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break
    return arr


random.shuffle(integer_list)
sorted_list = shuffle_sort(integer_list)
print(sorted_list)


# сортировка подсчетом для списка из 99999 случайных вещественных чисел в диапазоне [-1, 1]
def counting_sort(arr):
    count = [0] * (len(arr) + 1)
    for num in arr:
        count[int((num + 1) * 10)] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[int((num + 1) * 10)] - 1] = num
        count[int((num + 1) * 10)] -= 1
    return output


float_list = [random.uniform(-1, 1) for _ in range(99)]
sorted_list = counting_sort(float_list)

print(sorted_list)


# поразрядная сортировка для 42000 разных точек комплексной плоскости внутри
# окружности радиуса r = birth_day / birth_month
def radix_sort(arr):
    max_num = max(abs(int(z.real)) for z in arr)
    exp = 1
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            index = abs(int(num.real) // exp) % 10
            buckets[index].append(num)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        exp *= 10
    return arr


print(complex_list)

# least significant digit для отрывка из книги
sorted_lines = []
for line in lines:
    words = line.split()
    sorted_words = sorted(words, key=lambda x: x[::-1])
    sorted_lines.append(' '.join(sorted_words))
for line in sorted_lines:
    print(line)
