import math

#Быстрая сортировка

def quick(array):
	if len(array) > 1:
		central_point = (array[0] + array[-1])/2
		left = []
		middle = []
		right = []
		for i in range(len(array)):
			if array[i] < central_point:
				left.append(array[i])
			elif array[i] == central_point:
				middle.append(array[i])
			else:
				right.append(array[i])
		left = quick(left)
		right = quick(right)
		array = left + middle + right
	return array


#Пирамидальная сортировка

def heapBranches(index):
	return 2*index+1, 2*index+2

def fixBranch(array, index, tree_len):
	b1, b2 = heapBranches(index)
	if b2 < tree_len:
		fixBranch(array, b2, tree_len)
		fixBranch(array, b1, tree_len)
		if array[index] < array[b1]:
			array[index], array[b1] = array[b1], array[index]
		if array[index] < array[b2]:
			array[index], array[b2] = array[b2], array[index]
	elif b1 < tree_len:
		if array[index] < array[b1]:
			array[index], array[b1] = array[b1], array[index]

def heap(array):
	i = len(array)
	while(i > 0):
		fixBranch(array, 0, i-1)
		array[0], array[i-1] = array[i-1], array[0]
		i -= 1

def mod(vector):
	summ = 0
	for i in range(len(vector)):
		summ += vector[i]**2
	return summ**0.5

#Сортировка слиянием

def merge(array):
	if len(array) < 2:
		return array
	mid = math.floor(len(array)/2)
	left = array[:mid]
	right = array[mid:]
	left = merge(left)
	right = merge(right)
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if mod(left[i]) <= mod(right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result

# Сортировка по наиболее значимой цифре

def most_significent_digit(array, length):
	left = []
	right = []
	for i in range(len(array)):
		number = str(bin(ord(array[i][0])))[2:]
		if len(number) < length or number[-length] == '0':
			left.append(array[i])
		else:
			right.append(array[i])
	if length >= 1:
		if len(left) > 1:
			left = most_significent_digit(left, length-1)
		if len(right) > 1:
			right = most_significent_digit(right, length-1)
	array = left + right
	return array