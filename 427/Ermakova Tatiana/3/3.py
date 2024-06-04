import math

def checkPoint(array, x, y):
	if (y >= 0 and y < len(array)) and (x >= 0 and x < len(array[0])):
		return array[y][x]
	else:
		return 0

def setPoint(array, x, y, symbol, depth = 0, container = []):
	depth += 1
	if checkPoint(array, x, y) == ' ':
		array[y][x] = symbol
		container.append(x)
		container.append(y)
		return True
	if checkPoint(array, x, y) == 0 or depth > 2:
		return False
	elif setPoint(array, x, y+1, symbol, depth, container):
		return True
	elif setPoint(array, x+1, y, symbol, depth, container):
		return True
	elif setPoint(array, x, y-1, symbol, depth, container):
		return True
	elif setPoint(array, x-1, y, symbol, depth, container):
		return True
	else: 
		return False

class Point(object):
	def __init__(self, array, x, y):
		self.x = x
		self.y = y
		self.weigh = math.inf
		self.passed = False
		self.next = []

class Graph(object):
	def __init__(self, array):
		self.array = {}

		for y in range(len(array)):
			for x in range(len(array[0])):
				if (array[y][x] != '#'):
					self.array[x, y] = (Point(array, x, y))

		for point in self.array.values():
			if self.array.__contains__((point.x, point.y+1)):
				point.next.append(self.array[(point.x, point.y+1)])
			if self.array.__contains__((point.x+1, point.y)):
				point.next.append(self.array[(point.x+1, point.y)])
			if self.array.__contains__((point.x, point.y-1)):
				point.next.append(self.array[(point.x, point.y-1)])
			if self.array.__contains__((point.x-1, point.y)):
				point.next.append(self.array[(point.x-1, point.y)])



def step_forward(front_line, finish_node):
	fire_addition = set()
	for node in front_line:
		if node == finish_node:
			return True
		else:
			for direction in node.next:
				fire_addition.add(direction)
				if direction.weigh > node.weigh+1:
					direction.weigh = node.weigh+1
	front_line.update(fire_addition)
	front_line.discard(node)
	step_forward(front_line, finish_node)

def step_backward(node, path = []):
	min_weight = node.weigh
	min_node = node
	if min_weight == 0:
		return
	for direction in node.next:
		if direction.weigh < min_weight:
			min_weight = direction.weigh
			min_node = direction
	x = min_node.x
	y = min_node.y
	path.append((x,y))
	step_backward(min_node, path)
	return path

def dextra(graph, start_cords, finish_cords):
	for node in graph.array.values():
		node.weigh = math.inf
	start_cords = tuple(start_cords)
	finish_cords = tuple(finish_cords)
	start_node = graph.array[finish_cords]
	finish_node = graph.array[start_cords]
	start_node.weigh = 0
	front_line = set()
	front_line.add(start_node)

	step_forward(front_line, finish_node)
	path = []
	path = step_backward(finish_node, path)

	return path, front_line





start = [50, 45]
key = [30, 80]
finish = [11, 2]

map_array = []
file = open('maze-for-u.txt', 'r')
for line in file:
	map_array.append(list(line.strip('\n')))

start_cords = []
setPoint(map_array, start[0], start[1], '@', 0, start_cords)

key_cords = []
setPoint(map_array, key[0], key[1], '*', 0, key_cords)

finish_cords = []
setPoint(map_array, finish[0], finish[1], '6', 0, finish_cords)

print(f"Игрок: {start_cords}, ключ: {key_cords}, выход: {finish_cords}")

map_graph = Graph(map_array)


path, front_line = dextra(map_graph, start_cords, key_cords)
for cord in path:
	map_array[cord[1]][cord[0]] = '.'


path, front_line = dextra(map_graph, key_cords, finish_cords)

for cord in path:
	map_array[cord[1]][cord[0]] = ','

file = open("maze-for-me-done.txt", 'w')
for line in map_array:
	for symbol in line:
		file.write(symbol)
	file.write('\n')
file.close()
