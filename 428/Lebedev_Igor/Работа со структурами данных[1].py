import random
from datetime import datetime


schoolgrades = {              
    "Алгебра": 5,
    "Геометрия": 4,
    "Физика": 5,
    "Химия": 3,
    "Биология": 3,
    "География": 3,
    "ОБЖ": 4,
    "Физ-ра": 5,
    "Музыка": 3,
    "ИКТ": 5,
    "История": 4,
}     





#Популярные имена и фамилии Нижнео Новгорода
m_names = ['Александр', 'Иван', 'Сергей', 'Дмитрий', 'Алексей', 'Андрей', 'Максим', 'Евгений', 'Михаил', 'Владимир']
m_family = ['Иванов', 'Смирнов', 'Петров', 'Кузнецов', 'Волков', 'Соколов', 'Белов', 'Морозов']
names_list = [(name, family) for name in m_names for family in m_family]
random.shuffle(names_list)


actor_birthday = datetime(1930, 5,31 )
actor = ("Clint", "Eastwood", (actor_birthday.day, actor_birthday.month, actor_birthday.year))
print(actor_birthday.year)

# Имя для пета
pet_name = "Зеленый слон" 

# Действия 
average_grade = sum(schoolgrades .values()) / len(schoolgrades ) 
print(f"Средняя оценка в аттестате: {average_grade}")

print("Список из уникальных имен:", names_list)
unique_names = list(set([name for name, _ in names_list]))
print(f"Уникальные имена: {unique_names}")

total_length = sum(len(subject) for subject in schoolgrades )
print(f"Общая длина всех названий предметов: {total_length}")

unique_letters = set("".join(schoolgrades .keys()))
print(f"Уникальные буквы в названиях предметов: {unique_letters}")

binary_pet_name = "".join(format(ord(char), '08b') for char in pet_name)
print(f"Имя домашнего тамандуа в бинарном виде: {binary_pet_name}")

days_since_birth = (datetime.now() - actor_birthday).days
print(f"Количество дней от даты рождения актера до текущей даты: {days_since_birth}")

# Материалы
material_queue = []
while True:
    material = input("Введите стройматериал (Введите 'stop' для останоки): ")
    if material.lower() == 'stop':
        break
    material_queue.append(material)
print("Список стройматериалов:", material_queue)






#Замена имени на императора династии Чжоу
index = int(input("Индекс имени для замены"))
print(names_list[index])
names_list.sort()
names_list[index] = ("Чжоу", "Сянь-ван")
print(f"Имя китайского императора династии Чжоу для замены в списке имён: {names_list[index]}")
print("Список имён с вставленным именем китайскго императора", names_list)

#Словарь со странными городами
cring_cities = {
    "г. Манды": 1,
    "Красная Могила": 2,
    "Да-да": 3,
    "Болотная Рогавка": 4,
    "Дешевки": 5,
    "Свиновье": 6,
    "Такое": 7
}
print("Список странных названий населенных пунктов:", cring_cities)

while True:
    city_name = input("Введите название города для удаления или введите 'Конец' для вставки этого города в список(для завершения введите 'stop'): ")
    if city_name.lower() == 'stop':
        break
    if city_name in cring_cities:
        del cring_cities[city_name]
        print(f"Город '{city_name}' удален.")
    elif city_name == 'Конец':
        insert_index = int(input("Введите индекс для вставки города 'Конец': "))
        cring_cities["Конец"] = insert_index
        cring_cities=sorted(cring_cities.items(),key=lambda x: x[1])
        cring_cities=dict(cring_cities)
        print(f"Город 'Конец' вставлен по индексу {insert_index}.")
    else:
        print("Такого города нет в списке.")

print("Изменённый список странных названий населенных пунктов:" , cring_cities)