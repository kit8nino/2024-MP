import math

file = open('maze-for-u.txt', 'r')
map = []
for line in file:
	map.append(list(line.replace('\n', '')))
file.close()


# Создание графа:
class point():
	def __init__(self, x, y, weigh = math.inf):
		self.x = x
		self.y = y
		self.weigh = weigh
		self.neighbour = set()

def makeGraph(map):
	graph = {}
	# Создание точек графа
	for y in range(1, len(map)-1):
		for x in range(1, len(map[0])-1):
			if map[y][x] != "#":
				graph[x, y] = point(x, y)

	# Задание соседей вершинам графа
	for coords, point in graph.items():
		x, y = coords
		if graph.__contains__((x+1, y)):
			point.neighbour.add(graph[x+1, y])
		if graph.__contains__((x-1, y)):
			point.neighbour.add(graph[x-1, y])
		if graph.__contains__((x, y+1)):
			point.neighbour.add(graph[x, y+1])
		if graph.__contains__((x, y-1)):
			point.neighbour.add(graph[x, y-1])
	return(graph)



start = [132, 45]
# start[0] = int(input("Введите начальную координату (x): "))
# start[1] = int(input("Введите начальную координату (y): "))
key = [160, 70]
# key[0] = int(input("Введите координату ключа (x): "))
# key[1] = int(input("Введите координату ключа (y): "))
exit = [100, 3]
# exit[0] = int(input("Введите координату выхода (x): "))
# exit[1] = int(input("Введите координату выхода (y): "))

x, y = start[0], start[1]
while map[start[0]][start[1]] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if map[i][j] == ' ':
				start = [i, j]
	x += 1
	y += 1

x, y = key[0], key[1]
while map[key[0]][key[1]] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if map[i][j] == ' ':
				key = [i, j]
	x += 1
	y += 1

x, y = exit[0], exit[1]
while map[exit[0]][exit[1]] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if map[i][j] == ' ':
				exit = [i, j]
	x += 1
	y += 1

print("Начало установлено на", str(start), "ключ на", str(key), "выход на", str(exit))

