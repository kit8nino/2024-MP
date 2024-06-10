import random
from datetime import datetime
dictionary={
    'математика':5,
    'русский язык':3,
    'литература':4,
    'английский язык':3,
    'физика':5,
    'химия':4,
    'физра':5,
    'история':5,
    'информатика':4,
    'биология':3,
    'обж':5,
    'география':4,
    'общество':3,
    'геометрия':5,
}

tuple=('Джон','Уэйн','26.05.1907')

men_names=[
    'Иван',
    'Александр',
    'Сергей',
    'Дмитрий',
    'Андрей',
    'Алексей',
    'Евгений',
    'Максим',
    'Владимир',
    'Денис',
    ]
men_surnames=[
    'Иванов',
    'Петров',
    'Кузнецов',
    'Смирнов',
    'Сергеев',
    'Попов',
    'Васильев',
    'Волков',   
]
women_names=[
    'Елена',
    'Ольга',
    'Екатерина',
    'Мария',
    'Наталья',
    'Анастасия',
    'Анна',
    'Татьяна',
    'Ирина',
    'Светлана',
]
women_surnames=[
    'Иванова',
    'Петрова',
    'Кузнецова',
    'Смирнова',
    'Попова',
    'Соколова',
    'Васильева',
    'Романова',
]


name_tamandya='мыльный пузырь'

#1
def calculate_average_score(subject_scores):
    total_score = sum(subject_scores.values())
    num_subjects = len(subject_scores)
    average_score = total_score / num_subjects
    return average_score
average_score = calculate_average_score(dictionary)
print(f"Средняя оценка в аттестате: {average_score:.2f}")

#2
def generate_unique_FIO(men_names, men_surnames, women_names, women_surnames, count):
    FIO = set()  
    total_people = len(men_names) + len(women_names)  
    
    
    if count > total_people:
        print(f"Невозможно сгенерировать {count} уникальных ФИО. Максимальное количество: {total_people}")
        return list(FIO)  
    
    
    while len(FIO) < count:
        if random.choice([True, False]):  
            name = random.choice(men_names)
            surname = random.choice(men_surnames)
        else:
            name = random.choice(women_names)
            surname = random.choice(women_surnames)
        
        
        full_name = f"{surname} {name}"
        FIO.add(full_name)
    
    return list(FIO)  
generated_FIO = generate_unique_FIO(men_names, men_surnames, women_names, women_surnames, 10)
print("Сгенерированные уникальные ФИО:")
for fio in generated_FIO:
    print(fio,'\n')
#3
def calculate_total_length_of_subjects_names(subject_scores):
    total_length = sum(len(subject) for subject in subject_scores.keys())
    return total_length
total_length = calculate_total_length_of_subjects_names(dictionary)
print(f"Общая длина всех названий предметов: {total_length}")
#4
def unique_letters_in_word(word):
    letters = set(word.replace(' ', ''))
    return letters
for subject, score in dictionary.items():
    unique_letters = unique_letters_in_word(subject)
    unique_letters_str = ', '.join(sorted(unique_letters))
    print(f"Уникальные буквы в слове \"{subject}\":  {{{unique_letters_str}}}")
#5
def string_to_binary(name):
    binary_representation = ' '.join(format(ord(char), 'b') for char in name)
    return binary_representation
binary_name = string_to_binary(name_tamandya)
print(f"Бинарное представление имени '{name_tamandya}':")
print(binary_name)
#6
def days_since_birthdate(birthdate):
    
    birth_date = datetime.strptime(birthdate, '%d.%m.%Y')
    
    
    current_date = datetime.now()
    
    
    time_difference = current_date - birth_date
    
   
    days_since_birth = time_difference.days
    
    return days_since_birth


birthdate = tuple[2]


days_since_birth = days_since_birthdate(birthdate)


print(f"Количество дней с даты рождения {birthdate} до текущей даты: {days_since_birth} дней")


#7
def material():
    
    materials = []

    material = input("\nВведите название стройматериала или введите \"СТОП\", чтобы прекратить ввод: ")

    while material.upper() != "СТОП":
        materials.append(material)
        material = input("\nВведите название стройматериала или введите \"СТОП\", чтобы прекратить ввод: ")

    if len(materials)==0:
        print("\nСтройматериалы отсутствуют")

    else: 
        print("\nНазвания стройматериалов в порядке очереди: \n")

        for material in materials:
            print(f"{material}") 
material()

#8
def dynasty_emperor(full_names):
    chinese_imperators=['У-ван','Чэн-ван','Кан-ван','Чжао-ван','Му-ван','Гун-ван','И-ван','Сяо-ван','Ли-ван','Гунхэ','Сюань-ван','Ю-ван','Пин-ван','Хуань-ван','Чжуан-ван','Си-ван','Хуэй-ван','Сян-ван','Цин-ван','Куан-ван','Дин-ван','Цзянь-ван','Лин-ван','Цзин-ван','Дао-ван','Цзин-ван','Юань-ван','Джэнь Дин-ван','Ай-ван','Сы-ван','Као-ван','Вэй Ле-ван','Ань-ван','Ле-ван','Сянь-ван','Шэнь Цзинь-ван','Нань-ван','Хуэй-ван']

    index = int(input(f"Введите индекс n, 0 <= n < {len(full_names)}: "))
    
    
    birthdate = tuple[2]
    
    day, month, year = map(int, birthdate.split('.'))
    
   
    number = (day + month**2 + year) % 39 + 1
    print(f"Номер китайского императора: {number}")
    
    
    emperor_name = chinese_imperators[number - 1]
    print(f"Имя китайского императора: {emperor_name}")
    
    
    full_names[index] = emperor_name
    
    
    print("\nОбновленный список популярных имен и фамилий:")
    for name in full_names:
        print(name)


dynasty_emperor(generated_FIO)
#9

def manage_strange_villages():
    list_of_strange_villages = [
        'Большая Пысса', 'Большие Пупсы', 'Дешевки', 'Такое', 'Тухлянка ', 
        'Большое Струйкино', 'Овнище', 'Трусово', 'Ширяево', 'Ломки'
    ]

    print("\nСтранные названия населенных пунктов:\n", list_of_strange_villages)

    
    city_to_delete = input("\nВведите название населенного пункта, который хотите удалить: ")
    if city_to_delete in list_of_strange_villages:
        list_of_strange_villages.remove(city_to_delete)
        print("\nЭлемент", city_to_delete, "удален из списка.")

        
        print("\nОбновленный список населенных пунктов:\n", list_of_strange_villages)
    else:
        print("\nНаселенный пункт", city_to_delete, "не найден в списке.")

    
    index = int(input("\nВведите индекс для вставки города 'Конец': "))

    
    if 0 <= index <= len(list_of_strange_villages):
        list_of_strange_villages.insert(index, "Конец")
        print("\nОбновленный список с вставленным городом 'Конец':\n", list_of_strange_villages)
    else:
        print("\nВведен некорректный индекс. Вставка не выполнена.")


manage_strange_villages()
