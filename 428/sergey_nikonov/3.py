from collections import deque 
from heapq import heappop, heappush 

maze_input_file = 'maze-for-u.txt' 
def read_maze(): 
    maze_map=[] 
    with open('maze-for-u.txt') as maze_file: 
        for line in maze_file: 
           maze_map.append(line.strip('\n')) 
        width, height = len(maze_map[0]), len(maze_map) 
    return width, height, maze_map 

def read(filename):  
    maze = [] 
    with open(filename, 'r') as file: 
        for line in file: 
            row = line.strip() 
            maze.append(list(row)) 
    return maze 

def set_coordinate(coord, sign): 
    global maze_layout 
    maze_row = list(maze_layout[coord[1]]) 
    maze_row[coord[0]] = sign 
    maze_layout[coord[1]] = ''.join(maze_row) 

def not_inside_wall(maze, coord): 
    if maze[coord[1]][coord[0]] == '#': 
        return False 
    return True 

# Жадный поиск 

def heuristic(node, goal): 
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1]) 

def get_neighbors_for_greedy_search(current, goal): 
    row, col = current 
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)] 
    neighbors = sorted(neighbors, key=lambda neighbor: heuristic(neighbor, goal),) 
    return neighbors 

def is_valid_neighbor_for_greedy_search(neighbor, maze, visited): 
    adjacent_row, adjacent_col = neighbor 
    if (0 <= adjacent_row < len(maze) and 0 <= adjacent_col < len(maze[0]) and maze[adjacent_row][adjacent_col] != "#" and neighbor not in visited): 
        return True 
    return False 

def greedy_search(maze, start_coord, goal): 
    queue = deque([(start_coord, [])]) 
    visited = set() 

    while queue: 
        current, path = queue.popleft() 
        if current == goal: 
            return path + [current] 
        visited.add(current) 

        neighbors = get_neighbors_for_greedy_search(current, goal) 

        for neighbor in neighbors: 
            if is_valid_neighbor_for_greedy_search(neighbor, maze, visited): 
                queue.append((neighbor, path + [current])) 
    return None  

def is_valid_neighbor_for_a_star_search(neighbor, maze): 
    if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != "#": 
        return True 
    return False 

def get_neighbors_for_a_star_search(current, maze): 
    row, col = current 
    neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)] 

    valid_neighbors = [] 
    for neighbor in neighbors: 
        if is_valid_neighbor_for_a_star_search(neighbor, maze): 
            valid_neighbors.append(neighbor) 

    return valid_neighbors 

def get_priority(neighbor, cost, goal, cost_weight, heuristic_weight): 
    new_cost = cost + 1 
    priority = new_cost * cost_weight + heuristic(neighbor, goal) * heuristic_weight 
    return priority 

def a_star_search(maze, start_coord, goal, cost_weight, heuristic_weight, max_steps): 
    queue = [] 
    heappush(queue, (heuristic(start_coord, goal), 0, start_coord, [])) 
    visited = set() 

    while queue: 
        _, cost, current, path = heappop(queue) 

        if current == goal: 
            return path + [current] 

        visited.add(current) 

        for neighbor in get_neighbors_for_a_star_search(current, maze): 
            if neighbor not in visited: 
                priority = get_priority(neighbor, cost, goal, cost_weight, heuristic_weight) 

                if priority <= max_steps: 
                    heappush(queue, (priority, cost + 1, neighbor, path + [current])) 

    return None 

def mark(maze, path, symbol):  
    marked_maze = [row.copy() for row in maze] 
    for position in path: 
        row, col = position 
        marked_maze[row][col] = symbol 
    return marked_maze 

width, height, maze_layout = read_maze() 
maze = read(maze_input_file) 

entry_coordinate = (0, 1) 
exit_coordinate = (1079, 1918) 
print("Координаты входа:", entry_coordinate) 
print("Координаты выхода:", exit_coordinate) 

key_x = 315
key_y = 313
key_coordinate = (key_x, key_y) 

if not not_inside_wall(maze, key_coordinate): 
    print("Ключ находится в стене, выберите другие координаты") 
    exit() 
 
set_coordinate(key_coordinate, '*') 

print("Координаты ключа:", key_coordinate) 

# жадный алгоритм 
greedy_path = greedy_search(maze, entry_coordinate, key_coordinate) 
if greedy_path: 
    print("Длина пути от входа до ключа:", len(greedy_path)) 
marked_maze = mark(maze, greedy_path, ".") 

# алгоритм А*  
cost_weight = 1  
heuristic_weight = 1   
max_steps = 15000   
a_star_path = a_star_search(maze, key_coordinate, exit_coordinate, cost_weight, heuristic_weight, max_steps) 
if a_star_path: 
    print("Длина пути от ключа до выхода:", len(a_star_path)) 
    marked_maze = mark(marked_maze, a_star_path, ",") 
 
maze_output_file = "maze-for-me-done.txt"  
with open(maze_output_file, "w") as file: 
    for row in marked_maze: 
        file.write("".join(row) + "\n")