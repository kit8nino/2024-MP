# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:28:35 2024

@author: vs890
"""
import random
import datetime
from collections import deque
# dictionary
subjects = {"математика": 5, 
              "физика": 5, 
              "география": 4, 
              "обществознание": 4, 
              "физкультура": 5, 
              "русский язык": 5, 
              "литература": 4,
              "химия": 3,
              "информатика": 5,
              "английский язык": 5,
              "немецкий язык": 3,
              "биология": 5,
              "история": 4,
              "труды": 5}

#full name with birth date
actor = ("Clint", "Eastwood", "31.05.1930")

#list of names and surnames
popular_name = ["Иван", "Сергей", "Александр", "Андрей", "Дмитрий", "Алексей", "Максим", "Владимир", "Евгений", "Денис"]
popular_surname = ["Иванов", "Петров", "Сергеев", "Кузнецов", "Смирнов", "Андреев", "Васильев", "Попов"]
people_list=[]
for i in range(31):
    people_list.append(random.choice(popular_name)+" " + random.choice(popular_surname))

#name of tamandua
tamandua = "Оранжевый пневмослон"

#1
sum=0
for i in subjects.keys():
    sum+=subjects[i]
print("1. Средняя оценка в аттестате: ",sum/len(subjects))

#2
unique_names = set()
for full_name in people_list:
    parts = full_name.split()
    if len(parts) > 0:
        unique_names.add(parts[0])
print("2. Вывод уникальных имен среди взятых из таблицы популярных: ", unique_names)

#3
sum=0
for word in subjects:
    sum+=len(word)
print("3. Общая длина всех названий предметов: ", sum-3)

#4
subjects_list = list(subjects)
unique_letters = []
for i in range(len(subjects_list)):
    for j in subjects_list[i]:
        unique_letters.append(j)
unique_letters = set(unique_letters)
        
print('4. Уникальные буквы в названиях предметов: ', unique_letters)

#5
binary_tamandua = ' '.join(format(ord(char), '08b') for char in tamandua)
print("5. Имя домашнего тамандуа в бинарном виде: ", binary_tamandua)

#6 
print("6. Количество дней от даты рождения актера вестерна до текущей даты:", (datetime.datetime.now() - datetime.datetime(1930, 5, 31)).days)

#7 
materials_queue = deque()
while True:
    material = input("Введите название строительного материала (или 'стоп' для завершения): ")
    if material == "стоп":
        break
    materials_queue.append(material)
print("Названия строительных материалов:")
while materials_queue:
    print(materials_queue.popleft())

#8
index = int(input("Введите индекс имени для замены: "))
if index < 0 or index >= len(people_list):
    print("Введен некорректный индекс")
else:
    people_list[index] = "Цзи Юй"
print(people_list)

#9
silly_cities = ["Раздериха", "Хотелово", "Новопозорново", "Лохово", "Дешевки", "Мусорка", "Добрые Пчелы"]
print(silly_cities)
city_to_remove = input("Введите название города для удаления: ")
if city_to_remove in silly_cities:
    silly_cities.remove(city_to_remove)
else:
    print("Этот город не найден в списке")
print("Список городов после удаления:")
print(silly_cities)
index_to_insert = int(input("Введите индекс для вставки города 'Конец': "))
silly_cities.insert(index_to_insert, "Конец")
print("Окончательный список городов:")
print(silly_cities)