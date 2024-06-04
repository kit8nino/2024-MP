import datetime 
import collections
from random import choice

# Аттестат с 14 предметами
school_grades = {'Математика': 1,
                 'Русский язык': 4,
                 'Родной язык': 2,
                 'Литература': 4,
                 'Родная литература': 5,
                 'Физика': 3,
                 'Физ-ра': 5,
                 'Биология': 2,
                 'История': 7,
                 'Обществознание': 2,
                 'Информатика': 3,
                 'технология': 4,
                 'Химия': 357,
                 'Иностранный язык': 5} 

# Имя-Фамилия актёра 60-х годов, его дата рождения
actor = ('Henry Fonda', '1905-05-16') 

# Популярные мужские имена и фамилии города Пермь
pop_Mnames = ["Иван", "Александр", "Сергей", "Андрей", "Дмитрий", 
              "Алексей", "Максим", "Владимир", "Евгений", "Денис"]
pop_Msurnames = ["Иванов", "Петров", "Ростовский", "Попов", 
                 "Смирнов", "Сергеев", "Волков", "Романов"]

# Имя домашнего тамандуа
tamandua = "Дикий Ёж" #который колется

# Список "Самые смешные названия российских городов"
towns = ["Большое Бухалово", "Большие Пупсы", "Дураково", "Иннах", "Синие Лепяги",
         "Тухлянка", "Засосная", "Лохово", "Крутая", "Большое Струйкино",
         "Большая Пысса", "Дно", "Трусово", "Баклань", "Куриловка", "Ширяево",
         "Ломки", "Овнище", "Такое", "Крутые Хутора", "Манды", "Новые Алгаши" 
         "Новопозорново", "Болотная Рогавка", "Старые Черви", "Верхнее Зачатье", 
         "Косяковка", "Козявкино", "Цаца", "Дешевки", "Муходоево", "Да-да", "Большой Куяш",
         "Блювиничи", "Хреновое", "Свинорье", "Факфак", "Жабино"]


# Task 1
count = 0
for i in school_grades.values():
    count += i  
print("1. Средняя оценка в аттестате:", count / len(school_grades.values()), '\n')

# Task 2
N = 100
new_list = [0]*N
for i in range(N):
    random_name = choice(pop_Mnames)
    random_surname = choice(pop_Msurnames)
    random_fullname = random_name + " " + random_surname
    new_list[i] = random_fullname
    
fullnames = sorted(new_list)
unique_list = set()
for fullname in fullnames:
    unique_list.add(fullname)
print("2. Уникальные ФИ города Пермь:", sorted(unique_list))
print("Количество случайных ФИ:", len(fullnames))
print("Количество уникальных ФИ:", len(unique_list), '\n')

# Task 3
length = 0
for key in school_grades.keys():
    length += len(key)
print("3. Общая длина всех названий предметов:", length, '\n')

# Task 4
letters = set()
for key in school_grades.keys():
    for i in range(len(key)):
        letters.add(key[i])
print("4. Уникальные буквы в названиях предметов:", sorted(letters), '\n')

# Task 5
print("5. Имя моего домашнего тамандуа:", tamandua, '\n', ''.join(format(ord(letter), '08b') for letter in tamandua), '\n')

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
print(f"6. Количество дней от даты рождения Генри Фонда (1905-05-16) до текущей даты ({datetime.date.today()}):", days_from_date(actor[1]), '\n')

# Task 7
print("7. FIFO очередь, в которую можно добавлять строковые названия стройматериалов, вводимые с клавиатуры (до команды остановки \"stop\"):")
q = collections.deque()
word = ''
while True:
    word = input()
    if word == 'stop':
        break
    q.append(word)
print("Все стройматериалы:", list(q), '\n')

# Task 8
#print((16 + 5*2 + 1905) % 39 + 1)
print("8. Введите индекс имени, которого хотите изменить:")
index = int(input())
fullnames[index] = "Чжоу Куан-ван"
print("Изменённый список имен:", fullnames, '\n')

# Task 9
print("9.")
def column_print(dict_towns):
        print(">>")
        for x in dict_towns:
            print(x)
        print("<<")
        
dict_towns = {}
for i in range(len(towns)):
    dict_towns[towns[i]] = i
dict_towns = dict(sorted(dict_towns.items(), key=lambda x:x[1]))
column_print(dict_towns)   
        
print("\nВведите название города, который хотите удалить:")
town = str(input())
print("После удаления:")
dict_towns.pop(town)
column_print(dict_towns)
    
print("\nВведите номер места, куда хотите добавить слово \"Конец\":")
index = int(input())
word = "Конец"
    
items = list(dict_towns.items())
items.insert(index, (word, index))
dict_towns = dict(items)
print("Список после добавления:")
column_print(dict_towns)