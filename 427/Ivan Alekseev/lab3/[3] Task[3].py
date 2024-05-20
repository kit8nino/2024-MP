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

	exit_x = randint(0, len(maze[0]) - 1)

	return [avatar_coordinates, key_coordinates, [exit_x, 0]]


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


def a_star_search(g, h, max_length):
	pass


my_maze = read_maze()
avatar, key, exit_from_maze = generate_objects_coordinates(my_maze)

path_to_key = bfs(my_maze, (avatar[0], avatar[1], []), key)
max_cost = len(path_to_key) * 2
print(path_to_key[0], key, avatar)


def write_path_to_exit(maze, path, key_cords):
	new_maze = maze
	new_maze[key_cords[0]][key_cords[1]] = '*'
	for i, point in enumerate(path):
		if i != len(path) - 1:
			new_maze[point[0]][point[1]] = '.'

	with open('maze-for-me-done.txt', 'w') as w_file:
		for line in new_maze:
			for c in line:
				w_file.write(c)
			w_file.write('\n')


write_path_to_exit(my_maze, path_to_key, key)
