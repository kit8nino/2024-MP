from datetime import datetime, timedelta
import random
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
while (n_count < 30):
      full_name.append(random.choice(nizh_name) + ' ' +random.choice(nizh_surname))
      n_count += 1  

summ = 0
quant = len(subj)
for key in subj:
      summ += subj[key]
print(summ/quant, ' - средний балл ' )


unique_names = list(set(full_name))  
sorted_names = sorted(unique_names)  
print(len(sorted_names, ' уникальных имен' ))
                  

current_date = datetime.now()
other_date = datetime(act[2],act[3],act[4])
result = other_date - current_date
print(abs(result.days), 'дней после смерти', act[0], '', act[1])
