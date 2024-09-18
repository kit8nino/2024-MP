import datetime
import queue
from collections import deque


atestat = {
    "Информатика": 5,
    "Алгебра": 5,
    "Геометрия": 5,
    "Русский язык": 3,
    "Английский язык": 4,
    "Физика": 4,
    "Астрономия": 5,
    "История России": 4,
    "Химия": 4,
    "ОБЖ": 4,
    "Музыка": 5,
    "Всеобщая история": 5,
    "Физкультура": 5,
    "Литература": 4,
    "Биология": 5
}

actor = ('ДЖОН', 'УЭЙН', '26.05.1907')

popular_names_voronezh = [
    "Иван Иванов", "Иван Петров","Александр Попов", "Сергей Сергеев", "Дмитрий Новиков", "Андрей Иванов", 
    "Алексей Смирнов", "Евгений Попов", "Владимир Петров", "Роман Иванов", "Елена Иванова", "Елена Попова", 
    "Мария Смирнова", "Ольга Петрова", "Ирина Новикова", "Наталья Кузнецова", "Татьяна Волкова", 
    "Юлия Романова", "Светлана Попова", "Анастасия Романова", "Натлья Новикова","Роман Васильев", 
    "Евгений Кузнецов", "Максим Иванов","Екатерина Романова", "Татьяна Петрова", "Татьяна Попова", 
    "Светлана Волкова","Сергей Иванов","Дмитрий Новиков","Алексей Кузнецов" ]

tamandua_name = 'Лютый дэдпул'


# cредний балл


average_atestat = sum(atestat.values()) / len(atestat)
print(f'Средняя оценка в аттестате: {average_atestat} балла \n')


# уникальные имена


unique_names = set(name.split()[0] for name in popular_names_voronezh)
print(f"Уникальные имена: {unique_names} \n")


# Общая длина всех названий предметов
total_subjects_length = sum(len(subject) for subject in atestat)
print(f"Общая длина всех названий предметов: {total_subjects_length} \n")

# Уникальные буквы в названиях предметов
unique_letters = set(char for subject in atestat for char in subject)
print(f"Уникальные буквы в названиях предметов: {unique_letters} \n")

# tamandua_name v binare


def binary_name(str):
    binary = ' '.join(format(ord(x), 'b') for x in str)
    return binary


print(f'Имя в двоичном представлении: {binary_name(tamandua_name)} \n')



# Дней с др актера
def days_difference(birth_date):
    birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y")
    current_date = datetime.datetime.now()
    return (current_date - birth_date).days

print("Количество дней от даты рождения актера:",  days_difference(actor[2]))


# FIFO очередь, в которую можно добавлять строковые названия стройматериалов
queue = deque()
while True:
    material = input("Введите название стройматериала (для завершения введите 'стоп'): ")
    if material.lower() == 'стоп':
        break
    queue.append(material)
print(f"Очередь стройматериалов: {queue} \n") 

# №9

def change_name_by_index(names_list, index):
    names_list.sort()
    chinese_emperors = [
    "Чжоу Чэн-ван", "Чжоу Кан-ван", "Чжоу Ай-ван", "Чжоу Сы-ван", "Чжоу Као-ван", "Чжоу Чжао-ван", 
    "Чжоу Му-ван", "Чжоу Гун-ван", "Чжоу И-ван (Си)", "Чжоу Сяо-ван", "Чжоу И-ван (Се)", "Чжоу Ай-ван", 
    "Чжоу Сы-ван", "Чжоу Као-ван", "Чжоу Ли-ван", "Гунхэ", "Чжоу Сюань-ван", "Чжоу Ю-ван", "Чжоу Пин-ван",
    "Чжоу Хуань-ван", "Чжоу Чжуан-ван", "Чжоу Си-ван", "Чжоу Хуэй-ван", "Чжоу Сян-ван", "Чжоу Цин-ван", 
    "Чжоу Куан-ван", "Чжоу Кан-ван", "Чжоу Чжао-ван", "Чжоу Му-ван"
]
    emperor_index = (datetime.datetime.strptime(actor[2], "%d.%m.%Y").day + datetime.datetime.strptime(actor[2], "%d.%m.%Y").month ** 2 + datetime.datetime.strptime(actor[2], "%d.%m.%Y").year) % 39 +1
    if 0 <= index < len(names_list):
        names_list[index] = chinese_emperors[emperor_index]
        return names_list
    else:
        return "Неверный индекс."
print(f'Измененный список популярных имен и фамилий: {change_name_by_index(popular_names_voronezh[:], int(input("Введите индекс для изменения имени: ")))} \n')



def strange_cities_operations(cities):
    while True:
        print(f"Текущий список странных названий населенных пунктов: {list(cities.keys())} \n")
        action = input(f"Выберите действие: (1 - удалить элемент, 2 - вставить город 'Конец', 3 - выход): \n")
        
        if action == '1':
            city_to_remove = input(f"Введите название города для удаления: \n")
            if city_to_remove in cities:
                del cities[city_to_remove]
                print("Город успешно удален.")
            else:
                print("Город не найден.")
        elif action == '2':
            insert_index = int(input(f"Введите индекс для вставки города 'Конец': \n"))
            if 0 <= insert_index <= len(cities):
                cities["Конец"] = None
                print("Город 'Конец' успешно вставлен.")
            else:
                print("Неверный индекс.")
        elif action == '3':
            break
        else:
            print("Некорректный ввод.")


#


strange_cities_operations({
    "Бигас": 1,
    "Пудж": 2,
    "Дота": 3,
    "Большая Пысса": 4,
    "Большие Пупсы": 5,
    "ул. Минструактивная": 6,
    "г. Манды": 7,
    "Дешевки": 8,
    "ул. Новый русский спуск": 9,
    "Такое": 10,
    "Тухлянка": 11,
    "Баклань": 12,
    "Лохово": 13,
    "Факфак": 14,
    "Большое Струйкино": 15,
    "Овнище": 16,
    "Дно": 17,
    "Трусово": 18,
    "ул. Забойная": 19,
    "Кокаиновые горы": 20,
    "Косяковка": 21,
    "Куриловка": 22,
    "Ширяево": 23,
    "Ломки": 24,
    "Большой Куяш": 25,
    "Иннах": 26,
    "Крутые Хутора": 27,
    "Крутая": 28,
    "Новые Алгаши": 29
})