import numpy as np
import random
import string

#исходные данные
A=np.empty([999999],dtype=int)
for i in range (999999):
    A[i]=i
    
B=np.empty([999999],dtype=float)
for i in range (999999):
    B[i]=random.uniform(-1,1)
    
C=np.empty([42000],dtype=complex)
for i in range (42000):
    x=random.randint(0,10)
    y=random.randint(0,10)
    z=complex(x,y)
    C[i]=z
    
data = []

with open("P&P for lab2.txt", encoding="utf-8") as f:
    for line in f:
        data += line.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()
        
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
##############################################################################

#GNOMESORT

def swap(a,b):
    t=a
    a=b
    b=t
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

##############################################################################

#BUCKETSORT not working :(

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
        print(buckets)
        for i in range(1, len(buckets)):
            if buckets[i][0] < buckets[min_index][0]:
                min_index = i
        return min_index
    
def delete_the_empty_bucket(buckets):
    buckets=buckets.pop(index_of_the_bucket_with_min(buckets))
    return buckets

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
            buckets=delete_the_empty_bucket(buckets)
    return result

##############################################################################
