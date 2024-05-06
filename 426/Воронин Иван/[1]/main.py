# here'll be imports
import random

# Data structures:

# №1
subject_list = {"memology", "astrology", "biology", "geology", "language", "pe", "soft development", "hard envelopment", "physics",
	"thaumaturgy", "navigation", "sailing", "mailing", "stealth chatting", "party making"}

sertificate = {}

for subject in subject_list:
	mark = random.randint(1, 6) + 1
	if mark > 5:
		sertificate[subject] = 5
	else:
		sertificate[subject] = mark
# int[] sertificate - random generated dictionary with marks (with correction to average about 4.5 and limited to [2; 5])



# №2
actor = ("John Wayne", "26.05.1907")



# №3
# birthday: 09.02.2003, city is Samara
names = ("Иван", "Сергей", "Александр", "Андрей", "Дмитрий", "Алексей", "Максим", "Владимир", "Евгений", "Денис")
surnames = ("Иванов", "Петров", "Сергеев", "Кузнецов", "Смирнов", "Андреев", "Васильев", "Попов")

names_array = []

for i in range(30):
	names_array.append(random.choice(names)+' '+random.choice(surnames))



# №4
tamandua_name = "long bear"


