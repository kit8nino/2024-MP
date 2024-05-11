# Modules
from random import choice
from datetime import date, datetime


# Data
certificate = {'Физика': 5,
               'Алгебра': 5,
               'Геометрия': 4,
               'Русский язык': 5,
               'Литература': 5,
               'История России': 4,
               'Всеобщая история': 5,
               'Английский язык': 4,
               'Краеведение': 5,
               'Музыка': 5,
               'Технология': 4,
               'Биология': 5,
               'География': 5,
               'Обществознание': 5}

actor = ('Юлий', 'Бринер', '11.07.1920')

data = [choice(['Сергей', 'Иван', 'Александр', 'Андрей',
                'Дмитрий', 'Алексей', 'Максим', 'Кузнецов',
                'Петров', 'Сергеев', 'Волков', 'Попов', 'Васильев'])
        for _ in range(20)]

tamandua_name = 'Пушистый колобок'


# Task 1.1
def task_1_1(d: dict) -> float:
    s = sum(d.values())
    count = len(d.values())

    result = s / count

    return round(result, 2)


# Task 1.2
def task_1_2(a: list) -> list:
    result = []
    for element in a:
        if element[len(element) - 1] != 'в':
            result.append(element)

    return list(set(result))


# Task 1.4
def task_1_4(name: str) -> bin:
    for c in name:
        name = name.replace(c, bin(ord(c)), 1)
    return name


# Task 1.5
def task_1_5(d: dict) -> set:
    s = ""
    for key in d.keys():
        s += key

    s = set(list(s))

    return s


# Task 1.6
def task_1_6(dt: str) -> int:
    today = list(map(int, str(datetime.now().date()).split('-')))
    date_birth = reversed(list(map(int, dt.split('.'))))

    return int((date(*today) - date(*date_birth)).days)


# Task 1.7
def task_1_7():
    q = []
    index = int(input('Введите индекс: '))
    while index != -1:
        title = input('Введите название стройматериала: ')
        index = int(input('Введите индекс: '))
        q.insert(index, title)

    return q


# Task 1.8
def task_1_8(a: list) -> list:
    name = 'Као-ван'
    a.sort()
    index = int(input('Введите индекс: '))
    while True:
        if index < 0 or index > len(a):
            print('Недопустимое значение!')
            index = int(input('Введите индекс: '))
        else:
            break

    a[index] = name

    return a


# Task 1.9
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next

    def insert(self, new_element, position):
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
        pass

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


test = ['Большая Пысса', 'Большие Пупсы', 'Манды', 'Дешевки', 'Новый русский спуск', 'Такое', 'Тухлянка ',
        'Баклань', 'Лохово', 'Большое', 'Струйкино',
        'Овнище', 'Дно', 'Трусово', 'Кокаиновые горы', 'Косяковка ',
        'Куриловка', 'Ширяево', 'Ломки', 'Большой', 'Куяш', 'Иннах']


def task_1_9(tst: list) -> None:
    ll = LinkedList(Node(tst[0]))
    for el in tst[1:]:
        ll.append(Node(el))

    ll.print()
    print()

    title = input('Введите название города, который необходимо удалить: ')
    ll.delete(title)
    ll.print()

    print()

    index = int(input('Введите индекс: '))
    ll.insert(Node('Конец'), index)
    ll.print()


# Task 1.1
print(task_1_1(certificate))

# Task 1.2
print(*task_1_2(data))

# Task 1.3
print(len(''.join(key for key in certificate.keys())))

# Task 1.4
print(task_1_4(tamandua_name))

# Task 1.5
print(task_1_5(certificate))

# Task 1.6
print(task_1_6(actor[2]))

# Task 1.7
print(*task_1_7())

# Task 1.8
print(*task_1_8(data))

# Task 1.9
task_1_9(test)
