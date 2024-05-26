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