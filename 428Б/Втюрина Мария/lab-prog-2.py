import numpy as np
import random
import string

#исходные данные
A=np.empty([999999],dtype=int)
for i in range (999999):
    A[i]=random.randint(0,1000)

B=np.empty([999999],dtype=float)
for i in range (999999):
    B[i]=random.uniform(-1,1)

C=np.empty([42000],dtype=complex)
for i in range (42000):
    x=random.randint(0,100)
    y=random.randint(0,100)
    z=complex(x,y)
    C[i]=z

D = []
with open("P&P for lab2.txt", encoding="utf-8") as f:
    for line in f:
        D += line.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()

#############################################################################

#COMBSORT
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def recount_gap(gap):
    return gap*4//5

def ind_a_gap_away(i,gap):
    return i+gap

def off_the_swaps(swapped):
    return False
    
def indicate_the_swap(swapped):
    return True

def sort_the_gap(A,gap,swapped):
    for i in range(len(A) - gap):
        j = ind_a_gap_away(i,gap)
        if A[i] > A[j]:
            A[i],A[j] = swap(A[i], A[j])
            swapped = indicate_the_swap(swapped)

def combsort(A):
    gap = len(A)
    swapped = True
    while gap > 1 or swapped:
        gap=recount_gap(gap)
        swapped=off_the_swaps(swapped)
        sort_the_gap(A,gap,swapped)
    return A

print(A[55:70],'\n')
print('--------------------------SORTED-------------------------------','\n')
print(combsort(A[55:70]),'\n\n')
##############################################################################

#GNOMESORT


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

print(B[5:17],'\n')
print('--------------------------SORTED-------------------------------','\n')
print(gnomesort(B[5:17]),'\n\n')
##############################################################################

def leave_the_modules(C):
    c=[]
    for i in range (len(C)):
        c.append(np.abs(C[i]))
    return c

def prepare_for_sorting(C):
    dict={}
    for el in C:
        dict[el]=np.abs(el)
    C1=dict.values()
    return dict,C1

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

#BUCKETSORT 
def size_of_one_bucket(A,number_of_buckets):
    l=len(A)%number_of_buckets
    q=0
    if l==0:
        q=len(A)/number_of_buckets
    else:
        q=len(A)//number_of_buckets+1
    return q

def fill_the_buckets(A,buckets,number_of_buckets):
    i=0
    bucket_size=int(size_of_one_bucket(A,number_of_buckets))
    while i<len(A):
        buckets.append(A[i:i+bucket_size])
        i+=bucket_size
    return buckets

def sort_the_buckets(buckets):
    for bucket in buckets:
        bucket=combsort(bucket)
    return buckets

def index_of_the_bucket_with_min(buckets):
        min_index=0
        for i in range(1, len(buckets)):
            if buckets[i][0] < buckets[min_index][0]:
                min_index = i
        return min_index
    

def bucketsort(A,number_of_buckets):
    buckets=[]
    fill_the_buckets(A,buckets,number_of_buckets)
    buckets=sort_the_buckets(buckets)
    result=[]
    while buckets:
        bucket_with_min=buckets[index_of_the_bucket_with_min(buckets)]
        result.append(bucket_with_min[0])
        bucket_with_min.pop(0)
        if len(bucket_with_min)==0:
            buckets.pop(buckets.index(bucket_with_min))
    return result

print(C[6:26],'\n')
prep_dict,modules=prepare_for_sorting(C[6:26])
#print(list(modules))  посмотреть модули

print('------------------SORTED--WITH--RESPECT--TO--MODULE-------------','\n')
res=bucketsort(list(modules)[6:26],50)
final=[]
for i in range (len(res)):
    final.append(get_key(prep_dict,res[i]))
print(final,'\n\n')
##############################################################################
#RADIX_SORT

def the_biggest_length(A):
    return max([len(str(len(str(x)))) for x in A])

def create_base_sized_empty_list(base):
    return [[] for _ in range(base)]

def value_of_the_current_digit(x,base,i):
    return (x // base ** i) % base

def add_element_in_temp(temp,place,x):
    return temp[place].append(x)

def save_the_significant_elements_in_the_start_array(A,temp):
    A = [x for subarray in temp for x in subarray]
    return A

def radix_sort(A,base):
    max_digits = the_biggest_length(A)
    temp = create_base_sized_empty_list(base)
    for i in range(0, max_digits):
        for x in A:
            digit = value_of_the_current_digit(len(x),base,i)
            add_element_in_temp(temp,digit,x)
        A = save_the_significant_elements_in_the_start_array(A,temp)

        temp = create_base_sized_empty_list(base)

    return A

print(D[5:20],'\n')
print('----------------SORTED--WITH--RESPECT--LENTGTH------------------------','\n')
print(radix_sort(D[5:20],10))
