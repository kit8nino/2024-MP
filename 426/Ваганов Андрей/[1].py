import random
import datetime
import queue

# Структуры данных
# Школьный аттестат
attestat = {
	"математика" : 5,
	"русский язык" : 4,
	"литература" : 3,
	"английский язык" : 4,
	"физика" : 4,
	"химия" : 4,
	"география" : 3,
	"биология" : 4,
	"история" : 4,
	"физкультура" : 5,
	"труд" : 5,
	"музыка" : 5,
	"изо" : 4,
	"обж" : 5,
	"религиоведение" : 5,
	"информатика" : 5,
	'немецкий': 5,
	'астрономия': 5
}

# Имя актёра
actor = ('Клинт Иствуд', "31.05.1930")

# 
# День рождения 22, выбран город 2 - Санктр-Петербург
man_names = ("Александр", "Иван", "Сергей", "Андрей", "Алексей", "Дмитрий", "Максим", "Михаил", "Владимир", "Игорь")
man_surnames = ("Иванов","Петров","Смирнов","Васильев","Андреев","Алексеев","Кузнецов","Соколов")
top_names = []
for i in range(30):
	top_names.append(man_names[random.randint(0, 9)] + " " + man_surnames[random.randint(0, 7)])

# Имя тамандуа
tamandua_name = "Пустыный Лис"

# Действия:

# 1
average_mark = sum(attestat.values())/len(attestat)
print("Средняя оценка = ", str(average_mark))

# 2
unique_names = list(set(top_names))
print("Уникальные имена: ", unique_names)

# 3
summ = 0
for subject in attestat:
	summ += len(subject)
print("Длина всех названий предметов = ", str(summ))

# 4
unique = list(set(''.join(attestat.keys())))
print("Уникальные буквы: ", unique)

# 5
tamandua_bin_name = ''
for letter in tamandua_name:
	tamandua_bin_name += str(bin(ord(letter))).split('b')[1]
print("Бинарное имя тамандуа: ", str(tamandua_bin_name))

# 6
birth_date = datetime.datetime.strptime(actor[1], '%d.%m.%Y')
current_date = datetime.datetime.now()
days_since_birth = (current_date - birth_date).days
print("Возраст актёра, если бы он был вампиром, в днях :", days_since_birth)

# 7
print("Вводите названия материалов, для завершения введите Q")
materials_queue = queue.Queue()
material = input()
while(material.lower() != 'q'):
	materials_queue.put(material)
	material = input()

print("Список введённых материалов")
while(materials_queue.empty() == False):
	print(materials_queue.get() + "; ", end='')
print()

# 8
# Вычисление китайского императора
# number = (31 + 5**2 + 1930) % 39 + 1
# print(number)
# номер 37, Цзи Бянь
unique_names = sorted(unique_names)
print(unique_names)
print("Введите индекс (цифра от 0 до", len(unique_names),"): ")
index = input()
while(not (0 <= int(index) and int(index) <= 29)):
	print("НЕВЕРНЫЙ ИНДЕКС. Ожидается цифра от 0 до", len(unique_names),": ")
	index = input()
unique_names[int(index)] = ("Цзи Бянь")
print(unique_names)

# 9
cities = {0: "Синие лепяги", 
	"Синие лепяги": "Да-да",
	"Да-да": "Пысса",
	"Пысса": "Большие Пупсы",
	"Большие Пупсы": "Манды",
	"Манды": "Дешевки",
	"Дешевки": "Новый русский спуск",
	"Новый русский спуск": "Такое",
	"Такое": "Тухлянка",
	"Тухлянка": 0}

print(cities)
delete_index = input("Введите название города для удаления или q для пропуска этого шага: ")
index = 0
if (delete_index != 'q'):
	limit = len(cities)
	counter = 0
	while (cities[index] != delete_index and counter < limit):
		index = cities[index]
		counter += 1
	if counter != limit:
		cities[index] = cities[cities[index]]
		del cities[delete_index]
	else:
		print("Такой город не найден")

print(cities)
delete_index = input("Введите индекс для вставки: ")
index = 0
if (delete_index != 'q'):
	delete_index = int(delete_index)
	i = 0
	while i != delete_index-1:
		index = cities[index]
		i += 1
	cities["Конец"] = cities[index]
	cities[index] = "Конец"
	print(cities)