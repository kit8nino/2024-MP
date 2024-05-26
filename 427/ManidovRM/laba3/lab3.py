def read_maze_from_file(file_name):
    maze = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(line.strip())
            maze.append(row)
    return maze

maze = read_maze_from_file('maze-for-u.txt')

avatar = (0, 0)
key = (144, 234)
exit = (1,1079)
def employment_check(obj, maze):
    x, y = obj
    rows = len(maze)
    cols = len(maze[0])
    while maze[y][x] == "#":
        if x + 1 < cols and maze[y][x + 1] != "#":
            x += 1
        elif y + 1 < rows and maze[y + 1][x] != "#":
            y += 1
        else:
            x += 1
            y += 1
    return (x, y)
def neighbor_check(x,y,Xmax,Ymax):
    if (0 <= x < Xmax and 0 <= y < Ymax and maze[y][x] != "#"):
        return True
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def get_min_f_score_node(open_set, f_score):
    min_node = open_set[0]
    min_f_score = f_score[min_node]
    for node in open_set:
        if f_score[node] < min_f_score:
            min_f_score = f_score[node]
            min_node = node
    return min_node
def deykstra(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    distances = []
    path = [[None] * cols for _ in range(rows)]

    for _ in range(rows):
        distances.append([float("inf")] * cols)
    distances[start[1]][start[0]] = 0

    queue = [(0, start)]
    while queue:
        cur_dist, (x, y) = queue.pop(0)
        if (x, y) == end:
            while (x, y) != start:
                x, y = path[y][x]
                if (x, y) != end:
                    maze[y][x] = "."
            return cur_dist

        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor_check(neighbor[0],neighbor[1],cols,rows):
                new_dist = cur_dist + 1
                if new_dist < distances[neighbor[1]][neighbor[0]]:
                    distances[neighbor[1]][neighbor[0]] = new_dist
                    path[neighbor[1]][neighbor[0]] = (x, y)
                    queue.append((new_dist, neighbor))
    return float("inf")
def a_star(maze, start, end, g_weight, h_weight):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    open_set = [start]
    came_from = {}
    h_score = heuristic(start, end)
    g_score = {start: 0}
    f_score = {start: g_weight * g_score[start] + h_weight * h_score}

    while open_set:
        current = get_min_f_score_node(open_set, f_score)
        open_set.remove(current)

        if current == end:
            while current in came_from:
                x, y = current
                if maze[y][x] == ".":
                    maze[y][x] = ";"
                else:
                    maze[y][x] = ","
                current = came_from[current]
            maze[start[1]][start[0]] = ","
            return g_score[end]

        x, y = current
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor_check(neighbor[0], neighbor[1], cols, rows):
                test_g_score = g_score[current] + 1
                if (neighbor not in g_score) or (test_g_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = test_g_score
                    f_score[neighbor] = g_weight * g_score[neighbor] + h_weight * h_score
                    if neighbor not in open_set:
                        open_set.append(neighbor)
    return float("inf")
avatar = employment_check(avatar,maze)
key = employment_check(key,maze)
print("Координаты вашего аватара:",avatar)
print("Координаты вашего ключа:",key)
maze[key[1]][key[0]] = "*"
maze[exit[1]][exit[0]] = " "
deykstra(maze, avatar, key)
a_star(maze, key, exit, 1, 1)
maze[key[1]][key[0]] = "*"
with open("maze-for-me-done.txt", "w") as f:
    for row in maze:
        f.write(''.join(row) + '\n')
