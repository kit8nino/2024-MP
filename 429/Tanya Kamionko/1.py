# -- coding: cp1251 --
from collections import deque
import datetime
import random

# 1. Исходные данные
grades = {
    'Математика': 4,
    'История': 5,
    'Биология': 3,
    'Физика': 4,
    'Химия': 4,
    'Английский': 5,
    'География': 4,
    'Physical Education': 5,
    'Литература': 5,
    'ИЗО': 4,
    'Музыка': 3,
    'Информатика': 5,
    'Обществознание': 4,
    'Экономика': 5
}

actor = ("Клинт Иствуд", datetime.date(1930, 5, 31))

# Для Перми
names_list = [
    'Елена', 'Мария', 'Ольга', 'Наталья', 'Екатерина', 'Татьяна', 'Анастасия',
    'Светлана', 'Ирина', 'Марина'
]

surnames_list = [
    'Иванова', 'Попова', 'Петрова', 'Кузнецова', 'Смирнова', 'Мальцева',
    'Новикова', 'Волкова'
]

tamandua_name = "Маленький тамандуа"

# Средняя оценка в аттестате
average_grade = sum(grades.values()) / len(grades)
print("Средняя оценка:", average_grade)
print()

# Уникальные имена из списка
unique_names = set(names_list)
print("Уникальные имена:", unique_names)
print()

# Общая длина всех названий предметов
length = sum(len(subject) for subject in grades.keys())
print("Общая длина названий предметов:", length)
print()

# Уникальные буквы в названиях предметов
temp = ""
for s in grades.keys():
    temp += s
unique_letters = set(temp)
print("Уникальные буквы:", unique_letters)
print()

# Имя тамандуа в бинарном виде
binary = [bin(ord(char))[2:] for char in tamandua_name]
print("Имя тамандуа:", *binary)
print()

# Количество дней от даты рождения актера до текущей даты
days_since_birth = (datetime.date.today() - actor[1]).days
print("Дней прошло:", days_since_birth)
print()

# FIFO очередь для стройматериалов
queue = deque()
print("Ввод материалов ('Конец' для завершения):")
while True:
    material = input()
    if material == 'Конец':
        break
    queue.append(material)

print("FIFO очередь:", list(queue))
print()

# Замена имени в отсортированном списке популярных имен и фамилий
names_list = [
    'Елена Иванова', 'Мария Кузнецова', 'Ольга Попова', 'Наталья Смирнова', 'Екатерина Петрова', 'Татьяна Мальцева',
    'Анастасия Новикова', 'Светлана Волкова', 'Ирина Петрова', 'Марина Смирнова'
]

sorted_names_list = sorted(names_list)
birth_day, birth_month, birth_year = actor[1].day, actor[1].month, actor[1].year
index = (birth_day + birth_month**2 + birth_year) % 39 + 1
print("Index:", index)
imperator = "Чжоу Шэнь Цзинь-ван"
print("Введите число, 0 <= n <= 9:")
index = int(input())
sorted_names_list[index] = imperator
print(sorted_names_list)
print()

# Связный список странных названий населенных пунктов
class LinkedList:
    def __init__(self):
        self.vals = []
        self.nexts = []
        self.head = None
    
    def insert(self, idx, val):
        if self.head is None:
            self.vals.append(val)
            self.nexts.append(None)
            self.head = 0
        else:
            new_idx = len(self.vals)
            self.vals.append(val)
            self.nexts.append(None)
            
            if idx == 0:
                self.nexts[new_idx] = self.head
                self.head = new_idx
            else:
                prev_idx = self.head
                for i in range(idx - 1):
                    if self.nexts[prev_idx] is None:
                        break
                    prev_idx = self.nexts[prev_idx]
                
                self.nexts[new_idx] = self.nexts[prev_idx]
                self.nexts[prev_idx] = new_idx
    
    def delete(self, val):
        if self.head is None:
            return
        
        if self.vals[self.head] == val:
            self.head = self.nexts[self.head]
        else:
            prev_idx = self.head
            cur_idx = self.nexts[prev_idx]
            while cur_idx is not None and self.vals[cur_idx] != val:
                prev_idx = cur_idx
                cur_idx = self.nexts[cur_idx]
            
            if cur_idx is not None:
                self.nexts[prev_idx] = self.nexts[cur_idx]
    
    def print_list(self):
        cur_idx = self.head
        while cur_idx is not None:
            print(self.vals[cur_idx])
            cur_idx = self.nexts[cur_idx]
            
towns = LinkedList()
towns.insert(0, "Большая Пысса")
towns.insert(2, "Большие Пупсы")
towns.insert(1, "Такое")
towns.insert(3, "Тухлянка")

print("Введите название:")
name = input()
towns.delete(name)

print("Введите индекс:")
index = int(input())
towns.insert(index, "Конец")
towns.print_list()
