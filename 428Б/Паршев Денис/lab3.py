# получаем начальные координаты
def get_coordinates(maze):

    x_start = int(input('Avatar X coordinate: '))  
    y_start = int(input('Avatar Y coordinate: '))  

    x_key = int(input('Key X coordinate: '))  
    y_key = int(input('Key Y coordinate: '))  
    maze[x_key][y_key] = " "
    start_position = (x_start, y_start)
    key_position = (x_key, y_key)

    for y in range(len(maze[0])):
        if maze[len(maze) - 1][y] == " ":
            exit_position = (len(maze) - 1, y)

    return start_position, exit_position, key_position
# поиск в глубину
def depth_first_search(start, end, maze):
    stack = [start]
    visited = {start}
    paths = {start: []}

    while stack:
        current_pos = stack.pop()
        if current_pos == end:
            return paths[current_pos]
        
        for neighbor in check_adjacent_cells(maze, current_pos):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                paths[neighbor] = paths[current_pos] + [current_pos]

    return None
#Алгоритм А*
def calculate_heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

def a_star_search(start, end, maze):
    open_list = [start]
    closed_list = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: calculate_heuristic(start, end)}

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

        for neighbor in check_adjacent_cells(maze, current):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + calculate_heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return open_list
    # проверяем соседей
def check_adjacent_cells(maze, coord):
    maze_height = len(maze)
    maze_width = len(maze[0])
    x_coord, y_coord = coord
    adjacent_cells = []

    if (x_coord - 1) >= 0 and maze[x_coord - 1][y_coord] == " ":
        adjacent_cells.append((x_coord - 1, y_coord))

    if (x_coord + 1) < maze_height and maze[x_coord + 1][y_coord] == " ":
        adjacent_cells.append((x_coord + 1, y_coord))

    if (y_coord - 1) >= 0 and maze[x_coord][y_coord - 1] == " ":
        adjacent_cells.append((x_coord, y_coord - 1))

    if (y_coord + 1) < maze_width and maze[x_coord][y_coord + 1] == " ":
        adjacent_cells.append((x_coord, y_coord + 1))

    return adjacent_cells
