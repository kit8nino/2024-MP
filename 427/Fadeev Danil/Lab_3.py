from collections import deque
from heapq import heappop, heappush

maze_file = 'maze-for-u.txt'

def place_key(maze_file, key_position):
    with open(maze_file, 'r+') as file:
        maze = [list(line.strip()) for line in file]
        
        if maze[key_position[0]][key_position[1]] != ' ':
            return False
        
        maze[key_position[0]][key_position[1]] = '*'

        file.seek(0)
        file.writelines([''.join(row) + '\n' for row in maze])
        file.truncate()

        return True
    
def load_maze(filename):
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

def get_entrance_exit(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = None
    exit = None

    print("Введите координаты аватара:")
    while True:
        try:
            start_row = int(input("Строка: "))
            start_col = int(input("Столбец: "))
            if maze[start_row][start_col] == ' ':
                start = (start_row, start_col)
                break
            else:
                print("Эта клетка не пустая. Попробуйте снова.")
        except (ValueError, IndexError):
            print("Неправильные координаты. Попробуйте снова.")

    for i in range(cols):
        if maze[rows - 1][i] == ' ':
            exit = (rows - 1, i)

    return start, exit

def greedy_search(maze, start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]

        visited.add(current)

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        neighbors.sort(
            key=lambda neighbor: abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1]),
        )

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (
                0 <= n_row < len(maze)
                and 0 <= n_col < len(maze[0])
                and maze[n_row][n_col] != "#"
                and neighbor not in visited
            ):
                queue.append((neighbor, path + [current]))

    return None

def mark_maze(maze, path, symbol):
    marked_maze = [row.copy() for row in maze]
    for position in path:
        row, col = position
        marked_maze[row][col] = symbol
    return marked_maze

########

key_pos = input("Введите координаты ключа (строка, столбец): ")
key_pos = tuple(map(int, key_pos.split(',')))

key_placed = place_key(maze_file, key_pos)
while not key_placed:
    print("Не удалось разместить ключ. Проверьте координаты.")
    key_pos = tuple(map(int, input("Введите координаты ключа (строка, столбец): ").split(',')))
    key_placed = place_key(maze_file, key_pos)

maze = load_maze(maze_file)

start, exit = get_entrance_exit(maze)
print("Координаты аватара и выхода: ", start, exit)

greedy_path = greedy_search(maze, start, key_pos)

if greedy_path:
    print("Путь от аватара до ключа:")
    print("Длина пути:", len(greedy_path))
    for position in greedy_path:
        print(position)

# Параметры для алгоритма A*
g_weight = 1
h_weight = 1
max_steps = 2000

a_star_path = a_star_search(maze, key_pos, exit, g_weight, h_weight, max_steps)

if a_star_path:
    print("Кратчайший путь от ключа до выхода:")
    print("Длина пути:", len(a_star_path))
    for position in a_star_path:
        print(position)

marked_maze = mark_maze(maze, greedy_path, '.')

if a_star_path:
    marked_maze = mark_maze(marked_maze, a_star_path, ',')

marked_maze_file = "maze-for-me-done.txt"
with open(marked_maze_file, "w") as file:
    for row in marked_maze:
        file.write("".join(row) + "\n")

print("Файл создан: maze-for-me-done.txt")
