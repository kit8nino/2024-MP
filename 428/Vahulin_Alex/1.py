from random import randint
import datetime

# Входные данные
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

western_actor_birthday=datetime.datetime(1925,1,9)
western_actor=tuple(["Lee Van Cleef",western_actor_birthday.day, western_actor_birthday.month, western_actor_birthday.year])

popular_fnames_Voronezh=["Елена","Екатерина","Ольга","Мария","Анастасия","Ирина","Наталья","Татьяна","Юлия","Светлана"]
popular_mnames_Voronezh=["Иван","Александр","Сергей","Дмитрий","Андрей","Алексей","Максим","Евгений","Владимир","Роман"]
popular_surnames_Voronezh=["Иванов","Попов","Петров","Кузнецов","Сергеев","Смирнов","Новиков","Васильев"]

popular_combos=[]

for i in range(15):
    popular_combos.append(popular_surnames_Voronezh[randint(0,7)]+" "+popular_mnames_Voronezh[randint(0,9)])
    
for i in range(15):
    popular_combos.append(popular_surnames_Voronezh[randint(0,7)]+"а"+" "+popular_fnames_Voronezh[randint(0,9)])
    
tamandua_name="Ушастая Булка"

# Действия с данными
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

difference_in_days = (datetime.datetime.now()-western_actor_birthday).days
print("\nЧисло дней с момента рождения актёра вестерна до текущей даты:", difference_in_days)

building_materials=[]
print("\nВведите наименование стройматериалов(q для вывода):")
k=1
while True:
    data=input("№{}:".format(k))
    if data=="q":
        for i in building_materials:
            print(i)
        break
    else:
        k+=1
        building_materials.append(data)

popular_combos.sort()
emperor_number=(western_actor[1]+western_actor[2]**2+western_actor[3])%39+1
emperor_name="Чжоу Цзин-ван Гуй"
name_index=int(input("\nВведите индекс элемента для замены (от 0 до 19):"))
popular_combos[name_index]=emperor_name
print(popular_combos)

strange_settlement_names={
    "Большой Куяш": 1,
    "Иннах": 2,
    "Да-да": 3,
    "Чуваки": 4,
    "Дно": 5,
    }
print("\nСписок странных названий населённых пунктов:", strange_settlement_names)
while True:
    text_entry=input("\nВведите название из списка для удаления либо индекс (от 0 до 4), по которому в список будет вставлен город Конец (q для выхода):")
    if text_entry=='q':
        break
    elif text_entry.isdigit():
        strange_settlement_names['Конец']=int(text_entry)+1
        for i in strange_settlement_names:
            if strange_settlement_names[i] > int(text_entry) and i!="Конец":
                strange_settlement_names[i]+=1
        print("\nСписок странных названий населённых пунктов с Концом:", strange_settlement_names)
        break
    elif not text_entry in strange_settlement_names.keys():
        print("\nНет такого города")
    else:
        for k,v in strange_settlement_names.items():
            if v==strange_settlement_names[text_entry]-1:
                strange_settlement_names[k]+=1
        del strange_settlement_names[text_entry]
        print("\nСтранный населённый пункт {} удалён".format(text_entry))
        print("\nСписок странных названий населённых пунктов без {}:\n{}".format(text_entry,strange_settlement_names))
        break
