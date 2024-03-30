# -*- coding: utf-8 -*-
import numpy as np
import datetime
import random
atestat={'русский язык':5,
         'химия':4,
         'литература':5,
         'математика':5,
         'биология':4,
         'история':5,
         'физика':5,
         'английский язык':5,
         'физкультура':5,
         'ОБЖ':5,
         'обществознание':5,
         'информатика':4,
         'латинский язык': 4,
         'финансовая грамотность':5}
actor_birthday=datetime.date(1924,2,19)
actor=("Lee","Marvin",(actor_birthday.day,actor_birthday.month,actor_birthday.year))
men_names=['Иван',
             'Сергей',
             'Александр',
             'Андрей',
             'Дмитрий',
             'Алексей',
             'Руслан',
             'Максим',
             'Марат',
             'Артур']

women_names=[   'Мария',
                'Екатерина',
                'Алина',
                'Елена',
                'Ольга',
                'Анастасия',
                'Лилия',
                'Ирина',
                'Марина',
                'Алсу']

men_surnames=['Иванов',
              'Петров',
              'Васильев',
              'Сафин',
              'Шакиров',
              'Смирнов',
              'Зарипов',
              'Хайрулин',]

women_surnames=['Иванова',
                'Романова',
                'Шакирова',
                'Хайрулина',
                'Смирнова',
                'Сафина',
                'Петрова',
                ]
men=[]
women=[]
for i in range(len(men_names)):
    person=[]
    person.append(random.choice(men_names))
    person.append(random.choice(men_surnames))
    men.append(person)
for i in range(len(women_names)):
    person=[]
    person.append(random.choice(women_names))
    person.append(random.choice(women_surnames))
    women.append(person)
tamandua='пушистая парабола'


#задание 1
def task1(atestat):
    subjects=set()
    for i in (atestat):
         subjects.add(i)
    sum=0
    for i in subjects:
        x=atestat.get(i)
        sum+=x
    b=float(sum)/len(atestat)
    print("{0:.2f}".format(b))


#задание 2
def task2(men,women):
    unique_men=set(men)
    unique_women=set(women)
    print(unique_men, unique_women, sep='\n\n')

#задание 3
def task3(atestat):
    count=0
    for i in atestat.keys():
        for j in i:
            count+=1
    print(count)

#задание 4
def task4(atestat):
    unique_letters=[]
    for i in atestat.keys():
        i=i.lower()
        for j in i:
            if j not in unique_letters and j!=' ': unique_letters.append(j)
    print(unique_letters)

#задание 5
def task5(tamandua):
    str=''
    for i in tamandua:
        if i!=' ':
            bin=(format(ord(i),'08b'))
            str+=(bin)
    print(str)
#задание 6
def task6(actor_birthday):
    actual_date=datetime.datetime.now()
    time_difference=(actual_date-actor_birthday).days
    print(f"Marvin Lee,  a famous actor,  was born {time_difference} days ago")

#задание 7
def task7():
    import queue
    materials=queue.Queue()
    print("Enter END to complete")
    def add_material(materials):
        item=input("Enter the material: ")
        if item=='END': 
            while materials.empty()==False:
               print(materials.get())
        else:
            materials.put(item)
            add_material(materials)
    add_material(materials)
