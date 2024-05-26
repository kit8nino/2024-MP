import random

# Загрузка лабиринта из файла
def load_maze(file_name):
    maze = []
    with open(file_name, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Сохранение лабиринта в файл
def save_maze(file_name, maze):
    with open(file_name, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

# Задание координат стартовой позиции
def find_start_position(maze):
    while True:
        i = random.randint(0, len(maze) - 1)
        j = random.randint(0, len(maze[i]) - 1)
        if maze[i][j] != '#':
            return i, j

# Задание координат выхода
def find_exit_position(maze):
    possible_exits = []
    for i in range(len(maze)):
        if maze[i][0] != '#':
            possible_exits.append((i, 0))
        if maze[i][-1] != '#':
            possible_exits.append((i, len(maze[i]) - 1))
    for j in range(len(maze[0])):
        if maze[0][j] != '#':
            possible_exits.append((0, j))
        if maze[-1][j] != '#':
            possible_exits.append((len(maze) - 1, j))
    return random.choice(possible_exits)


def get_neighbours(position, maze):
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Верх, низ, лево, право
    for direction in directions:
        x = position[0] + direction[0]
        y = position[1] + direction[1]
        if 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != '#':
            neighbours.append((x, y))
    return neighbours

# Поиск маршрута от начальной позиции до ключа
def depth_first_search(maze, start, key):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        visited.add(current)

        if current == key:
            return path

        neighbours = get_neighbours(current, maze)
        unvisited_neighbours = [n for n in neighbours if n not in visited]

        if unvisited_neighbours:
            for neighbour in unvisited_neighbours:
                stack.append((neighbour, path + [neighbour]))
                visited.add(neighbour)

    return None

# Вычисление перемещения от точки position1 до точки position2
def calculate_distance(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

# Находим оптимальный путь до выхода с помощью A*
def a_star_search(maze, start, goal, max_steps):
    open_list = [(start, 0, calculate_distance(start, goal))]
    closed_list = set()
    parent = {}
    g_scores = {start: 0}

    while open_list:
        current, g_score, f_score = min(open_list, key=lambda x: x[2])
        open_list.remove((current, g_score, f_score))
        closed_list.add(current)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        if len(closed_list) > max_steps:
            return None

        neighbours = get_neighbours(current, maze)
        for neighbour in neighbours:
            if neighbour in closed_list:
                continue

            tentative_g_score = g_score + 1
            if neighbour not in g_scores or tentative_g_score < g_scores[neighbour]:
                g_scores[neighbour] = tentative_g_score
                f_score = tentative_g_score + calculate_distance(neighbour, goal)
                open_list.append((neighbour, tentative_g_score, f_score))
                parent[neighbour] = current

    return None


# Загрузка лабиринта
maze = load_maze('maze-for-u.txt')

# Нахождение начальной позиции
start_position = find_start_position(maze)

# Нахождение позиции выхода
exit_position = find_exit_position(maze)

# Генерация позиции ключа
key_position = find_start_position(maze)  # Используем функцию find_start_position для выбора случайной позиции
while key_position == start_position:  # Проверяем, чтобы ключ и аватар не находились в одном месте
    key_position = find_start_position(maze)
maze[key_position[0]][key_position[1]] = '*'  # Устанавливаем ключ на выбранную позицию

# Поиск маршрута от начальной позиции до ключа
dfs_path = depth_first_search(maze, start_position, key_position)

if dfs_path is not None:
    # Отмечаем путь до ключа символом '.'
    for position in dfs_path:
        maze[position[0]][position[1]] = '.'

    # Находим оптимальный путь до выхода с помощью A*
    a_star_path = a_star_search(maze, key_position, exit_position, len(maze) * len(maze[0]))

    if a_star_path is not None:
        # Отмечаем путь от ключа до выхода символом ','
        for position in a_star_path:
            maze[position[0]][position[1]] = ','

        # Обновляем символы 'A' и 'E'
        maze[start_position[0]][start_position[1]] = 'A'
        maze[exit_position[0]][exit_position[1]] = 'E'
        maze[key_position[0]][key_position[1]] = '*'

        # Сохраняем результат в файл
        save_maze('maze-for-me-done.txt', maze)
        print("Маршрут успешно найден и сохранен в файле 'maze-for-me-done.txt'.")
    else:
        print("Невозможно найти маршрут до выхода.")
else:
    print("Невозможно найти маршрут до ключа.")