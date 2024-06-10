import random
from datetime import datetime as dt
from queue import Queue

imperator_info = "Цзи Пифан"


actor = ('Lee', 'Van Cleef', '1925-01-09')

tamandua = 'Паша Техник из группы Контейнер район Лефортово'

points = {0: "Пысса",
          "Пысса": "Большие Пупсы",
          "Большие Пупсы": "Манды",
          "Манды": "Дешевки",
          "Дешевки": "Новый русский спуск",
          "Новый русский спуск": "Такое",
          "Такое": "Тухлянка",
          "Тухлянка": 0}


certificate = {'Обществознание': 4,
               'География': 4,
               'Геометрия': 3,
               'Биология': 5,
               'Литература': 2,
               'История России': 5,
               'Всеобщая история': 5,
               'Английский язык': 4,
               'Музыка': 1,
               'Физическая культура': 5,
               'Технология': 4,
               'Русский язык': 2,
               'Алгебра': 3,
               'Физика': 1}


names_surnames = ['Иван Иванов', 'Иван Смирнов', 'Иван Сергеев', 'Иван Васильев', 'Александр Петров', 
                  'Александр Кузнецов', 'Александр Попов', 'Александр Волков', 'Сергей Иванов', 'Сергей Смирнов', 
                  'Сергей Сергеев', 'Сергей Васильев', 'Андрей Петров', 'Максим Ростовский', 'Евгений Васильев', 
                  'Максим Романов', 'Сергей Романов', 'Алексей Волков', 'Евгений Романов', 'Максим Попов', 'Александр Волков', 
                  'Алексей Иванов', 'Дмитрий Кузнецов', 'Владимир Иванов', 'Алексей Попов', 'Сергей Смирнов', 'Дмитрий Волков', 
                  'Сергей Смирнов', 'Максим Иванов', 'Алексей Волков']

#1
sum = 0
for sub in certificate:
    sum += certificate[sub]
avg = sum/len(certificate)
print('----------------------')
print('1:',avg)
print('----------------------')

#2
uniq_names = []
for people in names_surnames:
    name = people[:people.find(' ')]
    if name not in uniq_names:
        uniq_names.append(name)
print('2:',uniq_names)
print('----------------------')

#3
print('3:',len(''.join(key for key in certificate.keys())))
print('----------------------')

#4
uniq_symbols = []
for classes in certificate.keys():
    for symb in classes:
        if symb not in uniq_symbols:
            uniq_symbols.append(symb)
str_uniq_symbols = ", ".join(uniq_symbols)
print ('4:',str_uniq_symbols)
print('----------------------')

#5
bin_tamanduas_name = ''
for symb in tamandua:
        bin_tamanduas_name +=(format(ord(symb), '08b'))
print('5:', bin_tamanduas_name)
print('----------------------')

#6
date = actor[2]
now = dt.now()
date = dt.strptime(date, '%Y-%m-%d')
print('6:', str(now-date).split(",")[0])
print('----------------------')

#7
materials_line = Queue()
keyboard_text = ""
print("Введите название материала (для завершения end): ", end='')
keyboard_text = input()
while (keyboard_text != "end"):
    print("Введите название материала (для завершения end): ", end='')
    materials_line.put(keyboard_text)
    keyboard_text = input()
while (materials_line.empty() == False):
    print(materials_line.get() + ", ", end='')
print(' ')
print('----------------------')

#8
num = input("8: Введите номер, имя которого хотите заменить на имя императора:")
if int(num) > len(names_surnames):
    print("Ваше число слишком большое, введите число до", len(names_surnames))
    num = input("Введите номер, имя которого хотите заменить на имя императора:")
names_surnames[int(num)-1] = imperator_info
print(names_surnames)
print('----------------------')

# 9
print("9: Связный список" + str(points))

keyboard_input = input("Введите название города для удаления: ")
index = 0
if (keyboard_input != 'q'):
    limit = len(points)
    counter = 0
    while (points[index] != keyboard_input and counter < limit):
        index = points[index]
        counter += 1
    if counter != limit:
        points[index] = points[points[index]]
        del points[keyboard_input]
    else:
        print("Такой город не найден")

    print(points)

keyboard_input = input("Введите индекс для вставки: ")
index = 0
if (keyboard_input != 'q'):
    points["Конец"] = points[keyboard_input]
    points[keyboard_input] = "Конец"

    print(points)
print('----------------------')
