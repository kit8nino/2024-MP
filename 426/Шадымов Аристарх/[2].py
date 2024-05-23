import random

# print(random.sample(range(1, 18), 4))
# 8 17 16 3
# selection sort, bitonic sort, most significant digit, comp sort

# Исходные данные:
arr1 = []
for i in range(1000):
	arr1.append(random.randint(0, 999999))

arr2 = []
for i in range(99999):
	arr2.append(random.uniform(-1, 1))

arr3 = []
r = 31/10
for i in range(42000):
	x = random.uniform(-r, r)
	y = random.uniform(-(r**2-x**2)**0.5, (r**2-x**2)**0.5)
	arr3.append([x, y])

arr4 = []
file = open("text.txt", 'r', encoding="Windows-1251")
for line in file:
	for word in line.split(' '):
		if (word != '' and word != '\n' and word != '-'):
			arr4.append(word.replace('n', ''))



def selection_sort(array):
	i = 0
	length = len(array)
	while i < length-1:
		min_i = i
		for j in range(i+1, length):
			if array[j] < array[min_i]:
				min_i = j
		array[i], array[min_i] = array[min_i], array[i]
		i += 1
selection_sort(arr1)
# Отсортировано