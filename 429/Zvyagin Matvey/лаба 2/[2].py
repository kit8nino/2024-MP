import random 
import numpy as np
import codecs


list_int = [num for num in range(999999)]
random.shuffle(list_int)

list_rand_int = []
for i in range(99999):
    list_rand_int.append(random.uniform(-1,1))
    
def create_comlex_list(radius):
    A=[]
    B=[]
    while len(A) <42000:
        a=random.uniform(-radius,radius)
        b=random.uniform(-radius,radius)
        if np.sqrt(a**2+b**2) < radius:
            A.append(a)
            B.append(b)
    Z=[]
    for i in range(len(A)):
        z=complex(A[i],B[i])
        Z.append(z)
    return Z

def create_string_list():
    fileObj = codecs.open( "text_laba_2.txt", "r", "utf_8_sig" )
    text = fileObj.read()
    text = text.replace('–', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('.', '')
    text = text.replace(':', '')
    text = text.replace('-', '')
    text = text.replace('*', '')
    text = text.replace('—', '')
    fileObj.close()
    list_of_string = text.split()
    return list_of_string

complex_list=create_comlex_list(7/11)
list_string = create_string_list()
#bubble sort
#quick sort
#merge sort
#selection sort
def selection_sort(A):
    n=len(A)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if A[j]<A[min]:
                min=j
        t=A[min]
        A[min]=A[i]
        A[i]=t

def bubble_sort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-1-i):
            if A[j+1] < A[j]:
                t=A[j]
                A[j]=A[j+1]
                A[j+1]=t

def complex_module(z):
    return np.sqrt(z.real**2 + z.imag**2)
def merge_sort(A):
    n=len(A)
    B=[]
    C=[]
    if n>1:
        for i in range(int(n/2)):
            B.append(A[i])
        for i in range(int(n/2),n):
            C.append(A[i])
        merge_sort(B)
        merge_sort(C)
        merge(B,C,A)


def merge(B,C,A):
    p=len(B)
    q=len(C)
    i=0
    j=0
    k=0
    while i<p and j<q  :
        if complex_module(B[i]) <= complex_module(C[j]):
            A[k]=B[i]
            i+=1
        else:
            A[k]=C[j]
            j+=1
        k+=1
    if i == p:
        for n in range(j,q):
            A[k]=C[n]
            k+=1
    if j == q:
        for n in range(i,p):
            A[k]=B[n]
            k+=1
def quick_sort(A,l,r):
    if l<r:
        s=partition(A,l,r)
        quick_sort(A, l, s-1)
        quick_sort(A,s+1,r)
def partition(A,l,r):
    p=len(A[l])
    i=l+1
    j=r
    while True:
        while i<=j and len(A[j])>=p:
            j-=1
        while i<=j and len(A[i])<=p:
            i+=1
        if i<=j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[l], A[j] = A[j], A[l]
    return j
#сортируем список list_int
selection_sort(list_int)

#сортируем список list_rand_int (долго выполняет)
bubble_sort(list_rand_int)
#сортируем список complex_list
merge_sort(complex_list)
#сортируем список list_string
quick_sort(list_string,0,len(list_string)-1)
print(list_int)
print(list_rand_int)
print(complex_list)
print(list_string)