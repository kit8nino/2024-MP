import random
from datetime import date

# Словарь, составленный из оценок предметов в аттестате

certificate = {
     'русский язык' : 4,         
     'литература' : 5,
     'английский' : 5,     
     'геометрия' : 5,
     'алгебра' : 4,
     'информатика' : 5,
     'физика' : 4,
     'биолоия' : 4,
     'химия' : 3,
     'физкультура' : 5,
     'история' : 5,
     'обществознание' : 4,
     'география' : 5,
     'музыка' : 5,
     'обж' : 5      
}


# Полное имя, фамилия и дата рождения актера из вестерна 1960х годов как кортеж

actor = ('Оди',' Мерфи','20.06.1924')

# составление списка из имени и фамилии, по таблице самых популярных

popular_name_man = [
    'Иван',
    'Александр',
    'Сергей',
    'Андрей',
    'Дмитрий',
    'Алексей',
    'Максим',
    'Михаил',
    'Владимир',
    'Никита'
]

popular_surname_man = [   
    'Иванов',
    'Петров',
    'Смирнов',
    'Сергеев',
    'Волков',
    'Кузнецов',
    'Васильев',
    'Романов'
]

popular_name_woman = [   
    'Мария',
    'Екатерина',
    'Анастасия',
    'Анна',
    'Елена',
    'Ольга',
    'Наталья',
    'Ирина',
    'Татьяна',
    'Марина'
]

popular_surname_woman = [
    'Иванова',
    'Петрова',
    'Смирнова',
    'Кузнецова',
    'Волкова',
    'Романова',
    'Новикова',
    'Миронова'                          
]

person_data = []

#person_data.append('Мужчины: ')
for i in range(0,len(popular_name_man)):
    random_name_man = random.choice(popular_name_man)
    random_surname_man = random.choice(popular_surname_man)
    person_data.append(random_name_man)
    person_data.append(random_surname_man)

#person_data.append( 'Женщины: ')
for i in range(0,len(popular_name_man)):
    random_name_woman = random.choice(popular_name_woman)
    random_surname_woman = random.choice(popular_surname_woman)
    person_data.append(random_name_woman)
    person_data.append(random_surname_woman)

#print(person_data)

#Имя из прилагательного и существительного для домашнего тамандуа
name_pet = 'Милый малыш'

# 1-9 Задание

print ("\n1 задание")

total_score = sum(certificate.values())
num_subjects = len(certificate)
average_score = total_score / num_subjects
print(f"Средняя оценка в аттестате: {average_score}")



print ("\n2 задание")

all_names = popular_name_man + popular_name_woman
unique_names = set(all_names)
for name in unique_names:
    print(name)



print ("\n3 задание")

total_length = -1 # русский язык написан через пробел

for subject in certificate:
    total_length += len(subject)

print(f"Общая длина всех названий предметов: {total_length}")



print ("\n4 задание")

unique_letters = set()

for subject in certificate:
    for letter in subject:
        unique_letters.add(letter)

print("Уникальные буквы в названиях предметов:")
for letter in sorted(unique_letters):
    print(letter, end=" ")



print ("\n5 задание")

name_bytes = name_pet.encode('utf-8')

binary_string = ''.join(format(byte, '08b') for byte in name_bytes)

print("Имя домашнего тамандуа в бинарном виде:")
print(binary_string)



print ("\n6 задание")

birth_date_str = actor[2]
birth_date = date(int(birth_date_str[-4:]), int(birth_date_str[3:5]), int(birth_date_str[:2]))

today = date.today()

days_since_birth = (today - birth_date).days

print(f"Количество дней от даты рождения актера {actor[0]} {actor[1]} ({birth_date_str}) до текущей даты ({today}): {days_since_birth}")



print ("\n7 задание")

material_list = []

while True:
    material_name = input("Введите название строительного материала ('стоп' для завершения): ")
    if material_name.lower() == 'стоп':
        break
    material_list.append(material_name)

print("\nСписок материалов:")
for material in material_list:
    print(material)



print ("\n8 задание")
# Получаем информацию о дате рождения актера
name, surname, date_of_birth = actor

# Извлекаем день, месяц и год из даты рождения
day, month, year = map(int, date_of_birth.split('.'))

# Вычисляем номер императора
number = (day + month**2 + year) % 39 + 1 #31

# Список императоров династии Чжоу
zhou_emperors = [
    'У-ван','Чэн-ван','Кан-ван','Чжао-ван','Му-ван','Гун-ван','И-ван','Ли-ван','Сюань-ван',
    'Юй-ван','Пин-ван','Хуань-ван','Чжуан-ван','Си-ван','Хуэй-ван','Ай-ван','Цин-ван',
    'Гуан-ван','Дин-ван','Цзянь-ван','Лин-ван','Цзин-ван','Юань-ван','Чжэн-ван','Цзин-ван',
    'Куан-ван','Чжэн-дин-ван','Юань-ван','Гао-ван','Цзы-ван','Сы-ван','Сян-ван','Шэнь-цзин-ван',
    'Лэ-цзин-ван','Као-ван','Шэн-ван'
]

emperor_name = zhou_emperors[number - 1]

index_to_replace = int(input("Введите индекс имени для замены (Вводить только чётные индексы (или 0)) :"))

if index_to_replace < len(person_data) and person_data[index_to_replace] in popular_name_man + popular_name_woman:

    person_data[index_to_replace] = emperor_name
    print(f"\nОтсортированный список с измененным именем: {person_data}")
else:
    print("\nНеверный индекс или элемент не является именем.")



print ("\n9 задание")

names = ["Синегубово", "Дно", "Жабино", "Лысая Балда", "Козявкино", "Свиновье", "Кукуевка", "Верхнее Зачатье"]
new_names = []
print (names)

num_del = int(input('\nВведите индекс населенного пункта для удаления: '))

for i in range(len(names)):
    if i == num_del:
        continue
    new_names.append(names[i])

city = 'Конец'
num_in = int(input("\nВведите индекс, куда вставить город 'Конец':  "))
new_names.insert(num_in,city)
print('Конечный список:', new_names)