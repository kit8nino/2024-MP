import random

# print(random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне
# 10, 3, 2, 7

array_1 = [0]*99999
for i in range(99999):
	array_1[i] = (random.randint(0, 999999))

array_2 = [0]*99999
for i in range(99999):
	array_2[i] = (random.uniform(-1, 1))

array_3 = []
r = 22
x_list = []
y_list = []
for i in range(42000):
	x = random.uniform(-r, r)
	y = random.uniform(-(r**2-x**2)**0.5, (r**2-x**2)**0.5)
	array_3.append([x, y])

file = open("text.txt", 'r', encoding="utf-8")
array_4 = []
for line in file:
	for word in line.split(' '):
		array_4.append(word)



def quicksort(array):
	if len(array) <= 1:
		return array
	central = (array[0] + array[-1]) / 2
	left = []
	mid = []
	right = []
	for i in range(len(array)):
		if array[i] < central:
			left.append(array[i])
		elif array[i] == central:
			mid.append(array[i])
		else:
			right.append(array[i])
	left = quicksort(left)
	right = quicksort(right)
	return left + mid + right

array_1 = quicksort(array_1)
print("quicksort")



def compsort(array):
	max_len = len(array)
	for step in range(max_len, 0, -1):
		for	i in range(0, max_len-step):
			if (array[i] > array[i+step]):
				array[i], array[i+step] = array[i+step], array[i]
	return(array)

array_2 = compsort(array_2)
print("compsort")
# Долго соритрует такой массив, при длине в 9999 укладывается в секунду

def abs(number):
	return (number[0]**2+number[1]**2)**0.5

def bubblesort(array):
	last = len(array) - 1
	while(last > 0):
		for i in range(0, last):
			if abs(array[i]) > abs(array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
		last -= 1
		print(last)
	return array

array_3 = bubblesort(array_3)
print("bubblesort")
# Долго соритрует такой массив, при длине в 4200 укладывается в 5 секунд
