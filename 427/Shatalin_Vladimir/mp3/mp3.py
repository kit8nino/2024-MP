import numpy as np
from collections import deque

deleted_commas = []

def read_maze_file(file_name):
    with open(file_name, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def save_maze(maze, file_name):
    with open(file_name, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def create_avatar(maze):
    rows = len(maze)
    cols = len(maze[0])

    while True:
        y = np.random.randint(0, rows - 1)
        x = np.random.randint(0, cols - 1)
        if maze[x][y] == ' ':
            break
    maze[x][y] = '+'    
    return [x,y]

def find_nearest_exit(maze, x0, y0):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((x0, y0, []))

    global deleted_commas

    while queue:
        x, y, path = queue.popleft()

        if maze[x][y] == ' ' and (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
            for cell in path:
                path_x, path_y = cell
                if maze[path_x][path_y] not in ('+', '*'):
                    maze[path_x][path_y] = '-'
                    deleted_commas.append((path_x, path_x))
            return

        if not visited[x][y]:
            visited[x][y] = True
            if maze[x][y] not in ('+', '*', '?', '!'): 
                maze[x][y] = ' '

            neighbors = get_empty_neighbors(maze, x, y)

            for neighbor_x, neighbor_y in neighbors:
                new_path = path + [(x, y)]
                h = abs(neighbor_x - x0) + abs(neighbor_y - y0)
                queue.append((neighbor_x, neighbor_y, new_path))


def find_shortest_path(maze, x0, y0):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((x0, y0, []))

    while queue:
        x, y, path = queue.popleft()

        if maze[x][y] == '*':
            for cell in path:
                path_x, path_y = cell
                if maze[path_x][path_y] not in ('+', '*', '?'):
                    maze[path_x][path_y] = '?'
            return

        if not visited[x][y]:
            visited[x][y] = True
            if maze[x][y] not in ('+', '*', '?', '!'):
                maze[x][y] = ' '

            neighbors = get_empty_neighbors(maze, x, y)

            for neighbor_x, neighbor_y in neighbors:
                new_path = path + [(x, y)]
                h = abs(neighbor_x - x0) + abs(neighbor_y - y0)
                queue.append((neighbor_x, neighbor_y, new_path))

def get_empty_neighbors(maze, x, y):
    rows = len(maze)
    cols = len(maze[0])
    neighbors = []

    if x > 0 and maze[x - 1][y] in (' ', '*'):
        neighbors.append((x - 1, y))

    if x < rows - 1 and maze[x + 1][y] in (' ', '*'):
        neighbors.append((x + 1, y))

    if y > 0 and maze[x][y - 1] in (' ', '*'):
        neighbors.append((x, y - 1))

    if y < cols - 1 and maze[x][y + 1] in (' ', '*'):
        neighbors.append((x, y + 1))

    return neighbors

def find_key_coordinates(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == '*':
                return x, y
    return None, None


maze = read_maze_file('maze-for-u.txt')

avatar_x, avatar_y = find_random_empty_cell(maze)
key_x, key_y = find_key_coordinates(maze)

if key_x is None or key_y is None:
    key_x, key_y = find_random_empty_cell(maze)
    maze[key_x][key_y] = '*'

find_nearest_exit(maze, key_x, key_y)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '-':
            maze[i][j] = ' '

find_shortest_path(maze, avatar_x, avatar_y)

for x, y in deleted_commas:
    if maze[x][y] == '?':
        maze[x][y] = '!'
    else:
        maze[x][y] = '-'

maze[avatar_x][avatar_y] = '+'
maze[key_x][key_y] = '*'

save_maze(maze, 'result.txt')
print("Maze saved to 'result.txt'")
