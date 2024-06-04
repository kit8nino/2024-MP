import numpy as np
import random
from math import inf
import heapq

# Чтение лабиринта из файла
def read_maze(filename):
    maze = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            maze.append([])
            for char in line:
                if char != '\n':
                    maze[-1].append(char)
    return np.array(maze)

# Функция для вывода лабиринта на экран
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Функция для проверки, является ли текущая позиция позицией ключа
def is_key(key, x, y):
    return x == key[0] and y == key[1]

# Функция для проверки, является ли текущая ячейка пустой
def is_empty(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y] == '*'

# Функция для генерации случайных координат в пределах небольшого участка лабиринта
def generate_nearby_coords(maze, center, radius=5):
    max_x, max_y = maze.shape
    x, y = center
    while True:
        a = random.randint(max(0, x - radius), min(max_x - 1, x + radius))
        b = random.randint(max(0, y - radius), min(max_y - 1, y + radius))
        if maze[a][b] == ' ':
            return a, b

# Функция для создания объекта в лабиринте
def create_object_nearby(maze, center, radius=5):
    return generate_nearby_coords(maze, center, radius)

# Функция для поиска выходов из лабиринта
def exits(maze):
    exits = []
    for i in range(maze.shape[1]):
        if maze[0][i] == ' ':
            exits.append([0, i])
        if maze[maze.shape[0] - 1][i] == ' ':
            exits.append([maze.shape[0] - 1, i])
    return exits

# Функция для определения направления движения
def directions():
    return [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Функция для проверки, находятся ли координаты в пределах лабиринта
def is_in_boundaries(x, y, maze):
    return 0 <= x < maze.shape[0] and 0 <= y < maze.shape[1]

# Функция для получения соседних клеток
def neighbors(maze, node):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []
    for d in directions:
        ni, nj = node[0] + d[0], node[1] + d[1]
        if is_in_boundaries(ni, nj, maze) and maze[ni][nj] != '#':
            result.append((ni, nj))
    return result

# Алгоритм Дейкстры для поиска кратчайшего пути
def dijkstra(maze, start, goal):
    queue = [(0, start)]
    distances = {start: 0}
    previous_nodes = {start: None}
    visited = set()
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == goal:
            break
        
        for neighbor in neighbors(maze, current_node):
            distance = current_distance + 1
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    if goal not in previous_nodes:
        print(f"Не найден путь от {start} до {goal}")
        return []
                
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()
    return path

# Эвристическая функция для алгоритма A*
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Алгоритм A* для поиска кратчайшего пути
def a_star(maze, start, goal):
    queue = [(0, start)]
    g_costs = {start: 0}
    f_costs = {start: heuristic(start, goal)}
    previous_nodes = {start: None}
    visited = set()
    
    while queue:
        current_f_cost, current_node = heapq.heappop(queue)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == goal:
            break
        
        for neighbor in neighbors(maze, current_node):
            tentative_g_cost = g_costs[current_node] + 1
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                f_costs[neighbor] = f_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (f_cost, neighbor))
    
    if goal not in previous_nodes:
        print(f"Не найден путь от {start} до {goal}")
        return []
                
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()
    return path

# Функция для сохранения найденного пути в файл
def save_path(maze, path_to_key, path_to_exit, key, output_file):
    for (i, j) in path_to_key:
        if maze[i][j] not in ['S', 'E', 'K']:
            maze[i][j] = '.'
    for (i, j) in path_to_exit:
        if maze[i][j] not in ['S', 'E', 'K']:
            maze[i][j] = ','
    maze[key[0]][key[1]] = '*'
    
    with open(output_file, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

# Функция для поиска ближайшего выхода
def find_the_nearest_wayout(x, y, exits):
    nearest_exit = min(exits, key=lambda ex: (ex[0] - x)**2 + (ex[1] - y)**2)
    return nearest_exit

# Главная функция программы
def main():
    maze_file = 'maze-for-u.txt'
    output_file = 'maze-for-me-done.txt'
    
    maze = read_maze(maze_file)
    print("Лабиринт загружен:")
    print_maze(maze)
    
    # Генерация стартовой точки в пределах верхней четверти лабиринта
    center = (maze.shape[0] // 4, maze.shape[1] // 4)
    avatar_x, avatar_y = create_object_nearby(maze, center, radius=5)
    
    # Генерация ключа рядом со стартовой точкой
    key_x, key_y = create_object_nearby(maze, (avatar_x, avatar_y), radius=10)
    
    print(f"Start: {avatar_x}, {avatar_y}")
    print(f"Key: {key_x}, {key_y}")
    
    path_to_key = dijkstra(maze, (avatar_x, avatar_y), (key_x, key_y))
    if not path_to_key:
        print("Путь к ключу не найден!")
        return
    
    exits_list = exits(maze)
    exit_x, exit_y = find_the_nearest_wayout(key_x, key_y, exits_list)
    
    path_to_exit = a_star(maze, (key_x, key_y), (exit_x, exit_y))
    if not path_to_exit:
        print("Путь к выходу не найден!")
        return
    
    save_path(maze, path_to_key, path_to_exit, (key_x, key_y), output_file)
    print(f"Путь сохранен в {output_file}")

if __name__ == "__main__":
    main()
