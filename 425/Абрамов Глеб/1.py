
from datetime import date
import random

# Словарь, составленный из оценок
certificate = {
     "русский_язык": 4, 
    "алгебра": 4,
    "геометрия": 4,
    "литература": 5,
    "химия": 5,
    "география": 5,
    "английский_язык": 5,
    "информатика": 5,
    "ОБЖ":3,
    "физика": 4,
    "история": 5,
    "обществознание": 3,
    "физкультура": 5,
    "биология": 3
}

actor = ('Джон',' Расселл','03.01.1921')

# составление списка из имени и фамилии

popular_name_man = [
    'Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 
    'Алексей', 'Максим', 'Евгений', 'Антон', 'Владимир'
]

popular_surname_man = [   
   'Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Попов', 'Сергеев', 
    'Волков', 'Васильев'
]

popular_name_woman = [   
   'Екатерина', 'Мария', 'Елена','Анна', 
    'Ольга','Анастасия',  'Наталья', 'Ирина', 'Татьяна', 'Светлана'
]

popular_surname_woman = [
    'Иванова','Петрова', 'Кузнецова', 'Смирнова','Попова', 'Волкова', 
    'Васильева', 'Романова'     
]

person_data = []
#('Мужчины: ')
for i in range(0,len(popular_name_man)):
    random_name_man = random.choice(popular_name_man)
    random_surname_man = random.choice(popular_surname_man)
    person_data.append(random_name_man)
    person_data.append(random_surname_man)

#( 'Женщины: ')
for i in range(0,len(popular_name_man)):
    random_name_woman = random.choice(popular_name_woman)
    random_surname_woman = random.choice(popular_surname_woman)
    person_data.append(random_name_woman)
    person_data.append(random_surname_woman)


#Имя тамандуа
name_pet = 'Овальный Червонец'

# 1-9 Задание

print ("1 задание")

total_score = sum(certificate.values())
num_subjects = len(certificate)
average_score = total_score / num_subjects
print(f"Средняя оценка в аттестате: {average_score}")

print ("2 задание")

full_nam = popular_name_man + popular_name_woman
unique_names = set(full_nam)
for name in unique_names:
    print(name)

print ("3 задание")

total_length = 0 

for subject in certificate:
    total_length += len(subject)

print(f"Длина всех названий предметов: {total_length}")

print ("4 задание")

unique_letters = set()

for subject in certificate:
    for letter in subject:
        unique_letters.add(letter)

print("Уникальные буквы в названиях предметов:")
for letter in sorted(unique_letters):
    print(letter, end=" ")

print ("5 задание")

name_bytes = name_pet.encode('utf-8')

binary_string = ''.join(format(byte, '08b') for byte in name_bytes)

print("Имя домашнего тамандуа в бинарном виде:")
print(binary_string)

print ("6 задание")

birth_date_str = actor[2]
birth_date = date(int(birth_date_str[-4:]), int(birth_date_str[3:5]), int(birth_date_str[:2]))

today = date.today()

days_since_birth = (today - birth_date).days

print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} ({birth_date_str}) до текущей даты ({today}): {days_since_birth}")

print ("7 задание")

material_list = []

while True:
    material_name = input("Введите название строительного материала ('stop' для завершения): ")
    if material_name.lower() == 'stop':
        break
    material_list.append(material_name)

print("Список материалов:")
for material in material_list:
    print(material)
print ("8 задание")
name, surname, date_of_birth = actor

day, month, year = map(int, date_of_birth.split('.'))

number = (day + month**2 + year) % 39 + 1

emperors_zhou = [
    'Вэнь-ван', 'У-ван', 'Чжуан-ван', 'Си-ван', 'Хуэй-ван', 'Ин-ван', 'Сюань-ван',
    'Юй-ван', 'Пин-ван', 'Хуань-ван', 'Чжуан-ван', 'Си-ван', 'Цзинь-ван', 'Лин-ван',
    'Цзин-ван', 'Дао-ван', 'Сюань-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван', 'Дин-ван', 'Цзянь-ван', 'Лин-ван',
    'Цзин-ван', 'Сянь-ван', 'Шэнь-шэн-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван'
]

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

print ("\n9 задание")

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

def remove_node(head, name):
    if head is None:
        return head

    if head.name == name:
        return head.next

    current = head
    prev = None

    while current is not None and current.name != name:
        prev = current
        current = current.next

    if current is not None:
        prev.next = current.next

    return head

def insert_node(head, index, name):
    if index == 0:
        new_node = Node(name)
        new_node.next = head
        return new_node

    current = head

    for _ in range(index - 1):
        if current is None:
            return head
        current = current.next

    new_node = Node(name)
    new_node.next = current.next
    current.next = new_node

    return head

def create_linked_list(names):
    head = Node(names[0])
    current = head

    for name in names[1:]:
        new_node = Node(name)
        current.next = new_node
        current = new_node

    return head

names = ["Жабино","Свиновье","Цаца","Абракадабра", "Бумба-Яр", "Гадюкино", "Дрезны","Добрые Пчелы", "Голодранкино","Жалобные", "Небывальщина", "Кукуевка", "Новая Чертория"," Большая Пысса"," Дешевки" ]

linked_list = create_linked_list(names)

current = linked_list
while current is not None:
    print(current.name)
    current = current.next

to_remove = input("Введите название населенного пункта для удаления: ")
linked_list = remove_node(linked_list, to_remove)

to_insert = input("Введите индекс, куда вставить город 'Конец': ")
to_insert_index = int(to_insert)
linked_list = insert_node(linked_list, to_insert_index, "Конец")

current = linked_list
while current is not None:
    print(current.name)
    current = current.next
