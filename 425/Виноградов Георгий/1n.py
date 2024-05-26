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

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, index):
        step = 0
        if index == 0:
            self.head.data = "Конец"
        else:
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
                if step != self.len() - 1:
                    data_new = current_node.next.data
                    current_node.data = data_new
                    current_node = current_node.next
                    step += 1
                else:
                    data_new = current_node.next.data
                    current_node.data = data_new
                    current_node.next = None
                    break

    def len(self):
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


list = List()

list.append("0 Ширяево")
list.append("1 Верхнее Зачатье")
list.append("2 Голодранкино")
list.append("3 Муходоево")
list.append("4 Синегубово")
list.append("5 Кундрючья")
list.append("6 Заячий пузырь")
list.append("7 Синие Лепяги")
list.append("8 Овнище")
list.append("9 Манды")

list.remove(int(input("Введите цифру, которую нужно заменить словом Конец: ")))
list.insert(int(input("Введите номер для удаления: ")))
list.display()
