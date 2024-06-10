import datetime
import random
import queue

predmet = {
    "русский язык": 4, 
    "алгебра": 5,
    "геометрия": 5,
    "литература": 4,
    "химия": 5,
    "география": 5,
    "английский язык": 5,
    "информатика": 5,
    "ОБЖ":4,
    "физика": 5,
    "история": 4,
    "обществознание": 4,
    "физкультура": 5,
    "биология": 3
}

western_actor = ("Paul Newman", datetime.date(1925, 1, 26))


men_names = [
    'Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 
    'Алексей', 'Максим', 'Евгений', 'Антон', 'Владимир'
]

women_names = [
    'Екатерина', 'Мария', 'Елена','Анна', 
    'Ольга','Анастасия',  'Наталья', 'Ирина', 'Татьяна', 'Светлана'
]

men_surnames = [
    'Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Попов', 'Сергеев', 
    'Волков', 'Васильев'
]

women_surnames = [
    'Иванова','Петрова', 'Кузнецова', 'Смирнова','Попова', 'Волкова', 
    'Васильева', 'Романова'
]


popular_names = []

for _ in range(10):
    random_male_name = random.choice(men_names)
    random_male_surname = random.choice(men_surnames)
    popular_names.append(random_male_name + ' ' + random_male_surname)

for _ in range(10):
    random_female_name = random.choice(women_names)
    random_female_surname = random.choice(women_surnames)
    popular_names.append(random_female_name + ' ' + random_female_surname)


pet_name = "Яростный Лев"

# Задание 1
print("Задание 1")
total_grades = 0
subject_count = 0

for subject, grade in predmet.items():
    total_grades += grade
    subject_count += 1

average_grade = total_grades / subject_count
print("Средний балл =", average_grade)

#Задание 2
print("Задание 2")
names = [None] * 20

for i in range(20):
    split_name = popular_names[i].split()
    names[i] = split_name[0]

for i in range(20):
    count = 0
    for j in range(0, 20, 1):
        if (names[i] == names[j]) and (i != j):
            count += 1
    if count == 0:
        print(names[i])

# Задание 3
print("Задание 3")
total_letters = 0

for subject, _ in predmet.items():
    total_letters += len(subject)

print("Общее количество букв в названиях предметов =", total_letters)

#Задание 4
print("Задание 4")
concatenated_str = ""

for subject, _ in predmet.items():
    concatenated_str += str(subject)

for i in range(len(concatenated_str)):
    count = 0
    for j in range(len(concatenated_str)):
        if (concatenated_str[i] == concatenated_str[j]) and (i != j):
            count += 1
    if count == 0:
        print(concatenated_str[i])

#Задание 5
print("Задание 5")
bits = bin(int.from_bytes(pet_name.encode('utf-8', 'surrogatepass'), 'big'))[2:]
print(bits.zfill(8 * ((len(bits) + 7) // 8)))

# Задание 6
print("Задание 6")
сегодня = datetime.date.today()
print(сегодня - western_actor[1])

# Задание 7
print("Задание 7")
fifo_queue = queue.Queue()
flag = True

print("Введите название строительного материала, введите stop, чтобы остановиться и показать список:")

while flag:
    queue_element = input()

    if queue_element == "stop":
        print("Список строительных материалов:")
        for i in range(fifo_queue.qsize()):
            res = fifo_queue.get()
            print(res)
        break
    else:
        fifo_queue.put(queue_element)

# Задание 8
print("Задание 8")
number = (3 + 11**2 + 1921) % 39 + 1  # 18
emperor_name = "Чжоу Си-Ван"

print("Введите номер для замены:")
i = int(input())

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

list.append("0 Большые Пупсы")
list.append("1 Тухлянка")
list.append("2 Лохово")
list.append("3 Баклань")
list.append("4 Косякова")
list.append("5 Цаца")
list.append("6 Лысая Балда")
list.append("7 СиниеЛепяги")
list.append("8 Голодранкино")
list.append("9 Вобля")

list.remove(int(input("Введите цифру, которую нужно заменить словом Конец: ")))
list.insert(int(input("Введите номер для удаления: ")))
list.display()
