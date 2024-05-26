import random
import datetime
from datetime import date
import numpy as np
# ------------------------------------------
a ={'английский':2,
  'русский':5,
  'математика':4,
  'физика':3,
  'немецкий':2,
  'биология':4,
  'физра': 1,
  'матанализ':5,
  'алгем':5,
  'химия':1,
  'изо':3,
  'информатика':2,
  'окружающий мир':5,
  'обж':2,
  'история':5,
  'тфкп':5,
  'лабы':2}


Clint  = ('Clint Eastwood', datetime.date(1930,5,31))


names = ['Иван','Александр','Сергей','Андрей','Дмитрий','Алексей','Максим','Владимир','Евгений','Игорь']
surnames = ['Иванов','Петров','Смирнов','Сергеев','Попов','Волков','Кузнецов','Васильев']

Pet = 'Indiana Jeez'

# ---------------------------------------------

Sum = sum(a.values())
Avg = Sum/len(a)
print(Avg)
    
# -------------------------------------------------
UNames = []
for i in range(len(names)-1):
    UName = names[random.randint(0,len(names)-1)] + " " + surnames[random.randint(0,len(surnames)-1)]
    UNames.append(UName)
# ------------------------------------------------------

lenght = 0
subjects = list(a.keys())
for i in range(len(a)):
    lenght += len(subjects[i])
print(lenght)

# -------------------------------------------------
Uchars = []
subjects = list(a.keys())
for key in a:
    for i in range(len(key)):
        if key[i] not in Uchars:
            Uchars.append(key[i])
Uchars.remove(" ")
print(Uchars)

# ---------------------------------------------------


Pet2  = ' '.join(format(ord(char), '08b') for char in Pet)
print(Pet2)

# ------------------------------------------------------

print(date.today() - Clint[1])

# --------------------------------------------------------


# ------------------------------------------------------------      

number = (31 + 25  + 1930)%39 + 1;
name0 = "Чжоу Нань-ван"
UNames.sort()
print("Vvedite index")
UNames[int(input())] = name0
print(UNames)

# ----------------------------------------------------------------

Towns = ["Большая Пысса","Большие Пупсы","Минструактивная"," Манды", "Дешевки ", "Новый русский спуск","Такое","Тухлянка","Овнище"]
Towns.remove(str(input("КАкой город удалить?: ")))
print(Towns)
Towns[int(input("Куда добавить конец? "))] = "Конец"
print(Towns)
# -----------------------------------------------------------
import queue
q = queue.Queue()
print("Введите стройматериалы")
while True:
    c = input()
    if c == "Остановить":
        break
    q.put(c)
while not q.empty():
    print(q.get())
