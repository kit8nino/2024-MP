import random
import queue
from datetime import datetime

# данные
 
# предметы в школьном аттестате, как словарь

attestat = {'русский язык' : 5,         
     'немецкий' : 4,
     'французский' : 3,
     'математика' : 3,
     'география' : 5,
     'астрономия' : 3,
     'физика' : 3,
     'технология' : 4,
     'обж' : 5,
     'история родного края' : 3,
     'обществознание' : 5,
     'информатика' : 4,
     'геоиетрия' : 3,
     'физическая культура' : 5}

# полное имя с фамилией и дата рождения актера из вестерна 1960х годов как кортеж 
actor = ('Юл','Бриннер','11.07.1920')

# списки из имени и фамилии, по таблице самых популярных

name_man = ['Денис',
            'Дмитрий',
            'Илья',
            'Алексей',
            'Виталий',
            'Кирилл',
            'Иван',
            'Артем',
            'Евгений',
            'Максим'
            ]

surname_man = ['Петров',
               'Дмитриев',
               'Смирнов',
               'Алексеев',
               'Попов',
               'Кузнецов',
               'Сидоров',
               'Васильев'
               ]

name_woman = ['Алина',
              'Елизавета',
              'Мария',
              'Юлия',
              'Алена',
              'Наталья',
              'Дарья',
              'Татьяна',
              'Ирина',
              'Александра'
              ]

surname_woman = ['Романова',
                 'Ваганова',
                 'Куприна',
                 'Корепанова',
                 'Смирнова',
                 'Николаева',
                 'Иванова',
                 'Сидорова'                        
                 ]

spisok = []

for i in range(0,len(name_man)):
    random_name_man = random.choice(name_man)
    random_surname_man = random.choice(surname_man)
    spisok.append(random_name_man)
    spisok.append(random_surname_man)
    
for i in range(0,len(name_woman)):
    random_name_woman = random.choice(name_woman)
    random_surname_woman = random.choice(surname_woman)
    spisok.append(random_name_woman)
    spisok.append(random_surname_woman)
    
#print(spisok)
    
#Имя домашнего таманда

name_pet = 'Оловянный солдатик'



#ЗАДАНИЕ 1
print('ЗАДАНИЕ 1')
average_grade = sum(attestat.values()) / len(attestat)
print(f"Средняя оценка аттестата: {average_grade}")



#ЗАДАНИЕ 2
print('ЗАДАНИЕ 2')
for i in range(1,len(spisok)+1):
        try:
            spisok.pop(i)
        except IndexError:
            pass
unika = set(spisok)

print("Имена уникальные:", unika)




#ЗАДАНИЕ 3
print('ЗАДАНИЕ 3')
attestat_list = list(attestat)
count = 0
for i in range(len(attestat_list)):
    for j in range(len(attestat_list[i])):
        count += 1
print("Общая длина всех предметов: ",count - 1,"\n")




#ЗАДАНИЕ 4
print('ЗАДАНИЕ 4')
unique_letters = set(''.join(attestat.keys()))
print("Уникальные буквы в названиях:", unique_letters)



#ЗАДАНИЕ 5
print('ЗАДАНИЕ 5')
binary_name_pet = ''.join(format(x,'08b') for x in bytearray(name_pet,'utf-8')) 
print("Имя 'Оловянный солдатик' в бинарном виде:", binary_name_pet )



#ЗАДАНИЕ 6
print('ЗАДАНИЕ 6')
# Исходные данные
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()

# Рассчитаем количество дней
days_since_birth = (current_date - birth_date).days

print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} до текущей даты: {days_since_birth} дней")



#ЗАДАНИЕ 7
print('ЗАДАНИЕ 7')

# Создаем FIFO очередь
materials_queue = queue.Queue()

# Заполняем очередь с клавиатуры
print("Введите названия стройматериалов (для завершения введите 'стоп'):")
while True:
    material = input()
    if material.lower() == 'стоп':
        break
    materials_queue.put(material)

# Выводим все элементы очереди
print("Все названия стройматериалов:")
while not materials_queue.empty():
    print(materials_queue.get())


#ЗАДАНИЕ 8
print('ЗАДАНИЕ 8')
#сортировка списка 
s = sorted(unika)
print(s)
imperator = 'Си-ван'

# Вычисление номера китайского императора
number = (11 + 7**2 + 1920) % 39 + 1
#print(number)

index = input("Введите индекс")

try:
    index = int(index)
    
except ValueError:
    print("Неверный индекс")
    
if index >= 0 and index < len(s):
    s[index] = imperator
    
print("Новый список:", s)




#ЗАДАНИЕ 9
print('ЗАДАНИЕ 9')

names = ["Лохово", 
         "Алгаши", 
         "Вобля", 
         "Дно",
         "Муходоево", 
         "Хреновое", 
         "Голодранкино", 
         "Мусорка"]
new_names = []
print (names)

num_del = int(input('Индекс элемента, который надо удалить: '))

for i in range(len(names)):
    if i == num_del:
        continue
    new_names.append(names[i])

print('Список с удаленным элементом: ', new_names)

city = 'Конец'

num_in = int(input('Индекс списка в который надо вставить город: '))

new_names.insert(num_in,city)

print('Конечный список:', new_names)
