import numpy as np
import random

wall, path, key, loot_key, avatar, way, a_way = "#", " ", "*", "+", "$", ".", ","

custom_maze = []

def read_maze_data(file_name, maze_data):

    with open(file_name, 'r', encoding="utf-8") as file_maze:
        line = file_maze.readline()
        line = line[:-1]
        while line != '':
            maze_data.append(list(line))
            line = file_maze.readline()
            line = line[:-1]
    return maze_data

custom_maze = read_maze_data('maze-for-u.txt', custom_maze)

start_x = random.randint(1, 1079)
start_y = random.randint(1, 1919)

while custom_maze[start_x][start_y] == wall:
    start_x = random.randint(1, 1079)
    start_y = random.randint(1, 1919)

print("Start coords (x ,  y):", start_x, ",", start_y)

x, y = start_x, start_y

cells_to_explore = [(x, y, [])]

visited_cells = set()

key_x = random.randint(540, 1079)
key_y = random.randint(810, 1919)

while custom_maze[key_x][key_y] == wall:
    key_x = random.randint(540, 1079)
    key_y = random.randint(810, 1919)

print("Key coords (x ,  y):", key_x, ",", key_y)
exit_x, exit_y = 1079, 1917

custom_maze[key_x][key_y] = key

def is_key_location(x, y, maze):
    return x == key_x and y == key_y

def add_to_explore_list(neighbours_list, path, visited, cells_to_explore=cells_to_explore):
    for nx, ny in neighbours_list:
        if (nx, ny) not in visited:
            cells_to_explore.append((nx, ny, path[:]))
    return cells_to_explore

def is_within_bounds(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0])

def is_cell_empty(x, y, maze):
    return maze[x][y] == path or maze[x][y] == key

def is_cell_accessible(x, y, direction, maze):
    new_x = x + direction[0]
    new_y = y + direction[1]
    return is_within_bounds(new_x, new_y, maze) and is_cell_empty(new_x, new_y, maze)

def get_neighbours(x, y, maze=custom_maze):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    neighbours_list = []
    for d in directions:
        if is_cell_accessible(x, y, d, maze):
            neighbours_list.append((x + d[0], y + d[1]))
    return neighbours_list

def explore_path(x_start, y_start, maze, path):
    for px, py in path:
        if px == x_start and py == y_start:
            maze[px][py] = loot_key
        else:
            maze[px][py] = way
    return maze

def depth_first_search(x_pos, y_pos, maze, visited=visited_cells, cells_to_explore=cells_to_explore):
    
    x_start = x_pos
    y_start = y_pos
    
    while cells_to_explore:
        x_pos, y_pos, path = cells_to_explore.pop(-1)

        if (x_pos, y_pos) in visited:
            continue

        visited.add((x_pos, y_pos))
        path.append((x_pos, y_pos))
        
        if is_key_location(x_pos, y_pos, maze):
            maze = explore_path(x_start, y_start, maze, path)
            maze[x_pos][y_pos] = key
            print("Key found!")
            return True

        neighbour_cells = get_neighbours(x_pos, y_pos, maze)
        
        cells_to_explore = add_to_explore_list(neighbour_cells, path, visited)
    
    print("Path to key not found!")
        
    return False

def write_maze_data(file_name, maze):
    
    with open(file_name, 'w', encoding="utf-8") as file_out:
        
        file_out.write('\n'.join(''.join(row) for row in maze))
    
    print("Done!")
    
def is_exit_custom(x, y, maze):
    return x == exit_x and y == exit_y

def is_empty_cell_a_star(x, y, maze):
    return maze[x][y] == path or maze[x][y] == key or maze[x][y] == way

def is_available_cell_a_star(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_within_bounds(x_new, y_new, maze) and is_empty_cell_a_star(x_new, y_new, maze)

def neighbours_list_a_star_custom(x, y, maze = custom_maze):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    list_of_neighbours = []
    for d in directions:
        if is_available_cell_a_star(x, y, d, maze):
            list_of_neighbours.append((x + d[0], y + d[1]))
    return list_of_neighbours

def cost_custom(x, y, x_0 = start_x, y_0 = start_y, x_exit = exit_x, y_exit=exit_y):
    g = abs(x - x_0) + abs(y - y_0)
    h = 2 * round(np.sqrt((x_exit - x) ** 2 + (y_exit - y) ** 2), 3)
    f = g + h
    return f

def cell_selector_custom(cells_to_visit):
    min_cost_cell = min(cells_to_visit, key=cost_key_custom)
    return min_cost_cell

def cost_key_custom(cell):
    return cell[2]

def path_drawer_a_star_custom(maze,path):
    for px, py in path:
        if maze[px][py]==way:
            maze[px][py] = avatar
        else:
            maze[px][py] = a_way
    return maze

def add_to_visit_list_a_star_custom(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit = cells_to_explore):
    for nx, ny in list_of_neighbours:
        if (nx, ny) in visited:
            continue

        new_path = path + [(nx, ny)]
        new_cost = cost_custom(nx, ny)
        new_path_length = path_length + 1  

        if new_path_length <= max_path_length: 
            if (nx, ny, new_cost, new_path, new_path_length) not in cells_to_visit:
                cells_to_visit.append((nx, ny, new_cost, new_path, new_path_length))
                
    return cells_to_visit

def a_star_custom(x_0_custom, y_0_custom, maze, max_path_length, visited = visited_cells, cells_to_visit = visited_cells):
    cells_to_visit = [(x_0_custom, y_0_custom, cost_custom(x_0_custom, y_0_custom), [], 0)]
    visited = set()

    while cells_to_visit:
        current_cell = cell_selector_custom(cells_to_visit)
        x, y, _, path, path_length = current_cell

        if is_exit_custom(x, y, maze):
            maze = path_drawer_a_star_custom(maze,path)
            print("Path found!")
            return True

        cells_to_visit.remove(current_cell)
        
        visited.add((x, y))

        list_of_neighbours = neighbours_list_a_star_custom(x, y, maze)

        cells_to_visit = add_to_visit_list_a_star_custom(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit = cells_to_visit)

    print("Path not found")
    return False


depth_first_search(x, y, custom_maze)
a_star_custom(key_x, key_y, custom_maze, max_path_length=5000)
write_maze_data('maze-for-me-done.txt', custom_maze)