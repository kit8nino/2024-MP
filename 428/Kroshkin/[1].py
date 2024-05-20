import datetime as dt
import random
import queue

atestat = {'Russian': 4,
         'liter': 5,
         'Alg': 5,
         'Geom': 5,
         'History': 4,
         'Geography': 5,
         'Phys': 5,
         'Biology': 3,
         'Chemistry': 4,
         'Eng': 5,
         'inform': 5,
         'fizra': 5,
         'Izo': 3,
         'Franch': 3,
         'lingua Latina': 3}
Actor = ('Clint', 'Eastwood', dt.datetime(1930, 5, 30))
Name = ["Ivan", "Alexandr","Sergey","Dmitriy","Andrey","Aleksey","Evgeniy","Maxim","Vladimir","Denis"]
surname=["Ivanov", "Petrov", "Kuznecov","Smirnov","Sergeev", "Popov", "Vasilev", "Volkov"]
tamadua="Fast Beast"
#1
def sr_otmetka(x):
    S = 0
    count = 0
    for value in x.values():
        S += value
        count += 1
    return S / count

print(sr_otmetka(atestat))
print()
#2
def random_fullname():
    ans = []
    N, S = random.randint(0, len(Name)-1), random.randint(0, len(surname)-1)
    ans.append(Name[N])
    ans.append(surname[S])
    return ans


for i in range(3):
    print(random_fullname())
print()
#3  
def lennn(x):
    S = 0
    for key in x.keys():
        S += len(key)
    return S

print(lennn(atestat))
print()
#4
def unique(x):
    ans = []
    for key in x.keys():
        for i in range(len(key)):
            if key[i].lower() not in ans and key[i] != ' ':
                ans.append(key[i].lower())
            else:
                continue
    return ans

unique_letters = unique(atestat)
print(unique_letters)
print()
#5
def unique(x):
    ans = []
    for key in x.keys():
        for i in range(len(key)):
            if key[i].lower() not in ans and key[i] != ' ':
                ans.append(key[i].lower())
            else:
                continue
    return ans

unique_letters = unique(atestat)
print(unique_letters)
print()
#6
print(dt.datetime.today() - Actor[2])
print()
#7
q1 = queue.Queue()
while True:
    material = input()
    if material == '0':
        break
    q1.put(material)

while not q1.empty():
    print(q1.get())
print()
#8
index = int(input())
Name.sort()
surname.sort()
Name[index] = "Чжоу Пин-ван"
surname[index] = "Чжоу Пин-ван"
print(Name, surname)
print()
#9
towns = ["Малая Землянка", "Большая Красная", "Синяя Долина", "Зеленый Луг", "Радужный Город", "Черный Лес", "Белая Река", "Желтый Остров", "Фиолетовая Гора", "Оранжевое Небо"]


towns.remove(str(input("Выберите город, чтобы сравнять его с землей: ")))
print(towns)
print()

towns[int(input("Город умер! Да здравствует новый город!(номер города): "))] = "Конец"
print(towns)
print()