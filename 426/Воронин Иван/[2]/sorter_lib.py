# import random
import numpy as np
import math

# print(random.sample(range(1, 18), 4))
# [2, 3, 7, 17]

def sort_bubble(array):
	for i in range(len(array)):
		for j in range(len(array)-i):
			if array[j] > array[i]:
				array[i], array[j] = array[j], array[i]
	return(array)





def sort_comp(array):
	Lenght = len(array)
	for step in range(Lenght, 0, -1):
		for	i in range(0, Lenght-step):
			if (array[i] > array[i+step]):
				array[i], array[i+step] = array[i+step], array[i]
	return(array)





def module(vector):
	return(vector[0]**2+vector[1]**2)**0.5

def sort_gnome(array):
	i_max = len(array)
	i = 0
	while(i < i_max-1):
		if module(array[i]) <= module(array[i+1]):
			i += 1
		elif (i != 0):
			array[i], array[i+1] = array[i+1], array[i]
			i -= 1
		else:
			array[i], array[i+1] = array[i+1], array[i]





def bitonic_merge(left, right):
	return(np.concatenate([left, right]))

def array_optimisation(array):
	addition = 2**math.ceil(math.log2(len(array))) - len(array)
	array_addition = np.empty((addition))
	array_addition.fill(math.inf)
	array = bitonic_merge(array, array_addition)
	return array

def comp_and_switch(array, a, b, inverted):
	size = b - a
	step = int(size / 2)
	if not inverted:
		for i in range(a, math.floor(a + size / 2)):
			if array[i] <= array[i + step]:
				pass
			else:
				array[i], array[i + step] = array[i + step], array[i]
	else:
		for i in range(a, math.floor(a + size / 2)):
			if array[i] >= array[i + step]:
				pass
			else:
				array[i], array[i + step] = array[i + step], array[i]
	if size > 2:
		comp_and_switch(array, a, a + step, inverted)
		comp_and_switch(array, a+step, b, inverted)

def sort_bitonic_subfunction(array, limit_size, inverted):
	if len(array) == limit_size:
		comp_and_switch(array, 0, limit_size, inverted)	
	else:
		middle = int(len(array)/2)
		left = array[:middle]
		right = array[middle:]
		sort_bitonic_subfunction(left, limit_size, False)
		sort_bitonic_subfunction(right, limit_size, True)
		array = bitonic_merge(left, right)

def sort_bitonic(array): 
	# Preparation to sort (adjust the size to degree of 2)
	array = array_optimisation(array)
	# Ready for sort
	sort_interval = 2
	limit_interval = len(array)+1
	while(sort_interval < limit_interval):
		sort_bitonic_subfunction(array, sort_interval, False)
		sort_interval *= 2
	return array