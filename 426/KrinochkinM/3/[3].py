import random
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

def find_random_empty_cell(maze):
    rows = len(maze)
    cols = len(maze[0])

    while True:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if maze[row][col] == ' ':
            return row, col

def create_avatar(maze):
    row, col = find_random_empty_cell(maze)
    maze[row][col] = '+'
    return row, col

def find_nearest_exit(maze, start_row, start_col):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((start_row, start_col, []))
    
    global deleted_commas
    
    while queue:
        row, col, path = queue.popleft()

        if maze[row][col] == ' ' and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
            for cell in path:
                path_row, path_col = cell
                if maze[path_row][path_col] not in ('+', '*'):
                    maze[path_row][path_col] = ','
                    deleted_commas.append((path_row, path_col))  # Запись позиций удаленных запятых
            return
        
        if not visited[row][col]:
            visited[row][col] = True
            if maze[row][col] not in ('+', '*', '.', '!'): 
                maze[row][col] = ' '
            
            neighbors = get_empty_neighbors(maze, row, col)
            
            for neighbor_row, neighbor_col in neighbors:
                new_path = path + [(row, col)]
                h = abs(neighbor_row - start_row) + abs(neighbor_col - start_col)
                queue.append((neighbor_row, neighbor_col, new_path))

    
def find_shortest_path(maze, start_row, start_col):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((start_row, start_col, []))
    
    while queue:
        row, col, path = queue.popleft()

        if maze[row][col] == '*':
            for cell in path:
                path_row, path_col = cell
                if maze[path_row][path_col] not in ('+', '*', '.'):
                    maze[path_row][path_col] = '.'
            return
        
        if not visited[row][col]:
            visited[row][col] = True
            if maze[row][col] not in ('+', '*', '.', '!'):
                maze[row][col] = ' '
            
            neighbors = get_empty_neighbors(maze, row, col)
            
            for neighbor_row, neighbor_col in neighbors:
                new_path = path + [(row, col)]
                h = abs(neighbor_row - start_row) + abs(neighbor_col - start_col)
                queue.append((neighbor_row, neighbor_col, new_path))

def get_empty_neighbors(maze, row, col):
    rows = len(maze)
    cols = len(maze[0])
    neighbors = []
    
    if row > 0 and maze[row - 1][col] in (' ', '*'):
        neighbors.append((row - 1, col))
    
    if row < rows - 1 and maze[row + 1][col] in (' ', '*'):
        neighbors.append((row + 1, col))
    
    if col > 0 and maze[row][col - 1] in (' ', '*'):
        neighbors.append((row, col - 1))
    
    if col < cols - 1 and maze[row][col + 1] in (' ', '*'):
        neighbors.append((row, col + 1))
    
    return neighbors

def find_key_coordinates(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == '*':
                return row, col
    return None, None

# Считываем лабиринт из файла
maze = read_maze_file('maze-for-u.txt')

# Создаем аватара
avatar_row, avatar_col = find_random_empty_cell(maze)
key_row, key_col = find_key_coordinates(maze)

if key_row is None or key_col is None:
    #  Создаем ключ
    key_row, key_col = find_random_empty_cell(maze)
    maze[key_row][key_col] = '*'

# Находим оптимальный путь до ближайшего выхода с использованием алгоритма A*
find_nearest_exit(maze, key_row, key_col)

# Удаляем все символы ','
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == ',':
            maze[i][j] = ' '

# Поиск наименьшего пути от '+' к '*' и прокладывание путь символом '.'
find_shortest_path(maze, avatar_row, avatar_col)

# Восстановление символов ',' с наложением на '.'
for row, col in deleted_commas:
    if maze[row][col] == '.':
        maze[row][col] = '!'
    else:
        maze[row][col] = ','

# Восстанавливаем исходные позиции '+' и '*'
maze[avatar_row][avatar_col] = '+'
maze[key_row][key_col] = '*'

# Сохраняем лабиринт в файл 'maze-for-me-done.txt'
save_maze(maze, 'maze-for-me-done.txt')
print("Maze saved to 'maze-for-me-done.txt'")
