from collections import deque
from heapq import heappop, heappush

# Функция для размещения ключа в лабиринте
def place_key(maze_file, key_position):
    with open(maze_file, 'r+') as file:
        # Чтение лабиринта из файла
        maze = [list(line.strip()) for line in file]
        # Проверка, является ли позиция свободной
        if maze[key_position[0]][key_position[1]] != ' ':
            return False
        # Размещение ключа в лабиринте
        maze[key_position[0]][key_position[1]] = '*'
        file.seek(0)
        file.writelines([''.join(row) + '\n' for row in maze])
        file.truncate()
        return True

# Функция для загрузки лабиринта из файла
def load_maze(filename):
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Функция для определения начальной и конечной точек в лабиринте
def get_start_and_end(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = None, None
    print("Введите начальные координаты:")
    while True:
        try:
            start_row = int(input("Строка: "))
            start_col = int(input("Столбец: "))
            if maze[start_row][start_col] == ' ':
                start = (start_row, start_col)
                break
            else:
                print("Эти координаты заняты, попробуйте снова.")
        except (ValueError, IndexError):
            print("Неверные координаты, попробуйте снова.")
    # Определение конечной точки на нижней строке
    for col in range(cols):
        if maze[rows - 1][col] == ' ':
            end = (rows - 1, col)
    return start, end

# Функция для поиска пути методом жадного поиска
def find_greedy_path(maze, start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]
        visited.add(current)
        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        # Сортировка соседних позиций по расстоянию до цели
        neighbors.sort(key=lambda neighbor: abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1]))
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != '#' and neighbor not in visited:
                queue.append((neighbor, path + [current]))
    return None

# Функция для поиска пути методом A*
def a_star_search(maze, start, goal, g_weight, h_weight, max_steps):
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set()
    while queue:
        _, cost, current, path = heappop(queue)
        if current == goal:
            return path + [current]
        visited.add(current)
        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != '#' and neighbor not in visited:
                new_cost = cost + 1
                priority = new_cost * g_weight + heuristic(neighbor, goal) * h_weight
                if priority <= max_steps:
                    heappush(queue, (priority, new_cost, neighbor, path + [current]))
    return None

# Функция для пометки пути в лабиринте
def mark_path(maze, path, symbol):
    marked_maze = [row.copy() for row in maze]
    for pos in path:
        row, col = pos
        marked_maze[row][col] = symbol
    return marked_maze

data = 'maze-for-u.txt'

# Получение координат ключа от пользователя
key_position = input("Введите координаты ключа (строка, столбец): ")
key_position = tuple(map(int, key_position.split(',')))

# Попытка размещения ключа в лабиринте
while not place_key(data, key_position):
    print("Координаты заняты, попробуйте снова.")
    key_position = tuple(map(int, input("Введите координаты ключа (строка, столбец): ").split(',')))

# Загрузка лабиринта
maze = load_maze(data)

# Определение начальной и конечной точек
start, end = get_start_and_end(maze)

# Поиск пути от начальной точки до ключа методом жадного поиска
path_to_key = find_greedy_path(maze, start, key_position)

# Поиск пути от ключа до выхода методом A*
path_from_key = a_star_search(maze, key_position, end, g_weight=1, h_weight=1, max_steps=3000)

# Пометка пути от начальной точки до ключа
marked_maze = mark_path(maze, path_to_key, '.')

# Пометка пути от ключа до выхода, если он найден
if path_from_key:
    marked_maze = mark_path(marked_maze, path_from_key, ',')

# Сохранение результата в файл
output_file = "maze-for-me-done.txt"
with open(output_file, "w") as file:
    for row in marked_maze:
        file.write("".join(row) + "\n")

print(f"Результат сохранен в файле: {output_file}")
