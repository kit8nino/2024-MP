# 1
subjects = {
    "Математика": 5,
    "Русский язык": 4,
    "Литература": 5,
    "Информатика": 4,
    "Физика": 5,
    "Химия": 4,
    "Биология": 5,
    "История": 4,
    "Обществознание": 5,
    "География": 4,
    "Английский язык": 5,
    "Французский язык": 4,
    "Искусство": 5,
    "Физкультура": 4
}


average_grade = sum(subjects.values()) / len(subjects)
print("Задание1:Средняя оценка по предметам в аттестате: ", average_grade)
# 2
import random
# Ростов на дону(10)
men_names = ['Иван', 'Александр','Сергей',  'Андрей', 'Дмитрий', 'Алексей', 'Максим', 'Владимир', 'Евгений', 'Денис']
women_names = [ 'Екатерина',  'Елена','Мария', 'Анна', 'Анастасия','Ольга', 'Наталья', 'Ирина', 'Татьяна', 'Светлана']
men_surnames = ['Иванов', 'Петров', 'Ростовский', 'Попов','Смирнов','Сергеев', 'Волков', 'Романов']
women_surnames = ['Иванова', 'Петрова', 'Попова',  'Смирнова', 'Морозова', 'Романова','Волкова','Кузнецова']


# Создаем список уникальных сочетаний имени и фамилии
full_names1 = [[name, surname] for name in men_names for surname in men_surnames]
full_names2 = [[name, surname] for name in women_names for surname in women_surnames]
s_full_namesm = random.sample(full_names1, 10)
s_full_namesw = random.sample(full_names2, 5)
# Выводим список уникальных сочетаний имени и фамилии    
print("Задание2:",s_full_namesm ,s_full_namesw)

# 3# 
total_length = sum(len(subject) for subject in subjects.keys())
print("Задание3:Общая длина всех названий предметов: ", total_length)
# 4
unique_letters = set()
for subject in subjects.keys():
    unique_letters.update(set(subject))

print("Задание4:Уникальные буквы в названиях предметов:")
print(unique_letters)

# 5
name = "вонючий Этил"
binary_name = ' '.join(format(ord(char), '08b') for char in name)
print("Задание5:",binary_name)
# 6
import datetime
actor_birthday=datetime.datetime(1951,1,20,0,0,0)
actual_date=datetime.datetime.now()
kolvo_day=(actual_date-actor_birthday).days
print("Задание6:",kolvo_day)
# 7
queue = []

while True:
    user_input = input("Введите название стройматериала (или 'stop' для остановки): ")
    if user_input.lower() == 'stop':
        break
    queue.append(user_input)

print("Все добавленные стройматериалы:")
for material in queue:
    print(material)
#  8
from datetime import datetime

def t8(actor_birthday, name):
    def get_name(person):
        return person[0]

    number = (actor_birthday.day + actor_birthday.month**2 + actor_birthday.year) % 39 + 1
    index = int(input(f"Введите индекс, чтобы поменять чьё-то имя (0-{len(name)-1}): "))
    while index < 0 or index >= len(name):
        print(f"Можно ввести индекс только в данном диапазоне (0-{len(name)-1})")
        index = int(input(f"Введите индекс ещё раз, учитывая границы (0-{len(name)-1}): "))
    uniq = name.copy()  # создаем копию списка
    uniq.sort(key=get_name)
    print(f" Было выбрано имя императора под номером {number}")  # 37 - Чжоу И-ван
    uniq[index][0] = 'Чжоу'
    uniq[index][1] = 'И-ван'

    print(uniq)

# пример использования
# actor_birthday = datetime(1951, 1, 20)  # дата рождения актера
name = s_full_namesm + s_full_namesw  # список имен из задания 2
t8(actor_birthday, name)
# 9
places = {
    'Большое Бухалово': 1,
    'Крутая': 2,
    'Свиновье': 3,
    'Куриловка': 4,
    'Такое': 5,
    'Ломки': 6,
    'Иннах': 7,
    'Косяковка': 8,
    'Трусово': 9,
    'Забойная': 10,
    'Баклань': 11,
    'Лохово': 12,
    'Факфак': 13,
    'Большое Струйкино': 14,
    'Дно': 15,
    'Овнище': 16,
    'Большой Куяш': 17,
}

places_list = [
    ['Большое Бухалово'],
    ['Крутая'],
    ['Свиновье'],
    ['Куриловка'],
    ['Такое'],
    ['Ломки'],
    ['Иннах'],
    ['Косяковка'],
    ['Трусово'],
    ['Забойная'],
    ['Баклань'],
    ['Лохово'],
    ['Большое Струйкино'],
    ['Дно'],
    ['Овнище'],
    ['Большой Куяш'],
]

def city(places): 
    print("Исходные данные:\n")
    print(places)
    
    def delete_place():
        town = input('Введите город, который хотите удалить: ')
        if town in places:
            del places[town]
            places['Конец'] = len(places) + 1
            print("\nСловарь после удаления города и добавления 'Конец':\n")
            print(places)
            print("\n\n")
        else:
            print("Данный город отсутствует в списке.\n")

    def insert_konets(): 
        position = int(input('Введите позицию, на которую хотите вставить слово "Конец": '))
        places['Конец'] = position
        sorted_places = dict(sorted(places.items(), key=lambda x: x[1]))
        print("\nОбновленный словарь после добавления 'Конец':\n")
        print(sorted_places)
        print("\n\n")
    
    delete_place()
    insert_konets()

city(places)