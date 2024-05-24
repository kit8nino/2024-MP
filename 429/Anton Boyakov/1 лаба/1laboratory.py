import datetime as dt
import random
import queue

school_rates = {'Русский': 4,
                'Литература': 4,
                'Алгебра': 4,
                'Информатика': 5,
                'Физика': 5,
                'Биология': 1,
                'Химия': 3,
                'Геометрия': 4,
                'История': 2,
                'География': 4,
                'Английский': 5,
                'Физическая культура': 3,
                'Экономика': 3,
                'Технология': 5}

names = ['Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Алексей', 'Максим', 'Евгений', 'Антон', 'Владимир']
surnames = ['Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Попов', 'Сергеев', 'Волков', 'Васильев']
random_names = []
for i in range(30):
    random_names +=[names[random.randint(0, len(names) - 1)] + ' ' + surnames[random.randint(0, len(surnames) - 1)]]
western_actor = ('John Wayne', dt.datetime(1907, 5, 26))
home_tamandua = 'Король Джулиан'

#1
print('задание 1')
print('Средняя оценка: ', sum(school_rates.values())/len(school_rates), '\n')

#2
print('задание 2')
unique_names = []
for name in random_names:
    if name in unique_names:
        continue
    else:
        unique_names.append(name)
print(len(unique_names), 'Уникальных имен:', unique_names, '\n')

#3
print('задание 3')
print("Длина всех названий предметов: ", len("".join(school_rates.keys())), '\n')

#4
print('задание 4')
all_letters = []
for key in school_rates:
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
binary_tamandua = [bin(ord(letter))[2:] for letter in home_tamandua]
print('Бинарное имя тамандуа:', binary_tamandua, '\n')
for elem in binary_tamandua: 
    print(chr(int(elem,2)))

#6
print('задание 6')
print('Дней с рождения', western_actor[0], ':', dt.datetime.today() - western_actor[1], '\n')

#7
print('задание 7')
build_materials = queue.Queue()
material = ''
while material != '!':
    material = input("Введите материалы('!' = выход):")
    if material != '!': build_materials.put(material)
print(build_materials.queue, '\n')


#8
print('задание 8')
year, month, day = western_actor[1].year, western_actor[1].month, western_actor[1].day
number = (day + month**2 + year) % 39 + 1 # =9
chinese_emperor = 'Чжоу И-ван'
index = int(input('Введите индекс(0-29):'))
random_names.sort()
random_names[index] = chinese_emperor
print(random_names, '\n')


#9
print('задание 9')
towns = ['Большая Пысса', 'Ломки', 'Куриловка', 'Лохово', 'Факфак', 'Чуваки', 'Красная Могила', 'Хотелово',
                       'Добрые Пчелы', 'Синегубово', 'Большое Бухалово','Старые Черви']
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
            print('Нет такого города в списке')
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
for elem in towns:
    mer.append(elem)
mer.display()

mer.delete(input("Введите название города для удаления:"))
mer.display()

mer.remove(int(input("Введите индекс города для замены его названия на 'Конец':")))
mer.display()


