import datetime as dt
import random
import queue

atestat = {
    "геометрия": 4,
    "русский": 4,
    "литература": 4,
    "история": 5,
    "физика": 5,
    "обществознание": 5,
    "химия": 5,
    "биология": 4,
    "география": 5,
    "английский": 3,
    "ОБЖ": 5,
    "физкультура": 5,
    "информатика": 5,
    "алгебра": 5
}

actor = ("Wiliam", "Holden", dt.datetime(1918, 4, 17))

names = [
    "Иван",
    "Александр",
    "Сергей",
    "Андрей",
    "Дмитрий",
    "Алексей",
    "Максим",
    "Евгений",
    "Владимир",
    "Денис"]

surnames = [
    "Иванов",
    "Петров",
    "Сергеев",
    "Смирнов",
    "Кузнецов",
    "Попов",
    "Волков",
    "Васильев"]

#pet_name = "Exotic Bobik"
pet_name = "Мура"

#1

def sr_z(x):
    Sum = 0
    count = 0
    for value in x.values():
        Sum += value
        count += 1
    return Sum / count


print(sr_z(atestat))
print()

#2

full_names = []
for i in range(50):
    full_name = random.choice(names) + " " + random.choice(surnames)
    full_names.append(full_name)
print("Уникальные имена:")
for name in full_names:
    print(name)

#3

def length1(x):
    Sum = 0
    for k in x.keys():
        Sum += len(k)
    return Sum


print(length1(atestat))

#4

def uniq_chars(x):
    rez = []
    for name in x.keys():
        for j in range(len(name)):
            if name[j].lower() not in rez and name[j] != ' ':
                rez.append(name[j].lower())
            else:
                continue
    return rez

print(uniq_chars(atestat))

#5

name_bin = ' '.join(format(ord(char), '08b') for char in pet_name)
print("Имя питомца в бинарном виде:", name_bin)

#6

print(dt.datetime.today() - actor[2])

#7

q7 = queue.Queue()
while True:
    # enter 0 to stop
    material = input()
    if material == '0':
        break
    q7.put(material)

while not q7.empty():
    print(q7.get())

#8

print('Введите индекс от 0 до 49')
index = int(input())
#2 Чжоу Чэн-ван
full_names.sort()
full_names[index] = "Чжоу Чэн-ван"
print(full_names)

#9

cities = ["Большая Пысса", "Лысая Балда", " Болотная Рогавка", "Синегубово ", "Свиновье",
               "Тухлянка ", "Добрые Пчелы ", "Понт Ванис", "Крутые Хутора",
               "Блювиничи ", "Заячий пузырь", "Цинтра", "Лохово"]
print(cities)
cities.remove(str(input("Введите название города, который хотели бы заменить: ")))

ind = int(input("Введите номер того места, куда бы хотели добавить новый город: "))
cities.append("Конец")
for i in range(len(cities) - ind):
    a = cities[ind+i-1]
    cities[ind+i-1] = cities[len(cities) - 1]
    cities[len(cities) - 1] = a
print(cities)

