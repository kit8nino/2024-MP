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
		self.start = False
		self.out = False
		self.next = []

# Преобразует массив в граф возможных путей
class Graph(object):
	def __init__(self, array):
		self.array = {}

		for y in range(len(array)):
			for x in range(len(array[0])):
				if (array[y][x] != '#'):
					self.array[y, x] = (Point(array, x, y))

		# print(f"lenght of graph: {len(self.array)}, lenght of array: {len(array)*len(array[0])}")
		for point in self.array.values():
			if self.array.__contains__((point.x, point.y+1)):
				point.next.append(self.array[(point.x, point.y+1)])
			elif self.array.__contains__((point.x+1, point.y)):
				point.next.append(self.array[(point.x+1, point.y)])
			elif self.array.__contains__((point.x, point.y-1)):
				point.next.append(self.array[(point.x, point.y-1)])
			elif self.array.__contains__((point.x-1, point.y)):
				point.next.append(self.array[(point.x-1, point.y)])

# def dextraFindSymbol():
# 	