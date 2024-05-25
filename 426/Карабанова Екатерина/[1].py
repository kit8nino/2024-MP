import random
subjects = {
    'Алгебра': 4,
    'История': 5,
    'Немецкий': 5,
    'Физика': 4,
    'Информатика': 5,
    'Русский язык': 4,
    'ИРМ': 4,
    'Родной язык': 4,
    'Физкультура': 5,
    'Обществознание': 4,
    'Геометрия': 4,
    'Астрономия': 5,
    'Химия': 4,
    'Литература': 5
}

actor = ('Clint Eastwood', '31 May 1930')

popular_nam = ["Иван Иванов", "Александр Смирнов", "Мария Кузнецова", "Егор Петров", "Анна Соколова"]
day_of_birth = 12
cities = ["Новосибирск"]
full_nam = [(random.choice(popular_nam), random.choice(cities)) for _ in range(30)]

tamandua_name = "Муравьи́ный Жулик"

#Работа с данными
#1
average_grade = sum(subjects.values()) / len(subjects)
print("     Средняя оценка в аттестате:", average_grade)

#2
unique_nam = set(full_nam)
print("     Уникальные имена:", unique_nam)

#3
total_length = sum(len(subject) for subject in subjects)
print("     Общая длина всех предметов:", total_length)
#4
unique_letters = set(letter for subject in subjects for letter in subject)
print("     Уникальные буквы в названиях предметов:", unique_letters)
#5
tamandua_binary = ''.join(format(ord(char), '08b') for char in tamandua_name)
print("     Имя тамандуа в бинарном виде:", tamandua_binary)

# 6
from datetime import datetime

birth_date = datetime.strptime(actor[1], '%d %B %Y')
current_date = datetime.now()
days_difference = (current_date - birth_date).days
print("     Количество дней от даты рождения актера до текущей даты:", days_difference)

# 7
from collections import deque

materials_queue = deque()
while True:
    material = input("Введите название стройматериала (для остановки введите 'стоп'): ")
    if material.lower() == "стоп":
        break
    materials_queue.append(material)

print("     FIFO очередь стройматериалов:", list(materials_queue))

# 8
emperors_zhou = ["У", "Чэн", "Кан", "Лян", "Сян", "Гун", "Хуань", "Мин", "Ин", "Ай", "Си",
                 "Нонг", "Чжао", "Пинг", "Хуан", "Сюань", "И", "Дань", "Цзянь", "Цзин", "Цзи", "Дао",
                 "Ци", "Лин", "Хуэй"]

index = int(input("Введите индекс: "))

# Проверка на корректность введенного индекса
if index < 1 or index > len(full_nam):
    print("Индекс вне диапазона!")
else:
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    number = (day + month**2 + year) % 39 + 1

    full_nam[index-1] = emperors_zhou[number-1]
    print('     Готовый список:',full_nam)

#9
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StrangeTownLinkedList:
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
            print(current.data)
            current = current.next

    def remove(self, town_name):
        current = self.head
        prev = None
        while current:
            if current.data == town_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = None
                return
            prev = current
            current = current.next

    def insert(self, town_name, index):
        new_node = Node(town_name)
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        if prev:
            prev.next = new_node
            new_node.next = current
        else:
            new_node.next = self.head
            self.head = new_node

towns_list = StrangeTownLinkedList()
towns = ["Большая Пысса", "Большие Пупсы", "Манды", "Такое", "Тухлянка", "Баклань", "Лохово", "Факфак", "Большое Струйкино", 
         "Овнище", "Дно", "Трусово", "ул. Забойная", "Кокаиновые горы", "Косяковка", "Куриловка", "Ширяево", "Ломки", "Большой Куяш", 
         "Иннах", "Крутые Хутора", "Крутая", "Новые Алгаши", "Новопозорново", "Лысая Балда", "Болотная Рогавка", "Старые Черви", 
         "Верхнее Зачатье", "Дураково", "Заячий пузырь", "Козявкино", "Цаца", "Засосная", "Звероножка", "Муходоево", "Да-да", "Вобля", 
         "Хреновое", "Блювиничи", "Большое Бухалово", "Свиновье", "Синие Лепяги", "Жабино", "Кончинино", "Раздериха", "Чуваки", "Мусорка", 
         "Голодранкино", "Безводовка", "Красная Могила", "Кундрючья", "Хотелово", "Добрые Пчелы", "Синегубово"]

for town in towns:
    towns_list.append(town)

print("Список странных названий населенных пунктов:")
towns_list.print_list()

town_to_remove = input("Введите название населенного пункта для удаления: ")
towns_list.remove(town_to_remove)
print("Список после удаления:")
towns_list.print_list()

index = int(input("Введите индекс для вставки города 'Конец': "))
towns_list.insert("Конец", index)
print("       Список после вставки города 'Конец':")
towns_list.print_list()
