import random
from datetime import date

# Оценки предметов в аттестате

certificate = {
    'алгебра': 5,
    'геометрия': 5,
    'информатика': 5,
    'русский язык': 4,
    'литература': 4,
    'английский': 5,
    'биолоия': 4,
    'музыка': 5,
    'история': 5,
    'обществознание': 5,
    'география': 5,
    'физика': 5,
    'химия': 4,
    'обж': 5,
    'физкультура': 5
}

# Полное Имя и дата рождения актера из вестерна 1960х годов

actor_date = ('Джон', ' Уэйл', '11.06.1907')

# Список из имени и фамилии, по таблице самых популярных

popular_name_man = ['Александр','Иван','Сергей','Дмитрий','Алексей',
                    'Андрей','Максим','Евгений','Михаил','Владимир']

popular_surname_man = ['Иванов','Смирнов','Петров','Кузнецов',
                       'Волков','Соколов','Белов','Морозов']

popular_name_woman = ['Елена','Екатерина','Наталья','Мария','Ольга',
                      'Светлана','Татьяна','Ирина','Юлия','Анастасия']

popular_surname_woman = ['Иванова', 'Смирнова', 'Кузнецова', 'Петрова', 
                         'Волкова', 'Морозова', 'Соколова', 'Романова']

# Имя для домашнего тамандуа
pet = 'Легкий Демон'

person_data = []

for i in range(0, len(popular_name_man)):
    random_name_man = random.choice(popular_name_man)
    random_surname_man = random.choice(popular_surname_man)
    person_data.append(random_name_man)
    person_data.append(random_surname_man)


for i in range(0, len(popular_name_woman)):
    random_name_woman = random.choice(popular_name_woman)
    random_surname_woman = random.choice(popular_surname_woman)
    person_data.append(random_name_woman)
    person_data.append(random_surname_woman)

# Задание 1-9 

print("Задание 1")

average_score = sum(certificate.values())/len(certificate)
print("Средняя оценка в аттестате:", average_score)

print("\nЗадание 2")

all_names = popular_name_man + popular_name_woman
unique_names = set(all_names)
for name in unique_names:
    print(name)

print("\nЗадание 3")

total_length = -1  # русский язык написан через пробел

for subject in certificate:
    total_length += len(subject)

print("Общая длина всех названий предметов:", total_length)

print("\nЗадание 4")

unique_letters = set()

for subject in certificate:
    for letter in subject:
        unique_letters.add(letter)

print("Уникальные буквы в названиях предметов:")
for letter in sorted(unique_letters):
    print(letter, end="")

print("\nЗадание 5")

pet_bytes = pet.encode('utf-8')
binary_string = ''.join(format(byte, '08b') for byte in pet_bytes)
print("Имя домашнего тамандуа в бинарном виде:")
print(binary_string)

print("\nЗадание 6")

birth_date_str = actor_date[2]
birth_date = date(
    int(birth_date_str[-4:]), int(birth_date_str[3:5]), int(birth_date_str[:2]))

today = date.today()

days_since_birth = (today - birth_date).days

print(f"Количество дней от даты рождения актера {actor_date[0]}{actor_date[1]} ({birth_date_str}) до текущей даты ({today}): {days_since_birth}")

print("\nЗадание 7")

material_list = []

while True:
    material = input("Введите строительный материал ('стоп' для завершения): ")
    if material.lower() == 'стоп':
        break
    material_list.append(material)

print("Список строительных материалов:")
for material in material_list:
    print(material)
#print(material_list)

print("\nЗадание 8")
# Получаем информацию о дате рождения актера
name, surname, date_of_birth = actor_date

# День, месяц и год из даты рождения
day, month, year = map(int, date_of_birth.split('.'))

# Номер императора
number = (day + month**2 + year) % 39 + 1

# Список императоров династии Чжоу
imperator_list = [
    'Вэнь-ван', 'У-ван', 'Чжуан-ван', 'Си-ван', 'Хуэй-ван', 'Ин-ван', 'Сюань-ван',
    'Юй-ван', 'Пин-ван', 'Хуань-ван', 'Чжуан-ван', 'Си-ван', 'Цзинь-ван', 'Лин-ван',
    'Цзин-ван', 'Дао-ван', 'Сюань-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван', 'Дин-ван', 'Цзянь-ван', 'Лин-ван',
    'Цзин-ван', 'Сянь-ван', 'Шэнь-шэн-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван'
]

imperator_name = imperator_list[number - 1]
index_to_replace = 2*int(input("fВведите индекс имени для замены (от 0 до 19):"))

if index_to_replace < len(person_data) and person_data[index_to_replace] in popular_name_man + popular_name_woman:
    person_data[index_to_replace] = imperator_name
    print(f"Отсортированный список с измененным именем: {person_data}")
else:
    print("Неверный индекс")

print("\nЗадание 9")

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

names = ["Трусово", "Бумба-Яр", "Гадюкино", "Дрезны",
         "Дно", "Косяковка", "Кукуевка", "Муходоево"]

linked_list = create_linked_list(names)

current = linked_list
while current is not None:
    print(current.name)
    current = current.next

to_remove = input("Введите название населенного пункта для удаления: ")
linked_list = remove_node(linked_list, to_remove)

to_insert = input("Введите индекс, куда вставить город 'Конец' (от 1 до 8): ")
to_insert_index = int(to_insert)-1
linked_list = insert_node(linked_list, to_insert_index, "Конец")

current = linked_list
while current is not None:
    print(current.name)
    current = current.next