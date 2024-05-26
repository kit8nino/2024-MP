import random
import queue
from datetime import datetime


# School items
certificate = {'Английский язык': 5,
               'Алгебра': 4,
               'Геометрия': 3,
               'Русский язык': 4,
               'Литература': 5,
               'История России': 5,
               'Всеобщая история': 5,
               'Информатика':4,
               'Химия': 3,
               'Музыка': 5,
               'Технология': 5,
               'Биология': 5,
               'География': 4,
               'Обществознание': 5}
# Actor name
actor = ('Барбара', 'Эден', '23.08.1934')
# Lists of first and last names
name_man = ['Иван',
            'Сергей',
            'Александр',
            'Андрей',
            'Дмитрий',
            'Алексей',
            'Максим',
            'Владимир',
            'Евгений',
            'Денис'
            ]

surname_man = ['Иванов',
               'Петров',
               'Сергеев',
               'Кузнецов',
               'Смирнов',
               'Андреев',
               'Васильев',
               'Попов'
               ]

name_woman = ['Анастасия',
              'Екатерина',
              'Елена',
              'Ирина',
              'Мария',
              'Наталья',
              'Ольга',
              'Светлана',
              'Татьяна',
              'Юлия'
              ]

surname_woman = ['Васильева',
                 'Волкова',
                 'Иванова',
                 'Кузнецова',
                 'Петрова',
                 'Попова',
                 'Романова',
                 'Смирнова'                        
                 ]

spisok = []
for i in range(0,len(name_man)):
    name_man = random.choice(name_man)
    surname_man = random.choice(surname_man)
    spisok.append(name_man)
    spisok.append(surname_man)
    
for i in range(0,len(name_woman)):
    name_woman = random.choice(name_woman)
    surname_woman = random.choice(surname_woman)
    spisok.append(name_woman)
    spisok.append(surname_woman)
    

name_pet = 'Коржик'



# Task 1
print('Task 1')
average_certificate_grade = sum(certificate.values()) / len(certificate)
print(f"Средняя оценка в аттестате: {average_certificate_grade}")



# Task 2
print('Task 2')
for i in range(1,len(spisok)+1):
        try:
            spisok.pop(i)
        except IndexError:
            pass
unika = set(spisok)

print("Уникальные имена:", unika)




#Task 3
print('Task 3')
certificate_list = list(certificate)
count = 0
for i in range(len(certificate_list)):
    for j in range(len(certificate_list[i])):
        count += 1
print("Общая длина всех названных предметов: ",count - 1,"\n")




#Task 4
print('Task 4')
unique_letters = set(''.join(certificate.keys()))
print("Уникальные буквы в названиях предметов:", unique_letters)



#Task 5
print('Task 5')
binary_name_pet = ''.join(format(x,'08b') for x in bytearray(name_pet,'utf-8')) 
print("Имя 'Коржик' в бинарном виде:", binary_name_pet )



#Task 6
print('Task 6')
# Исходные данные
birth_date = datetime.strptime(actor[2], '%d.%m.%Y')
current_date = datetime.now()

# Рассчитываем количество дней
days_since_birth = (current_date - birth_date).days

print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} до текущей даты: {days_since_birth} дней")



#Task 7
print('Task 7')

# Создаем FIFO очередь
materials_queue = queue.Queue()

# Заполняем очередь с клавиатуры
print("Введите названия стройматериалов (для завершения введите 'стоп'):")
while True:
    material = input()
    if material.lower() == 'стоп':
        break
    materials_queue.put(material)

# Выводим все элементы очереди
print("Все названия стройматериалов:")
while not materials_queue.empty():
    print(materials_queue.get())


#Task 8
def change_the_name_to_chinese_imperator(list_of_names):
    chinese_imperators=['У-ван','Чэн-ван','Кан-ван','Чжао-ван','Му-ван','Гун-ван','И-ван','Сяо-ван','Ли-ван','Гунхэ','Сюань-ван','Ю-ван','Пин-ван','Хуань-ван','Чжуан-ван','Си-ван','Хуэй-ван','Сян-ван','Цин-ван','Куан-ван','Дин-ван','Цзянь-ван','Лин-ван','Цзин-ван','Дао-ван','Цзин-ван','Юань-ван','Джэнь Дин-ван','Ай-ван','Сы-ван','Као-ван','Вэй Ле-ван','Ань-ван','Ле-ван','Сянь-ван','Шэнь Цзинь-ван','Нань-ван','Хуэй-ван']
    number = ( 23+ 8**2 + 1934) % 39 + 1
    here=int(input("Введите индекс для имени, которое будет заменено на имя китайского императора:"))
    list_of_names[here]=chinese_imperators[number].upper()
    return list_of_names


print('Task 8')
unique_letters=list(spisok)
change_the_name_to_chinese_imperator(unique_letters)
print(unique_letters,'\n')


#Task 9
print('Task 9')

points = ["Чуваки", 
         "Хомяки", 
         "Веселая жизнь", 
         "Париж",
         "Животинки", 
         "Конец", 
         "Правда", 
         "Тайна"]
print("9: Связный список" + str(points))

keyboard_input = input("Введите название города для удаления: ")
index = 0
if (keyboard_input != 'q'):
	limit = len(points)
	counter = 0
	while (points[index] != keyboard_input and counter < limit):
		index = points[index]
		counter += 1
	if counter != limit:
		points[index] = points[points[index]]
		del points[keyboard_input]
	else:
		print("Такой город не найден")

	print(points)

keyboard_input = input("Введите индекс для вставки: ")
index = 0
if (keyboard_input != 'q'):
	points["Конец"] = points[keyboard_input]
	points[keyboard_input] = "Конец"
	
	print(points)
