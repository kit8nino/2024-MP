import datetime 
import collections
from random import choice

# Аттестат с 14 предметами
certificate = {'алгебра': 1,
                 'геометрия': 2,
                 'русский язык': 3,
                 'литература': 4,
                 'информатика': 5,
                 'физика': 4,
                 'химия': 3,
                 'биология': 2,
                 'физ-ра': 6,
                 'технология': 2,
                 'астрономия': 3,
                 'английский язык': 4,
                 'история': 5,
                 'обществознание': 5} 

# Имя-Фамилия актёра 60-х годов, его дата рождения
actor = ('Clint Eastwood', '1930-05-31') 

# Популярные мужские имена и фамилии города Пермь
pop_Mnames = ["Иван", "Александр", "Сергей", "Андрей", "Дмитрий", 
              "Алексей", "Максим", "Владимир", "Евгений", "Денис"]
pop_Msurnames = ["Иванов", "Петров", "Попов", "Смирнов", 
                 "Кузнецов", "Новиков", "Сергеев", "Мальцев"]

# Имя домашнего тамандуа
tamandua = "Shinobi"

# Список "Самые смешные названия российских городов"
towns = ["Большая Пысса", "Большие Пупсы", "Манды", "Дешевки", "Такое",
         "Тухлянка", "Баклань", "Лохово", "Факфак", "Большое Струйкино",
         "Овнище", "Дно", "Трусово", "Косяковка", "Куриловка", "Ширяево",
         "Ломки", "Большой Куяш", "Иннах", "Крутые Хутора", "Крутая", "Новые Алгаши" 
         "Новопозорново", "Болотная Рогавка", "Старые Черви", "Верхнее Зачатье", 
         "Дураково", "Козявкино", "Цаца", "Засосная", "Муходоево", "Да-да", "Хреновое",
         "Блювиничи", "Большое Бухалово", "Свиновье", "Синие Лепяги", "Жабино"]


# Функции для каждого задания

# Task 1
def average(certificate):
    summ = 0
    for value in certificate.values():
        summ += value
    return summ / len(certificate.values())

# Task 2
def generate_random_fullnames(pop_names, pop_surnames):
    N = 100
    new_list = [0]*N
    for i in range(N):
        random_name = choice(pop_names)
        random_surname = choice(pop_surnames)
        random_fullname = random_name + " " + random_surname
        new_list[i] = random_fullname
    return new_list

def unique_fullnames_function(fullnames):
    unique_list = set()
    for fullname in fullnames:
        unique_list.add(fullname)
    return sorted(unique_list)

# Task 3
def length_of_subjects(certificate):
    length = 0
    for key in certificate.keys():
        length += len(key)
    return length

# Task 4
def unique_letters(certificate):
    letters = set()
    for key in certificate.keys():
        for i in range(len(key)):
            letters.add(key[i])
    return sorted(letters)

# Task 5
def bin_name(name):
    new_name = ''.join(format(ord(letter), '08b') for letter in name)
    return new_name

# Task 6
def get_date_of_(date):
    arr_date = ['', '', '']
    i = 0
    for x in date:
        if x == '-':
            i += 1
            continue
        arr_date[i] += x
    return int(arr_date[0]), int(arr_date[1]), int(arr_date[2])

def days_from_date(date):
    year, month, day = get_date_of_(date)[0], get_date_of_(date)[1], get_date_of_(date)[2]

    today = datetime.date.today()
    
    later_time = datetime.date(year, month, day)
    now_time = datetime.date(today.year, today.month, today.day)
    
    delta = now_time - later_time
    
    return delta.days

# Task 7
def enter_stroy_materials():
    q = collections.deque()
    word = ''
    while True:
        word = input()
        if word == 'stop':
            break
        q.append(word)
    print("Все стройматериалы:", list(q), '\n')

# Task 8
def get_number_of_imperator(actor):
    date = actor[1]
    year, month, day = get_date_of_(date)[0], get_date_of_(date)[1], get_date_of_(date)[2]
    return (day + month*2 + year) % 39 + 1 
#print(get_number_of_imperator(actor)) # получилось 22 -> имя = Чжоу Дин-вай Юй

def renamed(array):
    print("8. Введите индекс имени, которого хотите изменить:")
    index = int(input())
    
    name_of_imperator = "Чжоу Дин-вай Юй"
    array[index] = name_of_imperator
    return array

# Task 9
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
    
    dict_towns = {}
    for i in range(len(towns)):
        dict_towns[towns[i]] = i
    dict_towns = dict(sorted(dict_towns.items(), key=lambda x:x[1]))
    column_print(dict_towns)
    del_name(dict_towns)
    add_word(dict_towns)
    
# Выполнение
print("1. Средняя оценка в аттестате:", average(certificate), '\n')

fullnames = sorted(generate_random_fullnames(pop_Mnames, pop_Msurnames))
unique_fullnames = unique_fullnames_function(fullnames)
#print("2. Случайные ФИ города Пермь:", fullnames)
print("2. Уникальные ФИ города Пермь:", unique_fullnames)
print("Количество случайных ФИ:", len(fullnames))
print("Количество уникальных ФИ:", len(unique_fullnames), '\n')

print("3. Общая длина всех названий предметов:", length_of_subjects(certificate), '\n')

print("4. Уникальные буквы в названиях предметов:", unique_letters(certificate), '\n')

print("5. Имя моего домашнего тамандуа:", tamandua, '\n', bin_name(tamandua), '\n')

print(f"6. Количество дней от даты рождения Клинта Иствуда (1930-05-31) до текущей даты ({datetime.date.today()}):", days_from_date(actor[1]), '\n')

print("7. FIFO очередь, в которую можно добавлять строковые названия стройматериалов, вводимые с клавиатуры (до команды остановки \"stop\"):")
enter_stroy_materials()

print("Изменённый список имен:", renamed(fullnames), '\n')

print("9.")
task_9()
