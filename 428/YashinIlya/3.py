import random
import heapq

maze = []
with open("maze-for-u.txt") as f:
    for line in f:
        mazeline = []
        for i in line:
            if i == "#":
                mazeline.append(1)
            elif i == " ":
                mazeline.append(0)
        maze.append(mazeline)



# Функция для поиска случайной свободной клетки
def search_random_free_cage(maze):
    free_cages = [(r, c) for r in range(len(maze)) for c in range(len(maze[0])) if maze[r][c] == 0]
    return random.choice(free_cages)

# Размещаем персонажа и ключ
avatar_position = search_random_free_cage(maze)
key_position = search_random_free_cage(maze)
while key_position == avatar_position:
    key_position = search_random_free_cage(maze)

# Обозначаем ключ
maze[key_position[0]][key_position[1]] = '*'

# Функция для поиска кратчайшего пути с помощью алгоритма Дейкстры
def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    distances = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    distances[start] = 0
    priority_queue = [(0, start)]
    came_from = { start: None }

    while priority_queue:
        current_distance, current_cell = heapq.heappop(priority_queue)
        if current_cell == end:
            break

        for d_r, d_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_cell[0] + d_r, current_cell[1] + d_c)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] in [0, '*']:
                new_distance = current_distance + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
                    came_from[neighbor] = current_cell

    # Восстанавливаем путь
    path = []
    if end in came_from:
        cell = end
        while cell is not None:
            path.append(cell)
            cell = came_from[cell]
        path.reverse()
    return path

# Находим путь от персонажа до ключа
path_to_key = dijkstra(maze, avatar_position, key_position)



# Находим путь от ключа до выхода
exit_pos = (0, 1)
if maze[exit_pos[0]][exit_pos[1]] == 0:  # Проверка, что выход свободен
    path_to_exit = dijkstra(maze, key_position, exit_pos)
    
    # Обозначаем путь запятыми
    for r, c in path_to_exit[1:-1]:
        maze[r][c] = ','
        
# Обозначаем путь точками
for r, c in path_to_key[1:-1]:
    maze[r][c] = '.'
    
# Выводим лабиринт с отмеченными путями

with open("maze-for-me-done.txt", "w" ) as f:
    for row in maze:
        string = "".join(str(cell) if cell != 1 else '#' for cell in row) + "\n"
        f.write(string.replace("0", " "))