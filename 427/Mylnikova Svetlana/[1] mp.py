import datetime 
import collections
import random

# ИСХОДНЫЕ ДАННЫЕ

# предметы в аттестате с оценками
attestat = {'русский язык': 5,
            'математика': 3,
            'география': 4,
            'физика': 5,
            'биология': 4,
            'химия': 3,
            'математический анализ': 3,
            'обж': 5,
            'история': 5,
            'физра': 5,
            'французский язык': 4,
            'английский язык': 4,
            'обществознание': 3,
            'окружающий мир': 3,
            'изо': 2,
            'литература': 5} 

# полное имя фамилия и др актера вестерна 60-х (Чарльз Бронсон)
western_actor = ('Charles Bronson', '1921-11-03') 

# список имен и фамилий города Ростов-на-Дону с  сайта
popular_names = ["Иван", "Александр", "Сергей", "Андрей", "Дмитрий", 
              "Алексей", "Максим", "Владимир", "Евгений", "Денис"]
popular_lastnames = ["Иванов", "Петров", "Ростовский", "Попов", 
                 "Смирнов", "Сергеев", "Волков", "Романов"]

# имя из прилагательного и существительного моего домашнего тамандуа
tamandua = "cool tree"

# хихи названия городов
hihi_towns = ["Большие Пупсы", "Кокаиновые горы", "Дешевки", "Такое","Тухлянка", "Баклань", 
         "Лохово", "Факфак", "Овнище", "Дно", "Косяковка", "Куриловка", "Ширяево",
         "Ломки","Крутая", "Новопозорново", "Дураково", "Козявкино", "Цаца", "Засосная", 
         "Муходоево", "Да-да", "Хреновое","Блювиничи", "Большое Бухалово", "Свиновье", "Жабино"]


# ДЕЙСТВИЯ

# пункт 1
def average(attestat):
    summ = 0
    for value in attestat.values():
        summ += value
    return summ / len(attestat.values())

print("1. cредняя оценка в аттестате:", average(attestat), '\n')

# пункт 2
def generate_uniqalny_fullnames(popular_names, popular_lastnames):
  
    uniqalny_fullnames = []

    for name in popular_names:
     for lastname in popular_lastnames:
      fullname = f"{name} {lastname}"

      if fullname not in uniqalny_fullnames:
        uniqalny_fullnames.append(fullname)

    return uniqalny_fullnames

uniqalny_fullnames = generate_uniqalny_fullnames(popular_names, popular_lastnames)

print("2. уникальные полные имена, взятые из популярных Ростова-на-Дону:", uniqalny_fullnames, '\n')

# пункт 3
def length_of_sch_sub(attestat):
    length = 0
    for key in attestat.keys():
        length += len(key)
    return length

print("3. общая длина всех названий предметов:", length_of_sch_sub(attestat), '\n')

# пункт 4
def uniqalny_letters(attestat):
    letters = set()
    for key in attestat.keys():
        for i in range(len(key)):
            letters.add(key[i])
    return sorted(letters)

print("4. уникальные буквы в названиях предметов:", uniqalny_letters(attestat), '\n')

# пункт 5
def binarny_name(name):
    new_name = ''.join(format(ord(letter), '08b') for letter in name)
    return new_name

print("5. имя моего домашнего тамандуа в бинарном виде:", tamandua, '\n', binarny_name(tamandua), '\n')

# пункт 6
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

print(f"6. количество дней от даты рождения актера вестерна (Чарльз Бронсон, 1921-11-03) до текущей даты ({datetime.date.today()}):", days_from_date(western_actor[1]), '\n')

# пункт 7
def stroymaterialy():
    q = collections.deque()
    word = ''
    while True:
        word = input()
        if word == 'end':
            break
        q.append(word)
    print("список стройматериалов:", list(q), '\n')
    
print("7. FIFO очередь, в которую можно добавлять строковые названия стройматериалов, вводимые с клавиатуры (команда для остановки - end):")
stroymaterialy()

# пункт 8
def get_number_of_imperator(western_actor):
    date = western_actor[1]
    year, month, day = get_date_of_(date)[0], get_date_of_(date)[1], get_date_of_(date)[2]
    return (day + month**2 + year) % 39 + 1 
#print ("получившееся число", get_number_of_imperator(western_actor))
# число 18 - император Чжоу Хуэй-ван

def renamed(array):
    print("8.1 индекс имени, которого хотите изменить:")
    index = int(input())
    
    name_of_imperator = "Чжоу Хуэй-ван"
    array[index] = name_of_imperator
    return array

print("8.2 новый список отсортированных имен (с императором):", renamed(uniqalny_fullnames), '\n')

# пункт 9
def zadaye_towns():
    def column_print(towns_spisok):
        for x in towns_spisok:
            print(x)
    
    def delete_t(towns_spisok):
        print("\n название города, который будем удалять:")
        town = str(input())
        print("список после удаления:")
        towns_spisok.pop(town)
        column_print(towns_spisok)
    
    def add_konets(towns_spisok):
        print("\n номер места, куда хотите добавить КОНЕЦ:")
        index = int(input())
        word = "КОНЕЦ"
        
        items = list(towns_spisok.items())
        items.insert(index, (word, index))
        towns_spisok = dict(items)
        print("список после добавления:")
        column_print(towns_spisok)
    
    towns_spisok = {}
    for i in range(len(hihi_towns)):
        towns_spisok[hihi_towns[i]] = i
    towns_spisok = dict(sorted(towns_spisok.items(), key=lambda x:x[1]))
    column_print(towns_spisok)
    delete_t(towns_spisok)
    add_konets(towns_spisok)

print("9. смешные города:")
zadaye_towns()




















