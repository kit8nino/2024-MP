# Для 42000 точек думает очень долго, но работает
import random
radius = 15//3
quantity = 42000
data_array=[]

for i in range(quantity):
    a = random.uniform(0,radius)
    b = radius - a
    data_array.append(complex(a,b))

print("Исходный массив данных:\n{}".format(data_array))

def gnome_sort(data_array):
    data_array=data_array.copy()
    i=1
    j=2
    
    while i < len(data_array):
        if abs(data_array[i-1]) < abs(data_array[i]):
            i = j
            j += 1
        else:
            data_array[i-1], data_array[i] = data_array[i], data_array[i-1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return data_array

print("\Отсортированный массив:\n{}".format(gnome_sort(data_array)))