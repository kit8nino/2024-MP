import random
import numpy as np
import codecs
import re
#print(random.sample(range(1, 18), 4)) #11, 10, 9, 7

#исходные данные
a=random.sample(range(0, 999999), 999999)

b=[]
for j in range(0,99999):
    b.append(random.uniform(-1,1))

r=3/9
compl=[]
j=1
while j<=42000:
    real=random.uniform(0, r)
    im=random.uniform(0, r)
    if (np.sqrt(real**2+im**2))<r:
        compl.append(complex(real,im))
        j+=1

file = codecs.open("Преступление и наказание.txt", "r", "utf_8_sig" )
text = file.readlines()
c=[]
i=0
t=len(text)
while (i<t):
    line=text[i]
    line=re.sub("[^А-Яа-я]"," ",line)
    c+=line.split()
    i+=1  


#11 Сортировка слиянием
def merge(list):
    loc_list = list
    n = len(loc_list)
    if n > 1:
        mid = n//2
        left = loc_list[:mid]
        right = loc_list[mid:]
        merge(left)
        merge(right)
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
P1 = merge(a)
print("Сортировка слиянием массива целых чисел:", P1)


#10 Быстрая сортировка
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

P2 = QuickSort(b)
print("Быстрая соортировка массива вещественных чисел:",P2)


#9 Пирамидальная сортировка
def headcompl(Mas,i,End):
    headd=i
    left=2*i+1
    right=2*i+2
    
    if left<End and abs(Mas[headd])<abs(Mas[left]):
        headd=left
    if right<End and abs(Mas[headd])<abs(Mas[right]):
        headd=right
    if headd!=i:
        t=Mas[i]
        Mas[i]=Mas[headd]
        Mas[headd]=t
        headcompl(Mas,headd,End)
def headsortcompl(Mas,Start,End):
    i=len(Mas)
    while i>=Start:
        headcompl(Mas,i,len(Mas))
        i-=1
    i=len(Mas)-1
    while i>Start:
        t=Mas[i]
        Mas[i]=Mas[0]
        Mas[0]=t
        headcompl(Mas,0, i)
        i-=1
    return Mas

compl1=compl.copy()
P3 = headsortcompl(compl1,0,len(compl1))
print("Пирамидальная сортировка массива комплексных чисел:", P3)


#7 Гномья сортировка
def swap(Mas,i):
    t=Mas[i]
    Mas[i]=Mas[i-1]
    Mas[i-1]=t

def gnome(Mas,Start,End):
    i=Start+1
    while Start < End:
        if Mas[Start-1]<Mas[Start]:
            Start=i
            i+=1
        else:
            swap(Mas,Start)
            Start-=1
            if Start == 0:
                Start=i
                i+=1
    return Mas  

#a=[34,4,22,5,7,0,2,66,111,3]
c1=c.copy()
P4 = gnome(c1,0,len(c1))
print("Гномья сортировка текста из книги:", P4)