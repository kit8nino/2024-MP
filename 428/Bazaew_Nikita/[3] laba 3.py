# координаты старта, выхода и ключа
def get_data(maze):

    x_start = int(input('Координаты аватара X: ')) # x=1
    y_start = int(input('Координаты аватара Y: ')) # y=7

    x_key = int(input('Координаты ключа X : ')) # x = 543
    y_key = int(input('Координаты ключа Y : ')) # y = 144
    maze[x_key][y_key] = " "

    start = (x_start, y_start)
    key = (x_key, y_key)

    for Y in range(len(maze[0])):
        if maze[len(maze) - 1][Y] == " ":
            end = (len(maze) - 1, Y)

    return start, end, key


# Проверка соседних клеток
def available_paths(maze, coord):
    len_maze_y = len(maze[0])
    len_maze_x = len(maze)
    x_coord, y_coord = coord
    possible_ways = []

    if (x_coord - 1) >= 0 and maze[x_coord - 1][y_coord] == " ":
        possible_ways.append((x_coord - 1, y_coord))

    if (x_coord + 1) < len_maze_x and maze[x_coord + 1][y_coord] == " ":
        possible_ways.append((x_coord + 1, y_coord))

    if (y_coord - 1) >= 0 and maze[x_coord][y_coord - 1] == " ":
        possible_ways.append((x_coord, y_coord - 1))

    if (y_coord + 1) < len_maze_y and maze[x_coord][y_coord + 1] == " ":
        possible_ways.append((x_coord, y_coord + 1))

    return possible_ways


# Поиск в глубину
def dfs(start, end, maze):
    stack = [start]
    visited = {start}
    paths = {start: []}

    while stack:
        current_pos = stack.pop()
        if current_pos == end:
            return paths[current_pos]
        # Проверяем все возможные направления
        for neighbor in available_paths(maze, current_pos):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                paths[neighbor] = paths[current_pos] + [current_pos]

    return None


# Алгоритм А*
def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


def a_star(start, end, maze):
    open_list = [start]
    closed_list = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_list:
        current = min(open_list, key=lambda x: f_score[x])
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in available_paths(maze, current):
            if neighbor in closed_list:
                continue
            preliminary_g_score = g_score[current] + 1
            if neighbor not in open_list or preliminary_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = preliminary_g_score
                f_score[neighbor] = preliminary_g_score + heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return open_list


# Построение пути
def create_path(path_to_key, path_to_exit, key):
    for coords in path_to_key:
        x, y = coords
        maze[x][y] = "."

    for coords in path_to_exit:
        x, y = coords
        if maze[x][y] == ".":
            maze[x][y] = ";"
        else:
            maze[x][y] = ","

    maze[key[0]][key[1]] = '*'


# Получение данных

# преобразуем лабиринт в матрицу
with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

start, end, key = get_data(maze)
path_to_key = dfs(start, key, maze)
path_to_exit = a_star(key, end, maze)

create_path(path_to_key, path_to_exit, key)


with open('maze-for-me-done.txt', 'w') as f:
    for line in maze:
        f.write("".join(line) + "\n")