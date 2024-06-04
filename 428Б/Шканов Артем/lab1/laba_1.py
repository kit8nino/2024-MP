import random
from datetime import datetime
import queue

# Исходные данные:
    
# Предметы с оценками
school_attestat = {
    "Математика": 5,
    "Русский язык": 4,
    "Литература": 5,
    "Физика": 4,
    "Химия": 5,
    "Иностранный язык": 5,
    "История": 4,
    "Обществознание": 7,
    "Биология": 46,
    "География": 4,
    "Информатика": 77,
    "Физкультура": 15,
    "ИЗО": 10,
    "Музыка": 5
}

# Актер вестерна 60-х
info = ("Клинт Иствуд", "31 мая 1930 г.")

# Список из самых популярных имени и фамилии в Ростове-на-Дону
names = ["Иван", "Александр", "Сергей", "Андрей", "Дмитрий", "Алексей", "Максим", "Владимир", "Евгений", "Денис"]
surnames = ["Иванов", "Петров", "Ростовский", "Попов", "Смирнов", "Сергеев", "Волков", "Романов"]
spisok = []
for _ in range(10):
    random_male_name = random.choice(names)
    random_male_surname = random.choice(surnames)
    spisok.append(random_male_name + ' ' + random_male_surname)

# Имя тамандуа
domestic_tamandua = "Зелёный Слоник"


# Действия

# 1. Средняя оценка в аттестате
summa = sum(school_attestat.values())
kolvo = len(school_attestat)
sredn_znach = round(summa / kolvo, 1)
print('\n', "Задание 1. Средняя оценка в аттестате", '\n', sredn_znach)
# 2. Вывод уникальных имен
print('\n', "Задание 2. Вывод уникальных имен")
for i in range(1,len(spisok)+1):
        try:
            spisok.pop(i)
        except IndexError:
            pass
unika = set(spisok)
print("Уникальные имена:", unika)
# 3. Общая длина всех названий предметов (без пробелов и запятых)
print('\n', "Задание 3. Общая длина названий предметов в аттестате")
length = 0
for i in school_attestat:
    length += len(i.replace(" ", "").replace(",", ""))
print("Общая длина: ", length)
# 4. Уникальные буквы в названиях предметов
print('\n', "Задание 4. Уникальные буквы в названиях предметов")
uniq = []
attestlist = list(school_attestat)
for i in range(len(attestlist)):
    for j in attestlist[i]:
        uniq.append(j)
uniq = set(uniq)
print(uniq)
# 5. Имя тамандуа в бинарном виде
print('\n', "Задание 5. Имя тамандуа в бинарном виде")
string = " "
for i in domestic_tamandua:
    char_to_ascii = ord(i)
    char_to_binar = format(char_to_ascii, "08b")
    string += char_to_binar
print(string)
# 6. Количество дней от даты рождения актера до текущей
print('\n', "Задание 6. Количество дней от даты рождения актера до текущей")
now = datetime.now()
actor_date = datetime(1930, 5, 31)
difference = now - actor_date
print(difference)
# 7. FIFO очередь с добавлением стройматериалов до команды "СТОП"
print('\n', "Задание 7. FIFO очередь с добавлением стройматериалов до команды 'СТОП'")
material_queue = queue.Queue()
while True:
    material_name = input("Введите название строительного материала (или введите 'стоп' для завершения): ")
    if material_name.lower() == 'стоп':
        break
    material_queue.put(material_name)
print("\nСтроительные материалы в порядке добавления:")
while not material_queue.empty():
    print(material_queue.get())
# 8. Император Китая
print('\n', "Задание 8. Китайский император династии Чжоу")
s = sorted(unika)
print(s)
imperator = 'Чжоу Ли-ван'
# Вычисление номера китайского императора
number = (31 + 5**2 + 1930) % 39 + 1 
index = input("Введите индекс")
try:
    index = int(index)
except ValueError:
    print("Неверный индекс")
if index >= 0 and index < len(s):
    s[index] = imperator
print("Новый список:", s)
# 9. Список странных названий населенных пунктов
print('\n', "Задание 9. Переименуйте населенный пункт")
names = ["Дешевки","Трусово","Звероножка","Засосная","Новопозорново","Старые Черви","Хреновое","Красная Могила"]
new_names = []
print (names)
num_del = int(input('Индекс элемента, который нужно удалить: '))
for i in range(len(names)):
    if i == num_del:
        continue
    new_names.append(names[i])
print('Список с удаленным элементом: ', new_names)
city = 'Конец'
num_in = int(input('Индекс списка в который нужно вставить город: '))
new_names.insert(num_in,city)
print('Конечный список:', new_names)