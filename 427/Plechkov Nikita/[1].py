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