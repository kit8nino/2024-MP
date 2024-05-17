import random
from datetime import datetime as dt
from queue import Queue

subjects = {'Русский язык': 4, 
            'Литература': 2, 
            'Математика': 3, 
            'Иностранный язык': 2, 
            'История': 2, 
            'Обществознание': 2, 
            'Биология': 4, 
            'Физика': 5, 
            'Химия': 5, 
            'География': 5, 
            'Информатика': 3, 
            'Технология': 4, 
            'Музыка': 4, 
            'ИЗО': 5, 
            'Физкультура': 4
}

actor = ('Clinton', 'Eastwood', '1930-05-31')

names_surnames = ['Сергей Волков', 'Денис Иванов', 'Денис Попов', 'Дмитрий Ростовский', 'Иван Сергеев', 
                  'Александр Ростовский', 'Владимир Сергеев', 'Иван Иванов', 'Иван Волков', 'Максим Ростовский', 
                  'Александр Попов', 'Максим Ростовский', 'Алексей Сергеев', 'Максим Ростовский', 'Алексей Смирнов', 
                  'Максим Романов', 'Сергей Романов', 'Алексей Волков', 'Евгений Романов', 'Максим Попов', 'Александр Волков', 
                  'Алексей Иванов', 'Алексей Волков', 'Владимир Иванов', 'Алексей Попов', 'Сергей Смирнов', 'Дмитрий Волков', 
                  'Сергей Смирнов', 'Алексей Попов', 'Алексей Иванов']

tamandua = 'Пушистый Пылесос'

#1
sum = 0
for sub in subjects:
    sum += subjects[sub]
avg = sum/len(subjects)
print(f'1: {avg}')
print('----------------------')

#2
names = []
for elem in names_surnames:
    names.append(elem.split()[0])
names = set(names)
print(f'2: {names}')
print('----------------------')

#3
total = ''
for sub in subjects:
    total += sub
total = total.replace(' ','')
print(f'3: {len(total)}')
print('----------------------')

#4
print(f'4: {sorted(set(total.lower()))}')
print('----------------------')

#5
res = ''
for sym in tamandua:
    res += str(bin(ord(sym)))
res = res.replace('b','')
print(f'5: {res}')
print('----------------------')

#6
date = actor[2]
now = dt.now()
date = dt.strptime(date, '%Y-%m-%d')
print(f'6: {str(now-date).split(",")[0]}')
print('----------------------')

#7
print('7: \nInput:')
mats = Queue()
while True:
    cmd = input()
    if cmd == 'stop':
        break
    mats.put(cmd)
print('Output:')
while not mats.empty():
    print(mats.get())
print('----------------------')

#8
print('8: \nInput:')
chin = 'Цзи Янь'
index = int(input())
names_surnames[index] = chin + ' ' + names_surnames[index].split()[1]
print('Output:')
print(names_surnames)
print('----------------------')

#9
print('9: \nInput:')
cities = ["Большая Пысса", "Большие Пупсы", "Манды", 
          "Дешевки", "Такое", "Тухлянка", "Баклань", 
          "Лохово", "Факфак", "Большое Струйкино", "Овнище", "Дно", "Трусово", 
          "Кокаиновые горы", "Косяковка", "Куриловка", "Ширяево", 
          "Ломки", "Большой Куяш", "Иннах", "Крутые Хутора", "Крутая", "Новые Алгаши"]
result = {}
i=1
for cit in cities:
    if i == len(cities):
        i = 0
    result[cit] = i
    i += 1
key = input("Key: ")
del result[key]
print(f'Output: {result}')

ind = int(input("Index: "))
cities = list(result.keys())[0:ind]+["Конец"]+list(result.keys())[ind:]
result = {}
i=1
for cit in cities:
    if i == len(cities):
        i = 0
    result[cit] = i
    i += 1
print(f'Output: {result}')
