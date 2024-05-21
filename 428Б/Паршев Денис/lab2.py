import random, re
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
with open("book.txt", "r", encoding="utf-8") as file:
    text = file.read()
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

#Gnome sort, гномья сортировка
def gnome_sort(a):
    N = len(a) - 1
    i = 0
    while i < N:
        if a[i] <= a[i+1]:
            i+=1
        else:
            a[i], a[i+1] = a[i+1], a[i]
            i -= 1 if i > 0 else i
    return a

print("Второй список: ", generate_random_float, "\n")     
print("Сортировка 2 списка гномами: ", gnome_sort(generate_random_float[::100]), "\n")

#Merge sort, сортировка слиянием;
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if abs(L[i]) < abs(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
merge_sort(generate_random_points)
print(generate_random_points[:10])

#insertion sort, сортировка вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sort(words)
print(words[:1000])  
