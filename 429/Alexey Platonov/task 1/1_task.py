import datetime as dt
import queue
import random

school_scores = {'Русский': 3,
                 'Физика': 5,
                 'Литература': 5,
                 'Алгебра': 4,
                 'Информатика': 3,
                 'Английский': 5,
                 'Биология': 2,
                 'Геометрия': 4,
                 'Химия': 3,
                 'История': 2,
                 'География': 4,
                 'Физическая культура': 5,
                 'Обществознание': 3,
                 'ОБЖ': 5}

western_actor = ('Robert Mitchum', dt.datetime(1917, 8, 6))
first_names = ['Иван', 'Александр', 'Сергей', 'Дмитрий', 'Андрей', 'Алексей', 'Евгений', 'Максим', 'Владимир', 'Денис']
sec_names = ['Иванов', 'Петров', 'Кузнецов', 'Смирнов', 'Сергеев', 'Попов', 'Васильев', 'Волков']
names = []
for i in range(30):
    names +=[first_names[random.randint(0, len(first_names) - 1)] + ' ' + sec_names[random.randint(0, len(sec_names) - 1)]]
home_tamandua = 'Змей Горыныч'

#1
print('задание 1')
print('Средняя оценка: ', sum(school_scores.values())/len(school_scores), '\n')

#2
print('задание 2')
unique_names = []
for i in names:
    if i in unique_names:
        continue
    else:
        unique_names.append(i)
print(len(unique_names), 'Уникальных имен:', unique_names, '\n')

#3
print('задание 3')
print("Длина названий всех предметов: ", len("".join(school_scores.keys())), '\n')

#4
print('задание 4')
all_letters = []
for key in school_scores:
    unique_letters = ''
    for letter in key:
        if letter in unique_letters:
            continue
        else:
            unique_letters += letter
    all_letters += [unique_letters]
print('Уникальные буквы в названиях предметов:', all_letters, '\n')

#5
print('задание 5')
bin_tamandua = []
print(home_tamandua)
for letter in home_tamandua:
    bin_tamandua += [bin(ord(letter))[2:] ]
print('Бинарное имя тамандуа:', bin_tamandua, '\n')

#6
print('задание 6')
print('Дней с рождения', western_actor[0], ':', dt.datetime.today() - western_actor[1], '\n')

#7
print('задание 7')
build_materials = queue.Queue()
material = ''
while material != '&':
    material = input("Введите материалы('&' = выход):")
    if material != '&': build_materials.put(material)
print(build_materials.queue, '\n')


#8
print('задание 8')
year, month, day = western_actor[1].year, western_actor[1].month, western_actor[1].day
number = (day + month**2 + year) % 39 + 1 # =38
chinese_emperor = 'Чжоу Нань-ван'
index = int(input('Введите индекс(0-29):'))
names.sort()
names[index] = chinese_emperor
print(names, '\n')


#9
print('задание 9')
villages = ['Большие Пупсы', 'Манды', 'Дно', 'Тухлянка', 'Большое Струйкино', 'Иннах', 'Засосная', 'Верхнее Зачатье',
                       'Муходоево', 'Синегубово', 'Новые Алгаши','Мусорка']
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

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current:
            if current.data == value:
                break
            previous = current
            current = current.next
        if current is None:
            print('Такого города нет')
        else:
            previous.next = current.next

    def display(self):
        current_node = self.head
        data = []
        while current_node:
            data += [current_node.data]
            current_node = current_node.next
        print(data, '\n')

mer = LinkedList()
for elem in villages:
    mer.append(elem)
mer.display()

mer.delete(input("Удалить город:"))
mer.display()

mer.remove(int(input("Переименовать город на 'Конец' по индексу:")))
mer.display()


