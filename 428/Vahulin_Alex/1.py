from random import randint
import datetime

subjects={
    "Algebra": 5,
    "Geometry": 4,
    "Physics": 5,
    "Biology": 3,
    "Psychology": 4,
    "Theology": 3,
    "English": 5,
    "Russian": 4,
    "French": 3,
    "Alchemy": 5,
    "Demonology": 5,
    "3D-modeling": 5,
    "Radioelectronics": 5,
    "Physical education": 5
    }

western_actor=tuple(["Lee Van Cleef","09","01","1925"])

popular_fnames_Voronezh=["Елена","Екатерина","Ольга","Мария","Анастасия","Ирина","Наталья","Татьяна","Юлия","Светлана"]
popular_mnames_Voronezh=["Иван","Александр","Сергей","Дмитрий","Андрей","Алексей","Максим","Евгений","Владимир","Роман"]
popular_surnames_Voronezh=["Иванов","Попов","Петров","Кузнецов","Сергеев","Смирнов","Новиков","Васильев"]

popular_combos=[]

for i in range(15):
    popular_combos.append(popular_surnames_Voronezh[randint(0,7)]+" "+popular_mnames_Voronezh[randint(0,9)])
    
for i in range(15):
    popular_combos.append(popular_surnames_Voronezh[randint(0,7)]+"а"+" "+popular_fnames_Voronezh[randint(0,9)])
    
tamandua_name="Ушастая Булка"

average_mark=0
for i in subjects.values():
    average_mark+=i
print("\nСредняя оценка в аттестате:",average_mark/len(subjects))

unique_names=[]
for i in popular_combos:
    unique_names.append(i.split()[1])
print("\nУникальные имена:",set(unique_names))

length_of_subjects=0
for i in subjects.keys():
    length_of_subjects+=len(i)
print("\nОбщая длина всех названий предметов:",length_of_subjects)

unique_simbols=[]
for i in subjects.keys():
    for j in range(len(i)):
        unique_simbols.append(i[j])
unique_simbols.remove(" ")
unique_simbols.remove("-")
unique_simbols.remove("3")
print("\nУникальные буквы в названиях предметов:",set(unique_simbols))

bin_tamandua=""
bin_tamandua = ''.join(format(ord(x), '08b') for x in tamandua_name)
print("\nИмя домашнего тамандуа в бинарном виде:",bin_tamandua)

current_date = datetime.datetime.now()
print(str(current_date)[:10])
