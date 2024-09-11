#Исходные данные
import datetime as dt
import random
from queue import Queue

school_attestation = {
    "геометрия": 5,
    "русский": 4,
    "литература": 2,
    "история": 4,
    "физика": 5,
    "химия": 4,
    "биология": 5,
    "география": 4,
    "английский": 3,
    "французский": 4,
    "испанский": 3,
    "информатика": 4,
    "алгебра": 5,
    "обществознание": 4}

actor = ("STEVE", "MCQUEEN", dt.datetime(1930, 3, 24))

names = [
    "Иван",
    "Александр",
    "Сергей",
    "Андрей",
    "Дмитрий",
    "Алексей",
    "Максим",
    "Владимир",
    "Евгений",
    "Игорь"]

surnames = [
    "Иванов",
    "Петров",
    "Смирнов",
    "Сергеев",
    "Попов",
    "Волков",
    "Кузнецов",
    "Васильев"]

pet_name = "spiky bristleback"

#Задание №1
average_grade = sum(school_attestation.values()) / len(school_attestation)
print("Средняя оценка в школьном аттестате:", average_grade)

#Задание №2
full_names = []
for i in range(30):
    full_name = random.choice(names) + " " + random.choice(surnames)
    full_names.append(full_name)
unique_names = set([name.split()[0] for name in full_names])
print("Уникальные имена:")
for name in unique_names:
    print(name)

#Задание №3
total_length = sum(len(subject) for subject in school_attestation.keys())
print("Общая длина всех предметов:", total_length)

#Задание №4
unique_letters = set()
for subject in school_attestation.keys():
    unique_letters.update(set(subject))
print("Уникальные буквы в названиях предметов:", unique_letters)

#Задание №5
binary_name = ' '.join(format(ord(char), '08b') for char in pet_name)
print("Имя домашнего тамандуа в бинарном виде:", binary_name)

#Задание №6
days_alive = (dt.datetime.now() - actor[2]).days
print(f"{actor[0]} {actor[1]} прожил {days_alive} дней.")

#Задание №7
queue = Queue()
while True:
    material = input("Введите название стройматериала (или 'стоп(stop)' для завершения): ")
    if material.lower() == "стоп" or "stop":
        break
    else:
        queue.put(material)
print("Названия стройматериалов:")
while not queue.empty():
    print(queue.get())

#Задание №8
year, month, day = actor[2].year, actor[2].month, actor[2].day
number = (day + month**2 + year) % 39 + 1
print("Номер императора, дата, год и месяц рождения актёра:", number, year, month, day)
emperor = "Чжоу Пин-ван"
index = int(input("Введите индекс от 0 до 29:"))
full_names.sort()
full_names[index] = emperor
print(full_names)


#Задание №9
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print(f"{data} не найден")
            return
        prev.next = current.next
    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for k in range(index - 1):
            if current is None:
                print("Индекс вне диапазона")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

l = LinkedList()
cities = ["Большая", "Пысса", "Большие Пупсы", "Манды", "Дешевки", "Новый русский спуск", "Такое",
          "Тухлянка", "Баклань", "Лохово", "Факфак", "Большое Струйкино", "Овнище", "Дно", "Трусово",
          "Кокаиновые горы", "Косяковка", "Куриловка", "Ширяево", "Ломки", "Большой Куяш", "Иннах",
          "Крутые Хутора", "Крутая", "Новые Алгаши", "Новопозорново", "Лысая Балда", "Болотная Рогавка",
          "Старые Черви", "Верхнее Зачатье", "Дураково"]
for city in cities:
    l.append(city)

print("Список карт в cs:go:")
l.print_list()

city_to_delete = input("Введите название карты в cs:go для её удаления: ")
l.delete(city_to_delete)

index_to_insert = int(input("Введите индекс для добавления новой карты 'Конец': "))
l.insert_at_index(index_to_insert, "Конец")

print("\nСписок карт после удаления и добавления:")
l.print_list()



























