import datetime
import random
import queue

# Словарь с оценками предметов
grades = {
    "Русский язык": 5, 
    "Алгебра": 4,
    "Геометрия": 4,
    "Литература": 5,
    "Химия": 4,
    "География": 5,
    "Английский язык": 5,
    "Информатика": 5,
    "ОБЖ": 5,
    "Физика": 5,
    "История": 5,
    "Обществознание": 5,
    "Физ-ра": 5,
    "Биология": 4
}

# Данные о западном актере
western_actor = ("Чарльз Бронсон", datetime.date(1921, 11, 3))

# Списки имён и фамилий
male_names = ['Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Алексей', 'Максим', 'Евгений', 'Владимир', 'Денис']
female_names = ['Елена', 'Екатерина', 'Мария','Анастасия', 'Ольга','Наталья',  'Анна', 'Татьяна', 'Ирина', 'Юлия']
male_surnames = ['Иванов', 'Петров', 'Сергеев', 'Смирнов', 'Кузнецов', 'Попов', 'Волков', 'Васильев']
female_surnames = ['Иванова','Петрова', 'Кузнецова', 'Смирнова','Попова', 'Васильева', 'Волкова', 'Романова']

# Случайные имена и фамилии
random_names = []
for _ in range(10):
    random_male_name = random.choice(male_names)
    random_male_surname = random.choice(male_surnames)
    random_names.append(random_male_name + ' ' + random_male_surname)

for _ in range(10):
    random_female_name = random.choice(female_names)
    random_female_surname = random.choice(female_surnames)
    random_names.append(random_female_name + ' ' + random_female_surname)

# Имя для питомца
pet_name = "Тестостероновый монстр"

# Задание 1: Вычисление средней оценки
print("Задание 1")
total_grades = sum(grades.values())
average_grade = total_grades / len(grades)
print("Средний балл =", average_grade)

# Задание 2:
print("Задание 2")
names = [name.split()[0] for name in random_names]
unique_names = [name for name in names if names.count(name) == 1]
print("\n".join(unique_names))

# Задание 3: 
print("Задание 3")
total_letters = sum(len(subject) for subject in grades.keys())
print("Общее количество букв в названиях предметов =", total_letters)

# Задание 4:
print("Задание 4")
concatenated_str = "".join(grades.keys())
unique_letters = [char for char in concatenated_str if concatenated_str.count(char) == 1]
print("\n".join(unique_letters))

# Задание 5: 
print("Задание 5")
bits = bin(int.from_bytes(pet_name.encode('utf-8', 'surrogatepass'), 'big'))[2:]
print(bits.zfill(8 * ((len(bits) + 7) // 8)))

# Задание 6: 
print("Задание 6")
today = datetime.date.today()
age_difference = today - western_actor[1]
print(age_difference)

# Задание 7:
print("Задание 7")
material_queue = queue.Queue()
print("Введите название строительного материала, или 'stop' для завершения:")
while True:
    material = input()
    if material == "stop":
        print("Список строительных материалов:")
        while not material_queue.empty():
            print(material_queue.get())
        break
    else:
        material_queue.put(material)

# Задание 8: 
print("Задание 8")
number = (3 + 11**2 + 1921) % 39 + 1  # 18
emperor_name = "Чжоу Хуэй-Ван"
print("Введите номер для замены:")
index = int(input())
random_names[index] = emperor_name
print(random_names)

# Задание 9: 
print("Задание 9")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def remove(self, index):
        if index == 0:
            self.head.data = "Конец"
        else:
            step = 0
            current_node = self.head
            while step < index:
                current_node = current_node.next
                step += 1
            current_node.data = "Конец"

    def insert(self, index):
        step = 0
        current_node = self.head
        while current_node.next:
            if step < index:
                current_node = current_node.next
                step += 1
            elif step == index:
                current_node.data = current_node.next.data
                current_node = current_node.next
                step += 1
            else:
                if step != self.length() - 1:
                    data_new = current_node.next.data
                    current_node.data = data_new
                    current_node = current_node.next
                    step += 1
                else:
                    data_new = current_node.next.data
                    current_node.data = data_new
                    current_node.next = None
                    break

    def length(self):
        step = 0
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            step += 1
        return step      

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
linked_list.append("0 Дебеловское")
linked_list.append("1 Хохотуй")
linked_list.append("2 Выдропужск")
linked_list.append("3 Лохи")
linked_list.append("4 Хреновое")
linked_list.append("5 Чуваки")
linked_list.append("6 Свиновье")
linked_list.append("7 Большие Пупсы")
linked_list.append("8 Большой Куяш")
linked_list.append("9 Хотелово")

index_remove = int(input("Введите номер элемента, который нужно заменить на 'Конец': "))
index_insert = int(input("Введите номер для удаления: "))
linked_list.remove(index_remove)
linked_list.insert(index_insert)
linked_list.display()
