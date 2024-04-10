import datetime
import random

#Исходные данные
academic_subjects = {
    "русский язык": 4, 
    "алгебра": 4,
    "геометрия": 4,
    "литература": 5,
    "химия": 4,
    "география": 4,
    "английский язык": 4,
    "информатика": 5,
    "обж": 5,
    "физика": 4,
    "история": 5,
    "обществознание": 5,
    "физкультура": 5,
    "биология": 4
    }

western_actor = ("Чарльз Бронсон", datetime.date(1921, 11, 3))

#Популярные имена (Нижний Новгород)
names = ["Александр", "Иван", "Сергей", "Дмитрий", "Алексей", "Андрей", "Максим", "Евгений", "Михаил", "Владимир"]
surnames = ["Иванов", "Смирнов", "Петров", "Кузнецов", "Волков", "Соколов", "Белов", "Морозов"]
popular_names = [None] * 20

for i in range(20):
    popular_names[i] = names[random.randint(0, 9)] + " " + surnames[random.randint(0, 7)]

pet_name = "карнавальный Джо"

#Задание 1
print("Задание 1")

sum = 0
count = 0

for key, value in academic_subjects.items():
    sum += value
    count += 1

average_grade = sum / count

print("average grade = " + str(average_grade))

#Задание 2
print("Задание 2")

name = [None] * 20

for i in range(20):
    split_str = popular_names[i].split()
    name[i] = split_str[0]

for i in range(20):
    count = 0
    for j in range(0, 20, 1):
        if(name[i] == name[j]) and (i != j):
            count += 1
    if(count == 0):
        print(name[i])

#Задание 3
print("Задание 3")

sum_char = 0

for key, value in academic_subjects.items():
    sum_char += len(key)

print("Сумма букв предметов = " + str(sum_char))

#Задание 4
print("Задание 4")

big_str = ""

for key, value in academic_subjects.items():
    big_str += str(key)

for i in range(len(big_str)):
    count = 0
    for j in range(len(big_str)):
        if (big_str[i] == big_str[j]) and (i != j):
            count += 1
    if(count == 0):
        print(big_str[i])

#Задание 5
print("Задание 5")

bits = bin(int.from_bytes(pet_name.encode('utf-8', 'surrogatepass'), 'big'))[2:]
print(bits.zfill(8 * ((len(bits) + 7) // 8)))

#Задание 6
print("Задание 6")

today = datetime.date.today()
print(today - western_actor[1])

#Задание 7
print("Задание 7")

fifo_queue = queue.Queue()
flag = True

print("Введите название стройматериала, для остановки и вывода введите 0")

while flag:
    queue_element = input()

    if queue_element == "0":
        print("Список стройматериалов:")
        for i in range(fifo_queue.qsize()):
            res = fifo_queue.get()
            print(res)
        break
    else:
        fifo_queue.put(queue_element)

#Задание 8
print("Задание 8")

number = (3 + 11**2 + 1921) % 39 + 1 #18
emperor_name = "Чжоу Хуэй-ван"

print("Введите номер для замены: ")
i = int(input())

popular_names[i] = emperor_name

print(popular_names)

#Задание 9
print("Задание 9")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
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
        if index == 0:
            self.head.next = None
        else:
            current_node = self.head
            while current_node.next:
                if step < index:
                    current_node = current_node.next
                    step += 1
                elif step == index:
                    current_node = current_node.next
                    current_node = current_node.next
                    step += 1
                else:
                    if step != list.len() - 2:
                        data_new = (current_node.next).data
                        current_node.data = data_new
                        current_node = current_node.next
                        step += 1
                    else:
                        data_new = (current_node.next).data
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

list = LinkedList()

list.append("Большая Пысса")
list.append("Дно")
list.append("Манды")
list.append("Иннах")
list.append("Старые черви")
list.append("Засосная")
list.append("Чуваки")
list.append("Красная Могила")
list.append("Хреновое")
list.append("Верхнее Зачатье")

list.remove(0)
list.insert(3)
list.display()
