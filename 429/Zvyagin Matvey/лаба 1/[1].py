import datetime
import queue
import random
import collections 
object={'математика': 5,
      'русский': 3,
      'химия': 5,
      'биология': 5,
      'физика': 3,
      'история': 4,
      'обществознание': 4,
      'экономика': 5,
      'английский': 4,
      'обж': 3,
      'литература': 3,
      'изо': 5,
      'геометрия': 5,
      'краеведение': 3,
      'физра': 4}
info=('Dack','Rambo', 1941,11,13)

mass_name=['Ivan','Alexandr','Sergey','Andrey','Dmitriy','Alexey','Maxim','Mihail','Vladimir','Nikita']
mass_family=['Ivanov','Petrov','Smirnov','Sergeev','Volkov','Kuznetsov','Vasilyev','Romanov']
p=int(input("Enter size of FIO:"))
mass=[]
for i in range(p):
    s=random.choice(mass_name)+random.choice(mass_family)
    mass.append(s)
    
name='Соленый пупок'


sum=0
for key in object:
    sum+=object[key]
print("Средняя оценка в аттестате",sum/len(object))

unik=[]
for i in range(len(mass)):
    count=0
    for j in range(len(mass)):
        if(i == j):
            continue
        count+=1
        if(mass[i] == mass[j]):
            break
        if(count == len(mass)-1):
            unik.append(mass[i])
print(unik)

lenth=0
for key in object:
    lenth+=len(key)
print('Lenth of school subject strings:',lenth)

print("Uniqe letter:")
for key in object:
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
print('Enter index(less than ',len(mass),'):')
i=int(input())
name_china='Zhou Yi-wang'
mass[i]=name_china
print(mass)
print('')

city=collections.deque() 
city.append('Дно')
city.append('Конча')
city.append('Факфак')
city.append('Ширяево')
city.append('Хреновое')
city.append('Большое Бухалово')
city.append('Работки')
value=str(input('Enter value of city for delete:'))
i=int(input('Enter index of city:'))
city.remove(value)
city.insert(i,'Конец')
print('Cities: ',city)







