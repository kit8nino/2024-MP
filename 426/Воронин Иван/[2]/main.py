import random
# import matplotlib.pyplot as plt

# print(random.sample(range(1, 18), 4))
# [2, 3, 7, 17]

array_1 = []
for i in range(10000):
	array_1.append(random.randint(0, 999999))



array_2 = []
for i in range(99999):
	array_2.append(random.uniform(-1, 1))



array_3 = [[]]
r = 9/2
x_list = []
y_list = []
for i in range(42000):
	x = random.uniform(-r, r)
	y = random.uniform(-(r**2-x**2)**0.5, (r**2-x**2)**0.5)
	array_3.append([x, y])
	# x_list.append(x)
	# y_list.append(y)
# plt.scatter(x_list, y_list)
# plt.show()



file = open("text.txt", 'r', encoding="utf-8")
array_4 = []
to_remove_symbols = ['"', "'", '.', '«', '»', '!']
for line in file:
	for word in line.split(' '):
		if (word != '' and word != '\n' and word != '-'):
			for symbol in to_remove_symbols:
				word.replace(symbol, '')
			array_4.append(word.replace('\n', ''))
# print(len(array_4))