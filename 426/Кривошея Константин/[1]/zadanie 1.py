from datetime import datetime
from collections import deque

#Задание предметов с оценками
shkol_attestat = {
    "Алгебра": 5,
    "Русский язык": 4,
    "Литература": 5,
    "Физика": 4,
    "Геометрия": 3,
    "История": 5,
    "География": 5,
    "Биология": 5,
    "Английский язык": 3,
    "Информатика": 5,
    "Физкультура": 5,
    "Изобразительное искусство": 4,
    "Музыка": 4,
    "Технология": 5
}

#полное имя с фамилией и дату рождения любого актера из вестерна 1960х годов
actervestrn_infa = ("Генри Джейнс Фонд", "16.05.1905")

#список из имени и фамилии
populyarnie_FI = [
    "Иван Иванов", "Иван Петров", "Александр Иванов", "Александр Петров",
    "Сергей Иванов", "Андрей Иванов", "Дмитрий Иванов", "Алексей Иванов",
    "Максим Иванов", "Евгений Иванов", "Владимир Иванов", "Денис Иванов",
    "Иван Петров", "Александр Петров", "Сергей Петров", "Андрей Петров",
    "Дмитрий Петров", "Алексей Петров", "Максим Петров", "Евгений Петров"
    "Сергей Сергеев", "Андрей Андреев", "Александр Смирнов","Александр Кузнецов",
    "Екатерина Иванова", "Елена Иванова", "Мария Иванова", "Анастасия Иванова",
    "Ольга Иванова", "Наталья Иванова", "Татьяна Иванова", "Анна Иванова",
    "Ирина Иванова", "Юлия Иванова"
]
#имя = прил+сущ, которое приналежит тамандау
tamaduy_ima = "Слепой Пью"

#задание 1: сред.балл аттестата
sred_ocenka = sum(shkol_attestat.values()) / len(shkol_attestat)
print(f"Средняя оценка аттестата:{sred_ocenka}")

#задание 2: вывести уникальные имена
unik_imena = set([imena.split()[0] for imena in populyarnie_FI])
print(f"Уникальные имена из списка популярных: {unik_imena}")

#задание 3: вывести  длину всех предметов
obsh_dlina = sum(len(dlina) for dlina in shkol_attestat.keys())
print(f"Общая длина всех названий предметов: {obsh_dlina}")

#задание 4: вывести уникальные буквы в названиях предметов
unikalnie_bukvi = set()
[unikalnie_bukvi.add(bukva.lower()) for nazv in shkol_attestat.keys() for bukva in nazv if bukva != " "]
print(f"Список уникальных букв{unikalnie_bukvi}")

#задание 5: имя тамандуа в бинарном виде
tamaday_binarnie = " ".join(format(ord(bukv), "b") for bukv in tamaduy_ima)
print(f"Имя тамадуа в бинарном виде {tamaday_binarnie}")

#задание 6: количество дней с даты рождения актера
import datetime
import pytz  # Убедитесь, что библиотека pytz установлена

actervestrn_infa = ("Генри Джейнс Фонд", "16.05.1905")

# Преобразуем строку даты в объект datetime
birthdate = datetime.datetime.strptime(actervestrn_infa[1], "%d.%m.%Y")

# Устанавливаем временную зону (например, UTC)
birthdate = birthdate.replace(tzinfo=pytz.UTC)

# Получаем временные метки
birthdate_timestamp = birthdate.timestamp()
current_timestamp = datetime.datetime.now(pytz.UTC).timestamp()

# Вычисляем количество дней с даты рождения
days_since_birthdate = (current_timestamp - birthdate_timestamp) / (60 * 60 * 24)

# Печатаем результат
print(f"Количество дней с даты рождения актера: {int(days_since_birthdate)}")
#задание 7: список стройматериалов
def poluchenit_spiska_materialov():
    """Получить список стройматериалов от пользователя."""
    spisok_materialov = []
    print("Введите названия стройматериалов (или 'стоп' для выхода):")
    while True:
        material = input()
        if material.lower() == "стоп":
            break
        spisok_materialov.append(material)
    return spisok_materialov

