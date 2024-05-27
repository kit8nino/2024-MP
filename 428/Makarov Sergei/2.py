#Сортировка пузырьком
import random
L = []
for x in range(1, 1000):
    ch = random.randint(1, 999999)
    L.append(ch)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort(L))

#Сортировка расческой
random_list = [random.uniform(-1, 1) for _ in range(99999)]
def comb_sort(arr):
    n = len(arr)
    gap = n
    while gap > 1 or False:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            i += 1
    return arr
print(comb_sort(random_list))

#Гномья сортировка 
import random
with open('alice_in_wonderland.txt', 'r') as f:
    words = f.read().split()

def gnome_sort(words):
    n = len(words)
    i = 0
    while i < n:
        if i > 0 and words[i] < words[i-1]:
            words[i], words[i-1] = words[i-1], words[i]
            i -= 1
        else:
            i += 1
    return words
sorted_words = gnome_sort(words)
#Поразрядная сортировка
