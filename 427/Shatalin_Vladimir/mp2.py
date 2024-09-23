import numpy as np

N1 = 10000
N2 = 42000

#1 массив
intlist = np.arange(0,N1,1)

#2 массив
floatlist = np.random.rand(N1-1)*2-1

#3 массив
r = 5/3
rolist = np.random.rand(N2)*r
filist = np.random.rand(N2)*2*np.pi
pointlist = np.array([rolist,filist]).T.tolist()

#4 массив
file = open('kniga.txt','r')
book = file.read()
file.close()
book = book.split()
'''
#Преобразуем каждую строку в число, суммируя значения символов по Unicode
for i in range(len(book)):
    r = 0
    for elem in book[i]:
        r+=ord(elem)
    book[i] = int(r)
'''

#1    
def combsort(ls):
    n = len(ls)
    step = n
    while step > 1 or flag:
       if step > 1:
           step = int(step / 1.25)
       flag, i = False, 0
       while i + step < n:
          if ls[i] > ls[i + step]:
              ls[i], ls[i + step] = ls[i + step], ls[i]
              flag = True
          i += step
    return ls       
print(f'1:\n {combsort(intlist)}')

#2
def bubblesort(list):
    N = len(list)
    for i in range(N-1):
        for j in range(N-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
print(f'2:\n {bubblesort(floatlist)}')

#3
def shellsort(lst):
    last_index = len(lst)
    step = len(lst)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta][0] > lst[j][0]:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst
    
print(f'3:\n {shellsort(pointlist)}')

#4
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = np.random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
       
print(f'4:\n {quicksort(book)}')
