import datetime
import queue
import random
import collections 
mark={'матеша': 2,
      'русский': 3,
      'химия': 5,
      'биология': 5,
      'физика': 3,
      'история': 1,
      'общество': 4,
      'экономика': 5,
      'инглиш': 4,
      'обж': 3,
      'литература': 2,
      'проект': 3,
      'изо': 5,
      'физра': 4}
info=('Clint','Eastwood', 1930,5,31)
moscow_name=['Ivan','Alexandr','Sergey','Andrey','Dmitriy','Alexey','Maxim','Mihail','Vladimir','Nikita']
moscow_family=['Ivanov','Petrov','Smirnov','Sergeev','Volkov','Kuznetsov','Vasilyev','Romanov']
p=int(input("Enter size of FIO:"))
moscow=[]
for i in range(p):
    s=random.choice(moscow_name)+random.choice(moscow_family)
    moscow.append(s)
name='Блинный слон'
#Да да, блинный слон существует и находится в ставрополе(загуглите: ставропольский блинный слон)

sum=0
for key in mark:
    sum+=mark[key]
print("Средняя оценка в аттестате",sum/len(mark))

unik=[]
for i in range(len(moscow)):
    count=0
    for j in range(len(moscow)):
        if(i == j):
            continue
        count+=1
        if(moscow[i] == moscow[j]):
            break
        if(count == len(moscow)-1):
            unik.append(moscow[i])
print(unik)

lenth=0
for key in mark:
    lenth+=len(key)
print('Lenth of school subject strings:',lenth)

print("Uniqe letter:")
for key in mark:
    unik2=[]
    for i in range(len(key)):
        count=0
        for j in range(len(key)):
            if(i == j):
                continue
            count+=1
            if(key[i] == key[j]):
                break
            if(count == len(key)-1):
                unik2.append(key[i])
    print(key,unik2)


bin_result = ''.join(format(x,'08b') for x in bytearray(name,'utf-8')) 
print("Bin result", bin_result)

n1=int(input("Enter year:"))
n2=int(input("Enter month:"))
n3=int(input("Enter day:"))
dt2 = datetime.datetime(n1,n2,n3)
dt1 = datetime.datetime(info[2],info[3],info[4])
tdelta = dt2 - dt1 
print(tdelta) 

q = queue.Queue()

s=0
while True:
    s=str(input("Enter material(if you want close - enter stop):"))
    if(s=='stop'):
        break
    q.put(s)

while not q.empty():
    print(q.get(), end=' ')
print('')
print('Enter index(less than ',len(moscow),'):')
i=int(input())
name_china='ZhòngDīng'
moscow[i]=name_china
print(moscow)
print('')

city=collections.deque() 
city.append('Овнище')
city.append('Трусово')
city.append('Да-да')
city.append('Большой Куяшь')
city.append('Лысая Балда')
city.append('Мусорка')
city.append('Добрые пчелы')
value=str(input('Enter value of linkedlist for delete:'))
i=int(input('Enter index of linked_list:'))
city.remove(value)
city.insert(i,'Конец')
print('Cities: ',city)








