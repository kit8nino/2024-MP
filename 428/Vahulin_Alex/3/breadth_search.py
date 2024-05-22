our_maze = []
f=open("maze-for-u.txt", "r")
while True:
    row=f.readline()
    if row=="":
        f.close()
        break
    mass_row=[]
    for i in row:
        mass_row.append(i)
    our_maze.append(mass_row)

x, y = 0, 0
x_key, y_key = 0, 0
list_to_visit = []

def is_exit(x, y):
    return y == len(our_maze[-1])-1 and x == len(our_maze)-1

def add_to_visit_list(list_of_neighbours, list_to_visit):
    return list_to_visit.extend(list_of_neighbours)

def is_in_boundaries(x, y, maze):
    return x < len(maze) and x >= 0 and y < len(maze[0]) and y >= 0

def is_empty(x, y, maze):
    return maze[x][y] != "#"

def is_available(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty(x_new, y_new, maze)

def is_in_route(x,y,route):
    node=(x,y)
    return node in route

def neighbours_list(x,y, maze, route):
    directions = ((-1,0),(1,0),(0,-1),(0,1))
    neighbours=[]
    for d in directions:
        x_n = x + d[0]
        y_n = y + d[1]
        if is_available(x, y, d, maze):
            if not is_in_route(x_n,y_n,route):
                neighbours.append((x + d[0], y + d[1]))
    return neighbours

def choose_cell_to_visit(list_to_visit):
    return list_to_visit.pop(0)

def is_key(x, y):
    return x == x_key and y == y_key

def put_object(x, y, maze):
    from random import randint
    x = randint(1, len(maze)//2)
    y = randint(1, len(maze[0])//2)
    while is_empty(x, y, maze) == False:
        x += randint(0, 1)
        y += randint(0, 1)
    return x, y

def paint_path(maze, route, symbol):
    for i in route:
        if maze[i[0]][i[1]] != "*": maze[i[0]][i[1]] = symbol
    return None

while x == x_key and y == y_key:
    x_key, y_key = put_object(x_key, y_key, our_maze)

x, y = 0, 1
# x_key, y_key = 24, 1      # отладочное положение ключа
our_maze[x_key][y_key]='*'

print(x, y, x_key, y_key, our_maze[x_key][y_key], our_maze[x][y])

def bfs_route(x, y, x_key, y_key, maze):
    
    route = []
    while not is_key(x, y):
        step = (x, y)
        if step not in route:
            route.append(step)
            add_to_visit_list(neighbours_list(x,y, our_maze, route), list_to_visit)
            x, y = choose_cell_to_visit(list_to_visit)
    return route

bfs_path = bfs_route(x, y, x_key, y_key, our_maze)
if bfs_path:
    print("Клеток пройдено от старта до ключа:", len(bfs_path))
    paint_path(our_maze, bfs_path, ".")

x_exit, y_exit = len(our_maze)-1, len(our_maze[-1])-2
print(our_maze[x_exit][y_exit])

from heapq import heappop, heappush
def key_search(maze, start_coord, goal, g_weight, h_weight, max_steps): 
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    queue = [(heuristic(start_coord, goal), 0, start_coord, [])]
    visited = set()
    while queue:
        _, cost, current, path = heappop(queue)
        if current == goal:
            return path + [current]
        visited.add(current)
        row, col = current
        neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbour in neighbours:
            n_row, n_col = neighbour
            if is_available(row, col, (n_row-row, n_col-col), maze) and not is_in_route(neighbour[0], neighbour[1], visited):
                new_cost = cost + 1
                priority = new_cost * g_weight + heuristic(neighbour, goal) * h_weight
                if priority <= max_steps:
                    heappush(queue, (priority, new_cost, neighbour, path + [current]))
    return None

g_weight = 1 
h_weight = 1  
max_steps = 7000
a_star_route = key_search(our_maze, (x_key, y_key), (x_exit, y_exit), g_weight, h_weight, max_steps)
if a_star_route:
    print("Длина пути от ключа до выхода:", len(a_star_route))
    paint_path(our_maze, a_star_route, ",")
    
f=open("maze-for-me-done.txt", "w")
for i in our_maze:
    f.write("".join(i))
f.close()