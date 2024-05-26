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
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printlist(self):
        current = self.head
        while current:
            print(current.data, end = ', ')
            current = current.next
        print()
    
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            print("Вы добрались до края света. Дальше живут драконы. Возвращайтесь.") #No such element in list
            return
        previous.next = current.next
        current = None
        
    def add(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                print("Шу-шу. Шу-шу. Сердце перекачивает жизнь...") #list index out of range
                return
            current = current.next
        if current is None:
            print("Шу-шу. Шу-шу. Сердце перекачивает жизнь...")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
            
cities = LinkedList()
cities.append("Новиград")
cities.append("Оксенфурт")
cities.append("Вызима")
cities.append("Боклер")
cities.append("Третогор")
cities.append("Ард Каррайг")
cities.append("Лан Эксетер")
cities.append("Понт Ванис")
cities.append("Нильфгаард")
cities.append("Венгерберг")
cities.append("Ривия")
cities.append("Цинтра")
cities.append("Виковаро")

cities.printlist()
print("---------------------------------------------------------------")
key = input("Выберите город, чтобы сравнять его с землей: ")
cities.delete(key)
print("---------------------------------------------------------------")
cities.printlist()
print("---------------------------------------------------------------")
ind = int(input("Город умер! Да здравствует новый город!(номер города): "))
cities.add(ind, "Конец")
print("---------------------------------------------------------------")
cities.printlist()
