import math
import time

start = [2, 40]
key = [40, 40]
exit = [4, 60]



maze = []
file = open('maze-for-u.txt', 'r')
for line in file:
	maze.append(list(line.replace('\n', '')))

# Устанавливает стартовую точку вне стены, проверяет область снизу справа и вокруг
x, y = start[0], start[1]
while maze[start[0]][start[1]] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if maze[i][j] == ' ':
				start = [i, j]
	x += 1
	y += 1

x, y = key[0], key[1]
while maze[key[0]][key[1]] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if maze[i][j] == ' ':
				key = [i, j]
	x += 1
	y += 1

x, y = exit[0], exit[1]
while maze[exit[0]][exit[1]] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if maze[i][j] == ' ':
				exit = [i, j]
	x += 1
	y += 1

print("Начало установлено на", str(start), "ключ на", str(key), "выход на", str(exit))


# Создание графа:
class graph_point():
	def __init__(self, x, y, distantion = math.inf):
		self.x = x
		self.y = y
		self.near = set()
		self.distantion = distantion

def generateGraph(map, targ_x, targ_y):
	graph = {}
	maze = map
	for y in range(1, len(maze)-1):
		for x in range(1, len(maze[0])-1):
			if maze[y][x] != "#":
				graph[x, y] = graph_point(x, y, abs(targ_x-x) + abs(targ_y-y))

	for coords, point in graph.items():
		x, y = coords
		if graph.__contains__((x+1, y)):
			point.near.add(graph[x+1, y])
		if graph.__contains__((x-1, y)):
			point.near.add(graph[x-1, y])
		if graph.__contains__((x, y+1)):
			point.near.add(graph[x, y+1])
		if graph.__contains__((x, y-1)):
			point.near.add(graph[x, y-1])
	return(graph)






# Сортирует соседние вершины по расстоянию до цели
def sort_by_distance(nears):
	size = len(nears)
	nears_list = list(nears)
	for i in range(size):
		for j in range(size-1):
			if nears_list[j].distantion > nears_list[j+1].distantion:
				nears_list[j], nears_list[j+1] = nears_list[j+1], nears_list[j]
	return(nears_list)

def node_step(node, path, none_repeat_set = None):
	if none_repeat_set == None:
		none_repeat_set = set()
	else:
		if node in none_repeat_set:
			return False
		else:
			none_repeat_set.add(node)
	if node.distantion == 0:
		print(f"{node.x, node.y}: Цель достигнута")
		path.append([node.x, node.y])
		return(True)
	else:
		nears = sort_by_distance(node.near)
		# print("Соседи:")
		# for point in nears:
			# print(f"Для {node.x, node.y} r = {node.distantion} ближ: {point.x, point.y} r = {point.distantion}")
		# print("Точка:")
		for point in nears:
			# print(f"Для {node.x, node.y} r = {node.distantion} ближ: {point.x, point.y} r = {point.distantion}")
			# time.sleep(1)
			if node_step(point, path, none_repeat_set):
				path.append([node.x, node.y])
				return True
			# print("Переход к следующей точке")
	
# Жадный алгоритм
def greedyAlgorithm(graph, start_point):
	path = []
	node_step(start_point, path)
	return path

graph1 = generateGraph(maze, key[0], key[1])

path1 = greedyAlgorithm(graph1, graph1[start[0], start[1]])

# for i in range(len(maze)):
# 	for j in range(len(maze[0])):
# 		if maze[i][j] == '#':
# 			print('#', end='')
# 		else:
# 			print(graph1[j,i].distantion, end = '')
# 	print()

graph2 = generateGraph(maze, exit[0], exit[1])

path2 = greedyAlgorithm(graph2, graph2[key[0], key[1]])

for coord in path1:
	maze[coord[1]][coord[0]] = '.'
for coord in path2:
	maze[coord[1]][coord[0]] = ','

maze[x][y] = '*'

file = open("maze-for-me-done.txt", 'w')
for line in maze:
	for symbol in line:
		file.write(symbol)
	file.write('\n')
file.close()