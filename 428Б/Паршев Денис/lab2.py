import random, re
#print(random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне
#15, 7, 8, 2

#1 список целых чисел от 0 до 999999
n=1000000
generate_random_int = [random.randint(0, 999999) for i in range(n)]

#2 список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
n1=99999
generate_random_float = [random.uniform(-1, 1) for _ in range(n1)]

#3 точки комплексной плоскости
birth_day = 1
birth_month = 7
r = birth_day / birth_month
generate_random_points = [random.uniform(-r, r) + random.uniform(-r, r) * 1j for _ in range(42000)]
sorted_points = sorted(generate_random_points, key=abs)
#print(sorted_points)

#4 отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
with open("C:\\Users\\CyberPC\\Desktop\\book.txt.txt", "r", encoding="utf-8") as file:
    text = file.read()
#Разбиваем текст на слова
words = re.findall(r'\w+', text.lower())
#print(words)

#Shellsort, сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
shell_sort(generate_random_int)
print(generate_random_int[:100])