building_materials = poluchenit_spiska_materialov()

print("Список стройматериалов:")
print("\n".join(building_materials))

#задание 8: имеператор династии Джоу
from datetime import datetime
imperatori= {
    1: "Чжоу У-ван",
    2: "Чжоу Чэн-ван",
    3: "Чжоу Кан-ван",
    4: "Чжоу Чжао-ван",
5: "Чжоу Му-ван",
6: "Чжоу Гун-ван",
7: "Чжоу И-ван",
8: "Чжоу Сяо-ван",
9: "Чжоу И-ван",
10: "Чжоу Ли-ван",
11: "Гунхэ",
12: "Чжоу Сюань-ван",
13: "Чжоу Ю-ван",
14: "Чжоу Пин-ван",
15: "Чжоу Хуань-ван",
16: "Чжоу Чжуан-ван",
17: "Чжоу Си-ван",
18: "Чжоу Хуэй-ван",
19: "Чжоу Сян-ван",
20: "Чжоу Цин-ван",
21: "Чжоу Куан-ван",
22: "Чжоу Дин-вай Юй",
23: "Чжоу Цзянь-ван",
24: "Чжоу Лин-ван",
25: "Чжоу Цзин-ван Гуй",
26: "Чжоу Дао-ван",
27: "Чжоу Цзин-ван Чай",
28: "Чжоу Юань-ван",
29: "Чжоу Дин-ван Цзе",
30: "Чжоу Ай-ван",
31: "Чжоу Сы-ван",
32: "Чжоу Као-ван",
33: "Чжоу Вэй Ле-ван",
34: "Чжоу Ань-ван",
35: "Чжоу Ле-ван",
36: "Чжоу Сянь-ван",
37: "Чжоу Шэнь Цзинь-ван",
38: "Чжоу Нань-ван",
}

# Преобразование строки в объект даты
date_str = actervestrn_infa[1]
date_obj = datetime.strptime(date_str, '%d.%m.%Y')

number = (date_obj.day + date_obj.month**2 + date_obj.year) % 39 + 1

sortirov_imena = sorted(populyarnie_FI)
index = int(input("Введите индекс для замены имени: "))
if 0 <= index < len(sortirov_imena):
    sortirov_imena[index] = imperatori.get(number, "Неизвестно")

print("Отсортированный список с измененным именем:")
print(sortirov_imena)

#задание 9: странные города
strannie_naspunkti = {
    "Большая Пысса": 1,
    "Лохово": 2,
    "Добрые Пчелы": 3,
    "Муходоево": 4,
    "Мутный Материк": 5,
    "Хохотуй": 6,
    "Кормёжка": 7,
    "Роскошь": 8,
    "Бухалово": 9,
    "Сковородка": 10,
}

# Печать первоначального списка
print("Первоначальный список с индексами:")
for index, nazv_nas in enumerate(strannie_naspunkti):
    print(f"{index + 1}. {nazv_nas}")

# Удаление элемента по введенному названию
udal_punkt = input("Введите название населенного пункта для удаления: ")
if udal_punkt in strannie_naspunkti:
    strannie_naspunkti.pop(udal_punkt)
    print("Населенный пункт успешно удален.")
else:
    print("Населенный пункт с таким названием не найден.")

# Получение индекса для вставки
index_vstavki = int(input("Введите индекс для вставки города \"Конец\": "))
# Преобразование словаря в список
strannie_naspunkti_list = list(strannie_naspunkti.items())

# Вставка города в указанный индекс
if 0 <= index_vstavki <= len(strannie_naspunkti):
    strannie_naspunkti_list.insert(index_vstavki, ("Конец", 11))
else:
    print("Неверный индекс.")

# Преобразование списка обратно в словарь
strannie_naspunkti = dict(strannie_naspunkti_list)

# Печать обновленного списка
print("Обновленный список:")
for index, nazv_nas in enumerate(strannie_naspunkti):
    print(f"{index + 1}. {nazv_nas}")