import queue
import random
from datetime import datetime

atestat={'астраномия':5,
         'алгебра':3,
         'литература':5,
         'мгеометрия':4,
         'биология':4,
         'история':5,
         'физика':5,
         'английский язык':4,
         'физкультура':5,
         'ОБЖ':5,
         'обществознание':5,
         'информатика':4,
         'русский язык': 4,
         'химия':3}

actor = ('Джим','Дэвис','28.07.1945')

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
tamandua='Быстрый муравьед'



#задание 1
print('Задание 1')
average_grade = sum(atestat.values()) / len(atestat)
print(f"Средний балл в атестате: {average_grade}")



#задание 2
print('Задание 2')
def task2(men):
    unique_men=[]
    for i in range(len(men)):
        person=[]
        person.append(men[i][0])
        person.append(men[i][1])
        if person not in unique_men:
            unique_men.append(person)
    return unique_men
print(f"Уникальный список имен: {task2(men)}\n")



#задание 3
print('Задание 3')
def task3(atestat):
    count=0
    for i in atestat.keys():
        for j in i:
            if j!=' ':
                count+=1
    return count
print(f" Общая длина всех названий предметов: {task3(atestat)}\n") 



#задание 4
print('Задание 4')
def task4(atestat):
    unique_letters=[]
    for i in atestat.keys():
        i=i.lower()
        for j in i:
            if j not in unique_letters and j!=' ': unique_letters.append(j)
    return unique_letters
print(f"Уникальные буквы в названиях предметов: {task4(atestat)}\n")



#задание 5
print('Задание 5')
def task5(tamandua):
    str=''
    for i in tamandua:
        if i!=' ':
            bin=(format(ord(i),'08b'))
            str+=(bin)
    return str
print(f"Имя тамандуа в бинарном виде: {task5(tamandua)}\n")


#задание 6
print('Задание 6')
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()
days_since_birth = (current_date - birth_date).days

print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} до текущей даты: {days_since_birth} дней")


#задание 7
print('Задание 7')
material_list = []

while True:
    material_name = input("Введите название строительного материала ('стоп' для завершения): ")
    if material_name.lower() == 'стоп':
        break
    material_list.append(material_name)

print("Список материалов:")
for material in material_list:
    print(material)

#задание 8
print('Задание 8')
unika = men_names + women_names
s = sorted(unika)
print(s)
number = (28 + 7**2 + 1945) % 39 + 1
imperator = 'Чэн-ван'

index = input("Введите индекс")

try:
    index = int(index)
    
except ValueError:
    print("Неверный индекс")
    
if index >= 0 and index < len(s):
    s[index] = imperator
    
print("Новый список:", s)

#задание 9
print('Задание 9')
names = ["Крутые Хутора", 
         "Мусорка", 
         "Добрые Пчелы", 
         "Синегубово",
         "Лохово", 
         "Хреновое", 
         "Свиновье", 
         "Такое"]
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

