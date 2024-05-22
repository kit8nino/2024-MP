import math



# Возвращает символ массива, либо 0 если достигнута граница
def checkPoint(array, x, y):
	if (y >= 0 and y < len(array)) and (x >= 0 and x < len(array[0])):
		return array[y][x]
	else:
		return 0


# Пытается установить символ в указанную координату, при неудаче ищет свободную клетку в радиусе двух клеток
def tryToSet(array, x, y, symbol, depth = 0, container = []):
	depth += 1
	if checkPoint(array, x, y) == ' ':
		array[y][x] = symbol
		container.append(x)
		container.append(y)
		return True
	if checkPoint(array, x, y) == 0 or depth > 2:
		return False
	elif tryToSet(array, x, y+1, symbol, depth, container):
		return True
	elif tryToSet(array, x+1, y, symbol, depth, container):
		return True
	elif tryToSet(array, x, y-1, symbol, depth, container):
		return True
	elif tryToSet(array, x-1, y, symbol, depth, container):
		return True
	else: 
		return False

# Подкласс путевой точки для графа
class Point(object):
	def __init__(self, array, x, y):
		self.x = x
		self.y = y
		self.weigh = math.inf
		self.passed = False
		self.next = []

# Преобразует массив в граф возможных путей
class Graph(object):
	def __init__(self, array):
		self.array = {}

		for y in range(len(array)):
			for x in range(len(array[0])):
				if (array[y][x] != '#'):
					self.array[x, y] = (Point(array, x, y))

		# print(f"lenght of graph: {len(self.array)}, lenght of array: {len(array)*len(array[0])}")
		for point in self.array.values():
			if self.array.__contains__((point.x, point.y+1)):
				point.next.append(self.array[(point.x, point.y+1)])
			if self.array.__contains__((point.x+1, point.y)):
				point.next.append(self.array[(point.x+1, point.y)])
			if self.array.__contains__((point.x, point.y-1)):
				point.next.append(self.array[(point.x, point.y-1)])
			if self.array.__contains__((point.x-1, point.y)):
				point.next.append(self.array[(point.x-1, point.y)])


# check all next nodes in fire_front and add them to fire_front, moves fire_front
def fireStep(fire_front, end_node):
	fire_addition = set()
	for node in fire_front:
		if node == end_node:
			return True
		else:
			for direction in node.next:
				fire_addition.add(direction)
				if direction.weigh > node.weigh+1:
					direction.weigh = node.weigh+1
	fire_front.update(fire_addition)
	fire_front.discard(node)
	fireStep(fire_front, end_node)

# while fireStep will have gone to end node this function make path from end to start
def fireBackStep(node, path = []):
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
	fireBackStep(min_node, path)
	return path

# Find the way from start to end and return path
def dextraPathByCoordinate(graph, start_cords, end_cords):
	for node in graph.array.values():
		node.weigh = math.inf
	# direction reversed because of fireBackStep function reverced return
	start_cords = tuple(start_cords)
	end_cords = tuple(end_cords)
	start_node = graph.array[end_cords]
	end_node = graph.array[start_cords]
	start_node.weigh = 0
	fire_front = set()
	fire_front.add(start_node)

	fireStep(fire_front, end_node)
	path = []
	path = fireBackStep(end_node, path)

	return path, fire_front