import random
import time
from dateutil.parser import parse

# ДАННЫЕ С КОТОРЫМИ РАБОТАЮ

# Словарь, составленный из оценок предметов в аттестате

certificate = {'русский язык' : 4,         
     'литература' : 4,
     'английский' : 5,
     'немецкий' : 5,
     'алгебра' : 5,
     'геометрия' : 5,
     'информатика' : 5,
     'история' : 5,
     'обществознание' : 5,
     'география' : 5,
     'физика' : 5,
     'химия' : 4,
     'биолоия' : 5,
     'музыка' : 5,
     'изо' : 4,
     'технология' : 5,
     'обж' : 5,
     'физкультура' : 5
     }

#print(certificate)

# Полное имя, фамилия и дата рождения актера из вестерна 1960х годов как кортеж
actor = ('Клинтон',' Иствуд','31.05.1930')

#print(actor)

# составление списка из имени и фамилии, по таблице самых популярных

popular_name_man = ['Александр',
                    'Иван',
                    'Сергей',
                    'Дмитрий',
                    'Алексей',
                    'Андрей',
                    'Максим',
                    'Евгений',
                    'Михаил',
                    'Владимир'
                    ]

popular_surname_man = ['Иванов',
                       'Смирнов',
                       'Петров',
                       'Кузнецов',
                       'Волков',
                       'Соколов',
                       'Белов',
                       'Морозов'
                       ]

popular_name_woman = ['Елена',
                      'Екатерина',
                      'Наталья',
                      'Мария',
                      'Ольга',
                      'Светлана',
                      'Татьяна',
                      'Ирина',
                      'Юлия',
                      'Анастасия'
                      ]

popular_surname_woman = ['Иванова',
                         'Смирнова',
                         'Кузнецова',
                         'Петрова',
                         'Волкова',
                         'Морозова',
                         'Соколова',
                         'Романова'                        
                         ]

person_data = []

#person_data.append('Мужчины: ')
for i in range(0,len(popular_name_man)):
    random_name_man = random.choice(popular_name_man)
    random_surname_man = random.choice(popular_surname_man)
    person_data.append(random_name_man)
    person_data.append(random_surname_man)

#person_data.append('Женщины: ')
for i in range(0,len(popular_name_man)):
    random_name_woman = random.choice(popular_name_woman)
    random_surname_woman = random.choice(popular_surname_woman)
    person_data.append(random_name_woman)
    person_data.append(random_surname_woman)

#print(person_data)

#Имя из прилагательного и существительного для домашнего тамандуа

name_pet = 'fastidious furry'

# 1-9 ЗАДАНИЯ

# 1 задание
print('TASK №1 \n\n')
Sum = 0
for i in certificate.keys():
    Sum +=certificate[i]
    
average = Sum/len(certificate)

print('Вывод среднего значения: ',average,'\n')

# 2 задание 
print('TASK №2 \n\n')
for i in range(1,len(person_data)+1):
        try:
            person_data.pop(i)
        except IndexError:
            pass
        
unique_person_data = set(person_data)

print('выделение уникальных имен среди взятых из таблиц популярных: ', unique_person_data,'\n')


# 3 задание
print('TASK №3 \n\n')
certificate_list = list(certificate)
count = 0
for i in range(len(certificate_list)):
    for j in range(len(certificate_list[i])):
        count += 1
    
print('Общая длина всех названных предметов: ',count - 1,'\n') # русский язык через пробел написан


# 4 задание
print('TASK №4 \n\n')
certificate_list = list(certificate)
unique_letters = []
for i in range(len(certificate_list)):
    for j in certificate_list[i]:
        unique_letters.append(j)
unique_letters = set(unique_letters)
        
print('Уникальные буквы в названиях предметов: ', unique_letters,'\n')

# 5 задание
print('TASK №5 \n\n')
bin_name_pet = []
for i in name_pet:
    j = format(ord(i),'08b')
    bin_name_pet.append(j)
    
str_bin_name_pet = ''

