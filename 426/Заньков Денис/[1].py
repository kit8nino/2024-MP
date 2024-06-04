from datetime import datetime
from queue import Queue




# школьные предметы
dictionary = {'Русский язык':4,
              'Алгебра':5,
              'Геометрия':4,
              'Иностранный язык':4,
              'Литература':4,
              'Обществознание':4,
              'Физика':5,
              'Химия':4,
              'Биология':4,
              'Информатика':5,
              'История России':5,
              'Всеобщая история':4,
              'ОБЖ':5,
              'География':5,
              'Физкультура':5,}


# актер из фильма 1960 (Сержант Ратледж)
actor = ('Джеффри', 'Хантер', '25.11.1926')


# популярные имена по Новосибирску
popularname = ['Иван Иванов','Иван Петров','Александр Иванов','Сергей Иванов',
               'Сергей Петров','Сергей Сергеев','Андрей Иванов','Дмитрий Иванов',
               'Алексей Иванов','Евгений Иванов','Мария Иванова','Мария Петрова',
               'Елена Иванова','Елена Кузнецова','Екатерина Иванова',
               'Екатерина Романова','Анастасия Иванова','Анастасия Смирнова',
               'Ольга Иванова','Ольга Петрова','Ольга Попова',
               'Наталья Иванова','Наталья Кузнецова','Наталья Васильева',
               'Анна Иванова','Анна Петрова','Татьяна Иванова',
               'Татьяна Петрова','Ирина Иванова','Юлия Иванова','Юлия Кузнецова']

# кличка из прилагательных
moniker = 'Ласковый комок'




# дата рождения актёра    
birthday_date = datetime(1926, 11, 25)


mater = Queue()






def task_1(dictionary):
    znach = dictionary.values()
    count = 0
    for i in znach:
        count+=1
    sred_znach = sum(znach)/count
    return sred_znach



def task_2(popularname):
    unique_name = set([name.split()[0] for name in popularname])
    unique_fullname = set([name.split()[1] for name in popularname])
    return unique_name, unique_fullname



def task_3(dictionary):
    a = [len(i) for i in dictionary]
    dlina = sum(a)
    return (dlina)


def task_4(dictionary):
    unique_letter = set(''.join(dictionary.keys()))
    return(unique_letter)
    
    
def task_5(moniker):
    binar = ''.join(format(ord(i), '08b') for i in moniker)
    return("Ласковый комк в бинарном виде: ", str(binar))
    

def task_6(birthday_date):
    now_date = datetime.now()
    raz = now_date - birthday_date
    return("Количество дней от даnы рождения актёра:", raz.days)

def task_7():
    print('\n',"Task 7: ")
    while True:
        material = input("Введите название стройматериала (или 'стоп' для завершения): ")
        if material.lower() == "стоп":
            break
        else:
            mater.put(material)

    print("Все введенные стройматериалы:")
    while not mater.empty():
        print(mater.get())

    return material



def task_8(popularname):
    number = (25+11**2+1926)%39 + 1
    print("Полученное значение: ", number)
    name_imperator = 'Цзи Иху'
    popularname.sort()
    index = int(input('Введите индекс: '))
    while True:
        if index < 0 or index > len(popularname):
            print('Недопустимое значение!')
            index = int(input('Введите индекс: '))
        else:
            break

    popularname[index] = name_imperator

    return popularname

   



print("Task 1: ",task_1(dictionary))

print('\n',"Task 2:", task_2(popularname))

print('\n',"Task 3:", task_3(dictionary))

print('\n',"Task 4:", task_4(dictionary))

print('\n',"Task 5:", task_5(moniker))

print('\n',"Task 6:", task_6(birthday_date))

print(task_7())

print('\n',"Task 8:", task_8(popularname))

print('\n',"Task 9:")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StrangeTownLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def remove(self, town_name):
        current = self.head
        prev = None
        while current:
            if current.data == town_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = None
                return
            prev = current
            current = current.next

    def insert(self, town_name, index):
        new_node = Node(town_name)
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        if prev:
            prev.next = new_node
            new_node.next = current
        else:
            new_node.next = self.head
            self.head = new_node

towns_list = StrangeTownLinkedList()
towns = ["Большая Пысса", "Большие Пупсы", "Манды", "Такое", "Тухлянка", "Баклань", "Лохово", "Факфак", "Большое Струйкино", 
         "Овнище", "Дно", "Трусово", "ул. Забойная", "Кокаиновые горы", "Косяковка", "Куриловка", "Ширяево", "Ломки", "Большой Куяш", 
         "Иннах", "Крутые Хутора", "Крутая", "Новые Алгаши", "Новопозорново", "Лысая Балда", "Болотная Рогавка", "Старые Черви", 
         "Верхнее Зачатье", "Дураково", "Заячий пузырь", "Козявкино", "Цаца", "Засосная", "Звероножка", "Муходоево", "Да-да", "Вобля", 
         "Хреновое", "Блювиничи", "Большое Бухалово", "Свиновье", "Синие Лепяги", "Жабино", "Кончинино", "Раздериха", "Чуваки", "Мусорка", 
         "Голодранкино", "Безводовка", "Красная Могила", "Кундрючья", "Хотелово", "Добрые Пчелы", "Синегубово"]

for town in towns:
    towns_list.append(town)

print("Список странных названий населенных пунктов:")
towns_list.print_list()

town_to_remove = input("Введите название населенного пункта для удаления: ")
towns_list.remove(town_to_remove)
print("Список после удаления:")
towns_list.print_list()

index = int(input("Введите индекс для вставки города 'Конец': "))
towns_list.insert("Конец", index - 1)
print("       Список после вставки города 'Конец':")
towns_list.print_list()

print(' ▓████████▓▒░  ▒▓███████▓▒░░▒▓███████▓▒░ '
     '  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  '
      ' ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░'
      ' ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ '
      ' ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    '
      ' ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░'
     '  ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ '  )
                                                                                                   
