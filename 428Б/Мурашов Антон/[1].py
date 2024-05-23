import random
from datetime import date
from queue import Queue
from collections import deque

#Исходные данные

#Предметы в школьном аттестате (не меньше 14), как словарь (dictionary) из названия и оценки

marks = {"Русский язык": 3, 
         "Английский язык": 3,
         "Физкультура": 5,
         "ОБЖ": 5,
         "Физика": 3,
         "Информатика": 5,
         "Алгебра": 5,
         "Геометрия": 5,
         "Химия": 4,
         "Биология": 4,
         "История": 5,
         "Обществознание": 4,
         "География": 5,
         "Литература": 4}

total_length_subjects=""

#Полное имя с фамилией и дата рождения любого актера из вестерна 1960х годов как кортеж (tuple)

western_actor = ("Аль", "Пачино", "25.04.1940")

#Cписок (list) из имени и фамилии, составленные случайно по таблице из самых популярных (с сайта http://topnamesinrussia.tilda.ws), свой город взять по номеру равному дню месяца вашего рождения
#Уфа

names_men=["Иван",
       "Александр",
       "Сергей",
       "Андрей",
       "Дмитрий",
       "Алексей",
       "Максим",
       "Владимир",
       "Евгений",
       "Денис"]

surnames_men=["Иванов",
          "Петров",
          "Ростовский",
          "Попов",
          "Смирнов",
          "Сергеев",
          "Волков",
          "Романов"]

names_women=["Екатерина",
             "Елена",
             "Мария",
             "Анна",
             "Анастасия",
             "Ольга",
             "Наталья",
             "Ирина",
             "Татьяна",
             "Светлана"]

surnames_women=["Иванова",
                "Петрова",
                "Попова",
                "Смирнова",
                "Морозова",
                "Романова",
                "Волкова",
                "Кузнецова"]

def full_names_creation(names, surnames, full_names):
    for i in range (len(names)-1):
        name_index=random.randint(0,len(names)-1)
        surname_index=random.randint(0,len(surnames)-1)
        full_name=[]
        full_name.append(names[name_index])
        full_name.append(surnames[surname_index])
        full_names.append(full_name)
    return full_names

        
def full_names_merge():
    global names_men,surnames_men, names_women,surnames_women
    full_names_men=[]
    full_names_women=[]

    full_names_creation(names_men,surnames_men,full_names_men)
    full_names_creation(names_women,surnames_women,full_names_women)

    full_names=full_names_men+full_names_women
    
    return full_names

full_names=full_names_merge()
#print(f"Мужчины: \n {full_names_men}, \n Женщины:\n {full_names_women}")

#print(full_names)

#Имя из прилагательного и существительного, которое вы бы дали своему домашнему тамандуа (строка)

tamandua="jouken son"

#Действия

#1. Вывести среднюю оценку в аттестате

def task_1(marks):
    
    summ=0

    for mark in marks:
        summ+=marks[mark]
        
    return round(summ/len(marks), 3)

#2. Вывести уникальные имена среди взятых из таблицы популярных

def task_2(full_names):

    unique_names_list=[]

    for full_name in full_names:
        if full_name[0] not in unique_names_list:
            unique_names_list.append(full_name[0])
    
    return unique_names_list


"""

# ИЛИ

unique_names_list_1=[]

for i in range(n):
    unique_names_list_1.append(full_names[i][0])

unique_full_names=set(unique_names_list_1)

print(f"\nУникальные имена среди взятых из таблицы популярных: {unique_full_names}")

"""

#3. Общая длина всех названий предметов

def task_3(marks):
    global total_length_subjects
    for mark in marks:
        total_length_subjects+=mark
    
    return len(total_length_subjects)

#4. Уникальные буквы в названиях предметов

def task_4(total_length_subjects):
    
    total_length_subjects=total_length_subjects.replace(' ', '')
    total_length_subjects=total_length_subjects.lower()

    unique_letters=[]

    for letter in total_length_subjects:
        if letter not in unique_letters:
            unique_letters.append(letter)
    
    unique_letters.sort()
        
    return unique_letters

"""#или

unique_letters_1=set(total_length_subjects)

unique_letters_1=list(unique_letters_1)

unique_letters_1.sort()

print(f"\nУникальные буквы в названиях предметов:\n\n{unique_letters_1}")"""

#5. Имя вашего домашнего тамандуа в бинарном виде

def task_5(tamandua):
    
    bin_tamandua=""

    for letter in tamandua:
        bin_tamandua+=" " + (bin(ord(letter))[2:])
    
    bin_tamandua = bin_tamandua.lstrip()
    
    return bin_tamandua

"""#reverse

n=len(bin_tamandua)

reverse_tamandua=""
bin_letter=""

for digit in bin_tamandua:
    if digit==" ":
        letter=int(bin_letter,2)
        reverse_tamandua+=(chr(letter))
        bin_letter=""
    else: 
        bin_letter+=digit
        
letter=int(bin_letter,2)
reverse_tamandua+=(chr(letter))
    
print(reverse_tamandua) """

#6. Количество дней от даты рождения актера вестерна до текущей даты (должна быть всегда актуальной)

#western_actor = ("Джон", "Уэйн", "26.05.1907")


def task_6(western_actor):
    
    i=0

    days=""
    
    today=date.today()

    western_actor_birth_date=western_actor[2]

    """
    day=int(western_actor_birth_date[:2])

    month=int(western_actor_birth_date[3:5])

    year=int(western_actor_birth_date[6:])

    western_actor_birth_date=date(year,month,day) 

    """

    western_actor_birth_date = western_actor_birth_date.split(".")

    western_actor_birth_date=date(int(western_actor_birth_date[2]),int(western_actor_birth_date[1]),int(western_actor_birth_date[0])) 

    delta = str(today-western_actor_birth_date)

    while delta[i].isdigit():
        days+=delta[i]
        i+=1
        
    return days

