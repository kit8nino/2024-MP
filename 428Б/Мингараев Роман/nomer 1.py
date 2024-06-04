from datetime import date

# Входные данные
subjects = {'Русский язык': 5, 'Литература': 4, 'Математика': 5, 'Физика': 4, 'Химия': 3, 'Биология': 4, 'История': 5, 'Обществознание': 4, 'География': 4, 'Иностранный язык': 5, 'Информатика': 5, 'ОБЖ': 5, 'Физкультура': 5, 'Технология': 4}
actor_name_and_dob = ('Клинт Иствуд', (1930, 5, 31))
popular_names = [('Александр', 'Иванов'), ('Мария', 'Кузнецова'), ('Анна', 'Смирнова'), ('Елена', 'Попова'), ('Михаил', 'Соколов'), ('Наталья', 'Лебедева'), ('Андрей', 'Козлов'), ('Екатерина', 'Новикова'), ('Николай', 'Морозов'), ('Ольга', 'Петрова'), ('Сергей', 'Волков'), ('Татьяна', 'Соловьева'), ('Алексей', 'Васильев'), ('Дмитрий', 'Зайцев'), ('Анастасия', 'Павлова'), ('Виктория', 'Семенова'), ('Ирина', 'Голубева'), ('Юрий', 'Виноградов'), ('Людмила', 'Богданова'), ('Марина', 'Воробьева'), ('Илья', 'Федоров'), ('Павел', 'Михайлов'), ('Роман', 'Беляев'), ('Олег', 'Комаров'), ('Игорь', 'Лазарев'), ('Ксения', 'Муравьева'), ('Антон', 'Богданов'), ('Яна', 'Сергеева'), ('Евгения', 'Кузьмина'), ('Денис', 'Попов')]
tamandua_name = 'Ленивый Вялый'

# Функции
def get_average_grade(subjects):
    total_grades = sum(subjects.values())
    num_subjects = len(subjects)
    average_grade = total_grades / num_subjects
    return average_grade

def get_unique_names(names):
    unique_names = set([name[0] for name in names])
    return unique_names

def get_total_subject_length(subjects):
    total_length = sum(len(subject) for subject in subjects.keys())
    return total_length

def get_unique_subject_letters(subjects):
    all_letters = ''.join(subjects.keys())
    unique_letters = set(all_letters)
    return unique_letters

def get_binary_name(name):
    binary_name = ''.join(format(ord(char), 'b') for char in name)
    return binary_name

def get_days_since_dob(dob):
    today = date.today()
    year, month, day = dob
    birth_date = date(year, month, day)
    days_since_dob = (today - birth_date).days
    return days_since_dob

def fifo_queue():
    queue = []
    while True:
        item = input("Введите строковое название стройматериала (или 'stop' для выхода): ")
        if item.lower() == 'stop':
            break
        queue.append(item)
    print("Содержимое очереди:")
    for item in queue:
        print(item)

def replace_name(names, index, actor_dob):
    sorted_names = sorted(names, key=lambda x: x[1])
    year, month, day = actor_dob  # Распаковываем кортеж с датой рождения
    number = (day + month**2 + year) % 39 + 1
    emperor_name = zhou_emperors[number - 1]
    sorted_names[index] = (emperor_name, sorted_names[index][1])
    print(f"Отсортированный список с измененным именем под индексом {index}:")
    for name in sorted_names:
        print(name)

# def create_linked_list(names):
#     linked_list = {}
#     for i, name in enumerate(names):
#         linked_list[name] = i + 1 if i < len(names) - 1 else None
#     print("\nСвязный список странных названий населенных пунктов:")
#     for name, next_index in linked_list.items():
#         print(f"{name} -> {next_index}")
#     return linked_list

# def delete_and_insert(linked_list):
#     name_to_delete = input(f"Введите название населенного пункта для удаления: ")
#     for name, next_index in linked_list.items():
#         if name == name_to_delete:
#             del linked_list[name]
#             break
#     insert_index = int(input("Введите индекс, куда вставить 'Конец': "))
#     new_linked_list = {}
#     for name, next_index in linked_list.items():
#         if next_index is None:
#             new_linked_list[name] = None
#         elif next_index >= insert_index:
#             new_linked_list[name] = next_index + 1
#         else:
#             new_linked_list[name] = next_index
#     new_linked_list['Конец'] = None
#     new_list = sorted(new_linked_list.items(), key=lambda x: x[1] if x[1] is not None else float('inf'))
#     print("Новый связный список:")
#     for name, next_index in new_list:
#         print(f"{name} -> {next_index}")



def manage_strange_villages():
    list_of_strange_villages = [
        'Большая Пысса', 'Большие Пупсы', 'Дешевки', 'Такое', 'Тухлянка ', 
        'Большое Струйкино', 'Овнище', 'Трусово', 'Ширяево', 'Ломки'
    ]

    print("\nСтранные названия населенных пунктов:\n")
    for i in list_of_strange_villages:
        print(f"{i}")

    
    city_to_delete = input("\nВведите название населенного пункта, который хотите удалить: ")
    if city_to_delete in list_of_strange_villages:
        list_of_strange_villages.remove(city_to_delete)
        print("\nЭлемент", city_to_delete, "удален из списка.")

        
        print("\nОбновленный список населенных пунктов:\n")
        for i in list_of_strange_villages:
            print(f"{i}")
    else:
        print("\nНаселенный пункт", city_to_delete, "не найден в списке.")

    
    index = int(input("\nВведите индекс для вставки города 'Конец': "))

    
    if 0 <= index <= len(list_of_strange_villages):
        list_of_strange_villages.insert(index, "Конец")
        print("\nОбновленный список с вставленным городом 'Конец':\n")
        for i in list_of_strange_villages:
            print(f"{i}")
    else:
        print("\nВведен некорректный индекс. Вставка не выполнена.")





# Вспомогательные данные
zhou_emperors = ['Ву', 'Чэн', 'Кан', 'Чжао', 'Му', 'Гун', 'Идин', 'Ли', 'Сюань', 'Ю', 'Пин', 'Хуань', 'Шао', 'Ю', 'Сян', 'Цин', 'Куан', 'Дин', 'Цзянь', 'Лин', 'Сян', 'Гао', 'И', 'Ли', 'Чжуан', 'Сюань', 'Чэн', 'Куан', 'Дин', 'Цзянь', 'Ай', 'Пин', 'Хуань', 'Шао', 'Ю', 'Сюань', 'Чжуан', 'Куан', 'Дин']

# Выполнение функций
print(f"Средняя оценка в аттестате: {float(get_average_grade(subjects))}\n")
print(f"Уникальные имена: {get_unique_names(popular_names)}\n")
print(f"Общая длина всех названий предметов: {get_total_subject_length(subjects)}\n")
print(f"Уникальные буквы в названиях предметов: {get_unique_subject_letters(subjects)}\n")
print(f"Имя вашего домашнего тамандуа в бинарном виде: {get_binary_name(tamandua_name)}\n")
print(f"Количество дней от даты рождения актера вестерна до текущей даты: {get_days_since_dob(actor_name_and_dob[1])}\n")
fifo_queue()
print(f"\nПод каким индексом хотим поменять имя?")
index = int(input())
replace_name(popular_names, index, actor_name_and_dob[1])
manage_strange_villages()

# linked_list = create_linked_list(['Рабочий Поселок', 'Выселки', 'Малая Ярославка', 'Большие Колки', 'Долгий Мыс', 'Нижние Муллы', 'Верхние Муллы', 'Старые Муллы', 'Новые Муллы', 'Малые Муллы', 'Средние Муллы'])
# delete_and_insert(linked_list)
