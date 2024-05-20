import random
from datetime import date

# Словарь, составленный из оценок предметов в аттестате

certificate = {
     'русский язык' : 3,         
     'литература' : 5,
     'английский' : 4,     
     'математика' : 4,
     'информатика' : 5,
     'история' : 4,
     'обществознание' : 5,
     'география' : 3,
     'физика' : 3,
     'химия' : 4,
     'биолоия' : 5,
     'музыка' : 4,
     'изо' : 5,
     'технология' : 5,
     'обж' : 5,
     'физкультура' : 5
}


# Полное имя, фамилия и дата рождения актера из вестерна 1960х годов как кортеж

actor = ('Джон',' Расселл','03.01.1921')

# составление списка из имени и фамилии, по таблице самых популярных

popular_name_man = [
    'Александр',
    'Иван',
    'Сергей',
    'Дмитрий',
    'Алексей',
    'Андрей',
    'Максим',
    'Евгений',
    'Михаил',
    'Владимир',
]

popular_surname_man = [   
    'Иванов',
    'Смирнов',
    'Петров',
    'Кузнецов',
    'Волков',
    'Соколов',
    'Белов',
    'Морозов'
]

popular_name_woman = [   
    'Елена',
    'Екатерина',
    'Наталья',
    'Мария',
    'Ольга',
    'Светлана',
    'Татьяна',
    'Ирина',
    'Юлия',
    'Анастасия'
]

popular_surname_woman = [
    'Иванова',
    'Смирнова',
    'Кузнецова',
    'Петрова',
    'Волкова',
    'Морозова',
    'Соколова',
    'Романова'                        
]

person_data = []

#person_data.append('Мужчины: ')
for i in range(0,len(popular_name_man)):
    random_name_man = random.choice(popular_name_man)
    random_surname_man = random.choice(popular_surname_man)
    person_data.append(random_name_man)
    person_data.append(random_surname_man)

#person_data.append( 'Женщины: ')
for i in range(0,len(popular_name_man)):
    random_name_woman = random.choice(popular_name_woman)
    random_surname_woman = random.choice(popular_surname_woman)
    person_data.append(random_name_woman)
    person_data.append(random_surname_woman)

#print(person_data)

#Имя из прилагательного и существительного для домашнего тамандуа
name_pet = 'Ленивый Едок'

# 1-9 Задание

print ("\n1 задание")

total_score = sum(certificate.values())
num_subjects = len(certificate)
average_score = total_score / num_subjects
print(f"Средняя оценка в аттестате: {average_score}")


##################################################################################################
print ("\n2 задание")

all_names = popular_name_man + popular_name_woman
unique_names = set(all_names)
for name in unique_names:
    print(name)


##################################################################################################
print ("\n3 задание")

total_length = -1 # русский язык написан через пробел

for subject in certificate:
    total_length += len(subject)

print(f"Общая длина всех названий предметов: {total_length}")


##################################################################################################
print ("\n4 задание")

unique_letters = set()

for subject in certificate:
    for letter in subject:
        unique_letters.add(letter)

print("Уникальные буквы в названиях предметов:")
for letter in sorted(unique_letters):
    print(letter, end=" ")

##################################################################################################
print ("\n5 задание")

name_bytes = name_pet.encode('utf-8')

binary_string = ''.join(format(byte, '08b') for byte in name_bytes)

print("Имя домашнего тамандуа в бинарном виде:")
print(binary_string)

##################################################################################################
print ("\n6 задание")

birth_date_str = actor[2]
birth_date = date(int(birth_date_str[-4:]), int(birth_date_str[3:5]), int(birth_date_str[:2]))

today = date.today()

days_since_birth = (today - birth_date).days

print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} ({birth_date_str}) до текущей даты ({today}): {days_since_birth}")

##################################################################################################
print ("\n7 задание")

material_list = []

while True:
    material_name = input("Введите название строительного материала ('стоп' для завершения): ")
    if material_name.lower() == 'стоп':
        break
    material_list.append(material_name)

print("Список материалов:")
for material in material_list:
    print(material)

###################################################################################################
print ("\n8 задание")
# Получаем информацию о дате рождения актера
name, surname, date_of_birth = actor

# Извлекаем день, месяц и год из даты рождения
day, month, year = map(int, date_of_birth.split('.'))

# Вычисляем номер императора
number = (day + month**2 + year) % 39 + 1

# Список императоров династии Чжоу
zhou_emperors = [
    'Вэнь-ван', 'У-ван', 'Чжуан-ван', 'Си-ван', 'Хуэй-ван', 'Ин-ван', 'Сюань-ван',
    'Юй-ван', 'Пин-ван', 'Хуань-ван', 'Чжуан-ван', 'Си-ван', 'Цзинь-ван', 'Лин-ван',
    'Цзин-ван', 'Дао-ван', 'Сюань-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван', 'Дин-ван', 'Цзянь-ван', 'Лин-ван',
    'Цзин-ван', 'Сянь-ван', 'Шэнь-шэн-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван'
]

emperor_name = zhou_emperors[number - 1]

index_to_replace = int(input("Введите индекс имени для замены (Вводить только чётные индексы (или 0)) :"))

if index_to_replace < len(person_data) and person_data[index_to_replace] in popular_name_man + popular_name_woman:

    person_data[index_to_replace] = emperor_name
    print(f"Отсортированный список с измененным именем: {person_data}")
else:
    print("Неверный индекс или элемент не является именем.")

##################################################################################################
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

names = ["Абракадабра", "Бумба-Яр", "Гадюкино", "Дрезны", "Жалобные", "Небывальщина", "Кукуевка", "Новая Чертория" ]

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
