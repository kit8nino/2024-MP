from datetime import datetime as dt
import collections


predmeti ={"Алгебра": 3,
           "Геометрия": 4,
           "Физика": 2,
           "Информатикa": 5,
           "Биология": 2,
           "Физкультура": 3,
           "Химия": 4,
           "ИЗО": 3,
           "Технология": 4,
           "ОБЖ": 3,
           "История": 5,
           "Обществознание": 5,
           "Английский язык": 3,
           "Русский язык": 2,
           "Литература": 4,
           }

actor = ("Альдо", "Джуффре", "10.04.1924")

novosibirskie_cheloveki = ['Иван Иванов',
                 'Александр Иванов',
                 'Сергей Иванов',
                 'Андрей Иванов',
                 'Дмитрий Иванов',
                 'Алексей Иванов',
                 'Максим Иванов',
                 'Евгений Иванов',
                 'Владимир Иванов',
                 'Денис Иванов',
                 'Иван Петров',
                 'Александр Петров',
                 'Сергей Петров',
                 'Андрей Петров',
                 'Дмитрий Петров',
                 'Алексей Петров',
                 'Максим Петров',
                 'Евгений Петров',
                 'Владимир Петров',
                 'Денис Петров',
                 'Иван Сергеев',
                 'Александр Сергеев',
                 'Сергей Сергеев',
                 'Андрей Сергеев',
                 'Дмитрий Сергеев',
                 'Алексей Сергеев',
                 'Максим Сергеев',
                 'Евгений Сергеев',
                 'Владимир Сергеев',
                 'Денис Сергеев',
                 'Иван Смирнов',
                 'Александр Смирнов',
                 'Сергей Смирнов',
                 'Андрей Смирнов',
                 ]

tamandua = "Крутой язычок"

#1
summa = 0
for i in predmeti:
    summa += predmeti[i]
sredn_ocenka = summa/len(predmeti)
print("1:", sredn_ocenka)

#2
uniqalinie_imena = []
for chelovek in novosibirskie_cheloveki:
    name = chelovek[:chelovek.find(' ')]
    if name not in uniqalinie_imena:
        uniqalinie_imena.append(name)
print("2:", uniqalinie_imena)

#3
dlina = 0
for j in predmeti:
        dlina += len(j)
print("3:", dlina)

#4
letter_set = set()
for word in predmeti:
    for letter in range(len(word)):
        letter_set.add(word[letter])
print("4:", letter_set)

#5
print("5:", end=' ')
for letter in tamandua:
    print(str(bin(ord(letter))).split('b')[1], end=' ')


#6
now_time = dt.now()
last_time = dt.strptime(actor[2], '%d.%m.%Y')
print("\n6:",  str(now_time-last_time).split(",")[0])

#7
print("7: Для остановки введите 'stop', \nВведите строковые названия стройматериалов:")
FIFO = collections.deque()

while True:
    word = input()
    if word == 'stop':
        break
    FIFO.append(word)
print("Стройматериалы:", tuple(FIFO))

#8
#number = (10 + 4**2 + 1924) % 39 + 1 = 1
name ="Чжоу У-ван"
print("8: Введите индекс в диапазоне от 0 до", len(novosibirskie_cheloveki)-1 )
while True:
    index = int(input())
    if index < 0 or index > len(novosibirskie_cheloveki)-1:
        print(f"Вы вышли за диапазона, введите верный индекс:")
    else:
        break
novosibirskie_cheloveki = sorted(novosibirskie_cheloveki)
novosibirskie_cheloveki[index] = name
   
print("Имя китайского императора", name, " было занесено в массив имён под индексом", index, ":", novosibirskie_cheloveki)

#9
goroda = ["Верхнее Зачатье", "Дураково", "Заячий пузырь", "Козявкино", "Цаца", "Засосная", "Звероножка", "Муходоево", "Да-да", "Вобля"]
slovar = {goroda[i]: goroda[i+1] for i in range(len(goroda)-1)}
slovar[goroda[-1]] = 0
print("\n9: Cвязный список:", slovar)
while True:
    deleted_city = input("\nВведите название города, который хотите удалить:")
    if deleted_city not in goroda:
        print("Названия вашего города нет в словаре")
    else:
        goroda.remove(deleted_city)
        slovar = {goroda[i]: goroda[i + 1] for i in range(len(goroda) - 1)}
        slovar[goroda[-1]] = 0
        break

print("\nСвязный список с удаленным городом:",slovar)
while True:
    put_end = input("\nВведите название города, который хотите заменить на 'Конец':")
    if put_end not in slovar.keys():
        print("Названия вашего города нет в словаре")
    else:
        for key, value in slovar.items():
            if value == put_end:
                slovar[key] = "КОНЕЦ"
        break

print("\nСвязный список с вставленным словом 'Конец'",slovar)
