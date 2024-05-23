import random
import string
import datetime
import collections


# 1. Предметы в школьном аттестате
grades = {
    "Математика": 5,
    "Физика": 4,
    "Химия": 3,
    "Биология": 5,
    "История": 4,
    "География": 5,
    "Литература": 4,
    "Русский язык": 5,
    "Иностранный язык": 3,
    "Информатика": 5,
    "Физкультура": 4,
    "МХК": 4,
    "Технология": 5,
    "Обществознание": 4
}

# 2. Полное имя с фамилией и дата рождения любого актера из вестерна 1960х годов
actor = ("John Vane", datetime.date(1907, 5, 26))

# 3. Челябинск
first_names = ["Иван", "Александр", "Сергей", "Андрей", "Дмитрий", "Алексей", "Максим", "Евгений"]
last_names = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Волков", "Васильев", "Сергеев", "Петров"]
names_list = [(name, surname) for name in first_names for surname in last_names]
random.shuffle(names_list)

# 4. Имя для домашнего тамандуа
pet_name = "Шустрый Муравьед"


# 1. Вывести среднюю оценку в аттестате
average_grade = sum(grades.values()) / len(grades)
print(f"Средняя оценка в аттестате: {average_grade}")

# 2. Вывести уникальные имена среди взятых из таблицы популярных
print("Список из имени и фамилии:", names_list)
unique_names = list(set([name for name, _ in names_list]))
print(f"Уникальные имена: {unique_names}")

# 3. Общая длина всех названий предметов
total_length_subject_names = sum(len(subject) for subject in grades)
print(f"Общая длина всех названий предметов: {total_length_subject_names}")

# 4. Уникальные буквы в названиях предметов
unique_letters = set(''.join(grades.keys()))
print(f"Уникальные буквы в названиях предметов: {unique_letters}")

# 5. Имя вашего домашнего тамандуа в бинарном виде
binary_pet_name = ' '.join(format(ord(char), '08b') for char in pet_name)
print(f"Имя домашнего тамандуа в бинарном виде: {binary_pet_name}")

# 6. Количество дней от даты рождения актера вестерна до текущей даты
today = datetime.date.today()
days_since_birth = (today - actor[1]).days
print(f"Количество дней от даты рождения актера до текущей даты: {days_since_birth}")

# 7. FIFO очередь для стройматериалов
materials = collections.deque()
while True:
    material = input("Введите стройматериал (или 'стоп' для завершения): ")
    if material.lower() == 'стоп':
        break
    materials.append(material)

print("Введенные стройматериалы:")
while materials:
    print(materials.popleft())

#8
# Имя китайского императора династии Чжоу 
index = int(input("Введите индекс для изменения имени в списке популярных имен и фамилий: "))
print("Имя которое будет заменено:", names_list[index])
names_list.sort()
names_list[index] = ("Чжоу", "Сяо-ван")
print(f"Имя китайского императора династии Чжоу для замены в списке имён: {names_list[index]}")
print("Список имён с вставленным именем китайскго императора", names_list)

#9
cities = ['Грязи', 'Большое Бухалово', 'Хреновое', 'Да-Да', 'Старые-черви', 'Манды', 'Иннах']
print(cities)

# Получаем название города для удаления и индекс для вставки
value = input('Введите название города, который вы хотите удалить: ')
index = int(input('Введите индекс массива, куда вы хотите вставить город Конец: '))

# Удаляем город из списка
if value in cities:
    cities.remove(value)
else:
    print(f'Город {value} не найден в списке.')

# Вставляем новый город в указанный индекс
cities.insert(index, 'Конец')

# Печатаем итоговый список городов
print('Города: ', cities)