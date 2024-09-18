import random
from datetime import datetime
from collections import deque
import binascii

# 1) Словарь предметов и оценок
school_subjects = {
    'Русский язык': 5,
    'Литература': 4,
    'Математика': 5,
    'Геометрия': 4,
    'История': 3,
    'Обществознание': 4,
    'Биология': 5,
    'Химия': 4,
    'Физика': 5,
    'Иностранный язык': 5,
    'Информатика': 5,
    'Физическая культура': 4,
    'География': 4,
    'ИЗО': 3,
    'Музыка': 4
}

# 2) Кортеж с данными актера из вестерна 1960-х годов
western_actor = ('Джон Уэйн', '1907-05-26')

# 3) Список из имени и фамилии, составленные случайно
names = ['Александр', 'Михаил', 'Дмитрий', 'Максим', 'Иван', 'Кирилл', 'Артем', 'Андрей', 'Алексей', 'Евгений']
surnames = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов', 'Попов', 'Васильев', 'Морозов', 'Новиков', 'Зайцев']

random_full_names = [f"{random.choice(names)} {random.choice(surnames)}" for _ in range(30)]

# 4) Имя для домашнего тамандуа
anteater_name = 'Ленивый Проводник'


# Действие 1: Средняя оценка в аттестате
average_grade = sum(school_subjects.values()) / len(school_subjects)
print("Средняя оценка:", average_grade)

# Действие 2: Уникальные имена
unique_names = set(name.split()[0] for name in random_full_names)
print("Уникальные имена:", unique_names)

# Действие 3: Общая длина всех названий предметов
total_length = sum(len(subject) for subject in school_subjects)
print("Общая длина названий предметов:", total_length)

# Действие 4: Уникальные буквы в названиях предметов
unique_letters = set(''.join(school_subjects.keys()))
print("Уникальные буквы в названиях предметов:", unique_letters)

# Действие 5: Имя тамандуа в бинарном виде
binary_name = ' '.join(format(ord(letter), 'b') for letter in anteater_name)
print("Имя тамандуа в бинарном виде:", binary_name)

# Действие 6: Количество дней от даты рождения актера до текущей даты
actor_birthdate = datetime.strptime(western_actor[1], '%Y-%m-%d')
current_date = datetime.now()
days_passed = (current_date - actor_birthdate).days
print("Количество дней с даты рождения актера:", days_passed)

# Действие 7: FIFO очередь стройматериалов
materials_queue = deque()
print("Введите названия стройматериалов (введите 'стоп' для завершения):")
while True:
    material = input()
    if material.lower() == 'стоп':
        break
    materials_queue.append(material)
print("Очередь стройматериалов:", list(materials_queue))

# Действие 8: Изменение имени в списке
# Примечание: Здесь предполагается, что пользователь вводит индекс вручную
# и что имя китайского императора уже известно и сохранено в переменной `emperor_name`
emperor_name = 'Известное имя императора'
index_to_change = int(input("Введите индекс для замены имени:"))
sorted_names = sorted(random_full_names)
sorted_names[index_to_change] = emperor_name
print("Измененный список имен:", sorted_names)

# Действие 9: Связный список странных названий населенных пунктов
# Примечание: Здесь предполагается, что пользователь вводит названия и индексы вручную
linked_list = {
    'Начало': 1,
    'Следующий': 2,
    'Еще Один': 3,
    # ...
}
# Пользователь вводит название для удаления и индекс для вставки "Конец"
name_to_remove = input("Введите название для удаления:")
index_to_insert = int(input("Введите индекс для вставки 'Конец':"))
# Удаление и вставка
if name_to_remove in linked_list:
    del linked_list[name_to_remove]
linked_list['Конец'] = index_to_insert
print("Связный список с изменениями:", linked_list)