"""#или

today=str(date.today())

today = today.split("-")

western_actor_birth_date=western_actor[2]

western_actor_birth_date = western_actor_birth_date.split(".")

print(western_actor_birth_date)

days=(int(today[0])*365+int(today[1])*30+int(today[2]))-(int(western_actor_birth_date[2])*365+int(western_actor_birth_date[1])*30+int(western_actor_birth_date[0]))

print(days)"""


#7. FIFO очередь

def task_7():
    
    materials = []

    material = input("\nВведите название стройматериала или введите \"СТОП\", чтобы прекратить ввод: ")

    while material.upper() != "СТОП":
        materials.append(material)
        material = input("\nВведите название стройматериала или введите \"СТОП\", чтобы прекратить ввод: ")

    if len(materials)==0:
        print("\nСтройматериалы отсутствуют")

    else: 
        print("\nНазвания стройматериалов в порядке очереди: \n")

        for material in materials:
            print(f"{material}")  
    
"""while len(materials)!=0:
    print(materials.pop(0))"""
    
"""#или

materials = Queue()

material = input("\nВведите название стройматериала или введите \"СТОП\", чтобы прекратить ввод: ")

while material.upper() != "СТОП":
    materials.put(material)
    material = input("\nВведите название стройматериала или введите \"СТОП\", чтобы прекратить ввод: ")

print("\nНазвания стройматериалов в порядке очереди: \n")

while materials.empty()!=True:
    print(materials.get()) """

#8. По введеному с клавиатуры индексу, поменять имя в отсортированном списке популярных имен и фамилий на имя, 
#под которым наиболее известен, китайский император династии Чжоу

def task_8(western_actor, full_names):
    
    western_actor_birth_date=western_actor[2]

    western_actor_birth_date = western_actor_birth_date.split(".")

    day = int(western_actor_birth_date[0])
    month = int(western_actor_birth_date[1])
    year = int(western_actor_birth_date[2])

    magic_number = (day+month**2+year)%39+1
    
    print(f"\nНомер китайского императора: {magic_number}")
    
    imperor_name = "Цзи Гуншэн"

    full_names=full_names_merge()
    full_names.sort()
    print(f"\nОтсортированный список популярных имен и фамилий:\n\n{full_names}")

    index = int(input(f"\nВведите индекс n, 0 <= n < {len(full_names)}: "))

    full_names[index][0]=imperor_name

    print(f"\nСписок популярных имен и фамилий с именем императора вместо обычного имени под индексом {index}:\n\n{full_names}") 

#9. Создать и напечатать связный список странных названий населенных пунктов любым способом

def cities_output(city, linked_strange_cities):
    for city in linked_strange_cities:
        print(city)

def task_9():
    
    linked_strange_cities=deque()

    strange_cities = ["Засосная", 
                      "Свиновье", 
                      "Жабино", 
                      "Лысая Балда", 
                      "Ширяево", 
                      "Муходоево", 
                      "Добрые Пчелы", 
                      "Цаца", 
                      "Большое Струйкино", 
                      "Дешевки"]

    for city in strange_cities:
        linked_strange_cities.append(city)
    
    print("\nСтранные названия населенных пунктов:\n")
    
    cities_output(city, linked_strange_cities)

    city_to_delete = input("\nВведите название населенного пункта, который хотите удалить: ")

    if city_to_delete in linked_strange_cities:
        linked_strange_cities.remove(city_to_delete)
    
    print("\nСтранные названия населенных пунктов без одного:\n")

    cities_output(city, linked_strange_cities)

    konec_city="Конец"

    index_to_insert=int(input(f"\nВведите индекс, куда вы хотите вставить город {konec_city}: "))

    linked_strange_cities.insert(index_to_insert, konec_city)

    print(f"\nСтранные названия населенных пунктов с городом {konec_city}:\n")

    cities_output(city, linked_strange_cities)

#Выполнение кода

def tasks_show(task_number):
    
        match (task_number):
            case '1':
                print ("\nЗадание 1\n")
                print(f"Средняя оценка в аттестате: {task_1(marks)}")
            case '2':
                print ("\nЗадание 2\n")
                print(f"Уникальные имена среди взятых из таблицы популярных:\n\n{task_2(full_names)}")
            case '3':
                print ("\nЗадание 3\n")
                print(f"Общая длина всех названий предметов: {task_3(marks)}")
            case '4':
                print ("\nЗадание 4\n")
                print(f"Уникальные буквы в названиях предметов:\n\n{task_4(total_length_subjects)}")
            case '5':
                print ("\nЗадание 5\n")
                print(f"Имя домашнего тамандуа в бинарном виде:\n\n{task_5(tamandua)}")
            case '6':
                print ("\nЗадание 6\n")
                print(f"Количество дней от даты рождения актера вестерна до текущей даты: {task_6(western_actor)}")
            case '7':
                print ("\nЗадание 7")
                task_7()
            case '8':
                print ("\nЗадание 8")
                task_8(western_actor, full_names) 
            case '9':
                print ("\nЗадание 9")
                task_9()
            case _:
                print("Такого задания не существует")
        
task_number = input("\nВведите номер задания, которое хотите проверить, или \"СТОП\" для прекращения проверки: ")

while task_number.upper()!="СТОП":
    tasks_show(task_number)
    task_number = input("\nВведите номер задания, которое хотите проверить, или \"СТОП\" для прекращения проверки: ")

print("\nСпасибо за то, что проверили мои задания! Надеюсь, я справился 👉👈 ")