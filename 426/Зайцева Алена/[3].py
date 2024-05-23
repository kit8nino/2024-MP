import random
import heapq

d_c = []

def load_m(file_name):
    with open(file_name, 'r') as file:
        m = [list(line.strip()) for line in file]
    return m

def write_m(m, file_name):
    with open(file_name, 'w') as file:
        for row in m:
            file.write(''.join(row) + '\n')

def get_random_empty_cell(m):
    rows = len(m)
    cols = len(m[0])
    
    while True:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        if m[row][col] == ' ':
            return row, col

def place_avatar(m):
    row, col = get_random_empty_cell(m)
    return row, col

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_empty_neighbors(m, row, col):
    rows = len(m)
    cols = len(m[0])
    neighbors = []
    
    if row > 0 and m[row - 1][col] in (' ', '*'):
        neighbors.append((row - 1, col))
    
    if row < rows - 1 and m[row + 1][col] in (' ', '*'):
        neighbors.append((row + 1, col))
    
    if col > 0 and m[row][col - 1] in (' ', '*'):
        neighbors.append((row, col - 1))
    
    if col < cols - 1 and m[row][col + 1] in (' ', '*'):
        neighbors.append((row, col + 1))
    
    return neighbors

def locate_key(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == '*':
                return row, col
    return None, None

def a_star_search(m, start_row, start_col, max_open_list_length):
    rows = len(m)
    cols = len(m[0])
    goal_cells = [(r, c) for r in range(rows) for c in range(cols) if m[r][c] == ' ' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)]
    visited = [[False] * cols for _ in range(rows)]
    priority_queue = [(0, 0, start_row, start_col, [])]
    
    while priority_queue:
        if len(priority_queue) > max_open_list_length:
            priority_queue.sort(key=lambda x: x[0])
            priority_queue = priority_queue[:max_open_list_length]
        
        _, g, row, col, path = heapq.heappop(priority_queue)
        
        if (row, col) in goal_cells:
            for cell in path:
                path_row, path_col = cell
                if m[path_row][path_col] not in ('*'):
                    m[path_row][path_col] = ','
                    d_c.append((path_row, path_col))
            return
        
        if not visited[row][col]:
            visited[row][col] = True
            if m[row][col] not in ('*', '.'):
                m[row][col] = ' '
            
            neighbors = find_empty_neighbors(m, row, col)
            
            for neighbor_row, neighbor_col in neighbors:
                if not visited[neighbor_row][neighbor_col]:
                    new_path = path + [(row, col)]
                    g_new = g + 1
                    h = min(calculate_manhattan_distance(neighbor_row, neighbor_col, goal_row, goal_col) for goal_row, goal_col in goal_cells)
                    f = g_new + h
                    heapq.heappush(priority_queue, (f, g_new, neighbor_row, neighbor_col, new_path))

def greedy_search(m, start_row, start_col, goal_row, goal_col):
    rows = len(m)
    cols = len(m[0])
    visited = [[False] * cols for _ in range(rows)]
    priority_queue = [(0, start_row, start_col, [])]
    
    while priority_queue:
        _, row, col, path = heapq.heappop(priority_queue)
        
        if (row, col) == (goal_row, goal_col):
            for cell in path:
                path_row, path_col = cell
                if m[path_row][path_col] not in ('*', '.'):
                    m[path_row][path_col] = '.'
            return
        
        if not visited[row][col]:
            visited[row][col] = True
            if m[row][col] not in ('*', '.'):
                m[row][col] = ' '
            
            neighbors = find_empty_neighbors(m, row, col)
            
            for neighbor_row, neighbor_col in neighbors:
                if not visited[neighbor_row][neighbor_col]:
                    new_path = path + [(row, col)]
                    priority = calculate_manhattan_distance(neighbor_row, neighbor_col, goal_row, goal_col)
                    heapq.heappush(priority_queue, (priority, neighbor_row, neighbor_col, new_path))

m = load_m('maze-for-u.txt')

# Размещение аватара
avatar_row, avatar_col = get_random_empty_cell(m)
key_row, key_col = locate_key(m)

if key_row is None or key_col is None:
    # 
    key_row, key_col = get_random_empty_cell(m)
    m[key_row][key_col] = '*'

# Поиск кратчайщего выхода
max_open_list_length = 1000  
a_star_search(m, key_row, key_col, max_open_list_length)

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == ',':
            m[i][j] = ' '

# Нахождение кратчайшего пути от аватара к ключу 
greedy_search(m, avatar_row, avatar_col, key_row, key_col)

for row, col in d_c:
    m[row][col] = ','

m[key_row][key_col] = '*'

# Сохранение файла
write_m(m, 'maze-for-me-done.txt')
print("Лабиринт сохранен")
