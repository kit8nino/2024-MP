vestern_actor = tuple(("Клинт Иствуд", "31", "05", "1930"))
my_marks = {
    'Русский язык': 5,
    'Математика': 5,
    'Физика': 5,
    'Литература': 5,
    'Биология': 5,
    'Информатика': 5,
    'Химия': 5,
    'Астрономиия': 5,
    'История': 5,
    'Обществознание': 5,
    'География': 5,
    'Физическая культура': 5,
    'Английский язык': 5,
    'Краеведение': 5,
    'Истрия России': 5,
    'Родной язык': 5,
    'Задачи в математике': 5}
popular_names = ['Елена Иванова', 'Екатерина Иванова', 'Мария Иванова',
               'Ольга Иванова', 'Анастасия Иванова', 'Ирина Иванова', 'Наталья Иванова',
               'Елена Кузнецова', 'Елена Петрова', 'Мария Петрова', 'Юлия Иванова', 'Ольга Кузнецова',
               'Ольга Васильева', 'Анастасия Романова', 'Татьяна Смирнова', 'Иван Иванов', 'Иван Петров',
               'Сергей Иванов','Александр Иванов','Сергей Сергеев','Дмитрий Иванов', 
               'Алексей Иванов','Андрей Иванов','Максим Иванов','Владимир Иванов',
               'Сергей Петров','Александр Петров','Андрей Петров','Александр Кузнецов',
               'Андрей Андреев','Екатерина Волкова','Ольга Попова']
home_tamandua = "Длинноногий удав"

all = 0
mid_mark = 0
for subject, mark in my_marks.items():
    all += mark
    mid_mark = all/len(my_marks)
print('1. Средняя оценка в аттестате:', mid_mark, '\n' )
mod_popular_names = popular_names.copy()
unique_popular_names = []
for x in mod_popular_names:
  name = x.split()[0]
  if not name in unique_popular_names:
      unique_popular_names.append(name)
print('2. Уникальные имена в списке:',unique_popular_names,'\n' )
letters_coun = 0
letters = []
for key, value in my_marks.items():
    letters.append(key)
    for x in range(len(letters)-1):
        length = len(letters[x])
        letters_coun += length
        unique_letters = []
letter = []
for i in letters:
    letter.append(i.lower())
    for m in range(len(letter)-1):
        for t in letter[m]:
            if not t in unique_letters:
                unique_letters.append(t)

print('3. Общая длина всех названий предметов:', letters_coun, '\n')

print('4. Уникальные буквы в назвнии предметов:', unique_letters, '\n')

bin_name = ''.join(format(ord(x), '08b') for x in home_tamandua)
print('5. Имя моего домашнего тамандуа в бинарном виде:', bin_name, '\n')

from datetime import date
klint_birthday = date(1930, 5, 31)
nowaday = date.today()
count_day = nowaday - klint_birthday
print ('6. Кол-во дней от дня рождения Клинта Иствуда до актуальной даты:', count_day, '\n')
print ('7. FIFO-очередь со стоп-словом "end":' )
FIFO_que = []
word = "end"
while True:
    list = input('Введите значение:')
    if list == word:
        for x in range(len(FIFO_que)):
            print(FIFO_que.pop(),end=" ")
        break
    FIFO_que.append(list)

name_chgou = ['Чжоу У-ван', 'Чжоу Чэн-ван', 'Чжоу Кан-ван', 'Чжоу Чжао-ван', 'Чжоу Му-ван',
                'Чжоу Гун-ван', 'Чжоу И-ван (Си)', 'Чжоу Сяо-ван', 'Чжоу И-ван (Се)', 'Чжоу Ли-ван', 'Гунхэ',
                'Чжоу Сюань-ван', 'Чжоу Ю-ван', 'Чжоу Пин-ван', 'Чжоу Хуань-ван', 'Чжоу Чжуан-ван', 'Чжоу Си-ван'
                'Чжоу Хуэй-ван','Чжоу Сян-ван','Чжоу Цин-ван','Чжоу Куан-ван','Чжоу Дин-вай Юй','Чжоу Цзянь-ван','Чжоу Лин-ван',
                'Чжоу Цзин-ван Гуй','Чжоу Дао-ван','Чжоу Цзин-ван Чай','Чжоу Юань-ван','Чжоу Дин-ван Цзе','Чжоу Ай-ван','Чжоу Сы-ван',
                'Чжоу Као-ван','Чжоу Вэй Ле-ван','Чжоу Ань-ван','Чжоу Ле-ван','Чжоу Сянь-ван','Чжоу Шэнь Цзинь-ван','Чжоу Нань-ван',
                'Чжоу Хуэй-ван']
def change(i,A):
    number = (31 + 5 ** 2 + 1930) % 39 + 1
    A[i] = name_chgou[number]
    return print ("8. Результат:", A,'\n')


city_names = {
    "Адский ручей": 0,
    "Озеро чудовищ": 1,
    "Дешевки": 2,
    "Деревня дураков": 3,
    "Козявкино": 4,
    "Старые Черви": 5,
    "Дураково": 6,
    "Вобля": 7
}

for city, index in city_names.items():
    print(f"{city} -> {index}")

delete_city = input("Введите название города для удаления: ")

if delete_city in city_names:
    del city_names[delete_city]
else:
    print("Такого города нет в списке.")

input_city = int(input("Введите индекс для вставки города Конец: "))

for city in city_names:
    if city_names[city] >= input_city:
        city_names[city] += 1

city_names["Конец"] = input_city
for city, index in city_names.items():
    print(f"{city} -> {index}")
print('9. Новый словарь:', city_names, '\n')
