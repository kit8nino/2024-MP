import numpy as np
import random
from datetime import datetime

#1. Предметы в школьном аттестате
schoolSubjects = {              
    "Algebra": 3,
    "Biology": 5,
    "Drawing": 5,
    "Chemistry": 4,
    "Computing": 2,
    "English": 5,
    "Geography": 3,
    "Geometry": 4,
    "History": 2,
    "Literature": 4,
    "Music": 2,
    "Physical education": 3,
    "Physics": 5,
    "Technology": 4
}     

#2. Актёр из вестерна
actorBirthday = datetime(1921, 11,3)
westernActor = ("Charles", "Bronson", (actorBirthday.day, actorBirthday.month, actorBirthday.year))

#3. Популярные имена и фамилии Омска
man=[]
woman=[]
manNames = ['Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Алексей', 'Максим', 'Евгений', 'Владимир', 'Николай']
manSurnames = ['Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Сергеев', 'Васильев', 'Волков', 'Попов']
womanNames = ['Елена', 'Ольга', 'Мария', 'Анастасия', 'Екатерина', 'Наталья', 'Татьяна', 'Ирина', 'Юлия', 'Светлана']
womanSurnames = ['Иванова', 'Петрова', 'Кузнецова', 'Смирнова', 'Васильева', 'Попова', 'Волкова', 'Романова']

for i in range(len(manNames)):
    name=[]
    name.append(random.choice(manNames))
    name.append(random.choice(manSurnames))
    man.append(name)
for i in range(len(womanNames)):
    name=[]
    name.append(random.choice(womanNames))
    name.append(random.choice(womanSurnames))
    woman.append(name)

#4. Имя тамандуа
tamanduaName = "Старый шкаф" 


#Средняя оценка в аттестате
averageSchoolGrade = sum(schoolSubjects.values()) / len(schoolSubjects) 
print(f"Средняя оценка в аттестате: {averageSchoolGrade}\n")

#Уникальные имена
uniqueManNames=[]
for i in range(len(man)):
    uniqueName=[]
    uniqueName.append(man[i][0])
    uniqueName.append(man[i][1])
    if uniqueName not in uniqueManNames:
        uniqueManNames.append(uniqueName)
        
uniqueWomanNames=[]
for i in range(len(woman)):
    uniqueName=[]
    uniqueName.append(woman[i][0])
    uniqueName.append(woman[i][1])
    if uniqueName not in uniqueWomanNames:
        uniqueWomanNames.append(uniqueName)

print(f"Список из уникальных мужских имен Омска: {uniqueManNames}\n")
print(f"Список из уникальных женских имен Омска: {uniqueWomanNames}\n")

#Общая длина всех названий предметов
subjectsLength = sum(len(subject) for subject in schoolSubjects)
print(f"Общая длина всех названий предметов: {subjectsLength}\n")

#Уникальные буквы в названиях предметов
uniqueSubjectsLetters = set("".join(schoolSubjects.keys()))
print(f"Уникальные буквы в названиях предметов: {uniqueSubjectsLetters}\n")

#Имя домашнего тамандуа в бинарном виде
formatTamanduaName = "".join(format(ord(char), '08b') for char in tamanduaName)
print(f"Имя домашнего тамандуа в бинарном виде: {formatTamanduaName}\n")

#Количество дней от даты рождения актера вестерна до текущей даты
numOfDays = (datetime.now() - actorBirthday).days
print(f"Количество дней от даты рождения актера до текущей даты: {numOfDays}\n")

#Очередь из названий стройматериалов
materialQueue = []
while True:
    newMaterial = input("Введите название стройматериала ('0' для остановки): ")
    if newMaterial.lower() == '0':
        break
    materialQueue.append(newMaterial)
print(f"Очередь из названий стройматериалов: {materialQueue}\n")

#Замена имени в списке на имя китайского императора
number = (actorBirthday.day + actorBirthday.month**2 + actorBirthday.year) % 39 + 1
print(f"Номер императора в списке династии Чжоу: {number}")
index = int(input("Введите номер имени в списке для замены: "))
man.sort()
man[index] = ["Чжоу", "Хуэй-ван"]
print(f"Список мужских имён с вставленным именем китайскго императора {man}\n")

#Словарь названий населенных пунктов
cityNames = {
    "Добрые пчёлы": 1,
    "Заячий пузырь": 2,
    "Крутые хутора": 3,
    "Чуваки": 4,
    "Кокаиновые горы": 5,
    "Дно": 6,
    "Мусорка": 7,
    "Большое Бухалово": 8,
    "Засосная": 9
}
print(f"Список странных названий населенных пунктов: {cityNames}")

while True:
    curCity = input("Введите название города для удаления или 'Конец' для вставки этого города ('0' для остановки): ")
    if curCity.lower() == '0':
        break
    if curCity in cityNames:
        del cityNames[curCity]
        print(f"Населенный пункт '{curCity}' удален")
    elif curCity == 'Конец':
        curIndex = int(input(f"Введите индекс: "))
        cityNames["Конец"] = curIndex
        cityNames = sorted(cityNames.items(), key = lambda x: x[1])
        cring_cities = dict(cityNames)
        print(f"'Конец' вставлен по индексу {curIndex}")
    else:
        print(f"Ошибка: неверное имя города")
        
print(f"Изменённый список странных названий населенных пунктов: {cityNames}")


