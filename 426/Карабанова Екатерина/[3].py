#3
import random
from collections import deque
from heapq import heappop, heappush

maze_file = 'maze-for-u.txt'

#ставим ключ
def place(maze_file, key_pos):
    with open(maze_file, 'r+') as file:
        maze = [list(line.strip()) for line in file]
        
        if maze[key_pos[0]][key_pos[1]] != ' ':
            return False
        
        maze[key_pos[0]][key_pos[1]] = '*'

    
        file.seek(0)
        file.writelines([''.join(row) + '\n' for row in maze])
        file.truncate()

        return True
    
def read(filename): 
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip()
            maze.append(list(row))
    return maze
# Координаты Аватара и выхода
def entrance_exit(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = None
    end = None

    print("Введите координаты аватара:")
    while True:
        try:
            start_row = int(input("Строка: "))
            start_col = int(input("Столбец: "))
            if maze[start_row][start_col] == ' ':
                start = (start_row, start_col)
                break
            else:
                print("Клетка не пустая. Введите координаты.")
        except (ValueError, IndexError):
            print("Нет таких кооржинат. Введите координаты ещё раз.")

    for i in range(cols):
        if maze[rows - 1][i] == ' ':
            end = (rows - 1, i)

    return start, end
#Поиска маршрута от начальной координаты аватара до ключа
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

        
        neighbors = sorted(
            neighbors,
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
# А*
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
            if (
                0 <= n_row < len(maze)
                and 0 <= n_col < len(maze[0])
                and maze[n_row][n_col] != "#"
                and neighbor not in visited
            ):
                new_cost = cost + 1
                priority = new_cost * g_weight + heuristic(neighbor, goal) * h_weight
                if priority <= max_steps:
                    heappush(queue, (priority, new_cost, neighbor, path + [current]))

    return None
# Путь в лабиринте
def mark(maze, path, symbol): 
    marked_maze = [row.copy() for row in maze]
    for position in path:
        row, col = position
        marked_maze[row][col] = symbol
    return marked_maze

#Вводим координаты
 
key_pos = input("Введите координаты ключа- строка,столбец: ")
key_pos = key_pos.split(',')
key_pos = (int(key_pos[0]), int(key_pos[1]))

placed = place(maze_file, key_pos)
while not placed: #Ищем свободную клетку
    print("Невозможно разместить ключ. Попробуйте другие координаты.")
    key_pos = input("Введите координаты ключа- строка,столбец: ")
    key_pos = key_pos.split(',')
    key_pos = (int(key_pos[0]), int(key_pos[1]))
    placed = place(maze_file, key_pos)

maze = read(maze_file)

start, end = entrance_exit(maze)
print("Координаты аватара и выхода: ", start, end)

greedy_path = greedy_search(maze, start, key_pos)

if greedy_path:
    print("Путь от начальных координат аватара до ключа:")
    print("Длина пути:", len(greedy_path))
    for position in greedy_path:
        print(position)
       

    
#Параметры для алгоритма A*   
g_weight = 1 
h_weight = 1  
max_steps = 1000  

a_star_path = a_star_search(maze, key_pos, end, g_weight, h_weight, max_steps)

if a_star_path:
    print("Кратчайший путь от ключа до выхода:")
    print("Длина пути:", len(a_star_path))
    for position in a_star_path:
        print(position)

marked_maze = mark(maze, greedy_path, ".")

if a_star_path:
    marked_maze = mark(marked_maze, a_star_path, ",")
# Сохраняем файл с помеченным путем.
marked_combined_maze_file = "maze-for-me-done.txt" #Создаем файл с помеченным путём.
with open(marked_combined_maze_file, "w") as file:
    for row in marked_maze:
        file.write("".join(row) + "\n")

print(" maze-for-me-done.txt")
