import random


# Исходные данные
list_of_int_numbers = list(range(0, 100000))

list_of_random_numbers = []
for e in range(99999):
    list_of_random_numbers.append(random.uniform(-1, 1))

birth_day = 4
birth_month = 1
r = birth_day / birth_month
list_of_complex_numbers = []
while len(list_of_complex_numbers) != 42000:
    z = complex(random.uniform(0, r), random.uniform(0, r))
    if abs(z) <= r:
        if z not in list_of_complex_numbers:
            list_of_complex_numbers.append(z)

list_of_words = []
with open("lord_of_the_rings.txt", encoding="utf-8") as book:
    data = book.read().split()
    for d in data:
        if d != '–':
            list_of_words.append(d)


# 2.bubble sort, сортировка пузырьком
def bubble_sort(a):
    index = True
    while index:
        index = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                c = a[i]
                a[i] = a[i+1]
                a[i+1] = c
                index = True


bubble_sort(list_of_int_numbers)
print("Sorted list_of_int_numbers: ", list_of_int_numbers)


# 10.Quicksort, быстрая сортировка
def quicksort(a):
    right_list = []
    left_list = []
    midl_list = []
    c = int(len(a) / 2)
    for i in range(len(a)):
        if a[i] < a[c]:
            left_list.append(a[i])
        elif a[i] > a[c]:
            right_list.append(a[i])
        else:
            midl_list.append(a[i])
    if all(a[i] < a[i+1] for i in range(len(a)-1)):
        return left_list + midl_list + right_list
    return quicksort(left_list) + midl_list + quicksort(right_list)


list_of_random_numbers = quicksort(list_of_random_numbers)
print("Sorted float: ", list_of_random_numbers)


# 1.shaker sort, сортировка перемешиванием
def shaker_sort(a):
    index = True
    while index:
        index = False
        start = 0
        end = len(a)-1
        for i in range(start, end):
            if abs(a[i]) > abs(a[i+1]):
                c = a[i]
                a[i] = a[i+1]
                a[i+1] = c
                index = True
        end -= 1

        for i in range(start, end):
            if abs(a[end-i]) < abs(a[end-i-1]):
                c = a[end-i]
                a[end-i] = a[end-i - 1]
                a[end-i - 1] = c
                index = True
        start += 1


test_list_of_complex_numbers = [6j, 2+2j, 3+1j, 18]
shaker_sort(test_list_of_complex_numbers)
print("Sorted complex: ", test_list_of_complex_numbers)

# В конечном итоге алогритм немного модифицирован. Так как сравнивать комлексные числа напрямую нельзя, приходится
# сравнивать их модули(ну или можно было придумать какой-то другой критерий для сравнения)
# для исходного массива из 42000 точек комплексной плоскости алгоритм работает очень долго(я не дождался его окончания)
# поэтому привожу пример работы для тестового массива


# 9.Heapsort, пирамидальная сортировка;
def heap(a, i, up):
    index = True
    while index:
        left = i*2+1
        right = i*2+2
        if max(left, right) < up:
            if a[i] >= max(a[left], a[right]):
                index = False
            elif a[left] > a[right]:
                c = a[i]
                a[i] = a[left]
                a[left] = c
                i = left
            else:
                c = a[i]
                a[i] = a[right]
                a[right] = c
                i = right
        elif left < up:
            if a[left] > a[i]:
                c = a[i]
                a[i] = a[left]
                a[left] = c
                i = left
            else:
                index = False
        elif right < up:
            if a[right] > a[i]:
                c = a[i]
                a[i] = a[right]
                a[right] = c
                i = right
            else:
                index = False
        else:
            index = False


def heapsort(a):
    for j in range((len(a)-2)//2, -1, -1):
        heap(a, j, len(a))
    for g in range(len(a)-1, 0, -1):
        c = a[0]
        a[0] = a[g]
        a[g] = c
        heap(a, 0, g)


heapsort(list_of_words)
print("Sorted book: ", list_of_words)