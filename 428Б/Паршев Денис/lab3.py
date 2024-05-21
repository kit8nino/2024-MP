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
