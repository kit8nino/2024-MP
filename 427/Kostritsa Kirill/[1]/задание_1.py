import datetime 
import collections

# Введение начальных данных
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
                 'обществознание': 5} # аттестат с 14 предметами

actor = ('Clint Eastwood', '1930-05-31') # Имя-Фамилия актёра 60-х годов, его дата рождения

'''
popular_names_M = {'Иван': 3363,
               'Александр': 1556,
               'Сергей': 1232,
               'Андрей': 929,
               'Дмитрий': 861,
               'Алексей': 740,
               'Максим': 586,
               'Евгений': 515,
               'Владимир': 334,
               'Денис': 257}
popular_names_W = {'Екатерина': 709,
               'Елена': 768,
               'Мария': 1002,
               'Анастасия': 709,
               'Ольга': 773,
               'Наталья': 782,
               'Татьяна': 661,
               'Анна': 655,
               'Ирина': 585,
               'Юлия': 442}
'''

tamandua = "Shinobi"


# функции для каждой задачи
def average(certificate):
    summ = 0
    for value in certificate.values():
        summ += value
    return summ / len(certificate.values())

def length_of_subjects(certificate):
    length = 0
    for key in certificate.keys():
        length += len(key)
    return length

def unique_letters(certificate):
    letters = set()
    for key in certificate.keys():
        for i in range(len(key)):
            letters.add(key[i])
    return sorted(letters)

def bin_name(name):
    new_name = ''.join(format(ord(letter), '08b') for letter in name)
    return new_name

def days_from_date(date):
    
    def write_date(date):
        arr_date = ['', '', '']
        i = 0
        for x in date:
            if x == '-':
                i += 1
                continue
            arr_date[i] += x
        return int(arr_date[0]), int(arr_date[1]), int(arr_date[2])
    
    year, month, day = write_date(date)[0], write_date(date)[1], write_date(date)[2]
    
    today = datetime.date.today()
    
    later_time = datetime.date(year, month, day)
    now_time = datetime.date(today.year, today.month, today.day)
    
    delta = now_time - later_time
    
    return delta.days

def enter_stroy_materials():
    q = collections.deque()
    word = ''
    while True:
        word = input()
        if word == 'stop':
            break
        q.append(word)
    print("Все стройматериалы:", list(q), '\n')


# выполнение
print("1. Средняя оценка в аттестате:", average(certificate), '\n')
print("2. *в стадии разработки :)", '\n')
print("3. Общая длина всех названий предметов:", length_of_subjects(certificate), '\n')
print("4. Уникальные буквы в названиях предметов:", unique_letters(certificate), '\n')
print("5. Имя моего домашнего тамандуа:", tamandua, '\n', bin_name(tamandua), '\n')
print(f"6. Количество дней от даты рождения Клинта Иствуда (1930-05-31) до текущей даты ({datetime.date.today()}):", days_from_date(actor[1]), '\n')
print("7. FIFO очередь, в которую можно добавлять строковые названия стройматериалов, вводимые с клавиатуры (до команды остановки \"stop\"):")
enter_stroy_materials()
print("8. *в стадии разработки :)", '\n')
print("9. *в стадии разработки :)", '\n')
























