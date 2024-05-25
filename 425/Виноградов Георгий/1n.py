import datetime
import random
import queue

# Данные
clint_eastwood = ("Клинт Иствуд", 31, 5, 1930)
School_marks = {
    "русский язык": 4,
    "литература": 5,
    "алгебра": 5,
    "геометрия": 5,
    "история": 4,
    "информатика": 5,
    "ОБЖ": 5,
    "физкультура": 5,
    "обществознание": 4,
    "химия": 4,
    "физика": 5,
    "география": 4,
    "английский язык": 5,
    "биология": 4
}
men_names = ['Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Алексей', 'Максим', 'Евгений', 'Антон', 'Владимир']
women_names = ['Екатерина', 'Мария', 'Елена','Анна','Ольга', 'Анастасия',  'Наталья', 'Ирина', 'Татьяна', 'Светлана']
men_surnames = ['Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Попов', 'Сергеев','Волков', 'Васильев']
women_surnames = ['Иванова','Петрова', 'Кузнецова', 'Смирнова','Попова', 'Волкова', 'Васильева', 'Романова']
Name_of_tamandua = "Таинственный Пират"
popular_names = []

for _ in range(10):
    random_male_name = random.choice(men_names)
    random_male_surname = random.choice(men_surnames)
    popular_names.append(random_male_name + ' ' + random_male_surname)

for _ in range(10):
    random_female_name = random.choice(women_names)
    random_female_surname = random.choice(women_surnames)
    popular_names.append(random_female_name + ' ' + random_female_surname)
# №1
avg_mark = sum(School_marks.values()) / len(School_marks)
print("1) Средняя оценка в аттестате:", avg_mark)

# №2
unique_names = list(set(men_names + women_names))
print("2) Уникальные имена среди родственников:", unique_names)

# №3
total_subject_len = sum(len(subject) for subject in School_marks)
print("3) Общая длина всех названий предметов:", total_subject_len)

# №4
unique_letters = set(''.join(School_marks.keys()))
print("4) Уникальные буквы в названиях предметов:", unique_letters)

# №5
tamandua_bin_name = ''.join(format(x, '08b') for x in bytearray(Name_of_tamandua, 'utf-8'))
print("5) Имя вашего домашнего тамандуа в бинарном виде:", tamandua_bin_name)

# №6
actor_birthdate = datetime.datetime(clint_eastwood[3], clint_eastwood[2], clint_eastwood[1])
days_since_birth = (datetime.datetime.now() - actor_birthdate).days
print("6) Количество дней от даты рождения актера до текущей даты:", days_since_birth)

# Задание 7
print("Задание 7")
fifo_queue = queue.Queue()
flag = True

print("Введите название строительного материала, введите stop, чтобы остановиться и показать список:")

while flag:
    queue_element = input()

    if queue_element == "stop":
        print("Список строительных материалов:")
        while not fifo_queue.empty():
            res = fifo_queue.get()
            print(res)
        break
    else:
        fifo_queue.put(queue_element)

# Задание 8
print("Задание 8")
number = (3 + 11**2 + 1921) % 39 + 1  # 18
emperor_name = "Чжоу Хуэй-Ван"

print("Введите номер для замены:")
i = int(input())

# Создаем список с названиями
popular_names[i] = emperor_name

print(popular_names)

print("Задание 9")

# Создание списка городов
cities = ["Ширяево", "Верхнее Зачатье", "Голодранкино", "Муходоево", "Синегубово", "Кундрючья", "Заячий пузырь", "Синие Лепяги", "Овнище", "Манды"]

# Вывод списка городов
print("Список городов:")
for index, city in enumerate(cities):
    print(f"{index} {city}")

# Замена названия города на "Конец"
index_to_replace = int(input("Введите цифру, которую нужно заменить словом Конец: "))
if 0 <= index_to_replace < len(cities):
    cities[index_to_replace] = "Конец"

# Удаление названия города по индексу
index_to_remove = int(input("Введите номер для удаления: "))
if 0 <= index_to_remove < len(cities):
    del cities[index_to_remove]

# Вывод обновленного списка городов
print("Обновленный список городов:")
for index, city in enumerate(cities):
    print(f"{index} {city}")
