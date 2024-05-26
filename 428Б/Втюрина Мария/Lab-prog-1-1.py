import numpy as np 
import random
import datetime
from datetime import date

#исходные данные
marks={'математика':5,'физика':4,'информатика':5,'русский язык':4,'литература':5,'английский язык':5,'химия':4,'биология':5,'обществознание':4,'история':5,'физкультура':5,'география':4,'индивидуальный проект':5,'латинский язык':4,'древнегреческий язык':5,}
actor=('Clinton',' Eastwood ',datetime.date(1930,5,31))

surnames_male=['Иванов','Петров','Смирнов','Васильев','Сафин','Зарипов','Хайруллин','Закиров']
surnames_female=['Иванова','Петрова','Смирнова','Романова','Сафина','Шакирова','Хайруллина','Закирова']
names_male=['Иван','Сергей','Александр','Андрей','Дмитрий','Алексей','Руслан','Максим','Марат','Артур']
names_female=['Мария','Екатерина','Алина','Елена','Ольга','Анастасия','Лилия','Ирина','Марина','Алсу']


def people(surnames_male,surnames_female,names_male,names_female):
    FIO=[]
    while (len(FIO))<56:
        a=random.randint(0,(len(surnames_female)-1))
        b=random.randint(0,(len(names_female)-1))
        FIO.append(surnames_female[a]+' '+names_female[b])
    return FIO

FIO=people(surnames_male,surnames_female,names_male,names_female)

tamandua_name='большая пчёлка'

#task 1
def averageball(marks):
    sum=0
    for k,v in marks.items():
        sum+=v
    av_ball=sum/(len(marks))
    return av_ball

print('Задание №1')
print('Средний балл аттестата:',averageball(marks),"\n\n")

#task2
def uniquenames(FIO):
    uniques=set(FIO)
    return uniques

print('Заданиие №2: Уникальные имена и фамилии')
uniques=uniquenames(FIO)
print(uniques,"\n\n")

#task 3
def full_length(marks):
    fullstr=''
    for k in marks.keys():
        fullstr+=k
    full_length=len(fullstr)
    return full_length
print('Задание №3')
print('Общая длина названий предметов: ',full_length(marks),'символа\n\n')

#task4
def unique_letters(word):
    return set(word)

for k in marks.keys():
    print('Уникальные буквы в слове \"',k,'\": ',unique_letters(k))
print('\n\n')

#task5
def to_bin(str):
    bin_str=''.join(format(ord(x),'08b') for x in str)
    return bin_str
print('Задание №5:')
print('Имя тамандуа:',tamandua_name)
print('Имя тамандуа в бинарном виде:',to_bin(tamandua_name),'\n\n')

#task6
actor_birthday=actor[2]#datetime.date(1930,5,31) 
print('Задание №6')
print('День рождения Клинта Иствуда:',actor_birthday)
current_date=date.today()
print('Текущая дата:',current_date)
delta = current_date-actor_birthday
print('Разница в днях:',delta.days,'\n')

#task7
class Queue:
    def __init__(self):
        self.queue=[]
        
    def add(self,val):
        self.queue.append(val)
        
    def remove(self,val):
        self.queue.pop(0)
        
    def insert(self): 
        print("Введите (-1) для остановки")
        while True:
            ind=int(input("Введите индекс:"))
            if ind== -1:
                print(self.queue)
                break
            else:
                if ind>len(self.queue) and ind!=0:
                    print('в очереди нет столько элементов')
                elif ind<0 and ind!=-1:
                    print('индекс должен быть положительным')
                else:
                    val=input("Введите стройматериал:")
                    self.queue.append(0)
                    j=len(self.queue)-1
                    while j!=ind:
                        self.queue[j]=self.queue[j-1]
                        j-=1
                    self.queue[ind]=val
                    print('Готово!')
materials=Queue()
materials.insert()

#task8
def change_the_name_to_chinese_imperator(list_of_names):
    chinese_imperators=['У-ван','Чэн-ван','Кан-ван','Чжао-ван','Му-ван','Гун-ван','И-ван','Сяо-ван','Ли-ван','Гунхэ','Сюань-ван','Ю-ван','Пин-ван','Хуань-ван','Чжуан-ван','Си-ван','Хуэй-ван','Сян-ван','Цин-ван','Куан-ван','Дин-ван','Цзянь-ван','Лин-ван','Цзин-ван','Дао-ван','Цзин-ван','Юань-ван','Джэнь Дин-ван','Ай-ван','Сы-ван','Као-ван','Вэй Ле-ван','Ань-ван','Ле-ван','Сянь-ван','Шэнь Цзинь-ван','Нань-ван','Хуэй-ван']
    number = (actor_birthday.day + actor_birthday.month**2 + actor_birthday.year) % 39 + 1
    here=int(input("Введите индекс для имени, которое будет заменено на имя китайского императора:"))
    list_of_names[here]=chinese_imperators[number].upper()
    return list_of_names


print('\nЗадание №8')
list_of_uniques=list(uniques)
change_the_name_to_chinese_imperator(list_of_uniques)
print(list_of_uniques,'\n')

#task9
print('Задание№9\n')
list_of_weird_places=[ 'Ломки','Да-да','Вобля','Хреновое','Блювиничи','Большое Бухалово','Свиновье','Синие Лепяги','Жабино','Кончинино','Раздериха','Чуваки','Мусорка','Голодранкино','Безводовка','Красная Могила','Кундрючья','Хотелово','Добрые Пчелы','Синегубово']
print('У вас сеть список странных названий географических объектов:\n\n',list_of_weird_places)

def create_a_linked_list(list):
    dict={}
    for i in range (len(list)-1):
        dict[list[i]]=i+1
    dict[list[len(list)-1]]=0
    return dict

def delete_the_node(linked_list,n):
    
    current_ref=linked_list[n]
    new_ref=current_ref-1
    key_list=list(linked_list.keys())
    val_list=list(linked_list.values())
    for i in range (len(linked_list)):
        if val_list[i]==new_ref:
            linked_list[key_list[i]]=current_ref
    return linked_list

def from_dict_to_key_list(dict):
    key_list=list(dict.keys())
    return key_list
        
def insert_konets(list_of_places):
    n=int(input("\nВведите индекс(от 0 до 20),куда будет вставлен \"КОНЕЦ\":"))
    list_of_places.append(0)
    j=len(list_of_places)-1
    while j!=n:
        list_of_places[j]=list_of_places[j-1]
        j-=1
    list_of_places[n]='КОНЕЦ'
    return create_a_linked_list(list_of_places)
    
weirdness=create_a_linked_list(list_of_weird_places)
n=input("\nВведите название для удаления:")
print(delete_the_node(weirdness,n)) 
print(insert_konets(from_dict_to_key_list(weirdness)))
