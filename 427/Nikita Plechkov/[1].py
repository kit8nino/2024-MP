from random import choice
import datetime
school_subjects = {"Алгебра": 5,
"Информатика":3,
"Химия":3,
"Геометрия":4,
"Астрономия":5,
"География":3,
"Литература":4,
"Физкультура":4,
"Биология":3,
"Физика":5,
"Обществознание":5,
"История":3,
"Музыка":4,
"Технология":5
}
actor = ("Clint","Eastwood","1930-31-05")
list_of_popular_male_names = ["Иван","Александр","Сергей","Андей","Дмитрий","Алексей","Максим","Владимир","Евгений","Денис"]
list_of_popular_female_names = ["Елена","Мария","Ольга","Наталья","Екатерина","Татьяна","Анастасия","Светлана","Ирина","Марина"]
list_of_popular_sernames =["Иванов","Петров","Попов","Смирнов","Кузнецов","Новиков","Сергеев","Мальцев"]



list_of_full_male_names = [f"{choice(list_of_popular_male_names)} {choice(list_of_popular_sernames)}" for i in range(15)]
list_of_full_female_names = [f"{choice(list_of_popular_female_names)} {choice(list_of_popular_sernames)}а" for i in range(15)]

list_of_full_names = list_of_full_male_names+list_of_full_female_names
print(list_of_full_names,"\n")
#print(list_of_full_names,len(list_of_full_names))

tamandua_name = "Весёлый смешарик"

#задание 1
def task_1(subj_dict):
    counter = 0
    avg = 0
    for subject in school_subjects:
        avg += school_subjects[subject]
        counter +=1
    avg/=counter
    return avg
print(f"Задание 1.\nСредняя оценка в аттестате: {task_1(school_subjects)}\n")
#задание 2
def task_2(w_names,m_names):
     names = w_names+m_names
     set_of_names = set(names)
     return (f"Задание 2.\nУникальные имена среди взятых из таблицы популярных: {set_of_names}\n")
     
print(task_2(list_of_popular_female_names,list_of_popular_male_names))
#задание 3
def task_3(subj_dict):
    sum_len = 0
    
    for subject in school_subjects:
        sum_len +=len(subject)
    return sum_len

print(f"Задание 3.\nОбщая длина всех названий предметов: {task_3(school_subjects)}\n")

#задание 4
def task_4(subj_dict):
    letter_set = set()
    for subj in subj_dict:
        for i in range(len(subj)):
            letter_set.add(subj[i])
    return letter_set
print(f"Задание 4.\nУникальные буквы в названиях предметов: {task_4(school_subjects)}\n")


#задание 5
def task_5(name):
    binary_name = ''.join(format(ord(i),'08b')for i in name)
    return(binary_name)
    
print(f"Задание 5.\nИмя тамандуа в бинарном виде: {task_5(tamandua_name)}\n")

#задание 6
def task_6(actor):
    actor_date = actor[2]
    actor_day = int(actor_date[5:7])
    actor_month = int(actor_date[8:10])
    actor_year = int(actor_date[:4])
    actor_date = datetime.date(actor_year,actor_month,actor_day)
   

    today = datetime.datetime.now()
    year_now = today.year
    month_now = today.month
    day_now = today.day
    date_now =datetime.date(year_now,month_now,day_now)
    return abs(actor_date-date_now).days


print(f"Задание 6.\nколичество дней от даты рождения актера вестерна до текущей даты: {task_6(actor)} \n")
#11 было 34314

#задание 7
def task_7():
    FIFO = []
    print("Задание 7.\n")
    while True:
        print("Введите название стройматериала (Введите 'stop' для завершения): \n")
        material = str(input())
        if material == "stop":
            return FIFO
        else:
            FIFO.append(material)
            
print(f"Список введённых стройматериалов {task_7()}\n")     

#задание 8

def task_8(name_list):
    full_name ="Чжоу И-ван"
    print(f"Задание 8.\nВведите индекс в диапазоне от 0 до {len(name_list)-1} ")
    while True:
        index = int(input())
        if index <0 or index > len(name_list)-1:
            print(f"Вы вышли за диапазон массива, пожалуйста введите индекс ещё раз")
        else:
            break
    name_list = sorted(name_list)
    name = full_name[5:]
    name_list[index] = name
    return f"Имя {name} китайского императора {full_name} было занесено в массив мужских имён под индексом {index}:{name_list}"
print(task_8(list_of_popular_male_names))

#задание 9

cities_dict = {
          "Хреновое":1,
          "Большое Бухалово":4,
          "Свиновье":5,
          "Кончинино":7,
          "Крутая":10,
          "Цаца":11,
          "Чуваки":12,
          "Такое":14,
          "Жабино":13,
          "Красная Могила":15,
          "Добрые Пчелы":9,
          "Синегубово":8,
          "Засосная":6,
          "Новые Алгаши":3,
          "Безводовка":2,
          "Верхнее Зачатье":0
          }
cities_list = ["Верхнее Зачатье","Хреновое","Безводовка","Новые Алгаши","Большое Бухалово","Свиновье","Засосная","Кончинино","Синегубово"
,"Добрые Пчелы","Крутая","Цаца","Чуваки","Жабино" ,"Такое","Красная Могила"]
def task_9(cities_dict: dict,cities_list: list):
    print("Задание 9.\n")
    print(f"Введите индекс города,который вы хотите удалить, от 0 до {len(cities_dict)-1}")
    while True:
        index1 = int(input())
        if index1 <0 or index1 > len(cities_dict)-1:
            print(f"Вы вышли за диапазон массива, пожалуйста введите индекс ещё раз")
        else:
            break
    for key,cities_dict[key] in cities_dict.items():
        if cities_dict[key] == index1:
            city = key
            break
    cities_dict.pop(city)
    print(f"Введите номер индекса, куда вы хотите вставить город 'конец' от 0 до {len(cities_list)-1}" )
    while True:
        index2 = int(input())
        if index2 <0 or index2 > len(cities_list)-1:
            print(f"Вы вышли за диапазон массива, пожалуйста введите индекс ещё раз")
        else:
            break
    first_part = cities_list[:index2]
    second_part =  cities_list[index2:]
    first_part.append("Конец")
    result = first_part+second_part
    return f"Из исходного словаря был удалён город '{city}'.\n {cities_dict}\n В список городов был добавлен город 'Конец' под индексом {index2}.\n{result}"
print(task_9(cities_dict,cities_list))




