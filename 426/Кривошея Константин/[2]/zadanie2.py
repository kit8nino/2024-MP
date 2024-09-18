import random
import math
import numpy as np
print(random.sample(range(1,18),4))
# выданный результат = [11, 10, 8, 2]
# список чисел от 0 до 999999
spisok_chisel = list(range(1000000))
print(spisok_chisel)

# список вещественных чисел от -1 до 1 в количестве 999999
spisok_veschisel = [random.uniform(-1,1) for _ in range(999999)]
print(spisok_veschisel)

# точки внутри окружности birth_day = 29, birth_month = 12
birth_day = 29
birth_month = 12
r = birth_day/birth_month
tochki = np.random.uniform(-r, r, size=(42, 2))
chisla = tochki[:, 0] + 1j * tochki[:, 1]
sortirovka_chisel = sorted(chisla, key = lambda x: abs(x))
for i in range(10):
    print(sortirovka_chisel[i])

# книжка
with open('otrivok.docx', 'r', encoding='utf-8', errors='ignore') as file:
    soderzanie = file.read()
spisok_slov = soderzanie.split()

#метод сортировки 2 - пузырьком
def sortirovka_puzirkom(spisok, key = lambda x:x):
    k = len(spisok)
    for i in range(k):
        for j in range(0, k - i - 1):
            if spisok[j] > spisok[j + 1]:
                spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]

    return spisok
print("Сортировка пузырьком")
# для списка чисел
spisok_chisel = sortirovka_puzirkom(spisok_chisel)
print(spisok_chisel)

# для вещественных чисел
spisok_veschisel = sortirovka_puzirkom(spisok_veschisel)
print(spisok_veschisel)

# для точек
sortirovka_chisel = sortirovka_puzirkom(sortirovka_chisel)
print(sortirovka_chisel)

# для строк
spisok_slov = sortirovka_puzirkom(spisok_slov)
print(spisok_slov)





# метод сортировки выбором
def sortirovka_viborom(spisok1):
    for i in range(len(spisok1)):
        min_value = spisok1[i]
        min_index = i
        for j in range(i + 1, len(spisok1)):
            if spisok1[j] < min_value:
                min_value = spisok1[j]
                min_index = j
        spisok1[i], spisok1[min_index] = spisok1[min_index], spisok1[i]
    return spisok1

print("Сортировка выбором")

# для списка чисел
spisok_chisel = sortirovka_viborom(spisok_chisel)
print(spisok_chisel)

# для вещественных чисел
spisok_veschisel = sortirovka_viborom(spisok_veschisel)
print(spisok_veschisel)

# для точек
sortirovka_chisel = sortirovka_viborom(sortirovka_chisel)
print(sortirovka_chisel)

# для строк
spisok_slov = sortirovka_viborom(spisok_slov)
print(spisok_slov)


# метод 10 - быстрая сортировка
def bistray_sortirovka(spisok2):
    if len(spisok2) <= 1:
        return spisok2

    pivot = spisok2[random.randint(0, len(spisok2) - 1)]
    left = [x for x in spisok2 if x < pivot]
    middle = [x for x in spisok2 if x == pivot]
    right = [x for x in spisok2 if x > pivot]

    return bistray_sortirovka(left) + middle + bistray_sortirovka(right)
print("Быстрая сортировка")
# для списка чисел
spisok_chisel = bistray_sortirovka(spisok_chisel)
print(spisok_chisel)

# для вещественных чисел
spisok_veschisel = bistray_sortirovka(spisok_veschisel)
print(spisok_veschisel)

# для строк
sortirovka_chisel = bistray_sortirovka(sortirovka_chisel)
print(sortirovka_chisel)

# для строк
spisok_slov = bistray_sortirovka(spisok_slov)
print(spisok_slov)


# метод 11 - сортровка слиянием

def sortirovka_sliyaniem(spisok3):
    if len(spisok3) > 1:
        mid = len(spisok3) // 2
        L = spisok3[:mid]
        R = spisok3[mid:]

        sortirovka_sliyaniem(L)
        sortirovka_sliyaniem(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                spisok3[k] = L[i]
                i += 1
            else:
                spisok3[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            spisok3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            spisok3[k] = R[j]
            j += 1
            k += 1
    return spisok3
print("Сортировка слиянием")

# для списка чисел
spisok_chisel = sortirovka_sliyaniem(spisok_chisel)
print(spisok_chisel)

# для вещественных чисел
spisok_veschisel = sortirovka_sliyaniem(spisok_veschisel)
print(spisok_veschisel)

# для строк
sortirovka_chisel = sortirovka_sliyaniem(sortirovka_chisel)
print(sortirovka_chisel)

# для строк
spisok_slov = sortirovka_sliyaniem(spisok_slov)
print(spisok_slov)
