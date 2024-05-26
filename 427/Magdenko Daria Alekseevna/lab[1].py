import random
import datetime as dt
import queue

# [1] Работа со структурами данных
# Аттестат
attestat = {
    "math": 5,
    "language": 4,
    "literature": 3,
    "foreing language": 4,
    "physics": 4,
    "chemistry": 3,
    "biology": 3,
    "geography": 3,
    "history": 4,
    "pe": 5,
    "technology": 5,
    "music": 5,
    "art": 4,
    "safety": 5,
    "religions": 3,
    "psychology": 4,
    "computer science": 5
}

# Актёр
actor = ("Yul", "Brynner", "11.07.1920")

# В списке 16 городов, так как день рождения 17 числа то взят 7 (челябинск)
topNames = ("Елена", "Ольга", "Екатирина", "Мария", "Наталья", "Анастасия", "Анна", "Татьяна", "Ирина", "Светлана")
topSurnames = ("Иванова", "Петрова", "Кузнецова", "Смирнова", "Попова", "Соколова", "Васильева", "Романова")
names = []
for i in range(30):
    names.append(topNames[random.randint(0, 9)] + " " + topSurnames[random.randint(0, 7)])

# Имя тамандуа
tamanduaName = "лысый броненосец"

# 1, 3
average = 0
strLen = 0
for subject in attestat:
    average += attestat[subject]
    strLen += len(subject)
average = average / len(attestat)
print("1: " + str(average))

# 2.
print("\n2:")
for name in names:
    counter = 0
    for name2 in names:
        if (name == name2):
            counter += 1
    if (counter == 1):
        print(name)

    # 3.
print("\n3: " + str(strLen))

# 4.
dictionary = {}
for subject in attestat:
    for letter in subject:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
print("\n4: " + str(len(dictionary)))

# 5.
print("\n5: ", end='')
for letter in tamanduaName:
    print(str(bin(ord(letter))).split('b')[1], end=' ')
print()  # лишний перенос строки

# 6.
print("\n6: ", end='')
bitrh_time_obj = dt.datetime.strptime(actor[2], '%d.%m.%Y')
now_time_obj = dt.datetime.now()
delta = now_time_obj - bitrh_time_obj
print(delta)

# 7.
print("\n7: ")
materials_line = queue.Queue()
keyboard_text = ""
print("Введите название материала (для завершения end): ", end='')
keyboard_text = input()
while (keyboard_text != "end"):
    print("Введите название материала (для завершения end): ", end='')
    materials_line.put(keyboard_text)
    keyboard_text = input()
while (materials_line.empty() == False):
    print(materials_line.get() + ", ", end='')
print()

# 8.
index = input("\n8: введите индекс:")
# imperator_number = (bitrh_time_obj.day + bitrh_time_obj.month**2 + bitrh_time_obj.year) % 39 + 1
# print(imperator_number)
# номер императора = 31
imperator_name = "Цзи Шу"
names[int(index) - 1] = imperator_name
print("Новый список имён: " + str(names) + "\n")

# 9.
points = {0: "Пысса",
          "Пысса": "Большие Пупсы",
          "Большие Пупсы": "Манды",
          "Манды": "Дешевки",
          "Дешевки": "Новый русский спуск",
          "Новый русский спуск": "Такое",
          "Такое": "Тухлянка",
          "Тухлянка": 0}

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
