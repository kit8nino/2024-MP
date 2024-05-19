from random import choice
from datetime import date, datetime



certificate = {'Обществознание': 5,
               'География': 4,
               'Геометрия': 3,
               'Биология': 5,
               'Литература': 4,
               'История России': 3,
               'Всеобщая история': 5,
               'Английский язык': 4,
               'Музыка': 3,
               'Краеведение': 5,
               'Технология': 4,
               'Русский язык': 3,
               'Алгебра': 5,
               'Физика': 4}

actor = ('Джеймс', 'Коберн', '31.08.1928')

data = [choice(['Александр','Иван','Сергей','Дмитрий','Алексей','Андрей','Максим','Иванов','Смирнов','Петров','Волков','Соколов','Кузнецов','Белов'])
        for _ in range(20)]

tamandua_name = 'маленький бро'


#1.1
def t_1_1(d: dict) -> float:
    s = sum(d.values())
    count = len(d.values())

    result = s / count

    return round(result, 2)


print(t_1_1(certificate))
#1.2
def t_1_2(a: list) -> list:
    result = []
    for element in a:
        if element[len(element) - 1] != 'в':
            result.append(element)

    return list(set(result))

print(*t_1_2(data))
#1.3

print(len(''.join(key for key in certificate.keys())))
#1.4
def t_1_4(d: dict) -> set:
    s = ""
    for key in d.keys():
        s += key

    s = set(list(s))

    return s

print(t_1_4(certificate))
#1.5
def t_1_5(name: str) -> bin:
    for c in name:
        name = name.replace(c, bin(ord(c)), 1)
    return name

print(t_1_5(tamandua_name))
#1.6
def t_1_6(dt: str) -> int:
    today = list(map(int, str(datetime.now().date()).split('-')))
    date_birth = reversed(list(map(int, dt.split('.'))))

    return int((date(*today) - date(*date_birth)).days)

print(t_1_6(actor[2]))

#1.7
def t_1_7():
    q = []
    index = int(input('Введите индекс: '))
    while index != -123:
        title = input('Введите название стройматериала: ')
        index = int(input('Введите индекс: '))
        q.insert(index, title)

    return q

print(*t_1_7())

#1.8
def t_1_8(a: list) -> list:
    name = 'Сы-ван'
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

print(*t_1_8(data))

#1.9
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


test = ['Добрые Пчелы',
        'Хотелово',
        'Кундрючья', 
        'Красная Могила', 
        'Голодранкино', 
        'Мусорка', 
        'Чуваки',
        'Раздериха',
        'Кончинино',
        'Жабино', 
        'Синие Лепяги',
        'Свиновье',
        'Большое Бухалово',
        'Хреновое', 
        'Блювиничи', 
        'Вобля', 
        'Лысая Балда']


def t_1_9(tst: list) -> None:
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

t_1_9(test)    
    
