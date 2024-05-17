# import random

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
# array = [4,3,8,4,1,2,0,9,114,12,64,98]
# sort_gnome(array)
# print(array)