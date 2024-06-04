import math

file = open('maze-for-u.txt', 'r')
map = []
for line in file:
	map.append(list(line.replace('\n', '')))
file.close()


# Создание графа:
class Point():
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
				graph[x, y] = Point(x, y)

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

def deijksrta(graph, pointA, pointB):
	unchecked = set()
	unchecked.add(pointA)
	pointA.weigh = 0
	addition = set()
	limit = 1000
	i = 0
	while(i < limit):
		if pointB in unchecked:
			print("Точка найдена...")
			break
		for unchecked_vertex in unchecked:
			for next_vertex in unchecked_vertex.neighbour:
				addition.add(next_vertex)
				if next_vertex.weigh > unchecked_vertex.weigh+1:
					next_vertex.weigh = unchecked_vertex.weigh+1
		unchecked.clear()
		unchecked.update(addition)
	print("Создание пути...")
	path = []
	point = pointB
	while(point != pointA):
		path.append([point.x, point.y])
		neighbours = point.neighbour
		for neighbour in neighbours:
			if neighbour.weigh < point.weigh:
				point = neighbour
	return(path)

start = [132, 45]
key = [160, 70]
exit = [100, 3]

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

graph1 = makeGraph(map)

path1 = deijksrta(graph1, graph1[start[0], start[1]], graph1[key[0], key[1]])


graph2 = makeGraph(map)

path2 = deijksrta(graph2, graph2[key[0], key[1]], graph2[exit[0], exit[1]])

# Запись пути в файл
for coord in path1:
	map[coord[1]][coord[0]] = '.'
for coord in path2:
	map[coord[1]][coord[0]] = ','

map[x][y] = '*'
file = open("maze-for-me-done.txt", 'w')
for line in map:
	for symbol in line:
		file.write(symbol)
	file.write('\n')
file.close()