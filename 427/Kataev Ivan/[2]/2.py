import numpy as np
import random
import string

#print(random.sample(range(1, 18), 4))
#[12, 7, 10, 4]

integers_max_value=1000000

def int_list_creator(integers_max_value):
    integers_list=[integer for integer in range (integers_max_value)]
    return integers_list

def shuffled_int_list(integers_max_value):
    integers_list = int_list_creator(integers_max_value)
    random.shuffle(integers_list)
    return integers_list

def random_int_list_creator(integers_max_value):
    random_integers_list = [random.randint(0,integers_max_value-1) for i in range (integers_max_value)]
    return random_integers_list

random_int_list = random_int_list_creator(integers_max_value)

B=np.empty([999999],dtype=float)
for i in range (999999):
    B[i]=random.uniform(-1,1)

def generate_points(num_points):
    points = []
    for _ in range(num_points):
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        if x**2 + y**2 <= 4:
            points.append(complex(x, y))
    return points

D = []
with open("Виктор Пелевин - Чапаев и Пустота.txt", encoding="utf-8") as f:
    for line in f:
        D += line.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()  


#COUNTINGSORT 12 
def elements_counter(random_int_list):
    n=len(random_int_list)
    amount_of_elements=np.zeros(n)
    for element in random_int_list:
        amount_of_elements[element]+=1
    return amount_of_elements   
    
def sorted_list_former(amount_of_elements):
    sorted_list=[]
    n=len(amount_of_elements)
    for i in range (n):
        if int(amount_of_elements[i])!=0:
            for j in range (int(amount_of_elements[i])):
                sorted_list.append(i)
    return sorted_list

def counting_sort(random_int_list):
    amount_of_elements = elements_counter(random_int_list)
    sorted_int_list = sorted_list_former(amount_of_elements)
    return sorted_int_list

print('COUNTINGSORT 12' , '\n')
print('--------------------------SORTED-------------------------------','\n')
print(counting_sort(random_int_list), '\n') 

         
#GNOMESORT 7
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def jump_to_savepoint(i,savepoint):
    i=savepoint
    return i

def next_savepoint(savepoint):
    return savepoint+1

def gnome_optimize(i,savepoint):
    i=jump_to_savepoint(i,savepoint)
    savepoint=next_savepoint(savepoint)
    return i,savepoint

def gnomesort(A):
    i, savepoint = 1, 2
    while i < len(A):
        if A[i - 1] <= A[i]:
            i,savepoint=gnome_optimize(i,savepoint)
        else:
            A[i - 1], A[i]=swap(A[i - 1], A[i])
            i -= 1
            if i == 0:
                i,savepoint=gnome_optimize(i,savepoint)
    return A

print('GNOMESORT 7' , '\n')
print(B[5:17],'\n')
print('--------------------------SORTED-------------------------------','\n')
print(gnomesort(B[5:17]),'\n')


#QUICKSORT 10
def quicksort_complex(array, a, b):
    first = a
    last = b
    pivot = array[a + int((b - a) / 2)]

    while a <= b:
        while abs(array[a]) < abs(pivot):
            a += 1
        while abs(array[b]) > abs(pivot):
            b -= 1
        if a <= b:
            array[a], array[b] = array[b], array[a]
            a += 1
            b -= 1

    if a - 1 > first:
        quicksort_complex(array, first, a - 1)
    if last > a:
        quicksort_complex(array, a, last)
    return array
complex_list = generate_points(42000)
print('QUICKSORT 10' , '\n')
print(complex_list[:10], '\n')
sorted_points = quicksort_complex(complex_list ,0, len(complex_list) - 1)
print('--------------------------SORTED-------------------------------','\n')
print(complex_list[:10] , '\n')

#INSERTIONSORT 4
def insertion_sort(A):
	for i in range(len(A)):
		j = i - 1 
		key = A[i]
		while A[j] > key and j >= 0:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
	return A

print('INSERTIONSORT 4' , '\n')
print(D, '\n')
print('--------------------------SORTED-------------------------------','\n')
print(insertion_sort(D), '\n')
