# here'll be imports
import random
import datetime as dt
import queue

# Data structures:

# №1
subject_list = {"memology", "astrology", "biology", "geology", "language", "pe", "soft development", "hard envelopment", "physics",
	"thaumaturgy", "navigation", "sailing", "mailing", "stealth chatting", "party making"}

certificate = {}

for subject in subject_list:
	mark = random.randint(1, 6) + 1
	if mark > 5:
		certificate[subject] = 5
	else:
		certificate[subject] = mark
# int[] certificate - random generated dictionary with marks (with correction to average about 4.5 and limited to [2; 5])



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



# Actions:

# №1
summ = 0
for i in certificate:
	summ += certificate[i]
average = summ / len(certificate)
print(f"action №1 (average mark): {average}\n")



# №2
names_array_uniq = []
counter2 = 0
for i in range(len(names_array)):
	counter = 0
	for j in range(i+1, len(names_array)):
		if names_array[i] == names_array[j]:
			counter += 1
			# print(f"name {names_array[i]} equal {names_array[j]}")
	if counter == 0:
		names_array_uniq.append(names_array[i])
	else:
		counter2 += 1
print(f"action №2 (unique names):\n{names_array_uniq}\n\n{counter2} names are repeated and have been removed\n")



# №3
summ = 0
for subject in certificate:
	summ += len(subject)
print(f"action №3 (total certificate lenght): {summ}\n")



# №4
alfabet = []
for subject in certificate:
	for letter in subject:
		counter = 0
		for alfabet_letter in alfabet:
			if alfabet_letter == letter:
				counter += 1
		if counter == 0:
			alfabet.append(letter)
alfabet.remove(' ')
print(f"action №4 (unique letters in certificate): {alfabet}\n")



# №5
tamandua_name_bin = ""
for letter in tamandua_name:
	tamandua_name_bin += str(bin(ord(letter)))[2:]
	# print(f"letter {letter} num is {ord(letter)} and bin is {str(bin(ord(letter)))}")
print(f"action №5 (tamandua binary name): {tamandua_name_bin}\n")



# №6
today = dt.datetime.now(tz=None)
time_past = today - dt.datetime.strptime(actor[1], "%d.%m.%Y")
print(f"action №6 (time past from actor birth date): {time_past.days}\n")



# №7
fifo_queue = queue.Queue()
print("<action №7>:\n\ttype material: ('q' to exit): ", end = '')
material = input()
while (material != "q"):
	print("\ttype material: ('q' to exit): ", end = '')
	fifo_queue.put(material)
	material = input()
print(f"\taction №7 (material_fifo): ")
print("\t", end='')
while(fifo_queue.empty() == False):
	print(f"{fifo_queue.get()}, ", end='')
print(f"\n</action №7>")



# №8
print("<action №8>")
# print((9 + 2**2 + 2003) % 39 + 1) = 28 (Yuánwáng)
for name_index in range(len(names_array)):	# output indexes and names
	print(f"\t{name_index} = {names_array[name_index]}")
print("\ttype name index: ", end='')
names_array[int(input())] = "Yuánwáng"		#switch name
for name_index in range(len(names_array)):	# output indexes and names
	print(f"\t{name_index} = {names_array[name_index]}")
print("</action №8>")



