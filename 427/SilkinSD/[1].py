from random import choice
from datetime import date, datetime
from queue import Queue

certificate = {'Всеобщая история': 4,
               'Английский язык': 5,
               'Искусство': 5,
               'Физика': 5,
               'Алгебра': 5,
               'Геометрия': 5,
               'Русский язык': 4,
               'Литература': 5,
               'История России': 4,
               'Музыка': 5,
               'Технология': 5,
               'Биология': 5,
               'География': 5,
               'Обществознание': 5}

actor = ('Clint ', 'Eastwood', '31.05.1930')

data = ['Сергей Волков', 'Денис Иванов', 'Денис Попов', 'Дмитрий Ростовский', 'Иван Сергеев', 
                  'Александр Ростовский', 'Владимир Сергеев', 'Иван Иванов', 'Иван Волков', 'Максим Ростовский', 
                  'Александр Попов', 'Максим Ростовский', 'Алексей Сергеев', 'Максим Ростовский', 'Алексей Смирнов', 
                  'Максим Романов', 'Сергей Романов', 'Алексей Волков', 'Евгений Романов', 'Максим Попов', 'Александр Волков', 
                  'Алексей Иванов', 'Алексей Волков', 'Владимир Иванов', 'Алексей Попов', 'Сергей Смирнов', 'Дмитрий Волков', 
                  'Сергей Смирнов', 'Алексей Попов', 'Алексей Иванов']

tamandua_name = 'Темный лорд'


#1.1
def t1_1(d: dict) -> float:
    su = sum(d.values())
    count = len(d.values())
    result = su / count
    return round(result, 2)

# Res 1.2
names = []
for elem in data:
    names.append(elem.split()[0])
names = set(names)
print(names)

#1.3
certificate_list = list(certificate)
Res3 = 0
for i in range(len(certificate_list)):
    for j in range(len(certificate_list[i])):
        Res3 += 1

#1.4
unique_letters = set(''.join(certificate.keys()))

#1.5
def t1_5(name: str) -> bin:
    for c in name:
        name = name.replace(c, bin(ord(c)), 1)
    return name

#1.6
actor = ('James',' Stewart', '20.05.1908')
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()

days_since_birth = (current_date - birth_date).days

#1.7
materials_line = Queue()
keyboard_text = ""
print("Введите название материала (для завершения end): ", end='')
keyboard_text = input()
while (keyboard_text != "end"):
    print("Введите название материала (для завершения end): ", end='')
    materials_line.put(keyboard_text)
    keyboard_text = input()
while (materials_line.empty() == False):
    print(materials_line.get() + ", ", end='')
print(' ')
print('----------------------')


# Res 1.1
print(t1_1(certificate))

# Res 1.3
print("Общая длина всех названных предметов: ",Res3 - 1,"\n")

#Res 1.4
print("Уникальные буквы в названиях предметов:", unique_letters)

#Res 1.5
print(t1_5(tamandua_name))

#Res 1.6
print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} до текущей даты: {days_since_birth} дней")

#Res 1.7
print("Все стройматериалы:")
while not materials_line.empty():
    print(materials_line.get())

###############################################
#1.8
#print((20 + 5**2 + 1908) % 39 + 1)
#4
print('Input:')
chin = 'Цзи Ся'
index = int(input())
data[index] = chin 
print(data)
###############################################
#1.9
towns = ["Блювиничи", "Хреновое", "Свинорье", "Факфак", "Жабино","Большое Бухалово", "Большие Пупсы", "Дураково", "Иннах", "Синие Лепяги",
         "Тухлянка", "Засосная", "Лохово", "Крутая", "Большое Струйкино", "Косяковка", "Козявкино", "Цаца", "Дешевки", "Муходоево", "Да-да", "Новопозорново", "Болотная Рогавка","Старые Черви", "Верхнее Зачатье",  "Большой Куяш","Ломки", "Овнище", "Такое", "Крутые Хутора", "Манды", "Новые Алгаши" "Большая Пысса", "Дно", "Трусово", "Баклань", "Куриловка", "Ширяево"]
         
def column_print(dict_towns):
        print(">>")
        for x in dict_towns:
            print(x)
        print("<<")
        
dict_towns = {}
for i in range(len(towns)):
    dict_towns[towns[i]] = i
dict_towns = dict(sorted(dict_towns.items(), key=lambda x:x[1]))
column_print(dict_towns)   

print("\nВведите название города, который хотите удалить:")
town = str(input())
print("После удаления:")
dict_towns.pop(town)
column_print(dict_towns)
    
print("\nВведите номер места, куда хотите добавить слово \"Конец\":")
index = int(input())
word = "Конец"
    
items = list(dict_towns.items())
items.insert(index, (word, index))
dict_towns = dict(items)
print("Список после добавления:")
column_print(dict_towns)

