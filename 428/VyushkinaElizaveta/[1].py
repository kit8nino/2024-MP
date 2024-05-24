import numpy as np
import datetime
import random
atestat={'Русский язык':5,
         'Химия':5,
         'Литература':5,
         'Геометрия':5,
         'Алгебра':5,
         'Биология':4,
         'История':4,
         'Физика':5,
         'Английский язык':5,
         'Физкультура':5,
         'ОБЖ':5,
         'Обществознание':5,
         'Информатика':5,
         'Технолигия': 4,
         'Экономика':5}
actor_birthday=datetime.datetime(1908,5,20,0,0,0)
actor=("Джеймс","Стюарт",(actor_birthday.day,actor_birthday.month,actor_birthday.year))
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

women_names=['Мария',
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
    
tamandua='Пушистик'


#1) Средняя оцнка в аттестате

def task1(atestat):
    subjects=set()
    for i in (atestat):
         subjects.add(i)
    sum=0
    for i in subjects:
        x=atestat.get(i)
        sum+=x
    b=float(sum)/len(atestat)
    return b

#2) Уникальные имена среди взятых из таблицы популярных

def task2(men):
    unique_men=[]
    for i in range(len(men)):
        person=[]
        person.append(men[i][0])
        person.append(men[i][1])
        if person not in unique_men:
            unique_men.append(person)
    return unique_men

#3) Общая длина всех названий предметов

def task3(atestat):
    count=0
    for i in atestat.keys():
        for j in i:
            if j!=' ':
                count+=1
    return count

#4) Уникальны буквы в назыании предмета

def task4(atestat):
    unique_letters=[]
    for i in atestat.keys():
        i=i.lower()
        for j in i:
            if j not in unique_letters and j!=' ': unique_letters.append(j)
    return unique_letters


#5) Имя тамандуа в бинарном виде

def task5(tamandua):
    str=''
    for i in tamandua:
        if i!=' ':
            bin=(format(ord(i),'08b'))
            str+=(bin)
    return str

#6) Количество дней от даты рождения актера до текущей даты (должна быть всегда актуальной)

def task6(actor_birthday):
    actual_date=datetime.datetime.now()
    time_difference=(actual_date-actor_birthday).days
    return time_difference
    
#7) FIFO очередь, в которую можно добавлять строковые названия стройматериалов

def task7():
    import queue
    materials=queue.Queue()
    print("Введите CLOUSE чтобы завершить ввод")
    def add_material(materials):
        item=input("Добавьте материал: ")
        if item=='CLOUSE': 
            while materials.empty()==False:
               print(materials.get())
        else:
            materials.put(item)
            add_material(materials)
    add_material(materials)

#8) Поменять имя в отсортированном списке

def task8(actor_birthday,men):

    def get_name(person):
        return person[0]
           
            
    number = (actor_birthday.day + actor_birthday.month**2 + actor_birthday.year) % 39 + 1
    index=int(input(f"Введите индекс, чтобы поменять чьё-то имя (0-{len(men)-1}): "))
    if index<0 or index>9:
        print(f"Можно ввести индекс только в данном диапазоне (0-{len(men)-1})")
        index=int(input(f"Введите индекс ещё раз, учитывая границы (0-{len(men)-1}): "))
    uniq=task2(men)
    uniq.sort(key=get_name)
    print(f" Было выбрано имя императора под номером {number}") #36 - Чжоу Гун-ван
    uniq[index][0]='Чжоу'
    uniq[index][1]='Гун-ван'
    
    print (uniq)

#9) Связный список странных названий населенных пунктов

places={'Большая Пысса ': 1,
        'Большое Бухалово': 2,
        'Манды': 3,
        'Синие Лепяги':4,
        'Дешевки': 5,
        'Такое': 6,
        'Тухлянка': 7,
        'Чуваки': 8,
        'Факфак': 9,
        'Овнище': 10,
        'Дно': 11,
        'Трусово': 12,
        'Кокаиновые горы': 13,
        'Хотелово': 14,
        'Косяковка': 15,
        'Куриловка': 0
    }
places_list=['Большая Пысса ','Большое Бухалово','Манды','Синие Лепяги','Дешевки','Такое','Тухлянка','Чуваки','Факфак','Овнище','Дно','Трусово','Кокаиновые горы','Хотелово','Косяковка','Куриловка',]
def task9(places): 
    print("Исходные данные:\n")
    print (places)
    
    
    def delete_place():
        town=input('Введите город, который хотите удалить:  ')
        temp=[]
        for key in places.keys():
                    if key==town:break
                    temp.append(key)
        if len(temp)==0: 
            list0=[]
            for x in places.keys():
                list0.append(x)
            places[list0[-1]]+=1
        else:places[temp[-1]]+=1
        print(f"\nСловарь, где {town} удален:\n")
        print(places)
        print("\n\n")
    def insert_konets(): 
        position=int(input('Введите позицию, на которую хотите вставить город "Конец": \n'))
        last=len(places)
        t='...'
        places.update({'Конец':position})
        for key in places.keys():
                    if places[key]==position and  key!='Конец': 
                            t=key
        
        del places[t]
        places.update({t:last})
        sorted_tuple=sorted(places.items(),key=lambda x: x[1])
        places_new=dict(sorted_tuple)
        print("\nОбновленный словарь: \n")
        print(places_new)
        print("\n\n")
    delete_place()
    insert_konets()
    
print(" Средний балл в аттестате: {0:.2f}\n".format(task1(atestat)))
print(f"Уникальный список имен: {task2(men)}\n")
print(f" Общая длина всех названий предметов: {task3(atestat)}\n") 
print(f"Уникальные буквы в названиях предметов: {task4(atestat)}\n")
print(f"Имя тамандуа в бинарном виде: {task5(tamandua)}\n")
print(f"Количество дней от даты рождения актера вестерна до текущей даты: {task6(actor_birthday)}\n")
task7()
print("\n")
task8(actor_birthday,men)
print("\n")
task9(places)
