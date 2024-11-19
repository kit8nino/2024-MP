import random
import datetime
import queue
import collections

#Предметы
marks = {"Трансгрессия": 5, "Травология": 3, "Уход за магическими существами": 5, "Трансфигурация": 5, "Заклинания": 4,
        "Зельеварение": 3, "История магии": 3, "Защита от темных искусств": 5, "Астрономия": 3, "Полеты на метлах": 5,
        "Нумерология": 4, "Прорицания": 3, "Изучение древних рун": 4, "Магловедение": 5}

#Актер. Допустим, что "Шанхайский полдень" и "Шанхайские рыцари" - это вестерны из 60-х годов, а не из 00-х.
actor = ("Jackie", "Chan", "07.04.1954")

#Имена/Фамилии. Самара.
m_names = ["Иван", "Сергей", "Александр", "Андрей", "Дмитрий", "Алексей", "Максим", "Владимир", "Евгений", "Денис"]
m_surnames = ["Иванов", "Петров", "Сергеев", "Кузнецов", "Смирнов", "Андреев", "Васильев", "Попов"]
w_names = ["Анастасия", "Екатерина", "Елена", "Ирина", "Мария", "Наталья", "Ольга", "Светлана", "Татьяна", "Юлия"]
w_surnames = ["Васильева", "Волкова", "Иванова", "Кузнецова", "Петрова", "Попова", "Романова", "Смирнова"]

#Создание ИФ.
def gen_fullnames(names, surnames, fullnames):
    for i in range(len(names) - 1):
        i_name = random.randint(0, len(names) - 1)
        i_surname = random.randint(0, len(surnames) - 1)
        fname = []
        fname.append(names[i_name])
        fname.append(surnames[i_surname])
        fullnames.append(fname)
    return fullnames

#Список ИФ.
def merge_fullnames():
    global m_names, m_surnames, w_names, w_surnames
    m_fnames = []
    w_fnames = []
    gen_fullnames(m_names, m_surnames, m_fnames)
    gen_fullnames(w_names, w_surnames, w_fnames)
    fullnames = m_fnames + w_fnames
    return fullnames

fullnames = merge_fullnames()

#ТАМандуа, нет ТУТандуа.
tam = "\nn33ps' maloy\n"

#Средний балл.
def t1(marks):
    s = 0
    for mark in marks:
        s += marks[mark]
    return round(s/len(marks), 2)

#Уникальные имена.
def t2(fullnames):
    uni_nlist = []
    for fname in fullnames:
        if fname[0] not in uni_nlist:
            uni_nlist.append(fname[0])
    return uni_nlist

#Длина названий предметов.
lensub = ""
def t3(marks):
    global lensub
    for mark in marks:
        lensub += mark
    return(len(lensub))

#Уникальные буквы.
def t4(lensub):
    lensub = lensub.replace(" ", "").lower()
    uni_letters = []
    for letter in lensub:
        if letter not in uni_letters:
            uni_letters.append(letter)
    return uni_letters

#ТУТандуа в бинарном.
def t5(tam):
    bin_tam = ""
    for letter in tam:
        bin_tam += " " + bin(ord(letter))[2::]
    bin_tam = bin_tam.lstrip()
    return bin_tam

#Сколько дней до сегодня.
def t6(actor):
    days = ""
    today = datetime.date.today()
    actor_bday = actor[2].split(".")
    actor_bday = datetime.date(int(actor_bday[2]), int(actor_bday[1]), int(actor_bday[0]))
    diff = str(today - actor_bday)
    i = 0
    while diff[i].isdigit():
        days += diff[i]
        i += 1
    return days

#FIFO.
def t7():
    mats = []
    mat = input('\nНазвание материала или "STOP" для остановки:\n')
    while mat.upper() != "STOP":
        mats.append(mat)
        mat = input('\nНазвание материала или "STOP" для остановки:\n')
    if len(mats) == 0:
        print("\nА где?\n")
    else:
        print('\nНазвания по порядку:\n')
        for mat in mats:
            print(f'{mat}')
    
#Chinese n-word.
def t8(actor, fullnames):
    actor_bday = actor[2]
    actor_bday = actor_bday.split(".")
    day = int(actor_bday[0])
    month = int(actor_bday[1])
    year = int(actor_bday[2])
    num = (day + month**2 + year) % 39 + 1
    print(f'\nНомер китаёзы: {num}.\n')
    chiname = "Чжоу Юань-ван"
    fullnames = merge_fullnames()
    fullnames.sort()
    print(f'\nSorted list of popular names:\n {fullnames}')
    i = int(input(f'\nВведите индекс от 0 до {len(fullnames)}: '))
    fullnames[i][0] = chiname
    print (f"\nSorted list of popular names with chinese n-word's name:\n {fullnames}")

#Странные города.
def output(city, l_city):
    for city in l_city:
        print(city)

def t9():
    l_city = collections.deque()
    s_city = ["Монкево", "Такое", "Кочевники", "Алохоморово", "Авадакедавраво", "Экспеллиармусово", "Форлайфово",
              "Грувстритово", "Инмайхартово", "Тудеево", "Инзиснайтово", "Ванлавово", "Тугезерово"]
    for city in s_city:
        l_city.append(city)
    print("Вполне обычные названия:\n")
    output(city, l_city)
    
    del_city = input("\nЧто удаляем?\n")
    if del_city in l_city:
        l_city.remove(del_city)
    print("\nВполне обычные названия, но одного не хватает:\n")
    output(city, l_city)
    
    end_city = "Конец"
    i_ins = int(input(f'\nКуда вставляем "Конец"?\n'))
    l_city.insert(i_ins, end_city)
    print("\nВполне обычные названия, но есть один нюанс:\n")
    output(city, l_city)

#Лес гоу, мегавывод по запросу.
def run_task(task_num):
    
    match(task_num):
        case "1":
            print(f'\n№1:\nСредняя оценка: {t1(marks)}')
        case "2":
            print(f'\n№2\nУникальные имена:\n{t2(fullnames)}')
        case "3":
            print(f'\n№3\nОбщая длина названий предметов: {t3(marks)}')
        case "4":
            print(f'\n№4\nУникальные буквы в названиях предметов:\n{t4(lensub)}')
        case "5":
            print(f'\n№5\nИмя ТУТандуа в бинарном: {t5(tam)}')
        case "6":
            print(f'\n№6\nСтолько дней до сегодня: {t6(actor)}')
        case "7":
            print(f'\n№7\n')
            t7()
        case "8":
            print(f'\n№8\n')
            t8(actor, fullnames)
        case "9":
            print(f'\n№9\n')
            t9()
        case _:
            print('Нет такого(')
task_num = input('\nВведите номер задания или "STOP", если хватит:\n')

while task_num.upper() != "STOP":
    run_task(task_num)
    task_num = input('\nВведите номер задания или "STOP", если хватит:\n')

print('\nLa fin.\n')
