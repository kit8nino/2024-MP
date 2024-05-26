import numpy as np
import random

my_maze = []

def maze_input(file_name,maze):

    with open (file_name,'r', encoding="utf-8") as file_in_maze:
        adding_line = file_in_maze.readline()
        adding_line = adding_line[:-1]
        while adding_line!='':
            maze.append(list(adding_line))
            adding_line = file_in_maze.readline()
            adding_line = adding_line[:-1]
    return maze

my_maze = maze_input('maze_for_u.txt',my_maze)

#print(my_maze)

x_0 = random.randint(1,1079)
y_0 = random.randint(1,1919)

while my_maze[x_0][y_0]=='#':
    x_0 = random.randint(1,1079)
    y_0 = random.randint(1,1919)

#x_0, y_0 = 19, 47

print(f"x-координата аватара: {x_0}")
print(f"y-координата аватара: {y_0}")

x, y = x_0, y_0 

cells_to_visit = [(x, y, [])]

visited = set()

x_key = random.randint(1,1079)
y_key = random.randint(1,1919)

while my_maze[x_key][y_key]=='#':
    x_key = random.randint(1,1079)
    y_key = random.randint(1,1919)

#x_key, y_key = 904, 362

print(f"x-координата ключа: {x_key}")
print(f"y-координата ключа: {y_key}")

x_exit, y_exit = 1079, 1918

my_maze[x_key][y_key]='*'

#Алгоритм поиска в глубину пути от начальной точки до ключа от выхода

def is_key(x,y,maze):
    return x==x_key and y==y_key

def add_to_visit_list(list_of_neighbours, path, visited, cells_to_visit = cells_to_visit):
    for nx, ny in list_of_neighbours:
        if (nx, ny) not in visited:
            cells_to_visit.append((nx, ny, path[:]))
    return cells_to_visit

def is_in_boundaries(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0])

def is_empty(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y]=='*' 

def is_available(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty(x_new, y_new, maze)

def neighbours_list(x, y, maze=my_maze):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    neighbours = []
    for d in directions:
        if is_available(x, y, d, maze):
            neighbours.append((x + d[0], y + d[1]))
    return neighbours

def path_drawer(x_0,y_0,maze,path):
    for px, py in path:
        if px == x_0 and py == y_0:
            maze[px][py] = '+'
        else:
            maze[px][py] = '.'
    return maze

def dfs(x, y, maze,visited = visited, cells_to_visit = cells_to_visit):
    
    x_0=x
    y_0=y
    
    while cells_to_visit:
        x, y, path = cells_to_visit.pop(-1) #cells_to_visit.pop(-1) - стек - DFS, cells_to_visit.pop(0) - очередь - BFS

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))
        
        if is_key(x, y, maze):
            maze = path_drawer(x_0,y_0,maze,path)
            maze[x][y] = '*'
            print("Ключ найден!")
            return True

        list_of_neighbours = neighbours_list(x, y, maze)
        
        cells_to_visit = add_to_visit_list(list_of_neighbours, path, visited)
    
    print("Путь к ключу не найден!")
        
    return False

def maze_output(file_name, maze):
    
    with open(file_name, 'w', encoding="utf-8") as file_out_maze:
        
        file_out_maze.write('\n'.join(''.join(row) for row in maze))
    
    print("Done!")
    
#Алгоритм A* поиска оптимального пути от ключа от выхода до выхода 
    
def is_exit(x, y, maze):
    return x == x_exit and y == y_exit

def is_empty_a_star(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y] == '*' or maze[x][y] == '.'

def is_available_a_star(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty_a_star(x_new, y_new, maze)

def neighbours_list_a_star(x, y, maze=my_maze):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    list_of_neighbours = []
    for d in directions:
        if is_available_a_star(x, y, d, maze):
            list_of_neighbours.append((x + d[0], y + d[1]))
    return list_of_neighbours

def cost(x, y, x_0=x_0, y_0=y_0, x_exit=x_exit, y_exit=y_exit):
    g = abs(x - x_0) + abs(y - y_0)  # Манхеттенское расстояние
    h = 2 * round(np.sqrt((x_exit - x) ** 2 + (y_exit - y) ** 2), 3)  # Евклидово расстояние
    f = g + h
    return f

def cell_selector(cells_to_visit):
    min_cost_cell = min(cells_to_visit, key=cost_key)
    return min_cost_cell

def cost_key(cell):
    return cell[2]

def path_drawer_a_star(maze,path):
    for px, py in path:
        if maze[px][py]=='.':
            maze[px][py] = '&'
        else:
            maze[px][py] = ','
    return maze

def add_to_visit_list_a_star(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit = cells_to_visit):
    for nx, ny in list_of_neighbours:
        if (nx, ny) in visited:
            continue

        new_path = path + [(nx, ny)]
        new_cost = cost(nx, ny)
        new_path_length = path_length + 1  

        if new_path_length <= max_path_length: 
            if (nx, ny, new_cost, new_path, new_path_length) not in cells_to_visit:
                cells_to_visit.append((nx, ny, new_cost, new_path, new_path_length))
                
    return cells_to_visit

def a_star(x_0, y_0, maze, max_path_length, visited=visited, cells_to_visit=cells_to_visit):
    cells_to_visit = [(x_0, y_0, cost(x_0, y_0), [], 0)]
    visited = set()

    while cells_to_visit:
        current_cell = cell_selector(cells_to_visit)
        x, y, _, path, path_length = current_cell

        if is_exit(x, y, maze):
            maze = path_drawer_a_star(maze,path)
            print("Выход найден!")
            return True

        cells_to_visit.remove(current_cell)
        
        visited.add((x, y))

        list_of_neighbours = neighbours_list_a_star(x, y, maze)

        cells_to_visit = add_to_visit_list_a_star(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit = cells_to_visit)

    print("Путь к выходу не найден!")
    return False

dfs(x, y, my_maze)
a_star(x_key, y_key, my_maze, max_path_length=5000)
maze_output('maze_for_me_done_dfs_and_a_star.txt', my_maze)


