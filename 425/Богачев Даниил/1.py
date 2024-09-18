import random
from datetime import date

grades = {
    "русский_язык": 5,
    "алгебра": 5,
    "геометрия": 4,
    "литература": 5,
    "химия": 4,
    "география": 4,
    "английский_язык": 4,
    "информатика": 5,
    "ОБЖ": 5,
    "физика": 5,
    "история": 5,
    "обществознание": 4,
    "физкультура": 5,
    "биология": 4
}

actor_info = ('Джон', 'Расселл', '03.01.1921')

popular_male_names = ['Иван', 'Александр', 'Сергей', 'Дмитрий', 'Андрей', 'Дмитрий', 'Алексей', 'Руслан', 'Артур', 'Денис']
popular_male_surnames = ['Иванов', 'Петров', 'Васильев', 'Кузнецов', 'Смирнов', 'Каримов', 'Сафин', 'Валеев']
popular_female_names = ['Елена', 'Мария', 'Екатерина', 'Ольга', 'Светлана', 'Ирина', 'Анна', 'Анастасия', 'Юлия', 'Алина']
popular_female_surnames = ['Иванова', 'Петрова', 'Васильева', 'Кузнецова', 'Смирнова', 'Каримова', 'Валеева', 'Сафина']

people = []

for _ in range(len(popular_male_names)):
    name = random.choice(popular_male_names)
    surname = random.choice(popular_male_surnames)
    people.append(f"{name} {surname}")

for _ in range(len(popular_female_names)):
    name = random.choice(popular_female_names)
    surname = random.choice(popular_female_surnames)
    people.append(f"{name} {surname}")

pet_name = 'Лохматый Бруно'

# 1. Средняя оценка в аттестате
print("Задание 1")
average_grade = sum(grades.values()) / len(grades)
print(f"Средняя оценка в аттестате: {average_grade:.2f}")

# 2. Уникальные имена
print("Задание 2")
unique_names = set(popular_male_names + popular_female_names)
print("Уникальные имена:", ", ".join(unique_names))

# 3. Длина всех названий предметов
print("Задание 3")
total_length_of_subjects = sum(len(subject) for subject in grades)
print(f"Общая длина всех названий предметов: {total_length_of_subjects}")

# 4. Уникальные буквы в названиях предметов
print("Задание 4")
unique_letters = set("".join(grades.keys()))
print("Уникальные буквы в названиях предметов:", " ".join(sorted(unique_letters)))

# 5. Имя питомца в бинарном виде
print("Задание 5")
binary_pet_name = ''.join(format(byte, '08b') for byte in pet_name.encode('utf-8'))
print("Имя домашнего тамандуа в бинарном виде:")
print(binary_pet_name)

# 6. Количество дней с даты рождения актера до текущей даты
print("Задание 6")
birth_date = date(int(actor_info[2][6:]), int(actor_info[2][3:5]), int(actor_info[2][:2]))
days_lived = (date.today() - birth_date).days
print(f"Количество дней с даты рождения {actor_info[0]} {actor_info[1]} ({actor_info[2]}) до сегодняшнего дня: {days_lived}")

# 7. Ввод названий строительных материалов
print("Задание 7")
materials = []
while True:
    material = input("Введите название строительного материала (или 'stop' для завершения): ")
    if material.lower() == 'stop':
        break
    materials.append(material)
print("Список материалов:")
print("\n".join(materials))

# 8. Персонализация списка имен
print("Задание 8")
day, month, year = map(int, actor_info[2].split('.'))
special_number = (day + month**2 + year) % 39 + 1
zhou_emperors = [
    'Вэнь-ван', 'У-ван', 'Чжуан-ван', 'Си-ван', 'Хуэй-ван', 'Ин-ван', 'Сюань-ван',
    'Юй-ван', 'Пин-ван', 'Хуань-ван', 'Чжуан-ван', 'Си-ван', 'Цзинь-ван', 'Лин-ван',
    'Цзин-ван', 'Дао-ван', 'Сюань-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван', 'Дин-ван', 'Цзянь-ван', 'Лин-ван',
    'Цзин-ван', 'Сянь-ван', 'Шэнь-шэн-ван', 'Чжао-ван', 'Му-ван', 'Гун-ван', 'И-ван',
    'Ли-ван', 'Сюань-ван', 'Чэнь-ван', 'Куан-ван'
]

index = int(input("Введите индекс: "))
if 1 <= index <= len(people):
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    special_number = (day + month**2 + year) % 39 + 1
    people[index - 1] = zhou_emperors[special_number - 1]
    print("Обновленный список:", people)
else:
    print("Индекс вне диапазона!")

# 9. Работа с односвязным списком
print("Задание 9")
class ListNode:
    def __init__(self, name):
        self.name = name
        self.next = None

def delete_node(head, target_name):
    if not head:
        return head
    if head.name == target_name:
        return head.next
    current = head
    while current.next and current.next.name != target_name:
        current = current.next
    if current.next:
        current.next = current.next.next
    return head

def add_node(head, index, new_name):
    new_node = ListNode(new_name)
    if index == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(index - 1):
        if not current:
            return head
        current = current.next
    new_node.next = current.next if current else None
    if current:
        current.next = new_node
    return head

def build_linked_list(name_list):
    if not name_list:
        return None
    head = ListNode(name_list[0])
    current = head
    for name in name_list[1:]:
        current.next = ListNode(name)
        current = current.next
    return head

towns = ["Хреновое", "Свиновье", "Цаца", "Абракадабра", "Раздериха", "Гадюкино", "Вобля", "Большое Струйкино", "Лысая Балда", "Жалобные", "Небывальщина", "Кукуевка", "Козявкино", "Засосная", "Дешевки"]
linked_list = build_linked_list(towns)

current_node = linked_list
print("Список населённых пунктов:")
while current_node:
    print(current_node.name)
    current_node = current_node.next

town_to_remove = input("Введите название населенного пункта для удаления: ")
linked_list = delete_node(linked_list, town_to_remove)

index_to_insert = int(input("Введите индекс, куда вставить 'Конец': "))
linked_list = add_node(linked_list, index_to_insert, "Конец")

current_node = linked_list
print("Обновленный список населённых пунктов:")
while current_node:
    print(current_node.name)
    current_node = current_node.next
