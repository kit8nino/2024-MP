
import random
subjects = {
    "Математика": 5,
    "Русский язык": 4,
    "Литература": 4,
    "Иностранный язык": 5,
    "Физика": 4,
    "Химия": 4,
    "Биология": 5,
    "География": 4,
    "История": 5,
    "Обществознание": 4,
    "Информатика": 5,
    "Физкультура": 5,
    "Музыка": 4,
    "ИЗО": 4
}

# Данные актера вестерна
actor_info = ("Чарльз Бронсон", "3.11.1921")
# списки из имени и фамилии, по таблице самых популярных
man_name = ['Иван', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Алексей', 'Максим', 'Евгений', 'Антон', 'Владимир']
fam_man = ['Иванов', 'Петров', 'Смитрнов', 'Кузнецов', 'Попов', 'Сергеев', 'Волков', 'Васильев']
wom_name = ['Екатерина', 'Мария', 'Елена', 'Анна', 'Ольга', 'Анастасия', 'Наталья', 'Ирина', 'Татьяна', 'Светлана']
fam_wom = ['Иванова', 'Петрова', 'Смитрнова', 'Кузнецова', 'Попова', 'Волкова', 'Романова', 'Васильева']

#Имя домашнего тамандуа
tamandua_name = "Мягкий Шелест"

# 1.Средняя оценка в аттестате
average_grade = sum(subjects.values()) / len(subjects)
print("Средняя оценка в аттестате:", average_grade)
# 2. Уникальные имена
spisok = []
for i in range(0,len(man_name)):
    random_name_man = random.choice(man_name)
    random_surname_man = random.choice(fam_man)
    spisok.append(random_name_man)
    spisok.append(random_surname_man)
    
for i in range(0,len(wom_name)):
    random_name_woman = random.choice(wom_name)
    random_surname_woman = random.choice(fam_wom)
    spisok.append(random_name_woman)
    spisok.append(random_surname_woman)
    
for i in range(1,len(spisok)+1):
        try:
            spisok.pop(i)
        except IndexError:
            pass
un_name = set(spisok)
print("Уникальные имена:", un_name)

# 3. Общая длина всех названий предметов
total_length = sum(len(subject) for subject in subjects)
print("Общая длина всех названий предметов:", total_length)

# 4. вывести уникальные буквы
unique_letters = set(letter for subject in subjects for letter in subject)
print("     Уникальные буквы в названиях предметов:", unique_letters)

#5. Имя тамандуа в бинарном виде
tamandua_binary = ''.join(format(ord(char), '08b') for char in tamandua_name)
print("     Имя тамандуа в бинарном виде:", tamandua_binary)

# 6. Вычисляем количество дней от даты рождения до текущей даты
from datetime import datetime
# Преобразуем дату рождения в формат datetime
birth_date = datetime.strptime(actor_info[1], "%d.%m.%Y")
days_since_birth = (datetime.now() - birth_date).days
print(f"Количество дней с момента рождения актера {actor_info[0]} до текущей даты:", days_since_birth)

# 7. FIFO очередь, названия стройматериалов
from collections import deque
queue = deque()
while True:
    material = input("Введите название строительного материала (для остановки введите 'стоп'): ")
    if material.lower() == 'стоп':
        break
    queue.append(material)
print("Список строительных материалов:")
for material in queue:
    print(material)
    
# 8. Замена имени на имя китайского императора
s = sorted(un_name)
print(s)
emperors_zhou = "Чжоу У-Ван"

index = int(input("Введите индекс: "))
try:
    index = int(index)
    
except ValueError:
    print("Неверный индекс")
    
if index >= 0 and index < len(s):
    s[index] = emperors_zhou   
print("Новый список:", s)
# Вычисление номера китайского императора
day = 3
month = 11
year = 1921
number = (day + month**2 + year) % 39 + 1
s[index] = emperors_zhou 


# 9. Создание списка странных населенный пунктов
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print(f"{data} not found in the linked list.")
            return
        prev.next = current.next

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                print("Index out of range.")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Создаем связный список с названиями населенных пунктов
towns_list = LinkedList()
towns = ["Большая Пысса", "Большие Пупсы", "Манды", "Такое", "Тухлянка", "Баклань", "Лохово", "Факфак", "Большое Струйкино", 
         "Овнище", "Дно", "Трусово", "ул. Забойная", "Кокаиновые горы", "Косяковка", "Куриловка", "Ширяево", "Ломки", "Большой Куяш", 
         "Иннах", "Крутые Хутора", "Крутая", "Новые Алгаши", "Новопозорново", "Лысая Балда", "Болотная Рогавка", "Старые Черви", 
         "Верхнее Зачатье", "Дураково", "Заячий пузырь", "Козявкино", "Цаца", "Засосная", "Звероножка", "Муходоево", "Да-да", "Вобля", 
         "Хреновое", "Блювиничи", "Большое Бухалово", "Свиновье", "Синие Лепяги", "Жабино", "Кончинино", "Раздериха", "Чуваки", "Мусорка", 
         "Голодранкино", "Безводовка", "Красная Могила", "Кундрючья", "Хотелово", "Добрые Пчелы", "Синегубово"]
for town in towns:
    towns_list.insert(town)

print("Исходный связный список:")
towns_list.print_list()

# Удаление элемента по введенному названию
delete_town = input("Введите название населенного пункта для удаления: ")
towns_list.delete(delete_town)
print("Связный список после удаления элемента:")
towns_list.print_list()

# Вставка города "Конец" в указанное место по индексу
insert_index = int(input("Введите индекс для вставки города 'Конец': "))
towns_list.insert_at_index(insert_index, "Конец")
print("Связный список после вставки 'Конец' по индексу:")
towns_list.print_list()
