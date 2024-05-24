import random
import numpy as np
import sortirovka as sort

# Исходные данные:
# print(random.sample(range(1, 18), 4))
# 10 - Quicksort
# 9  - Heapsort
# 11 - Merge sort
# 16 - Most significant digit

# Массив целых чисел
array_1 = []
for i in range(100000):
	array_1.append(random.randint(0, 999999))

# Массив чисел с плавающей точкой
array_2 = np.random.uniform(low = -1, high =  1, size = 999)

# Массив точек комплексной плоскости
array_3 = []
r = 25/1
for i in range(42000):
	x = np.random.uniform(-r, r)
	y = np.random.uniform(-(r**2-x**2)**0.5, (r**2-x**2)**0.5)
	array_3.append([x,y])

# Массив слов
array_4 = []
file = open("text.txt", 'r', encoding="utf-8")
for line in file:
	for word in line.split(' '):
		if (word != '' and word != '\n' and word != '-'):
			array_4.append(word.replace('\n', '').replace("\"", '').replace('.', '').replace(',', '').lower())
