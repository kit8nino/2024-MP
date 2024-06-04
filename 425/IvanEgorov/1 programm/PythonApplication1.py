import datetime
import random
import queue

subject = {
    "Russian language": 3, 
    "Algebra": 4,
    "Geometry": 4,
    "Literature": 4,
    "Chemistry": 4,
    "Geography": 5,
    "English language": 4,
    "Informatics": 5,
    "Life Safety":5,
    "Physics": 4,
    "History": 4,
    "Social Studies": 5,
    "Physical Education": 5,
    "Biology": 4
}

western_actor = ("Dean Martin", datetime.date(1917, 7, 6))

men_names = [
    'Ivan', 'Alexander', 'Sergei', 'Andrei', 'Dmitry', 
    'Alexey', 'Maxim', 'Vladimir', 'Evgeny', 'Igor'
]

women_names = [
    'Maria', 'Catherine', 'Anastasia','Elena', 
    'Anna','Olga',  'Natalia', 'Irina', 'Victoria', 'Tatiana'
]

men_surnames = [
    'Ivanov', 'Petrov', 'Smirnov', 'Sergeev', 'Popov', 'Volkov', 
    'Kuznetsov', 'Vasilev'
]

women_surnames = [
    'Ivanova','Petrova', 'Smirnova', 'Romanova','Popova', 'Volkova', 
    'Kuznetsova', 'Novikova'
]

popular_names = []

for _ in range(10):
    random_male_name = random.choice(men_names)
    random_male_surname = random.choice(men_surnames)
    popular_names.append(random_male_name + ' ' + random_male_surname)

for _ in range(10):
    random_female_name = random.choice(women_names)
    random_female_surname = random.choice(women_surnames)
    popular_names.append(random_female_name + ' ' + random_female_surname)

pet_name = "Vasya"

# Task 1
print("Task 1")
total_grades = 0
subject_count = 0

for subj, grade in subject.items():
    total_grades += grade
    subject_count += 1

average_grade = total_grades / subject_count
print("Average grade =", average_grade)

# Task 2
print("Task 2")
names = [None] * 20

for i in range(20):
    split_name = popular_names[i].split()
    names[i] = split_name[0]

for i in range(20):
    count = 0
    for j in range(0, 20, 1):
        if (names[i] == names[j]) and (i != j):
            count += 1
    if count == 0:
        print(names[i])

# Task 3
print("Task 3")
total_letters = 0

for subj, _ in subject.items():
    total_letters += len(subj)

print("Total number of letters in subject names =", total_letters)

# Task 4
print("Task 4")
concatenated_str = ""

for subj, _ in subject.items():
    concatenated_str += str(subj)

for i in range(len(concatenated_str)):
    count = 0
    for j in range(len(concatenated_str)):
        if (concatenated_str[i] == concatenated_str[j]) and (i != j):
            count += 1
    if count == 0:
        print(concatenated_str[i])

# Task 5
print("Task 5")
bits = bin(int.from_bytes(pet_name.encode('utf-8', 'surrogatepass'), 'big'))[2:]
print(bits.zfill(8 * ((len(bits) + 7) // 8)))

# Task 6
print("Task 6")
today = datetime.date.today()
print(today - western_actor[1])

# Task 7
print("Task 7")
fifo_queue = queue.Queue()
flag = True

print("Enter the name of the building material, enter stop to stop and display the list:")

while flag:
    queue_element = input()

    if queue_element == "stop":
        print("List of building materials:")
        for i in range(fifo_queue.qsize()):
            res = fifo_queue.get()
            print(res)
        break
    else:
        fifo_queue.put(queue_element)

# Task 8
print("Task 8")
number = (7 + 6**2 + 1917) % 39 + 1  # 18
emperor_name = "Chou Nan-Wan"

print("Enter the number to replace:")
i = int(input())

popular_names[i] = emperor_name

print(popular_names)

print("Task 9")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, index):
        step = 0
        if index == 0:
            self.head.data = "End"
        else:
            current_node = self.head
            while step < index:
                current_node = current_node.next
                step += 1
            current_node.data = "End"

    def insert(self, index):
        step = 0
        current_node = self.head
        while current_node.next:
            if step < index:
                current_node = current_node.next
                step += 1
            elif step == index:
                current_node.data = current_node.next.data
                current_node = current_node.next
                step += 1
            else:
                if step != self.len() - 1:
                    data_new = current_node.next.data
                    current_node.data = data_new
                    current_node = current_node.next
                    step += 1
                else:
                    data_new = current_node.next.data
                    current_node.data = data_new
                    current_node.next = None
                    break

    def len(self):
        step = 0
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            step += 1
        return step      

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


list = List()

list.append("0 Yes-yes")
list.append("1 Blyuvichi")
list.append("2 Svinovye")
list.append("3 Krutaya")
list.append("4 Bolshoy Kuyash")
list.append("5 Bezvodovka")
list.append("6 Mandy")
list.append("7 Zhabino")
list.append("8 Konchinino")
list.append("9 Khotlovo")

list.remove(int(input("Enter the number to replace with the word End: ")))
list.insert(int(input("Enter the number for removal: ")))
list.display()
