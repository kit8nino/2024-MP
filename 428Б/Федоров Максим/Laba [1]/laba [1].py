import random
from datetime import datetime
from collections import deque


#ИСХОДНЫЕ ДАННЫЕ
attestat={
    "Математика": 5,
    "Физика": 5,
    "Русский язык": 4,
    "Иностранный яязык": 5,
    "Химия": 4,
    "География": 5,
    "Физ-ра": 5,
    "Биология": 4,
    "Информатика": 5,
    "История": 4,
    "Литература": 4,
    "Труды": 5,
    "Музыка": 4,
    "Обществознание": 5
}

info=("Кирк Дуглас","9 декабря 1916 год")

names = ["Иван","Александр","Сергей","Андрей","Дмитрий","Алексей","Максим","Михаил","Владимир","Никита"]
surnames= ["Иванов","Петров","Смирнов","Сергеев","Волков","Кузнецов","Васильев","Романов"]

tamandua = "Муравьедовое нечто"

#ДЕЙСТВИЯ
# 1)
summa = sum(attestat.values())
kol_vo = len(attestat)
avarage_score = round(summa/kol_vo,1)
print(avarage_score)

# 2)
C = []
def random():
    N = random.randint(0,len(names) - 1)
    S = random.randint(0, len(surnames)-1)
    C.append(names[N])
    C.append(surnames[S])
    return C
for i in range(5):
    print(random())

# 3)
length = 0
for i in attestat.keys():
    length += len(i)
print("Общая длина:", length)

#4)
Zstr = ","
single_str = Zstr.join(attestat.keys())
uniq = set(single_str)
print(uniq)

#5)
string = " "
for i in tamandua:
    char_in_ascll = ord(i)
    char_in_binar = format(char_in_ascll,"08b")
    string += char_in_binar
print(string)    

#6)
now = datetime.now()
actor_date = datetime(1916,12,9)
raznica = now - actor_date
print(raznica)

#7)
materials_queue = deque()
print("Введите названия стройматериалов (введите 'стоп' для завершения):")

while True:
    material = input("Материал: ")
    if material.lower() == 'стоп':
        break
    materials_queue.append(material)
print("\nВсе введенные материалы в порядке очереди:")
while materials_queue:
     print(materials_queue.popleft())

#8
day = 9
month = 12
year = 1916
number = (day + month*2 + year) % 39 + 1
print("номер =",number)
index = int(input())
names.sort()
surnames.sort()
names[index] = "Чжоу Нань-ван"
surnames[index] = "Чжоу Нань-ван"
print(names, surnames)

#9
def cities_output(linked_cities):
    for i in linked_cities:
        print(i)

linked_cities = deque()

cities = ["Большая Пысса", "Большие Пупсы", "Манды", "Минструактивная", "Баклань", "Куриловка", "Старые Черви", "Блювиничи", "Синегубово", "Хреновое"]

for i in cities:
    linked_cities.append(i)
    
cities_output(linked_cities)

city_to_delete = input("\nКакой город удалить?: ")
if city_to_delete in linked_cities:
    linked_cities.remove(city_to_delete)
cities_output(linked_cities)

konec_city = "Конец"
index= int(input(f"\nНа какое место  вставить город {konec_city}? : "))
linked_cities.insert(index, konec_city)
cities_output(linked_cities)
