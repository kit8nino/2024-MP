from random import randint


def read_maze():
	with open('maze-for-u.txt', 'r') as r_file:
		maze = [[element for element in line.strip()] for line in r_file]
		return maze


def generate_objects_coordinates(maze):
	def generate_position_coordinates():
		position_x = randint(1, len(maze) - 2)
		position_y = randint(1, len(maze[0]) - 2)

		while maze[position_x][position_y] == '#':
			position_x = randint(1, len(maze) - 2)
			position_y = randint(1, len(maze[0]) - 2)

		return position_x, position_y

	avatar_coordinates = generate_position_coordinates()
	key_coordinates = generate_position_coordinates()
	while avatar_coordinates == key_coordinates:
		key_coordinates = generate_position_coordinates()

	return [avatar_coordinates, key_coordinates]


def bfs(maze, avatar_cords, key_cords):
	queue = [avatar_cords]
	visited = set()
	while queue:
		x, y, path = queue.pop(0)
		if (x, y) in visited:
			continue
		visited.add((x, y))
		if maze[x][y] != '#':
			if (x, y) == key_cords:
				return path + [(x, y)]
			queue.append((x + 1, y, path + [(x, y)]))
			queue.append((x - 1, y, path + [(x, y)]))
			queue.append((x, y + 1, path + [(x, y)]))
			queue.append((x, y - 1, path + [(x, y)]))
	return None


def get_neighbors(maze, pos):
	row, col = pos
	neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
	return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])]


def heuristic(current, end):
	return abs(current[0] - end[0]) + abs(current[1] - end[1])


def reconstruct_path(came_from, start, goal):
	current = goal
	path = []

	while current != start:
		path.append(current)
		current = came_from[current]

	path.append(start)
	path.reverse()

	return path


def heuristic(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_min_f_score_node(open_set, f_score):
	min_node = open_set[0]
	min_f_score = f_score[min_node]
	for node in open_set:
		if f_score[node] < min_f_score:
			min_f_score = f_score[node]
			min_node = node
	return min_node


def neighbor_check(maze, neigh, cols, rows):
	if 0 <= neigh[0] < cols and 0 <= neigh[1] < rows and maze[neigh[1]][neigh[0]] != "#":
		return True


def a_star(maze, start, end):
	y_max = len(maze)
	x_max = len(maze[0])
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	open_set = [start]
	came_from = {}
	g_score = {start: 0}
	f_score = {start: heuristic(start, end)}
	while open_set:
		current = get_min_f_score_node(open_set, f_score)
		open_set.remove(current)
		if current == end:
			while current in came_from:
				x, y = current
				if maze[y][x] == ".":
					maze[y][x] = ";"
				else:
					maze[y][x] = ","
				current = came_from[current]
			maze[start[1]][start[0]] = ","
			return g_score[end]

		x, y = current
		for dx, dy in directions:
			neighbor = (x + dx, y + dy)
			if neighbor_check(maze, neighbor, x_max, y_max):
				tentative_g_score = g_score[current] + 1
				if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
					came_from[neighbor] = current
					g_score[neighbor] = tentative_g_score
					f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
					if neighbor not in open_set:
						open_set.append(neighbor)
	return float("inf")


my_maze = read_maze()
avatar, key = generate_objects_coordinates(my_maze)
exit_from_maze = [0, randint(0, len(my_maze))]
path_to_key = bfs(my_maze, (avatar[0], avatar[1], []), key)

my_maze[key[0]][key[1]] = '*'
my_maze[exit_from_maze[0]][exit_from_maze[1]] = 'O'

for i, point in enumerate(path_to_key):
	if i != len(path_to_key) - 1:
		my_maze[point[0]][point[1]] = '.'


def write_new_maze(maze):
	with open('maze-for-me-done.txt', 'w') as w_file:
		for line in maze:
			for c in line:
				w_file.write(c)
			w_file.write('\n')


a_star(my_maze, key, exit_from_maze)
write_new_maze(my_maze)
