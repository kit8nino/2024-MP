import random
from datetime import datetime
import queue

diplom = {  
"math": 4,  "russian": 5,  "literature": 4,  "rodnayaliterature": 4,   "physics": 4,  "history": 5,  "biology": 5,  "geography": 5,  "technicaldrawing": 4,   "chemistry": 3,  
"technology": 4,  "music": 4,  "art": 3,   "obg": 5,  "religions": 4,   "sociology": 4, "informatika": 5
}

#1
medium = 0
strLen = 0
for subject in diplom:
    medium += diplom[subject]
    strLen += len(subject)
medium = medium / len(diplom)
print("1: " + str(medium))

#2 bithday 20 -> Ekaterinburg
names = ["Ivan", "Alexandr","Sergey","Andrey","Dmitrii","Aleksey","Maxim","Evgeniy","Anton","Vladimir"]
surnames = ["Ivanov", "Petrov", "Smirnov","Kuznethov","Sergeev", "Popov", "Volkov", "Vasilev"]
people = []
for _ in range(30):
    name = random.choice(names)
    surname = random.choice(surnames)
    people.append(name + surname)

def NamSur():
    unique_names = {}
    for full_name in people:
        unique_names[full_name] = True
    unique_names = list(unique_names.keys())
    for name in unique_names:
        print(name)
print("\n2: " ) 
print( NamSur())

#3
print("\n3: " + str(strLen))

#4
unique_letters = set(''.join(diplom.keys()))
print("\n4: ")
print(unique_letters)

#5
tamand_name = "Зевс"
bin_tamand_name = ''
for symb in tamand_name:
        bin_tamand_name +=(format(ord(symb), '08b'))
print("\n5: " + bin_tamand_name)

#6
actor = ('Клинт','Иствуд','31.05.1930')
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()
days_since_birth = (current_date - birth_date).days
print("\n6: ", end='')
print(days_since_birth)

#7
materials = []
print("\n7: ")
print("Для завершения записи материалов напишите <<Stop>>")
while True:
    material = input("Введите название материала:")
    if (material == "Stop"):
        print("Ваши материалы:")
        for i in range(0,len(materials)):
            print(materials[i])
        break
    else:
        materials.append(material)
        
#8
index = input("\n8: введите индекс:")
# номер императора = 36
imperator = "Цзи Бянь"
names[int(index) - 1] = imperator
print( str(names) + "\n")

#9
goroda = ['Муходоево', 'Ширяево', 'Старые Черви', 'Да-да','Ломки', 'Хотелово', 'Добрые Пчелы', 'Блювиничи']
new_goroda = []
print (goroda,"\n")
num_del = int(input('Индекс элемента, который нужно удалить: '))
for i in range(len(goroda)):
    if i == num_del:
        continue
    new_goroda.append(goroda[i])
print('Список с удаленным элементом: ', new_goroda,"\n")
Konec = 'Конец'
gorod_index = int(input('Индекс списка в который нужно вставить город: '))
new_goroda.insert(gorod_index,Konec)
print('Новый список:', new_goroda)