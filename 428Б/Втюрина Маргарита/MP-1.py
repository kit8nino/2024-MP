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
