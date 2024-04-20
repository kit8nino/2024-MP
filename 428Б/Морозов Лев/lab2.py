import numpy as np 
import random

#1. Список целых чисел от 0 до 999999

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

#2. Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]

reals_max_value=99999 

def random_real_list_creator(reals_max_value):
    random_real_list = [2*random.random()-1 for i in range (reals_max_value)]
    return random_real_list

random_real_list = random_real_list_creator(reals_max_value)

#3. 42000 разных точки комплексной плоскости, лежащие внутри окружности радиуса radius

complex_points_amount=42000

birth_day=27

birth_month=8

radius=birth_day/birth_month

def complex_module(c):
    return abs(c)

def complex_num_creator(r):
    a=round(random.uniform(0,r), 3)
    b=round(random.uniform(0,r), 3)
    c=complex(a,b)
    return c

def random_complex_list_creator(complex_points_amount,radius):
    random_complex_list=[]
    while len(random_complex_list)!=complex_points_amount:
        c=complex_num_creator(radius)
        if complex_module(c)<radius:
            random_complex_list.append(c)
    return random_complex_list

random_complex_list = random_complex_list_creator(complex_points_amount,radius) 

#4. Отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам

chars_to_remove = ['?', '!', '@', '#', '$', ',', '.', '»', '«', '–', '—', '\n', '...', '…',':', ';', '(', ')', '\"', '\'', '-', '№']

def special_symbols_remover(chars_to_remove,book_passage_line):
    for char in chars_to_remove:
        book_passage_line = book_passage_line.replace(char, " ")
    return book_passage_line

def numbers_remover(book_passage_line):
    book_passage_line_cleaned = ''
    for char in book_passage_line:  
        if char not in ('0','1','2','3','4','5','6','7','8','9'):  
            book_passage_line_cleaned+=char
    return book_passage_line_cleaned

def book_passage_creator(file_name,chars_to_remove):
    
    book_passage=''

    with open(file_name, 'r', encoding="utf-8") as book:
        book_passage_line = book.readline()
        while book_passage_line!='':
            book_passage_line_precleaned = special_symbols_remover(chars_to_remove,book_passage_line)
            book_passage_line_cleaned = numbers_remover(book_passage_line_precleaned)
            book_passage+=book_passage_line_cleaned
            book_passage_line = book.readline() 

    book_passage = book_passage.split()

    return book_passage

book_passage = book_passage_creator('book.txt', chars_to_remove)

#Алгоритмы

#my_algorithms = random.sample(range(1, 18), 4)

#print(my_algorithms)

#У меня выпали следующие алгоритмы:
#1 - 12. Counting sort, сортировка подсчетом
#2 - 5. Shellsort, сортировка Шелла
#3 - 13. Bucket sort, блочная (карманная) сортировка
#4 - 11. Merge sort, сортировка слиянием

#1 - 12. Counting sort, сортировка подсчетом

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

#print(counting_sort(random_int_list)) 

#2 - 5. Shellsort, сортировка Шелла

def shell_sort(random_real_list):
    list_length = len(random_real_list)
    step = list_length // 2

    while step > 0:
        for i in range(step, list_length):
            start_num = random_real_list[i]
            j = i
            while j >= step and random_real_list[j - step] > start_num:
                random_real_list[j] = random_real_list[j - step]
                j -= step
            random_real_list[j] = start_num
        step //= 2

    return random_real_list

#print(shell_sort(random_real_list))

#3 - 13. Bucket sort, блочная (карманная) сортировка

#random_complex_list_1 = random_complex_list_creator(10,radius)

#print(random_complex_list_1)

amount_of_blocks=100

def complex_modules_list_former(random_complex_list):
    complex_modules_list = []
    for c in random_complex_list:
        complex_modules_list.append(complex_module(c))
    return complex_modules_list

def complex_list_fragmentation(random_complex_list,amount_of_blocks,radius):
    blocks=[]
    block_border=radius/amount_of_blocks
    temp_block_border = block_border
    for i in range(amount_of_blocks):
        block=[]
        q=0
        while q<(len(random_complex_list)):
            if complex_module(random_complex_list[q])<temp_block_border:
                block.append(random_complex_list[q])
                random_complex_list.pop(q)
            else:
                q+=1
        blocks.append(block)
        temp_block_border+=block_border
    return blocks

