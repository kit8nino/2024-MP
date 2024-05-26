import random
import queue
from datetime import datetime

#1
print('№1')
dictionary = {'Физика' : 4,'Русский язык' : 5,'Биолоия' : 4,'Обществознание' : 4,'Информатика' : 5,   'Литература' : 4,'Английский язык' : 5,'Алгебра' : 5,'Геометрия' : 5,'Химия' : 4,'История' : 4,'ОБЖ' : 5,'География' : 4,'Физкультура' : 5}
print(f"Средняя оценка в аттестате: {sum(dictionary.values()) / len(dictionary)}","\n")

#2
print('№2')
imya_M = ['Александр','Иван','Сергей','Дмитрий','Алексей','Андрей','Максим','Евгений','Михаил','Владимир']

fam_M = ['Иванов','Смирнов','Петров','Кузнецов','Волков','Соколов','Белов','Морозов']

imya_W = ['Елена','Екатерина','Наталья','Мария','Ольга','Светлана','Татьяна','Ирина','Юлия','Анастасия']

fam_W = ['Иванова','Смирнова','Кузнецова','Петрова','Волкова','Морозова','Соколова','Романова']

rndm_imena = []

for i in range(len(imya_M)):
    rndm_imya_M = random.choice(imya_M)
    rndm_fam_M = random.choice(fam_M)
    rndm_imena.append(rndm_imya_M)
    rndm_imena.append(rndm_fam_M )
    
for i in range(len(imya_W)):
    rndm_imya_W = random.choice(imya_W)
    rndm_fam_W = random.choice(fam_W)
    rndm_imena.append(rndm_imya_W)
    rndm_imena.append(rndm_fam_W)
    
for i in range(len(rndm_imena)):
        try:
            rndm_imena.pop(i)
        except IndexError:
            pass
imena = set(rndm_imena)
print("Уникальные имена:", imena,"\n")

#3
print('№3')
dictionary_list = list(dictionary)
k = 0
for i in range(len(dictionary_list)):
    for j in range(len(dictionary_list[i])):
        k += 1
print("Общая длина всех названий предметов: ",k,"\n")

#4
print('№4')
unique_letters = set(''.join(dictionary.keys()))
print("Уникальные буквы в названиях предметов:", unique_letters)

#5
print('№5')
tamandua = 'Домашний тамандуа'
binary_tamandua = ''.join(format(x,'08b') for x in bytearray(tamandua,'utf-8')) 
print(f"Имя {tamandua} в бинарном виде:", binary_tamandua,"\n" )

#6
print('№6')
actor = ('Клинт','Иствуд','31.05.1930')
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()
days_since_birth = (current_date - birth_date).days
print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} до текущей даты: {days_since_birth} дней","\n")

#7
print('№7')
materials_queue = queue.Queue()
print("Введите названия стройматериалов (для завершения введите 'stop'):")
while True:
    material = input()
    if material.lower() == 'stop':
        break
    materials_queue.put(material)
print("Все названия стройматериалов:")
while not materials_queue.empty():
    print(materials_queue.get())

#8
print('№8') 
s = sorted(imena)
print(s,"\n")
number = (31 + 5**2 + 1930) % 39 + 1
imperator=['Цзи Фа','Цзи Сун','Цзи Ся','Цзи Мань','Цзи Иху','Цзи Цзянь','Цзи Се','Цзи Хуй','Цзи Цзин','Цзи Гуншэн','Цзи Ицзю','Цзи Линь','Цзи То','Цзи Хуци','Цзи Лан','Цзи Чжэн','Цзи Жэньчэнь','Цзи Бань','Цзи Юй','Цзи И','Цзи Сесинь','Цзи Гуй','Цзи Мэн','Цзи Гай','Цзи Жэнь','Цзи Цзе','Цзи Цюйцзи','Цзи Шу','Цзи Вэй','Цзи У','Цзи Цзяо','Цзи Си','Цзи Бянь','Цзи Дин','Цзи Янь']

# len(imperator)<number, поэтому сделал number=number-5

number=number-5
index = input("Введите индекс")

try:
    index = int(index)
    
except ValueError:
    print("Неверный индекс","\n")
    
if index >= 0 and index < len(s):
    s[index] = imperator[number]
    
print("Новый список:", s,"\n")

#9
print('№9')
goroda = ['Муходоево', 'Ширяево', 'Старые Черви', 'Да-да','Ломки', 'Хотелово', 'Добрые Пчелы', 'Блювиничи']
new_goroda = []
print (goroda,"\n")
num_del = int(input('Индекс элемента, который нужно удалить: '))
for i in range(len(goroda)):
    if i == num_del:
        continue
    new_goroda.append(goroda[i])
print('Список с удаленным элементом: ', new_goroda,"\n")
Konec = 'Конец'
gorod_index = int(input('Индекс списка в который нужно вставить город: '))
new_goroda.insert(gorod_index,Konec)
print('Новый список:', new_goroda)