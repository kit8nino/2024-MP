import datetime
dict = {"русский язык":3,
        "литература":2,
        "математика":2,
        "история":3,
        "английский язык":1,
        "физика":5,
        "химия":3,
        "биология":2,
        "обществознание":2,
        "география":3,
        "физкультура":1,
        "информатика":5,
        "ОБЖ":5,
        "черчение":5}
actor_info = ("Рори","Кэлхун",1922,8,8)
imperator_info = "Цзи Пифан"
samaras_peoples = ['Иван Иванов',
                 'Сергей Иванов',
                 'Александр Иванов',
                 'Дмитрий Иванов',
                 'Алексей Иванов',
                 'Андрей Иванов',
                 'Максим Иванов',
                 'Владимир Иванов',
                 'Иван Петров',
                 'Сергей Петров',
                 'Александр Петров',
                 'Андрей Петров',
                 'Дмитрий Петров',
                 'Алексей Петров',
                 'Максим Петров',
                 'Владимир Петров',
                 'Иван Сергеев',
                 'Сергей Сергеев',
                 'Александр Сергеев',
                 'Андрей Сергеев',
                 'Дмитрий Сергеев',
                 'Алексей Сергеев',
                 'Максим Сергеев',
                 'Владимир Сергеев',
                 'Иван Кузнецов',
                 'Сергей Кузнецов',
                 'Александр Кузнецов',
                 'Андрей Кузнецов',
                 'Дмитрий Кузнецов',
                 'Алексей Кузнецов',
                 'Максим Кузнецов'
                 ]

tamanduas_name = "свежий барбарис"

#1
average_mark = sum(dict.values())/len(dict)
print("Cредняя оценка аттестата",average_mark)

#2
uniq_names = []
for people in samaras_peoples:
    name = people[:people.find(' ')]
    if name not in uniq_names:
        uniq_names.append(name)
print(uniq_names)
#3
res = 0
for classes in dict:
        res += len(classes)
print("Cумма букв всех предметов:",res)

#4
uniq_symbols = []
for classes in dict.keys():
    for symb in classes:
        if symb not in uniq_symbols:
            uniq_symbols.append(symb)
str_uniq_symbols = ", ".join(uniq_symbols)
print ("Уникальные буквы в названиях предметов:", str_uniq_symbols)

#5
bin_tamanduas_name = ''
for symb in tamanduas_name:
        bin_tamanduas_name +=(format(ord(symb), '08b'))
print("Имя моего домашнего тамандуа в бинарном виде:", bin_tamanduas_name)

#6
birthday_date = datetime.date(actor_info[2],actor_info[3],actor_info[4])
print("Количество дней от даты рождения", str(actor_info[0]), str(actor_info[1])+"а" + ":", datetime.date.today()-birthday_date)

#7
materials = []
print("Для завершения записи материалов напишите <<Cтоп>>")
while True:
    material = input("Введите название материала:")
    if (material == "Стоп"):
        print("Ваши материалы:")
        for i in range(0,len(materials)):
            print(materials[i])
        break
    else:
        materials.append(material)
#8
num = input("Введите номер, имя которого хотите заменить на имя императора:")
if int(num) > len(samaras_peoples):
    print("Ваше число слишком большое, введите число до", len(samaras_peoples))
    num = input("Введите номер, имя которого хотите заменить на имя императора:")
samaras_peoples[int(num)-1] = imperator_info
print("Новый список имен:",samaras_peoples)

#9
towns = ["Большая Пысса", "Большие Пупсы", "Манды", "Дешевки", "Такое", "Баклань", "Факфак", "Лохово", "Дно", "Трусово"]
linked_list = {towns[i]: towns[i+1] for i in range(len(towns)-1)}
linked_list[towns[-1]] = None
print("Изначальный связный список:",linked_list)
sel_town = input("Введите название города, который хотите удалить:")
if sel_town in towns:
    towns.remove(sel_town)
    linked_list = {towns[i]: towns[i + 1] for i in range(len(towns) - 1)}
    linked_list[towns[-1]] = None
else:
    print("Названия вашего города нет в списке")
print("Связный список с выкинутым словом:",linked_list)
sel_key = input("Введите название города, который хотите заменить на <<Конец>>:")
if sel_key in linked_list.keys():
    for key, value in linked_list.items():
        if value == sel_key:
            linked_list[key] = "КОНЕЦ"
else:
    print("Названия вашего города нет в списке")
print("Связный список с вставленным словом <<Конец>>:",linked_list)

