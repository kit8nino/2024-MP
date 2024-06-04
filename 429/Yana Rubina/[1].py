import random
import queue
from datetime import datetime

# данные
 
# предметы в школьном аттестате

attestat = {'русский язык' : 5,         
     'литература' : 5,
     'история' : 5,
     'алгебра' : 5,
     'геометрия' : 5,
     'информатика' : 5,
     'физика' : 5,
     'химия' : 5,
     'биолоия' : 5,
     'английсикй язык' : 5,
     'география' : 5,
     'обж' : 5,
     'обществознание' : 5,
     'физкультура' : 5,
     'астрономия' : 5}

# полное имя с фамилией и дата рождения актера из вестерна 1960х годов как кортеж 
actor = ('Юл','Бриннер','11.07.1920')

# списки из имени и фамилии

name_woman = ['Мария',
              'Елена',
              'Екатерина',
              'Анна',
              'Наталья',
              'Ольга',
              'Ирина',
              'Татьяна',
              'Анастасия',
              'Светлана'
              ]

surname_woman = ['Иванова',
                 'Петрова',
                 'Попова',
                 'Смирнова',
                 'Романова',
                 'Морозова',
                 'Волкова',
                 'Кузнецова'                        
                 ]

spisok = []

for i in range(0,len(name_woman)):
    random_name_woman = random.choice(name_woman)
    random_surname_woman = random.choice(surname_woman)
    spisok.append(random_name_woman)
    spisok.append(random_surname_woman)
    
#print(spisok)
    
#Имя домашнего тамандуа

name_pet = 'Неуклюжая лапка'



#ЗАДАНИЕ 1
average_grade = sum(attestat.values()) / len(attestat)
print(f"ЗАДАНИЕ 1: Средняя оценка в аттестате: {average_grade}")



#ЗАДАНИЕ 2
for i in range(1,len(spisok)+1):
        try:
            spisok.pop(i)
        except IndexError:
            pass
unika = set(spisok)

print("ЗАДАНИЕ 2: Уникальные имена:", unika)




#ЗАДАНИЕ 3
attestat_list = list(attestat)
count = 0
for i in range(len(attestat_list)):
    for j in range(len(attestat_list[i])):
        count += 1
print("ЗАДАНИЕ 3: Общая длина всех названных предметов: ",count - 1,"\n")




#ЗАДАНИЕ 4
unique_letters = set(''.join(attestat.keys()))
print("ЗАДАНИЕ 4: Уникальные буквы в названиях предметов:", unique_letters)



#ЗАДАНИЕ 5
binary_name_pet = ''.join(format(x,'08b') for x in bytearray(name_pet,'utf-8')) 
print("ЗАДАНИЕ 5: Имя 'Неуклюжая лапка' в бинарном виде:", binary_name_pet )



#ЗАДАНИЕ 6
# Исходные данные
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()

# Рассчитываем количество дней
days_since_birth = (current_date - birth_date).days

print(f"ЗАДАНИЕ 6: Количество дней от даты рождения актера {actor[0]} {actor[1]}а до текущей даты: {days_since_birth} дней")



#ЗАДАНИЕ 7
# Создаем FIFO очередь
materials_queue = queue.Queue()

# Заполняем очередь с клавиатуры
print("ЗАДАНИЕ 7: Введите названия стройматериалов (для завершения введите 'хватит'):")
while True:
    material = input()
    if material.lower() == 'хватит':
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
imperator = 'Сянь-ван'

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
names = ["Скрив", 
         "Бентук", 
         "Венберг", 
         "Исмит",
         "Нирт", 
         "Гальт", 
         "Кварбут", 
         "Аскиф"]
new_names = []
print (names)

num_del = int(input('Индекс элемента, который нужно удалить: '))

for i in range(len(names)):
    if i == num_del:
        continue
    new_names.append(names[i])

print('Список с удаленным элементом: ', new_names)

city = 'Конец'

num_in = int(input('Индекс списка в который нужно вставить город: '))

new_names.insert(num_in,city)

print('Конечный список:', new_names)