import numpy as np
from collections import deque

my_maze = []

def maze_input(file_name,maze):

    with open (file_name,'r', encoding="utf-8") as file_in_maze:
        adding_line = file_in_maze.readline()
        adding_line = adding_line[:-1]
        while adding_line!='':
            maze.append(list(adding_line))
            adding_line = file_in_maze.readline()
            adding_line = adding_line[:-1]

maze_input('maze-for-u.txt',my_maze)


x_0, y_0 = 0, 1

x, y = x_0, y_0 

x_key, y_key = 1000, 1867

x_exit, y_exit = 1079, 1918

my_maze[x_key][y_key]='*'


def is_key(x,y,maze):
    return x==x_key and y==y_key

def is_in_boundaries(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0])

def is_empty(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y]=='*' 

def is_available(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty(x_new, y_new, maze)

def neighbours_current_list(x, y, maze=my_maze):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    neighbours = []
    for d in directions:
        if is_available(x, y, d, maze):
            neighbours.append((x + d[0], y + d[1]))
    return neighbours

def cell_selector(cells_to_visit):
    min_cost_cell = min(cells_to_visit, key=cost_key)
    return min_cost_cell

def cost_key(cell):
    return cell[2]

def cost_deikstra(x, y, x_0=x_0, y_0=y_0, x_exit=x_exit, y_exit=y_exit):
    g = abs(x - x_0) + abs(y - y_0)  
    return g

def path_draw_deikstra(maze,path):
    for px, py in path:
        maze[px][py] = '.'
    return maze

def add_to_visit_list_deikstra(list_of_neighbours, path, visited, cells_to_visit):
    for nx, ny in list_of_neighbours:
        if (nx, ny) in visited:
            continue

        new_path = path + [(nx, ny)]
        new_g = cost_deikstra(nx, ny)

        cells_to_visit.append((nx, ny, new_g, new_path))
                
    return cells_to_visit


def deikstra(x_0, y_0, maze):
    cells_to_visit = deque([(x_0, y_0, cost_deikstra(x_0, y_0), [])])  
    visited = set()
    
    maze[x_0][y_0] = 's'

    while cells_to_visit:
        current_cell = cell_selector(cells_to_visit)
        x, y, g, path = current_cell

        if is_key(x, y, maze):
            path_draw_deikstra(maze,path)
            maze[x][y] = '*'
            return True
        
        cells_to_visit.remove(current_cell)

        visited.add((x, y))

        list_of_neighbours = neighbours_current_list(x, y, maze)

        cells_to_visit = add_to_visit_list_deikstra(list_of_neighbours, path, visited, cells_to_visit)

    return False
    

cells_to_visit = []

visited = set()
    
def is_exit(x, y, maze):
    return x == x_exit and y == y_exit

def is_empty_a_key(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y] == '*' or maze[x][y] == '.'

def is_available_a_key(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty_a_key(x_new, y_new, maze)


def cost_a_star(x, y, x_0=x_0, y_0=y_0, x_exit=x_exit, y_exit=y_exit):
    g = abs(x - x_0) + abs(y - y_0)  
    h = 2 * round(np.sqrt((x_exit - x) ** 2 + (y_exit - y) ** 2), 3)
    f = g + h
    return f

def path_draw_a_key(maze,path):
    for px, py in path:
        maze[px][py] = ','
    return maze

def add_to_visit_list_a_key(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit = cells_to_visit):
    for nx, ny in list_of_neighbours:
        if (nx, ny) in visited:
            continue

        new_path = path + [(nx, ny)]
        new_cost = cost_a_star(nx, ny)
        new_path_length = path_length + 1  

        if new_path_length <= max_path_length: 
            if (nx, ny, new_cost, new_path, new_path_length) not in cells_to_visit:
                cells_to_visit.append((nx, ny, new_cost, new_path, new_path_length))
                
    return cells_to_visit

def find_exit(x_0, y_0, maze, max_path_length, visited=visited, cells_to_visit=cells_to_visit):
    cells_to_visit = [(x_0, y_0, cost_a_star(x_0, y_0), [], 0)]
    visited = set()

    while cells_to_visit:
        current_cell = cell_selector(cells_to_visit)
        x, y, _, path, path_length = current_cell

        if is_exit(x, y, maze):
            maze = path_draw_a_key(maze,path)
            return True

        cells_to_visit.remove(current_cell)
        
        visited.add((x, y))

        list_of_neighbours = neighbours_current_list(x, y, maze)

        cells_to_visit = add_to_visit_list_a_key(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit = cells_to_visit)

    return False

def maze_output(file_name, maze):
    
    with open(file_name, 'w', encoding="utf-8") as file_out_maze:
        
        file_out_maze.write('\n'.join(''.join(row) for row in maze))
    
    
def exist_way_to_key(key_is_exist):
    if key_is_exist == True:
        print("Путь к ключу найден!")
    else:
        print("Путь к ключу не найден!")
        
def exist_way_to_exit(exit_is_exist):
    if exit_is_exist == True:
        print("Путь к выходу найден!")
    else:
        print("Путь к выходу не найден!")
        

key_existence = deikstra(x_0, y_0, my_maze)
exist_way_to_key(key_existence)
exit_existence = find_exit(x_key, y_key, my_maze, max_path_length=3300)
exist_way_to_exit(exit_existence)
maze_output('maze-for-me-done.txt', my_maze)