for el in bin_name_pet:
    str_bin_name_pet += str(el)

print('имя моего домашнего тамандуа в бинарном виде: ', str_bin_name_pet,'\n')

# 6 задание
print('TASK №6 \n\n')
#print(time.asctime())

T = tuple(time.asctime())
T2 = T[4] + T[5] + T[6]
T1 = T[8] + T[9]
T3 = T[20] + T[21] + T[22] + T[23]
if T2 == 'Dec': 
    T2 = '12'
elif T2 == 'Jan':
    T2 = '01'
elif T2 == 'Feb':
    T2 = '02'
elif T2 == 'Mar':
    T2 = '03'
elif T2 == 'Apr':
    T2 = '04'
elif T2 == 'May':
    T2 = '05'
elif T2 == 'Jun':
    T2 = '06'
elif T2 == 'Jul':
    T2 = '07'
elif T2 == 'Aug':
    T2 = '08'
elif T2 == 'Sep':
    T2 = '09'
elif T2 == 'Oct':
    T2 = '10'
elif T2 == 'Nov':
    T2 = '11'
    
s_T = T1 +'.'+ T2 + '.' + T3

date1 = parse(actor[2])
date2 = parse(s_T)

num_days = (date2-date1).days

print('количество дней от даты рождения вестерна актера до текущей даты: ', num_days, '\n')


# 7 задание
print('TASK №7 \n\n')

material_list = []
while True:
    material_name = input("Введите название строительного материала (или введите 'стоп' для завершения): ")
    print('\n')
    if material_name.lower() == 'стоп':
        break
    material_index = input("Введите индекс строки из таблицы: ")
    print('\n')
    material_list.append((material_index, material_name))


material_list.sort()

#material_list.sort(key = lambda i: i[0]) # можно через лямбда-функцию: сортировка по ключам с нулевого элемента

print("\nНазвания строительных материалов в порядке добавления по индексам: ")

for index, name in material_list:
    print(f"Индекс {index}: {name}")

print('\n')

# 8 задание
print('TASK №8 \n\n')
us_s = tuple(actor[2])
var1 = ''
var2 = ''
var3 = ''
var1 = us_s[0] + us_s[1]

var2 =us_s[3] + us_s[4]

var3 = us_s[6] + us_s[7] + us_s[8] + us_s[9]

number = (int(var1) + int(var2)**2 + int(var3))%39 + 1
#print(number)

replace_name = 'Чжоу Шэнь Цзинь-ван'

count = 0
unique_person_data_list = list(unique_person_data)

while True:
    for i in range(len(unique_person_data_list)):
        if count == number:
            unique_person_data_list[i] = replace_name
            break
        count+=1
        if i == len(unique_person_data_list) - 1:
            i = 0
    if count >= number:
        break

print("Список уникальных имён с заменённым элементом: ")     
print(unique_person_data_list, '\n')   


# 9 задание
print('TASK №9 \n\n')

linked_list = []
linked_list.append("USA")
linked_list.append("Canada")
linked_list.append("Germany")
linked_list.append("France")

count_number = list(range(len(linked_list)))

new_linked_list = []

num_del = int(input('Введите индекс элемента, который нужно удалить: '))

for i in range(len(linked_list)):
    if i == num_del:
        continue
    new_linked_list.append(linked_list[i])

print('Связанный список с удаленным элементом: ', new_linked_list, '\n')


city_to_insert = 'Нижний новгород'

print('Первая вставка\n')
num_in = int(input('Укажите индекс списка в который нужно вставить город: '))

new_linked_list.insert(num_in,city_to_insert)

print('Связанный список с вставленным городом по вводимому индексу: ', new_linked_list, '\n')

# или нужно так (?)
new_linked_list = linked_list 
print('Вторая вставка\n')
num_in = int(input('Укажите индекс списка в который нужно вставить город: '))

new_linked_list.insert(num_in,city_to_insert)

print('Связанный список с вставленным городом по вводимому индексу: ', new_linked_list, '\n')
