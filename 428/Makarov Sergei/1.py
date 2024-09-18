from datetime import datetime, timedelta
import random
from collections import deque
import collections
subj={'Алгебра': 3,
      'Геометрия': 4,
      'Русский': 3,
      'Биология': 4,
      'Химия': 2,
      'Физика': 5,
      'Физкультура': 3,
      'Экономика': 3,
      'Иностранный ': 2,
      'История': 1,
      'Изо': 4,
      'География': 6,
      'Родной': 2,
      'Проект': 3}
act = ('John', 'Wayne', 1907, 5, 26)
nizh_name=['Александр','Иван','Сергей','Дмитрий','Алексей','Андрей','Максим','Евгений','Михаил','Владимир']
nizh_surname=['Иванов','Смирнов','Петров','Кузнецов','Волков','Соколов','Белов','Морозов']
full_name = []
name_taman = 'Мудрый танос'

n_count = 0
while (n_count < 31):
      full_name.append(random.choice(nizh_name) + ' ' +random.choice(nizh_surname))
      n_count += 1  

summ = 0
quant = len(subj)
for key in subj:
      summ += subj[key]
print(summ/quant, ' - средний балл ' )


unique_names = list(set(full_name))  
sorted_names = sorted(unique_names)  
print(sorted_names)


unique_letters = []
for item in subj:
    for i in range(len(item)):
        if item[i] not in unique_letters:
            unique_letters.append(item[i])
unique_letters.sort()
print(unique_letters)


b_result = ''.join(format(x,'08b') for x in bytearray(name_taman,'utf-8')) 
print("Bin result", b_result)
                  

current_date = datetime.now()
other_date = datetime(act[2],act[3],act[4])
result = other_date - current_date
print(abs(result.days), 'дней после смерти', act[0], '', act[1])


queue = deque()

while True:
    material = input("Введите название стройматериала или введите 'стоп', чтобы остановиться: ")
    if material == 'стоп':
        break
    queue.append(material)

print("Список стройматериалов:")
for material in queue:
    print(material)

print('Enter index < 31:')
ren=int(input())
china='Zhou Wu-wang'
sorted_names[ren]=china
print(sorted_names)
print('')

town=collections.deque() 
town.append('Горшки')
town.append('Рожки')
town.append('Комары')
town.append('Хомяки')
town.append('Вперед')
town.append('Мусорка')
value=str(input('Введите значение для удаления:'))
i=int(input('Введите индекс связанного списка:'))
town.remove(value)
town.insert(i,'Конец')
print('Towns: ',town)