def complex_insertion_sort(random_complex_list):
    n=len(random_complex_list)
    for i in range (1,n):
        start_num=random_complex_list[i]
        j=i-1
        while j>=0 and complex_module(random_complex_list[j])>complex_module(start_num):
            random_complex_list[j+1]=random_complex_list[j]
            j-=1
        random_complex_list[j+1]=start_num
    return random_complex_list 

def bucket_sort(random_complex_list,amount_of_blocks,radius):
    sorted_list=[]
    blocks = complex_list_fragmentation(random_complex_list,amount_of_blocks,radius)
    for block in blocks:
        sorted_block = complex_insertion_sort(block)
        for element in sorted_block:
            sorted_list.append(element)
    return sorted_list

#print(bucket_sort(random_complex_list,amount_of_blocks,radius)) 

#4 - 11. Merge sort, сортировка слиянием

def word_comparator(word_1,word_2,words_index_to_compare=0):
    i=words_index_to_compare
    if word_1[i].lower()==word_2[i].lower():
        if len(word_1)==len(word_2)==i+1 or len(word_1)==i+1:
            return True
        elif len(word_2)==i+1:
            return False
        else:
            return word_comparator(word_1,word_2,i+1)
    elif word_1[i].lower()<word_2[i].lower():
            return True
    else:
            return False
        
def merge(sorted_first_half, sorted_second_half):
    sorted_book_passage = []
    i = 0
    j = 0

    while i < len(sorted_first_half) and j < len(sorted_second_half):
        if word_comparator(sorted_first_half[i], sorted_second_half[j]) == True:
            sorted_book_passage.append(sorted_first_half[i])
            i += 1
        else:
            sorted_book_passage.append(sorted_second_half[j])
            j += 1

    sorted_book_passage.extend(sorted_first_half[i:])
    sorted_book_passage.extend(sorted_second_half[j:])

    return sorted_book_passage
            
def merge_sort(book_passage):
    n=len(book_passage)
    if n<=1:
        return book_passage
    else:
        middle = n//2
        
        first_half = book_passage[:middle]
        second_half = book_passage[middle:]
        
        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        
        return merge(sorted_first_half, sorted_second_half)
        
#sorted_book_passage = merge_sort(book_passage)

#print(sorted_book_passage)

#Результаты работы алгоритмов:

def algorithm_runner(algorithm_number):
    
        match (algorithm_number):
            case '1':
                print ("\n#1 - 12. Counting sort, сортировка подсчетом\n")
                print(f"\nРезультат работы сортировки подсчётом:\n\n{counting_sort(random_int_list)}")
            case '2':
                print ("\n#2 - 5. Shellsort, сортировка Шелла\n")
                print(f"\nРезультат работы сортировки Шелла:\n\n{shell_sort(random_real_list)}")
            case '3':
                print ("\n#3 - 13. Bucket sort, блочная (карманная) сортировка\n")
                print(f"\nРезультат работы блочной сортировки:\n\n{bucket_sort(random_complex_list,amount_of_blocks,radius)}")
            case '4':
                print ("\n#4 - 11. Merge sort, сортировка слиянием\n")
                print(f"\nРезультат работы сортировки слиянием:\n\n{merge_sort(book_passage)}")
            case _:
                print("\nТакого алгоритма нет")
                
def algorithms_demonstrator():
        
    algorithm_number = input("\nВведите номер алгоритма, который хотите проверить, или \"СТОП\" для прекращения проверки:\
                             \n\n#1 - 12. Counting sort, сортировка подсчетом\
                             \n#2 - 5. Shellsort, сортировка Шелла\
                             \n#3 - 13. Bucket sort, блочная (карманная) сортировка\
                             \n#4 - 11. Merge sort, сортировка слиянием\n\n")

    while algorithm_number.upper()!="СТОП":
        algorithm_runner(algorithm_number)
        algorithm_number = input("\nВведите номер алгоритма, который хотите проверить, или \"СТОП\" для прекращения проверки:\
                                 \n\n#1 - 12. Counting sort, сортировка подсчетом\
                                 \n#2 - 5. Shellsort, сортировка Шелла\
                                 \n#3 - 13. Bucket sort, блочная (карманная) сортировка\
                                 \n#4 - 11. Merge sort, сортировка слиянием\n\n")

    print("\nСпасибо за то, что проверили мои алгоритмы! Надеюсь, я справился 👉👈 ")
    
    return 0
    
algorithms_demonstrator()

 
    
    
        
        
        
    
    




        