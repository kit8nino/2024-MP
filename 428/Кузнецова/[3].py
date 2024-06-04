import heapq

# Функция для чтения файла с лабиринтом и возвращения его в виде двумерного списка.
def read_maze_file(file_path):
    maze = []
    with open(file_path, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Функция для поиска начальной координаты в лабиринте.
def find_start(maze):
    for y in range(len(maze[0])):
        if maze[0][y] == ' ':
            return (0, y)

# Функция для поиска координаты выхода в лабиринте.
def find_exit(maze):
    for y in range(len(maze[0])):
        if maze[len(maze) - 1][y] == ' ':
            return (len(maze) - 1, y)

# Функция для поиска координаты ключа в лабиринте.
def find_key(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '*':
                return (i, j)

# Функция для получения соседних координат от заданной координаты в лабиринте.
def get_neighbors(maze, x, y):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Верх, низ, лево, право
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
            neighbors.append((new_x, new_y))
    return neighbors

# Функция для выполнения поиска в глубину от начальной координаты до ключа в лабиринте.
def depth_first_search(maze, start_coord, key_coord):
    stack = [start_coord]  # Стек для хранения координат
    visited = set()  # Множество посещенных координат
    paths = {start_coord: []}  # Словарь для хранения пути до каждой координаты

    while stack:
        x, y = stack.pop() # Возвращает элемент, удаляя его из списка
        if (x, y) == key_coord:  # Если достигнута координата ключа, возвращаем путь
            return paths[(x, y)] + [(x, y)]
        if (x, y) in visited:  # Если координата уже была посещена, пропускаем ее
            continue
        visited.add((x, y))
        neighbors = get_neighbors(maze, x, y)  # Получаем соседние координаты
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                paths[neighbor] = paths[(x, y)] + [(x, y)]  # Обновляем путь до соседней координаты



def heuristic(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(maze, key_coord, exit_coord):
    heap = [(0, key_coord)]  # Куча для хранения координат с приоритетом
    path_costs = {key_coord: 0}  # Словарь для хранения стоимости пути до каждой координаты
    paths = {key_coord: []}  # Словарь для хранения пути до каждой координаты

    while heap:
        cost, coord = heapq.heappop(heap)
        if coord == exit_coord:  # Если достигнута координата выхода, возвращаем путь
            return paths[coord] + [coord]
        neighbors = get_neighbors(maze, *coord)  # Получаем соседние координаты
        for neighbor in neighbors:
            new_cost = path_costs[coord] + 1  # Стоимость перемещения к соседней координате (один шаг)
            if neighbor not in path_costs or new_cost < path_costs[neighbor]:
                path_costs[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, exit_coord)  # Приоритет = стоимость пути + эвристическое значение
                heapq.heappush(heap, (priority, neighbor))
                paths[neighbor] = paths[coord] + [coord]  # Обновляем путь до соседней координаты


# обновляет лабиринт, заменяя клетки на пути символом
def update_maze_with_path(maze, path, symbol):
    for coord in path:
        x, y = coord
        maze[x][y] = symbol

# функция для записи в файл
def save_maze_to_file(maze, file_path):
    with open(file_path, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

# Основная часть программы
maze = read_maze_file('maze-for-u.txt')
start_coord = find_start(maze)
key_coord = find_key(maze)
exit_cord = find_exit(maze)

# поиск пути от начальной координаты до ключа с использованием поиска в глубину
dfs_path = depth_first_search(maze, start_coord, key_coord)

if dfs_path:
    # Обновляем лабиринт с путем от начальной координаты до ключа, путь точками.
    update_maze_with_path(maze, dfs_path, '.')

    # Поиск пути от ключа до выхода с использованием алгоритма A*
    a_star_path = a_star_search(maze, key_coord, exit_cord)

    if a_star_path:
        # Обновляем лабиринт с путем от ключа до выхода, путь запятыми
        update_maze_with_path(maze, a_star_path, ',')

        # Обновляем символ ключа (он был затёрт)
        x, y = key_coord
        maze[x][y] = '*'

        # Сохраняем лабиринт в файл
        save_maze_to_file(maze, 'maze-for-me-done.txt')
        print("Маршрут найден и сохранен в файл 'maze-for-me-done.txt'.")
    else:
        print("Невозможно найти путь от ключа до выхода.")
else:
    print("Невозможно найти путь от начальной координаты до ключа.")