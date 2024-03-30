import datetime
import random

#Исходные данные
academic_subjects = {
    "русский язык": 4, 
    "алгебра": 4,
    "геометрия": 4,
    "литература": 5,
    "химия": 4,
    "география": 4,
    "английский язык": 4,
    "информатика": 5,
    "обж": 5,
    "физика": 4,
    "история": 5,
    "обществознание": 5,
    "физкультура": 5,
    "биология": 4
    }

western_actor = ("Чарльз Бронсон", datetime.date(1921, 11, 3))

#Популярные имена (Нижний Новгород)
names = ["Александр", "Иван", "Сергей", "Дмитрий", "Алексей", "Андрей", "Максим", "Евгений", "Михаил", "Владимир"]
surnames = ["Иванов", "Смирнов", "Петров", "Кузнецов", "Волков", "Соколов", "Белов", "Морозов"]
popular_names = [None] * 20

for i in range(20):
    popular_names[i] = names[random.randint(0, 9)] + " " + surnames[random.randint(0, 7)]

pet_name = "карнавальный Джо"

#Задание 1
print("Задание 1")

sum = 0
count = 0

for key, value in academic_subjects.items():
    sum += value
    count += 1

average_grade = sum / count

print("average grade = " + str(average_grade))

#Задание 2
print("Задание 2")

name = [None] * 20

for i in range(20):
    split_str = popular_names[i].split()
    name[i] = split_str[0]

for i in range(20):
    count = 0
    for j in range(0, 20, 1):
        if(name[i] == name[j]) and (i != j):
            count += 1
    if(count == 0):
        print(name[i])

#Задание 3
print("Задание 3")

sum_char = 0

for key, value in academic_subjects.items():
    sum_char += len(key)

print("Сумма букв предметов = " + str(sum_char))

#Задание 4
print("Задание 4")

big_str = ""

for key, value in academic_subjects.items():
    big_str += str(key)

for i in range(len(big_str)):
    count = 0
    for j in range(len(big_str)):
        if (big_str[i] == big_str[j]) and (i != j):
            count += 1
    if(count == 0):
        print(big_str[i])

#Задание 5
print("Задание 5")

bits = bin(int.from_bytes(pet_name.encode('utf-8', 'surrogatepass'), 'big'))[2:]
print(bits.zfill(8 * ((len(bits) + 7) // 8)))

#Задание 6
print("Задание 6")

today = datetime.date.today()
print(today - western_actor[1])
