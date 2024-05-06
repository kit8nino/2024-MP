from queue import Queue
import heapq

# Загрузка лабиринта из файла
def load_maze(file_name):
    with open(file_name, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

# Поиск пути от начальной точки до ключа с помощью поиска в ширину
def bfs(maze, start, key):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = Queue()
    queue.put(start)
    visited[start[1]][start[0]] = True

    while not queue.empty():
        x, y = queue.get()
        if (x, y) == key:
            return True  # Найден путь до ключа
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] != '#' and not visited[ny][nx]:
                queue.put((nx, ny))
                visited[ny][nx] = True
    return False  # Путь до ключа не найден

# Реализация алгоритма A* для поиска оптимального пути до выхода
def astar(maze, start, exit):
    def heuristic(node):
        return abs(node[0] - exit[0]) + abs(node[1] - exit[1])

    open_list = [(0, heuristic(start), start)]
    heapq.heapify(open_list)
    closed_set = set()

    while open_list:
        _, _, current = heapq.heappop(open_list)

        if current == exit:
            return True  # Найден оптимальный путь до выхода

        closed_set.add(current)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_node = (current[0] + dx, current[1] + dy)
            if next_node[0] < 0 or next_node[0] >= len(maze[0]) or next_node[1] < 0 or next_node[1] >= len(maze):
                continue
            if maze[next_node[1]][next_node[0]] != '#' and next_node not in closed_set:
                new_g = heuristic(next_node) + 1
                heapq.heappush(open_list, (new_g, new_g + heuristic(next_node), next_node))

    return False  # Оптимальный путь до выхода не найден

# Загрузка лабиринта и других исходных данных
maze_file = 'maze-for-u.txt'
maze = load_maze(maze_file)
start = (1, 1)  # Координаты аватара
key = (1, 3)    # Координаты ключа от выхода
exit = (4, 9)   # Координаты выхода

# Поиск пути от начальной точки до ключа
if bfs(maze, start, key):
    # Поиск оптимального пути до выхода с помощью A*
    if astar(maze, key, exit):
        # Сохранение обновленного лабиринта с маршрутом в файл
        maze_with_path = [list(row) for row in maze]
        maze_with_path[key[1]][key[0]] = '*'  # Указание точки ключа
        path_to_exit = [(key[0], key[1]), (exit[0], exit[1])]
        for x, y in path_to_exit:
            if (x, y) != key:
                maze_with_path[y][x] = ','
        with open('maze-for-me-done.txt', 'w') as file:
            for row in maze_with_path:
                file.write(''.join(row) + '\n')
        print("Маршрут сохранен в файл 'maze-for-me-done.txt'.")
    else:
        print("Оптимальный путь до выхода не найден.")
else:
    print("Путь до ключа не найден.")
