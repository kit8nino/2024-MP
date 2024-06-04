import random
import queue
import datetime as dt

attestat = {"история" : 4,
	"русский язык" : 5,
	"биология" : 3,
	"география" : 5,
	"физика" : 4,
	"физкультура" : 5,
	"информатика" : 3,
	"химия" : 3,
	"сопромат" : 4,
	"изо" : 5,
	"музыка" : 5,
	"религиоведение" : 4,
	"литература" : 5,
	"черчение" : 5,
	"английский" : 4}

actor = ("Клинт иствуд", "31.05.1930")

# 31.10.2004, понедельник - Москва
names = ("Иван", "Александр", "Сергей", "Андрей", "Дмитрий", "Алексей", "Максим", "Михаил", "Владимир", "Никита")
names_2 = ("Иванов", "Петров", "Смирнов", "Сергеев", "Волков", "Кузнецов", "Васильев", "Романов")

names_array = []

for i in range(30):
	names_array.append(random.choice(names)+' '+random.choice(names_2))

tamandua_name = "Игорь"



# 1
average = 0
for i in attestat:
	average = average + attestat[i]
average = average / len(attestat)
print("Средняя оценка:", str(average), "\n")

# 2
names_unique = []
k = 0
for i in names_array:
	k = 0
	for j in names_array:
		if i == j:
			k += 1
	if k == 1:
		names_unique.append(i)
print("Уникальные имена:", str(names_unique))

# 3
summ = 0
for subject in attestat:
	summ += len(subject)
print("Длина аттестата: ", summ)

# 4
unique_letters = []
for subject in attestat:
	for letter in subject:
		k = 0
		for unique_letters_letter in unique_letters:
			if unique_letters_letter == letter:
				k += 1
		if k == 0:
			unique_letters.append(letter)
unique_letters.remove(' ')
print("Уникальные буквы: ", str(unique_letters))

# 5
tamandua_name_bin = ""
for letter in tamandua_name:
	tamandua_name_bin += str(bin(ord(letter)))
print("Имя тамандуа в бинарном виде: ", str(tamandua_name_bin))

# 6
today = dt.datetime.now(tz=None)
days_past = today - dt.datetime.strptime(actor[1], "%d.%m.%Y")
print("Дней с даты рождения актёра: ", str(days_past.days))

# 7
FIFO = queue.Queue()
print("Введите название материала, команда для остановки 'стоп'")
material = input()
while (material != "стоп"):
	print("ввод материала: ", end = '')
	FIFO.put(material)
	material = input()
print("Список материалов: ")
while(FIFO.empty() == False):
	print(FIFO.get())

# 8
# print((31 + 5**2 + 2004) % 39 + 1) = 33 Цзи У
for name_index in range(len(names_array)):
	print(name_index, " = ", names_array[name_index])
print("type name index: ", end='')
names_array[int(input())] = "Цзи У"
for name_index in range(len(names_array)):
	print(name_index, " = ", names_array[name_index])

# 9
points = {0: "Большая Пысса",
	"Большая Пысса": "Такое",
	"Такое": "Лютые Болоты",
	"Лютые Болоты": "Кокаиновые горы",
	"Кокаиновые горы": "Большой Куяш",
	"Большой Куяш": "Верхнее Зачатье",
	"Верхнее Зачатье": "Новопозорново",
	"Новопозорново": "Козявкино",
	"Козявкино": "Звероножка",
	"Звероножка": 0}
index = 0
while points[index] != 0:
	print(points[index])
	index = points[index]
to_delete = input("Введите элемент для удаления: ")
index = 0
while points[index] != to_delete:
	index = points[index]
points[index] = points[points[index]]
del points[to_delete]

print("После удаления:")
index = 0
while points[index] != 0:
	print(points[index])
	index = points[index]

to_change = int(input("Введите номер элемента для замены: "))
i = 0
index = 0
while i != to_change-1:
	index = points[index]
	i += 1

points["Конец"] = points[points[index]]
points[index] = "Конец"

print("Итоговый результат:")
index = 0
while points[index] != 0:
	print("points[", index, "] = ", points[index])
	index = points[index]