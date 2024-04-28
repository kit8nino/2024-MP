import datetime as dt
import random
import queue

marks = {'Russian': 3,
         'Literature': 2,
         'Algebra': 2,
         'Geometry': 3,
         'History': 2,
         'Geography': 3,
         'Physics': 3,
         'Biology': 2,
         'Chemistry': 5,
         'English': 4,
         'Computer science': 2,
         'Physical education': 4,
         'Art': 2,
         'German': 3,
         'lingua Latina': 2}

Actor = ('Clinton', 'Eastwood', dt.datetime(1930, 5, 31))

Names = ["Ivan", "Alexander", "Sergei", "Andrew", "Dmitrii", "Alexei", "Max","Mikhail", "Vladimir", "Nikita"]
Surnames = ["Ivanov", "Petrov", "Smirnov", "Sergeev", "Volkov", "Kuznetsov", "Vasilyev", "Romanov"]

tamandua = "Exotic Bobik"

"""-----------------------------------#1------------------------------------"""
def avg(x):
    S = 0
    count = 0
    for value in x.values():
        S += value
        count += 1
    return S / count

print(avg(marks))
        
"""-----------------------------------#2------------------------------------"""
def random_fullname():
    fullname = ''
    N, S = random.randint(0, len(Names)-1), random.randint(0, len(Surnames)-1)
    fullname = Names[N] + " " + Surnames[S]
    return fullname

Fullnames = []
for i in range (50):
    Fullnames.append(random_fullname())
print(Fullnames)
"""-----------------------------------#3------------------------------------"""
def length(x):
    S = 0
    for key in x.keys():
        S += len(key)
    return S

print(length(marks))

"""-----------------------------------#4------------------------------------"""
def unique_chars(x):
    ans = []
    for key in x.keys():
        for i in range(len(key)):
            if key[i].lower() not in ans and key[i] != ' ':
                ans.append(key[i].lower())
            else:
                continue
    return ans
            
unique_letters = unique_chars(marks)
print(unique_letters)        

"""-----------------------------------#5------------------------------------"""
def tento2(x):
    s = ''
    while x > 0:
        s += str(x % 2)
        x //= 2
    return s[::-1]

for i in range(len(tamandua)):
    print(tento2(ord(tamandua[i])), " - ", tamandua[i])

"""-----------------------------------#6------------------------------------"""
print(dt.datetime.today() - Actor[2])

"""-----------------------------------#7------------------------------------"""
q1 = queue.Queue()
while True:
    #enter 0 to stop
    material = input()
    if material == '0':
        break
    q1.put(material)

while not q1.empty():
    print(q1.get())

"""-----------------------------------#8------------------------------------"""
index = int(input())
# year, month, day = Actor[2].year, Actor[2].month, Actor[2].day
# number = (day + month**2 + year) % 39 + 1
# print(number) #37 (Чжоу Шэнь Цзинь-ван)
Fullnames.sort()
Fullnames[index] = "Чжоу Шэнь Цзинь-ван"
print(Fullnames)

"""-----------------------------------#9------------------------------------"""
cities = ["Новиград", "Оксенфурт", "Вызима", "Боклер", "Третогор",
               "Ард Каррайг", "Лан Эксетер", "Понт Ванис", "Нильфгаард",
               "Венгерберг", "Ривия", "Цинтра", "Виковаро"]

cities.remove(str(input("Выберите город, чтобы сравнять его с землей: ")))
print(cities)

cities[int(input("Город умер! Да здравствует новый город!(номер города): "))] = "Конец"
print(cities)
