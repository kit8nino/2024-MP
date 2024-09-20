from random import choice
from datetime import date, datetime


# Data
certificate = {'Phisics': 5,
               'Math': 4,
               'Russian': 3,
               'Litrichure': 3,
               'History': 4,
               'English': 3,
               'Music': 5,
               'Technology': 5,
               'Biology': 3,
               'Geography': 3}

actor = ('Рори', 'Кэлхун', '08.08.1922')

data = [choice(['Иван', 'Александр', 'Сергей' 'Андрей',
                'Дмитрий', 'Алексей', 'Максим', 'Иванов',
                'Петров', 'Смирнов', 'Кузнецов', 'Сергеев', 'Васильев'])
        for _ in range(20)]

tamandua_name = 'Евстигней обыкновенный'

def task_1(d):
    s = sum(d.values())
    count = len(d.values())

    result = s / count

    return round(result, 2)


def task_2(a):
    result = []
    for element in a:
        if element[len(element) - 1] != 'в':
            result.append(element)

    return list(set(result))


# Task 3
def task_3(name):
    for c in name:
        name = name.replace(c, bin(ord(c)), 1)
    return name


# Task 4
def task_4(d):
    s = ""
    for key in d.keys():
        s += key

    s = set(list(s))

    return s


# Task 5
def task_5(dt):
    today = list(map(int, str(datetime.now().date()).split('-')))
    date_birth = reversed(list(map(int, dt.split('.'))))

    return int((date(*today) - date(*date_birth)).days)


# Task 6
def task_6():
    q = []
    index = int(input('Введите индекс: '))
    while index != -1:
        title = input('Введите название стройматериала: ')
        index = int(input('Введите индекс: '))
        q.insert(index, title)

    return q


# Task 7
def task_7(a: list) -> list:
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


# Task 8
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


def task_8(tst: list) -> None:
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


# Task 1
print(task_1(certificate))

# Task 2
print(*task_2(data))

# Task _3
print(task_3(tamandua_name))

# Task 4
print(task_4(certificate))

# Task 5
print(task_5(actor[2]))

# Task 6
print(*task_6())

# Task 7
print(*task_7(data))

# Task 8
task_1_8(test)


# Task_9
print(len(''.join(key for key in certificate.keys())))
