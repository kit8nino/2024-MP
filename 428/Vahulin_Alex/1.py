from random import randint

subjects={
    "Algebra": 5,
    "Geometry": 4,
    "Physics": 5,
    "Biology": 3,
    "Psychology": 4,
    "Theology": 3,
    "English": 5,
    "Russian": 4,
    "French": 3,
    "Alchemy": 5,
    "Demonology": 5,
    "3D-modeling": 5,
    "Radioelectronics": 5,
    "Physical education": 5
    }

western_actor=tuple(["Lee Van Cleef","09","01","1925"])

popular_fnames_Voronezh=["Елена","Екатерина","Ольга","Мария","Анастасия","Ирина","Наталья","Татьяна","Юлия","Светлана"]
popular_mnames_Voronezh=["Иван","Александр","Сергей","Дмитрий","Андрей","Алексей","Максим","Евгений","Владимир","Роман"]
popular_surnames_Voronezh=["Иванов","Попов","Петров","Кузнецов","Сергеев","Смирнов","Новиков","Васильев"]

popular_combos=[]

for i in range(15):
    popular_combos.append(popular_surnames_Voronezh[randint(0,7)]+" "+popular_mnames_Voronezh[randint(0,9)])
    
for i in range(15):
    popular_combos.append(popular_surnames_Voronezh[randint(0,7)]+"а"+" "+popular_fnames_Voronezh[randint(0,9)])
    
tamandua_name="Ушастая Булка"