import random
import numpy as np

#print(random.sample(range(1, 18), 4)) #11,10,4,7

#входные
integer_list = [random.randint(0,999999) for i in range(100000)]
real_list = [random.uniform(-1,1)for i in range(99999)]
radius = 30/9
complexity_list = [random.uniform(0, radius) * np.exp(1.j * random.uniform(0, 2 * np.pi)) for i in range(42000)]
with open('Hobbit.txt') as hobbit:
    word_list = str(hobbit.read()).split()

#функции

#11
def merge_sort(list):
    loc_list = list
    n = len(loc_list)
    if n > 1:
        mid = n//2
        left = loc_list[:mid]
        right = loc_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                loc_list[k] = left[i]
                i+=1
            else:
                loc_list[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            loc_list[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            loc_list[k] = right[j]
            j+=1
            k+=1
    return  loc_list

#10
def quick_sort(list):
    loc_list = list
    n=len(loc_list)
    if n==1:
        return loc_list
    else:
        return summ(quick_sort(loc_list[n//2:]), quick_sort(loc_list[:n//2]))

#4
def insertion_sort(list):
    loc_list = list
    n = len(loc_list)
    for i in range(1,n):
        temp = loc_list[i]
        j = i-1
        while j >= 0 and abs(temp) < abs(loc_list[j]):
            loc_list[j + 1] = loc_list[j]
            loc_list[j] = temp
            j -= 1
    return loc_list

def summ(m1, m2):
    m1i, m2i=0, 0
    ans=[]
    while len(ans)<len(m1)+len(m2):
        if m1i<len(m1) and m2i<len(m2):
            ans+=[min(m1[m1i], m2[m2i])]
            if m1[m1i] < m2[m2i]:
                m1i+=1
            else: m2i+=1
        elif m1i<len(m1):
            ans+=m1[m1i:]
        else:
            ans+=m2[m2i:]
    return ans


#7
def gnome_sort(list):
    loc_list = list
    n = len(loc_list)
    i = 0
    while i < n:
        if i == 0 or len(loc_list[i-1]) <= len(loc_list[i]): i += 1
        else:
            temp = loc_list[i]
            loc_list[i] = loc_list[i-1]
            loc_list[i-1] = temp
            i -= 1
    return loc_list

#код
print(merge_sort(integer_list))
print(quick_sort(real_list))
print(insertion_sort(complexity_list))
print(gnome_sort(word_list))
