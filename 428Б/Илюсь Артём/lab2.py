import random
import numpy as np
import re

# Алгоритмы под номерами 3, 5, 12, 16

#DATA
birth_day = 5
birth_month = 12
length = 42000
file_path = 'C:\\текст для второй лабы.txt'

"""
# список целых чисел от 0 до 999999
"""
def list_of_numbers():
   list_of_numbers = []
   while len(list_of_numbers)!=1000000:
       list_of_numbers.append(random.randrange(1000000))
       #list_of_numbers = set(list_of_numbers)
       #list_of_numbers = list(list_of_numbers)
   return list_of_numbers
#print(list_of_numbers())

"""
# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
"""

def list_of_random_numbers_from_minus_one_to_one():
    return list((-1)**random.randrange(2)*random.random() for x in range(100000))

#print(list_of_random_numbers())

"""
# 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса r = birth_day / birth_month
"""

def circle_radius(birth_day,birth_month):
    return birth_day/birth_month


def angles():
    return np.random.uniform(0, 2*np.pi, length)


def radius_of_points(circle_radius):
    return np.sqrt(np.random.uniform(0, circle_radius**2, length))


def sorted_points_of_complex(angles,radius_of_points):
    points = radius_of_points*np.exp(1j*angles)
    sorted_points = sorted(points,key = lambda x : np.abs(x))
    return sorted_points


def converting_a_complex_number_to_a_real_number(list_of_complex,length):
    
    for i in range(length):
        current_value = list_of_complex[i].real
        list_of_complex[i] = current_value
        
    return list_of_complex

print(sorted_points_of_complex(angles(),radius_of_points(circle_radius(birth_day,birth_month))))

"""
# отрывок из книги разбитый в список по словам
"""

def partition_text_to_word_list(file_path):
    with open(file_path, 'r',encoding = 'utf-8') as file:
        text = file.read()
    return text


def delete_marks_in_text(text):
    new_text = re.sub('[^\w\s]', '', text)
    return new_text


def text_to_word_list(text):
    new_text = delete_marks_in_text(text)
    words = new_text.split()
    return  words


def list_words_from_text():  
    return text_to_word_list(partition_text_to_word_list(file_path))[:400]

#print(list_words_from_text())

#------------------------------------------------------------------------------------------------------------------

def gapInsertionSort(alist,start,gap):
    
    for i in range(start+gap,len(alist),gap):

        current_array_element = alist[i]
        position = i

        while position>=gap and alist[position-gap]>current_array_element:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=current_array_element


def counting_sort_for_msd(arr):
    count_arr = [0] * 26
    result = [None] * len(arr)

    for word in arr:
        if word:
            char_index = ord(word[0].lower()) - ord('a')
        else:
            char_index = 0
        count_arr[char_index] += 1

    for i in range(1, 26):
        count_arr[i] += count_arr[i - 1]

    i = len(arr) - 1
    
    while i >= 0:
        word = arr[i]
        if word:
            char_index = ord(word[0].lower()) - ord('a')
        else:
            char_index = 0
        result[count_arr[char_index] - 1] = word
        count_arr[char_index] -= 1
        i -= 1

    return result
#------------------------------------------------------------------------------------------------------------------

# Третий алгорит сортировки, сортировка расчёской, использовал sorted_points_of_complex

def comb_sort(array):
    optimal_shrink = len(array)
    shrink = 1.247
    sorted = False
    
    while not sorted:
        optimal_shrink = int(optimal_shrink / shrink)
        
        if optimal_shrink <= 1:
            optimal_shrink = 1
            sorted = True
        i = 0
        
        while i + optimal_shrink < len(array):
            
            if abs(array[i]) > abs(array[i+optimal_shrink]):
                array[i],array[i + optimal_shrink] =array[i + optimal_shrink ], array[i]
                sorted = False
            i+=1
            
    return array


#------------------------------------------------------------------------------------------------------------------

# Пятый алгоритм сортировки, сортировка Шелла, использовал list_of_random_numbers_from_minus_one_to_one()

def shellSort(alist):
    sublistcount = len(alist)//2
    while  sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
      sublistcount = sublistcount // 2
      
    return alist
   
   
#------------------------------------------------------------------------------------------------------------------   

# Двенадцатый алгоритм сортировки, сортировка подсчётом, использовал list_of_numbers()

def counting_sort(array):
    maximum_of_numbers = max(array)
    minimum_of_numbers = min(array)
    count_arr = [0] * (maximum_of_numbers - minimum_of_numbers + 1)
    
    for i in array:
        count_arr[i - minimum_of_numbers] +=1

    sorted_array = []
    
    for i,count in enumerate(count_arr):
        sorted_array.extend([i+minimum_of_numbers]*count)
    return sorted_array  


#------------------------------------------------------------------------------------------------------------------

# Шестнадцатый алгоритм MSD для списка из слов

def msd_sort(arr):
    if not arr:
        return []


    buckets = [[] for i in range(26)]
    for word in arr:
        if word:
            buckets[ord(word[0].lower()) - ord('a')].append(word)

    result = []
    for i in range(26):
        if buckets[i]:
            result.extend(counting_sort_for_msd(buckets[i]))

    return result


#------------------------------------------------------------------------------------------------------------------



print("Алгоритм сортировки расчёской, входные данные: список комплексных чисел в количестве 42000\n")
print(comb_sort(sorted_points_of_complex(angles(),radius_of_points(circle_radius(birth_day,birth_month)))),"\n")

print("Алгорим сортировки Шелла, входные данные: список чисел в диапазоне от -1 до 1 от 0 до 999999\n")
print(shellSort(list_of_random_numbers_from_minus_one_to_one()),'\n')

print("Алгорим сортировки подсчётом, входные данные: список чисел от 0 до 999999\n")
print(counting_sort(list_of_numbers()),'\n')       

print("Алгорим сортировки MSD, входные данные: список слов из текста размером >=10000 \n")
print(msd_sort(list_words_from_text()),'\n')



