# -- coding: cp1251 --
from collections import deque
import datetime
import random

# Исходные данные
grades = {
    'Алгебра': 5,
    'Геометрия': 4,
    'История России': 4,
    'Физическая культура': 5,
    'Химия': 3,
    'Литература': 4,
    'Русский язык': 5,
    'Экология': 4,
    'Астрономия': 4,
    'Технология': 5,
    'ОБЖ': 3,
    'Социология': 4,
    'География': 4,
    'Философия': 5
}

actor = ("Джон Уэйн", datetime.date(1907, 5, 26))

names_list = [
    'Иван', 'Сергей', 'Александр', 'Андрей', 'Дмитрий', 'Алексей', 'Максим',
    'Владимир', 'Евгений', 'Денис'
]
surnames_list = [
    'Иванов', 'Петров', 'Сергеев', 'Ккузнецов', 'Смирнов', 'Андреев', 'Васильев', 'Попов'
]

def generate_names():
    full_names = []
    for i in range(30):
        name = random.choice(names_list)
        surname = random.choice(surnames_list)
        full_names.append(f"{name} {surname}")
    return full_names

animal_name = "Большой ленивец"

# Задания
# 1.
print(f"Средний балл: {sum(grades.values()) / len(grades)}\n")

# 2.
print(f"Уникальные имена: {set(names_list)}\n")

# 3.
print(f"Суммарная длина всех названий предметов: {sum(len(grade) for grade in grades.keys())}\n")

# 4.
print(f"Уникальные буквы в названиях предметов: {set(''.join(grades.keys()))}\n")

# 5.
print(f"Имя животного в бинарном виде: {' '.join([bin(ord(char))[2:] for char in animal_name])}\n")

# 6.
print(f"{actor[0]} родился {(datetime.date.today() - actor[1]).days} дней назад\n")

# 7.
queue = deque()
print("Введите название материалов (введите 'Стоп' для завершения): ")
while True:
    material = input()
    if material.lower() == 'стоп':
        break
    queue.append(material)

print(f"Материалы в порядке добавления: {list(queue)}\n")

# 8.
sorted_names_list = sorted(generate_names())
b_day, b_month, b_year = actor[1].day, actor[1].month, actor[1].year
index = (b_day + b_month ** 2 + b_year) % 10
print("Введите число от 0 до 9:")
index = int(input())
sorted_names_list[index] = "Сюань-цзун"
print(f"Обновлённый список: {sorted_names_list}\n")

# 9.
values = []
links = []
head = None

def add(idx, value):
    global head, values, links
    if head is None:
        values.append(value)
        links.append(None)
        head = 0
    else:
        new_idx = len(values)
        values.append(value)
        links.append(None)

        if idx == 0:
            links[new_idx] = head
            head = new_idx
        else:
            prev = head
            for _ in range(idx - 1):
                if links[prev] is None:
                    break
                prev = links[prev]
                
            links[new_idx] = links[prev]
            links[prev] = new_idx

def remove(value):
    global head, values, links
    if head is None:
        return
    
    if values[head] == value:
        head = links[head]
    else:
        prev = head
        current = links[prev]
        while current is not None and values[current] != value:
            prev = current
            current = links[current]
        
        if current is not None:
            links[prev] = links[current]

def display():
    global head, values, links
    current = head
    while current is not None:
        print(values[current])
        current = links[current]

add(0, "Большая Пысса")
add(2, "Большие Пупсы")
add(1, "Дно")
add(3, "Баклань")

print("Введите название для удаления:")
remove(input())

print("Введите индекс для вставки:")
add(int(input()), "Конец")

print("Список населённых пунктов:")
display()
