import random 
import numpy as np
import math

def quicksort(nums, fst, lst):
   if fst >= lst: return
 
   i, j = fst, lst
   pivot = nums[random.randint(fst, lst)]
 
   while i <= j:
       while nums[i] < pivot: i += 1
       while nums[j] > pivot: j -= 1
       if i <= j:
           nums[i], nums[j] = nums[j], nums[i]
           i, j = i + 1, j - 1
   quicksort(nums, fst, j)
   quicksort(nums, i, lst)


def bubble_sort(arr):
    for i in range(len(arr)-1):
        done = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
                done = False
        if done:
            break
        

def bucket_sort(input_list):
    
    max_value = max(input_list)
    size = max_value/len(input_list)


    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

   
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

  
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output



def complex_modulus(z):
    return math.sqrt(z.real**2 + z.imag**2)
# Сортировка точек по модулю
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and complex_modulus(var) < complex_modulus(bucket[j])):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


def shaker_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        
        swapped = False
 
        
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
 
        
        if (swapped==False):
            break
 
        
        swapped = False
 

        end = end-1
 
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
 
        
        start = start+1


#1) 
list_int = []
for i in range(100000):
    list_int.append(random.randint(0,999999))
print("Начальный список целых чисел:", list_int[:10])
#quicksort(list_int,0,len(list_int)-1)
#print(list_int)
#print(bucket_sort(list_int))
shaker_sort(list_int)
print(list_int),



#2) 
floats_list = [random.uniform(-1, 1) for _ in range(99999)]
print("Начальный список случайных вещественных чисел:",floats_list[:10])
bubble_sort(floats_list)
print(floats_list)


#3)
birth_day = 4
birth_month =7
r = birth_day / birth_month

points = [complex(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(42000 )]
print ("до",points)
insertion_sort(points)
print("после",points)




#4) 
with open("war_and_peace.txt", "r", encoding='utf-8') as file:
 war_and_peace_words = file.read().split()
print("Не отсортированный отрывок из кникги 'Война и мир':",war_and_peace_words[:10])
quicksort(war_and_peace_words,0,len(war_and_peace_words)-1)
print(war_and_peace_words)

