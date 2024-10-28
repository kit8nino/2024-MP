from datetime import datetime
import random
# Данные
subjects_mark = {
    "Математика": 4,
    "Русский язык": 5,
    "Литература": 4,
    "История": 5,
    "Физика": 4,
    "Химия": 4,
    "Биология": 5,
    "География": 4,
    "Информатика": 5,
    "Физкультура": 5,
    "Иностранный язык": 5,
    "Искусство": 4,
    "Обществознание": 4,
    "Технология": 5
}

westwood_actor = ("Henry Fond", "16.05.1905")

#Популярные имена и фамилии в Екатеринбурге 
names = ["Иван", "Александр", "Сергей", "Андрей", "Дмитрий", "Алексей", "Максим", "Евгений", "Антон", "Владимир"]
surnames = ["Иванов", "Петров", "Смирнов", "Кузнецов", "Попов", "Сергеев", "Волков", "Васильев", "Иванов", "Петров"]


tamandua_name = "Мягкий Хвост"  #  имя для Тамандуа
 

print(f"Средняя оценка в аттестате: {sum(subjects_mark.values()) / len(subjects_mark)}","\n")


#Уникальное имя
unique_combinations = set()

while len(unique_combinations) < len(names):  
    name = random.choice(names)
    surname = random.choice(surnames)
    if name != surname: 
        combination = name + " " + surname
        if combination not in unique_combinations:
            unique_combinations.add(combination)

print("Уникальные имена:", list(unique_combinations))

total_length = sum(len(subject) for subject in subjects_mark)
print(f"Общая длина всех названий предметов: {total_length}")

unique_letters = set("".join(subjects_mark.keys()))
print(f"Уникальные буквы в названиях предметов: {unique_letters}")

binary_tamandua = ''.join(format(x,'08b') for x in bytearray(tamandua_name,'utf-8')) 
print(f"Имя {tamandua_name} в бинарном виде:", binary_tamandua,"\n" )

actor_date = datetime.strptime(westwood_actor[1], '%d.%m.%Y')
now_date = datetime.now()
days = (now_date - actor_date).days
print(f"Количество дней от даты рождения актера {westwood_actor[0]} {westwood_actor[1]} до текущей даты: {days} дней","\n")

material_queue = []
while True:
    material = input("Введите стройматериал (для завершения введите 'стоп'): ")
    if material.lower() == 'стоп':
        break
    material_queue.append(material)
print("Список стройматериалов:")
print(material_queue)

names_and_surnames = [name + " " + surname for name, surname in zip(names, surnames)]
index = int(input("Введите индекс для изменения имени в списке популярных имен и фамилий: "))
print("Имя которое будет заменено:", names_and_surnames[index])
names_and_surnames.sort()
names_and_surnames[index] = "Чжоу", "Лин-ван"
print(f"Имя китайского императора династии Чжоу для замены в списке имён: {names_and_surnames[index]}")
print("Список имён с вставленным именем китайского императора", names_and_surnames)

strange_names = {
    "Тухлянка": 1,
    "Лохово": 2,
    "Факфак": 3,
    "Дно": 4,
    "Трусово": 5,
    "Косяковка": 6,
    "Ширяево": 7,
    "Крутые Хутора": 8
}

name_to_delete = input("Введите название для удаления: ")

# Удаляем элемент с указанным названием города, если он есть
if name_to_delete in strange_names:
    del strange_names[name_to_delete]
    print(f"'{name_to_delete}' успешно удален.")
else:
    print(" не найден в списке.")

# Вводим индекс для вставки нового города
index = int(input("Введите индекс для вставки: "))

# Вставляем новый город "Конец" в указанное место по индексу
strange_names["Конец"] = index
strange_names=sorted(strange_names.items(),key=lambda x: x[1])
print("Обновленный список мест:")
print(strange_names)

