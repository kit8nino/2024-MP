import datetime
dict = {"русский язык":4,
        "математика":5,
        "литература":3,
        "история":5,
        "химия":3,
        "физика":5,
        "биология":3,
        "английский язык":3,
        "обществознание":4,
        "география":4,
        "физкультура":3,
        "информатика":5,
        "обж":5,
        "история России":5}
actor_info = ("Денверн","Пайл",1920,5,11)
samara = ['Максим Сергеев',
 'Владимир Петров',
 'Андрей Кузнецов',
 'Александр Петров',
 'Андрей Сергеев',
 'Александр Кузнецов',
 'Сергей Петров',
 'Иван Кузнецов',
 'Иван Иванов',
 'Андрей Иванов',
 'Александр Иванов',
 'Алексей Сергеев',
 'Максим Иванов',
 'Алексей Иванов',
 'Сергей Сергеев',
 'Сергей Иванов',
 'Алексей Петров',
 'Дмитрий Кузнецов',
 'Максим Кузнецов',
 'Владимир Иванов',
 'Дмитрий Петров',
 'Иван Сергеев',
 'Александр Сергеев',
 'Иван Петров',
 'Дмитрий Сергеев',
 'Андрей Петров',
 'Владимир Сергеев',
 'Дмитрий Иванов',
 'Сергей Кузнецов',
 'Максим Петров'
                 ]

tamanduas = "ленивый кабан"
imperator = "Сы Се"

# /////////////////////////////////////////////////////////////////////////////////


# Задание 1
print('Задание 1')
total_marks = 0
subjects = len(dict)
for mark in dict.values():
    total_marks += mark
average_mark = total_marks / subjects
print("Средняя оценка аттестата", average_mark)
print('-----------------------------------------------------------------------------------------')

# Задание 2
print('Задание 2')
unique_names = []
for person in samara:
    first_name = person.split(' ')[0]
    if first_name not in unique_names:
        unique_names.append(first_name)
print(unique_names)
print('-----------------------------------------------------------------------------------------')

# Задание 3
print('Задание 3')
total_length = sum(len(subject) for subject in dict.keys())
print("Сумма букв всех предметов:", total_length)
print('-----------------------------------------------------------------------------------------')

# Задание 4
print('Задание 4')
unique_symbols = set()
for subject in dict.keys():
    unique_symbols.update(subject)
print("Уникальные буквы в названиях предметов:", ", ".join(unique_symbols))
print('-----------------------------------------------------------------------------------------')

# Задание 5
print('Задание 5')
binary_representation = ''.join(format(ord(char), '08b') for char in tamanduas)
print("Имя моего домашнего тамандуа в бинарном виде:", binary_representation)
print('-----------------------------------------------------------------------------------------')

# Задание 6
print('Задание 6')
birthday_date = datetime.date(actor_info[2],actor_info[3],actor_info[4])
print("Количество дней от даты рождения", str(actor_info[0]), str(actor_info[1])+"а" + ":", datetime.date.today()-birthday_date)
print('-----------------------------------------------------------------------------------------')

# Задание 7
print('Задание 7')
materials = []
print("Для завершения записи материалов напишите <<Закончить>>")
while True:
    material = input("Введите название материала:")
    if material == "Закончить":
        print("Ваши материалы:")
        for m in materials:
            print(m)
        break
    else:
        materials.append(material)
print('-------------------------------------------------------------------------------------------------------------------------')

# Задание 8
print('Задание 8')
try:
    num = int(input("Введите номер, имя которого хотите заменить на имя императора:"))
    if num > len(samara):
        raise ValueError("Ваше число слишком большое")
    samara[num - 1] = imperator
    print("Новый список имен:", samara)
except ValueError as e:
    print(e)
print('-------------------------------------------------------------------------------------------------------------------------')

# Задание 9
print('Задание 9')
towns = ["Крутая", "Засосная", "Синие Лепяги", "Добрые челы", "Мусорка", "Факфак", "Синегубово", "Дно", "Жабино", "Хреновое"]
linked_list = {town: next_town for town, next_town in zip(towns, towns[1:] + [None])}
print("Изначальный связный список:", linked_list)

selected_town = input("Введите название города, который хотите удалить:")
if selected_town in towns:
    towns.remove(selected_town)
    linked_list = {town: next_town for town, next_town in zip(towns, towns[1:] + [None])}
else:
    print("Названия вашего города нет в списке")
print("Связный список с выкинутым словом:", linked_list)

key_to_replace = input("Введите название города, который хотите заменить на <<Конец>>:")
if key_to_replace in linked_list:
    for key, value in linked_list.items():
        if value == key_to_replace:
            linked_list[key] = "Конец"
else:
    print("Названия вашего города нет в списке")
print("Связный список с вставленным словом <<Конец>>:", linked_list)
