import random
import numpy as np

# После случайно выбраных чисел алгоритм показал 10,1,3,5






#   Quicksort
arrc = random.sample(range(1000000), 1000000)
print("Список до изменений: ",arrc)
def Quicksort(arrc):
    if len(arrc) <= 1:
        return arrc
    else:
        pivot = arrc[0]
        less = [x for x in arrc[1:] if x <= pivot]
        greater = [x for x in arrc[1:] if x > pivot]
        return Quicksort(less) + [pivot] + Quicksort(greater)

    sortarr = Quicksort(arrc)
    return(sortarr)
print("Список после изменений: ",Quicksort(arrc))





# Шейкерная сортировка, сортировка перемешиванием
arrv = [random.uniform(-1, 1) for numbers in range(9999) ]
print("Список до изменений: ",arrv)
left_border = 0 
right_border = len(arrv) - 1
def Shake(arrv):
    n = len(arrv)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, n-1):
            if arrv[i] > arrv[i+1]:
                arrv[i], arrv[i+1] = arrv[i+1], arrv[i]
                sorted = False
        if sorted:
            break
        sorted = True
        for i in range(n-2, -1, -1):
            if arrv[i] > arrv[i+1]:
                arrv[i], arrv[i+1] = arrv[i+1], arrv[i]
                sorted = False
                
    return arrv
print("Список после изменений: ",Shake(arrv))






# Сomp sort, сортировка расческой
random.seed(42)  # Для воспроизводимости результата
birth_day = 24  # Пример значения дня рождения
birth_month = 3  # Пример значения месяца рождения
r = birth_day / birth_month

points = np.random.uniform(-r, r, size=42000) +1j*np.random.uniform(low=-r, high=r, size=42000)



# Сортировка точек по модулю
arrcs = sorted(points, key=lambda x: np.abs(x))
def comp_sort(arrcs):
    def compare(a, b):
        if a.real < b.real:
            return -1
        elif a.real > b.real:
            return 1
        else:
            if a.imag < b.imag:
                return -1
            elif a.imag > b.imag:
                return 1
            else:
                return 0

    arrcs.sort(key=lambda x: (x.real, x.imag))
    return arrcs


# Сортировка с помощью comp_sort
sorted_numbers = comp_sort(arrcs)

# Вывод отсортированных чисел
print(sorted_numbers)



# Shellsort
def shellsort(arr):
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

if __name__ == "__main__":
    file_name = "otrivok.txt"
    
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    
    shellsort(lines)
    
    sorted_file_name = "output.txt"
    
    with open(sorted_file_name, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + "n")
    
    print("File sorted and saved to", sorted_file_name)
