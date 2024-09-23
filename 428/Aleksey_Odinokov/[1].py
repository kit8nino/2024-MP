from datetime import datetime, timedelta
import random
import collections 


subjects = {
    "Математика": 5,
    "Русский язык": 4,
    "Физика": 5,
    "Химия": 4,
    "Биология": 5,
    "География": 4,
    "История": 4,
    "Обществознание": 5,
    "Английский язык": 5,
    "Немецкий язык": 4,
    "Физкультура": 5,
    "Информатика": 5,
    "Черчение": 4,
    "Музыка": 5
}

actor = ("Клинт", "Иствуд")
birthdate = datetime(1930, 5, 31)

names = []
krasnoyarsk_name=['Ivan','Alexandr','Sergey','Andrey','Dmitriy','Alexey','Maxim','Evgeniy','Vladimir','Denis']
krasnoyarsk_family=['Ivanov','Petrov','Smirnov','Sergeev','Vasilyev','Kuznetsov','Andreev','Popov']
p=int(input("Enter size of FIO:"))
for i in range(p):
    s=random.choice(krasnoyarsk_name)+"_"+random.choice(krasnoyarsk_family)
    names.append(s)


animal_name = "Мудрый Джава"



avg_grade = sum(subjects.values()) / len(subjects)
print("Средняя оценка в аттестате:", avg_grade)


unique_names = set([name.split()[0] for name in names])
print("Уникальные имена:", unique_names)


total_length = sum([len(subject) for subject in subjects])
print("Общая длина всех названий предметов:", total_length)


unique_letters = set()
for subject in subjects:
    for letter in subject:
        unique_letters.add(letter)
print("Уникальные буквы в названиях предметов:", unique_letters)


animal_name_binary = "".join([bin(ord(char))[2:] for char in animal_name])
print("Имя вашего домашнего тамандуа в бинарном виде:", animal_name_binary)


days_since_birthdate = (datetime.today() - birthdate).days
print("Количество дней от даты рождения актера вестерна до текущей даты:", days_since_birthdate)


buildinMaterials = []
print("Введите названия стройматериалов (для остановки введите 'стоп'):")
while True:
    material = input()
    if material == "стоп":
        break
    buildinMaterials.append(material)
print("FIFO очередь для названий стройматериалов:", buildinMaterials)


number = (birthdate.day + birthdate.month**2 + birthdate.year) % 39 + 1
sorted_names = sorted(names)

print("Отсортированный список популярных имен и фамилий с измененным именем:", sorted_names)


city=collections.deque() 
city.append('Овнище')
city.append('Трусово')
city.append('Да-да')
city.append('Большой Куяшь')
city.append('Лысая Балда')
city.append('Мусорка')
city.append('Добрые пчелы')
value=str(input('Введите название city для удаления:'))
i=int(input("Введите индекс для вставки city 'Конец':"))
city.remove(value)
city.insert(i+1,'Конец')
print('Cities: ',city)
