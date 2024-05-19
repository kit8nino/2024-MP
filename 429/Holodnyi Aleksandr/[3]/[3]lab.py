import numpy as np
from collections import deque

#определяем входные данные
def maze_read(filename):
    f = open(filename, 'r')
    temp = f.readlines()
    result = [list(elem) for elem in temp]
    for i in range(len(result)):
        result[i].remove("\n")
    f.close()
    return result

def set_avatar_coord(x,y,maze):
    if maze[x][y] != '#':
        print('Avatar coords:', x, y)
        maze[x][y] = 'o'
        avatar_coords = [x, y]
    elif maze[x + 1][y] != '#':
        print('Avatar coords:', x + 1, y, '( wall at', x, y, ')')
        maze[x+1][y] = 'o'
        avatar_coords = [x + 1, y]
    elif maze[x][y + 1] != '#':
        print('Avatar coords:', x, y + 1, '( wall at', x, y, ')')
        maze[x][y+1] = 'o'
        avatar_coords = [x, y+1]
    elif maze[x - 1][y] != '#':
        print('Avatar coords:', x - 1, y, '( wall at', x, y, ')')
        maze[x-1][y] = 'o'
        avatar_coords = [x - 1, y]
    elif maze[x][y - 1] != '#':
        print('Avatar coords:', x, y - 1, '( wall at', x, y, ')')
        maze[x][y-1] = 'o'
        avatar_coords = [x, y-1]
    return avatar_coords

def set_key_coord(x,y,maze):
    if maze[x][y] != '#':
        maze[x][y] = '*'
        print('Key coords:', x, y)
        key_coords = [x, y]
    elif maze[x+1][y] != '#':
        maze[x+1][y] = '*'
        print('Key coords:', x+1, y, '( wall at', x, y, ')')
        key_coords = [x+1, y]
    elif maze[x][y+1] != '#':
        maze[x][y+1] = '*'
        print('Key coords:', x, y+1, '( wall at', x, y, ')')
        key_coords = [x, y+1]
    elif maze[x-1][y] != '#':
        maze[x-1][y] = '*'
        print('Key coords:', x-1, y, '( wall at', x, y, ')')
        key_coords = [x+1, y]
    elif maze[x][y-1] != '#':
        maze[x][y-1] = '*'
        print('Key coords:', x, y-1, '( wall at', x, y, ')')
        key_coords = [x, y+1]
    return key_coords

def set_exit_coords(maze):
    for i in range(len(maze[0])):
        if maze[0][i] == " ":
            print('First exit coords:', 0,i)
            exit1 = [0,i]
    for i in range(len(maze[-1])):
        if maze[-1][i] == " ":
            print('Second exit coords:', len(maze)-1,i)
            exit2 = [len(maze)-1, i]

    return [exit1,exit2]

#входные данные
maze_filename = "maze-for-u.txt"
maze_list = maze_read(maze_filename)

avatar_coords = set_avatar_coord(799,566,maze_list)  #output: Avatar coords: 800 566 ( wall at 799 566 )
key_coords = set_key_coord(476,55,maze_list)         #output: Key coords: 476 56 ( wall at 476 55 )
exit1, exit2 = set_exit_coords(maze_list)            #output: First exit coords: 0 1
                                                     #        Second exit coords: 1079 1918(no way to this exit)

cells_to_visit = [(avatar_coords[0], avatar_coords[1], [])]
visited = set()

#жадный алгоритм
def is_key(x, y):
    return x == key_coords[0] and y == key_coords[1]

def is_in_boundaries(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0])

def is_empty(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y] == '*'

def is_available(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty(x_new, y_new, maze)

def neighbours_list(x, y, maze):
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

def cost_greedy(x, y, x_exit = key_coords[0] , y_exit = key_coords[1]):
    h = round(np.sqrt((x_exit - x) ** 2 + (y_exit - y) ** 2), 3) #евклидово расстояние
    return h

def path_drawer_greedy(maze, path):
    for px, py in path:
        maze[px][py] = '.'
    return maze

def add_to_visit_list_greedy(list_of_neighbours, path, visited, cells_to_visit):
    for nx, ny in list_of_neighbours:
        if (nx, ny) in visited:
            continue

        new_path = path + [(nx, ny)]
        new_h = cost_greedy(nx, ny)
        cells_to_visit.append((nx, ny, new_h, new_path))

    return cells_to_visit

def greedy(x_0, y_0, maze):
    cells_to_visit = deque([(x_0, y_0, cost_greedy(x_0, y_0), [])])  # (x, y, h, path)
    visited = set()

    while cells_to_visit:
        current_cell = cell_selector(cells_to_visit)
        x, y, h, path = current_cell

        if is_key(x, y):
            path_drawer_greedy(maze, path)
            maze[x][y] = '*'
            print("Key has been founded")
            return True

        cells_to_visit.remove(current_cell)
        visited.add((x, y))
        list_of_neighbours = neighbours_list(x, y, maze)
        cells_to_visit = add_to_visit_list_greedy(list_of_neighbours, path, visited, cells_to_visit)

    print("No way to key")
    return False


#A* агоритм
cells_to_visit = []
visited = set()

def is_exit(x, y):
    return x == exit1[0] and y == exit1[1]

def is_empty_a_star(x, y, maze):
    return maze[x][y] == ' ' or maze[x][y] == '*' or maze[x][y] == '.'

def is_available_a_star(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty_a_star(x_new, y_new, maze)

def neighbours_list_a_star(x, y, maze=maze_list):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    list_of_neighbours = []
    for d in directions:
        if is_available_a_star(x, y, d, maze):
            list_of_neighbours.append((x + d[0], y + d[1]))
    return list_of_neighbours

def cost_a_star(x, y, x_0=key_coords[0], y_0=key_coords[1], x_exit=exit1[0], y_exit=exit1[1]):
    g = abs(x - x_0) + abs(y - y_0)  #манхеттенское расстояние
    h = 2 * round(np.sqrt((x_exit - x) ** 2 + (y_exit - y) ** 2), 3)  #евклидово расстояние
    f = g + h
    return f

def path_drawer_a_star(maze, path):
    for px, py in path:
        maze[px][py] = ','
    return maze

def add_to_visit_list_a_star(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit=cells_to_visit):
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

def a_star(x_0, y_0, maze, max_path_length, visited=visited, cells_to_visit=cells_to_visit):
    cells_to_visit = [(x_0, y_0, cost_a_star(x_0, y_0), [], 0)]
    visited = set()

    while cells_to_visit:
        current_cell = cell_selector(cells_to_visit)
        x, y, _, path, path_length = current_cell

        if is_exit(x, y):
            maze = path_drawer_a_star(maze, path)
            print("Exit has been founded")
            return True

        cells_to_visit.remove(current_cell)
        visited.add((x, y))
        list_of_neighbours = neighbours_list_a_star(x, y, maze)
        cells_to_visit = add_to_visit_list_a_star(list_of_neighbours, path, visited, path_length, max_path_length, cells_to_visit=cells_to_visit)

    print("No way to exit")
    return False

def save_solved_maze(maze_list):
    f = open('maze-for-me-done.txt', 'w')
    f.write('\n'.join(''.join(elem) for elem in maze_list))

#ищем путь
greedy(avatar_coords[0], avatar_coords[1], maze_list)
a_star(key_coords[0], key_coords[1],maze_list,max_path_length=3000)
save_solved_maze(maze_list)
