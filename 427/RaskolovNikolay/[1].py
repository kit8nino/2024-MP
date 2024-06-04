from random import choice
from datetime import date, datetime
import queue

# Data
attestat = {'геометрия':4,
'физика':4,
'алгебра':5,
'информатика':3,
'литератруа':2,
'русский язык':5,
'география':3,
'химия':4,
'религовединие':2,
'физкультура':5,
'английский язык':3,
'биололгия':5,
'обществознание':2,
'астрономия':5}

actor = ('Gojko',' Mitic', '13.06.1940')

name_man = ['Иван',
'Александр',
'Сергей',
'Дмитрий',
'Андрей',
'Алексей',
'Евгений',
'Максим',
'Владимир',
'Денис'
]

surname_man = ['Иванов',
'Петров',
'Кузнецов',
'Смирнов',
'Сергеев',
'Попов',
'Васильев',
'Волков'
]

name_woman = ['Елена',
'Ольга',
'Екатерина',
'Мария',
'Наталья',
'Анастасия',
'Анна',
'Татьяна',
'Ирина',
'Светлана'
]

surname_woman = ['Иванова',
'Петрова',
'Кузнецова',
'Смирнова',
'Попова',
'Соколова',
'Васильева',
'Романова'
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

#print(spisok)

name_pet = 'Злобный рекс'





# Task 1
print('Task 1')
average_certificate_grade = sum(attestat.values()) / len(attestat)
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
attestat_list = list(attestat)
count = 0
for i in range(len(attestat_list)):
    for j in range(len(attestat_list[i])):
        count += 1
print("Общая длина всех названных предметов: ",count - 1,"\n")




#Task 4
print('Task 4')
unique_letters = set(''.join(attestat.keys()))
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
    number = ( 13+ 6**2 + 1940) % 39 + 1
    here=int(input("Введите индекс для имени, которое будет заменено на имя китайского императора:"))
    list_of_names[here]=chinese_imperators[number].upper()
    return list_of_names


print('Task 8')
unique_letters=list(spisok)
change_the_name_to_chinese_imperator(unique_letters)
print(unique_letters,'\n')


#Task 9
print('Task 9')

points = ["Конец", 
         "Веселая жизнь", 
         "Осень", 
         "Культура",
         "Принцип", 
         "Печать", 
         "Сказачная ночь", 
         "Принцесса"]
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




















