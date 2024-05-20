import random
from datetime import datetime

# Исходные данные
subjects = {              
    "алгебра": 5,
    "химия": 4,
    "литература": 5,
    "биология": 4,
    "история": 5,
    "физика": 5,
    "геометрия": 5,
    "физкультура": 5,
    "обж": 5,
    "обществознание": 5,
    "информатика": 4,
}     # Предметы в аттестате

actor_birthday = datetime(1901, 5,7 )
actor = ("Gary ", "Cooper", (actor_birthday.day, actor_birthday.month, actor_birthday.year)) #Актёр вестернов Гэрри Купер 7.05.1901 г.р.

#Популярные имена и фамилии в городе Санк-Петербург
men_names = ['Александр', 'Иван', 'Сергей', 'Андрей', 'Алексей', 'Дмитрий', 'Максим', 'Михаил', 'Владимир', 'Игорь']
men_surnames = ['Иванов', 'Петров', 'Смирнов', 'Васильев', 'Андреев', 'Алексеев', 'Кузнецов', 'Соколов']
names_list = [(name, surname) for name in men_names for surname in men_surnames]
random.shuffle(names_list)

# Имя для тамандуа
pet_name = "Прожорливый лис" 

# Действия 
average_grade = sum(subjects.values()) / len(subjects) 
print(f"Средняя оценка в аттестате: {average_grade}")

print("Список из имени и фамилии:", names_list)
unique_names = list(set([name for name, _ in names_list]))
print(f"Уникальные имена: {unique_names}")

total_length = sum(len(subject) for subject in subjects)
print(f"Общая длина всех названий предметов: {total_length}")

unique_letters = set("".join(subjects.keys()))
print(f"Уникальные буквы в названиях предметов: {unique_letters}")

binary_pet_name = "".join(format(ord(char), '08b') for char in pet_name)
print(f"Имя домашнего тамандуа в бинарном виде: {binary_pet_name}")

days_since_birth = (datetime.now() - actor_birthday).days
print(f"Количество дней от даты рождения актера до текущей даты: {days_since_birth}")

# FIFO очередь для стройматериалов
material_queue = []
while True:
    material = input("Введите стройматериал (для завершения введите 'стоп'): ")
    if material.lower() == 'стоп':
        break
    material_queue.append(material)
print("Список стройматериалов:")
print(material_queue)

#Замена имени на императора династии Чжоу
index = int(input("Введите индекс для изменения имени в списке популярных имен и фамилий: "))
print("Имя которое будет заменено:", names_list[index])
names_list.sort()
names_list[index] = ("Чжоу", "Лин-ван")
print(f"Имя китайского императора династии Чжоу для замены в списке имён: {names_list[index]}")
print("Список имён с вставленным именем китайскго императора", names_list)

#Словарик со странными городами
strange_cities = {
    "Большая Пысса": 1,
    "Большие Пупсы": 2,
    "ул. Минструактивная": 3,
    "г. Манды": 4,
    "Дешевки": 5,
    "ул. Новый русский спуск": 6,
    "Такое": 7
}
print("Список странных названий населенных пунктов:", strange_cities)

while True:
    city_name = input("Введите название города для удаления или введите 'Конец' для вставки этого города в список(для завершения введите 'стоп'): ")
    if city_name.lower() == 'стоп':
        break
    if city_name in strange_cities:
        del strange_cities[city_name]
        print(f"Город '{city_name}' удален.")
    elif city_name == 'Конец':
        insert_index = int(input("Введите индекс для вставки города 'Конец': "))
        strange_cities["Конец"] = insert_index
        strange_cities=sorted(strange_cities.items(),key=lambda x: x[1])
        strange_cities=dict(strange_cities)
       
        print(f"Город 'Конец' вставлен по индексу {insert_index}.")
    else:
        print("Такого города нет в списке.")

print("Изменённый список странных названий населенных пунктов:" , strange_cities)
