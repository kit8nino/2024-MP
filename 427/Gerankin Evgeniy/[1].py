import datetime 
import collections
from random import choice

# Аттестат с предметами
certificate = {'алгебра': 3,
                 'геометрия': 5,
                 'русский язык': 2,
                 'литература': 2,
                 'информатика': 4,
                 'физика': 4,
                 'химия': 5,
                 'биология': 2,
                 'физ-ра': 5,
                 'технология': 3,
                 'астрономия': 4,
                 'английский язык': 5,
                 'история': 2,
                 'обществознание': 2} 

# Имя и фамилия актёра 60-х годов, его дата рождения
actor = ('Kirk Douglas', '1916-12-09') 

# Популярные мужские имена и фамилии города Волгоград
mNames = ["Иван", "Сергей", "Александр", "Андрей", "Дмитрий", 
              "Алексей", "Максим", "Владимир", "Антон", "Евгений"]
mSurnames = ["Иванов", "Петров", "Попов", "Смирнов", 
                 "Сергеев", "Кузнецов", "Васильев", "Андреев"]

# Имя домашнего тамандуа
tamandua = "Macintosh"

# Странные названия городов"
city = ["Лобово", "Лохово", "Дураки", "Вагина", "Одышка",
         "Богово", "Косолапово", "Петухи", "Малая игра", "Кушина",
         "Овощево", "Дно", "Каравай", "Опочка", "Язвы", "Писяево",
         "Барсуки", "Медведь", "Дупло", "Пупкино", "Путино", "Козюльки" 
         "Зубы", "Кривошляпы", "Лямоны", "Попки", 
         "Кабак", "Новая жизнь", "Саки", "Мамай", "Бибики", "Гаи", "Гнилево",
         "Усох", "Гобики", "Кондон", "Сурок", "Пиксяси"]

# Первое задание
def average_rating(certificate):
    summ = 0
    for value in certificate.values():
        summ += value
    return summ / len(certificate.values())

# Второе задание
def fullnames_random(popnames, popsurnames):
    N = 200
    new_register = [0]*N
    for i in range(N):
        name_random = choice(popnames)
        surname_random = choice(popsurnames)
        fullname_random = name_random + " " + surname_random
        new_register[i] = fullname_random
    return new_register

def unique_fullnames_function(fullnames):
    unique_register = set()
    for fullname in fullnames:
        unique_register.add(fullname)
    return sorted(unique_register)

# Третье задание
def length_of_subjects(certificate):
    length = 0
    for key in certificate.keys():
        length += len(key)
    return length

# Четвертое задание
def unique_abc(certificate):
    letters = set()
    for key in certificate.keys():
        for i in range(len(key)):
            letters.add(key[i])
    return sorted(letters)

# Пятое задание
def binomial_name(name):
    noviy_name = ''.join(format(ord(letter), '08b') for letter in name)
    return noviy_name

# Шестое занятие
def kolvo_days(date):
    arr_date = ['', '', '']
    i = 0
    for x in date:
        if x == '-':
            i += 1
            continue
        arr_date[i] += x
    return int(arr_date[0]), int(arr_date[1]), int(arr_date[2])

def days_from_date(date):
    year, month, day = kolvo_days(date)[0], kolvo_days(date)[1], kolvo_days(date)[2]

    today = datetime.date.today()
    
    later_time = datetime.date(year, month, day)
    now_time = datetime.date(today.year, today.month, today.day)
    
    delta = now_time - later_time
    
    return delta.days

# Седьмое задание
def enter_stroy_materials():
    q = collections.deque()
    word = ''
    while True:
        word = input()
        if word == 'stop':
            break
        q.append(word)
    print("Стройматериалы:", list(q), '\n')

# Восьмое задание
def get_number_of_imperator(actor):
    date = actor[1]
    year, month, day = kolvo_days(date)[0], kolvo_days(date)[1], kolvo_days(date)[2]
    return (day + month*2 + year) % 39 + 1 

def renamed(array):
    print("8. Введите индекс имени, которого хотите изменить:")
    index = int(input())
    
    name_of_imperator = "Чжоу Хуэй-ван"
    array[index] = name_of_imperator
    return array

# Девятое задание
def task_9():
    def column_print(dict_towns):
        print(">>")
        for x in dict_towns:
            print(x)
        print("<<")
    
    def del_name(dict_towns):
        print("\nВведите название города, который хотите удалить:")
        town = str(input())
        print("После удаления:")
        dict_towns.pop(town)
        column_print(dict_towns)
    
    def add_word(dict_towns):
        print("\nВведите номер места, куда хотите добавить слово \"Конец\":")
        index = int(input())
        word = "Конец"
        
        items = list(dict_towns.items())
        items.insert(index, (word, index))
        dict_towns = dict(items)
        print("Список после добавления:")
        column_print(dict_towns)
    
    dic_city = {}
    for i in range(len(city)):
        dic_city[city[i]] = i
    dic_city = dict(sorted(dic_city.items(), key=lambda x:x[1]))
    column_print(dic_city)
    del_name(dic_city)
    add_word(dic_city)
    
# Выполнение
print("1. Средняя оценка в школьном аттестате:", average_rating(certificate), '\n')

fullnames = sorted(fullnames_random(mNames, mSurnames))
unique_fullnames = unique_fullnames_function(fullnames)
#print("2. Случайные ФИ города Волгоград:", fullnames)
print("2. Уникальные ФИ города Волгоград:", unique_fullnames)
print("Количество случайных ФИ:", len(fullnames))
print("Количество уникальных ФИ:", len(unique_fullnames), '\n')

print("3. Общая длина всех названий предметов:", length_of_subjects(certificate), '\n')

print("4. Уникальные буквы в названиях предметов:", unique_abc(certificate), '\n')

print("5. Имя домашнего тамандуа в бинарном виде:", tamandua, '\n', binomial_name(tamandua), '\n')

print("6. Количество дней от даты рождения Кирка Дугласа (1916-12-09) до текущей даты :", days_from_date(actor[1]), '\n')

print("7. FIFO очередь, в которую можно добавлять строковые названия стройматериалов, вводимые с клавиатуры (до команды остановки \"stop\"):")
enter_stroy_materials()

print("Изменённый список имен:", renamed(fullnames), '\n')

print("9.")
task_9()