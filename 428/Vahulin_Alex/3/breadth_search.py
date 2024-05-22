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
    
print(len(our_maze), len(our_maze[0]))

x, y = 0, 0
x_key, y_key = 0, 0
list_to_visit = []
route = []

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
            if  not is_in_route(x_n,y_n,route):
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

# x, y = put_object(x, y, our_maze)
# x_key, y_key = put_object(x_key, y_key, our_maze)

x, y = 0, 1
x_key, y_key = 718, 328
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

route = bfs_route(x, y, x_key, y_key, our_maze)
for i in route:
    our_maze[i[0]][i[1]]='.'
print(route)

# x_exit, y_exit = len(our_maze)-1, len(our_maze[-1])-2
# print(our_maze[x_exit][y_exit])

# from math import sqrt
# def h(x, y, x_key, y_key):
#     return sqrt((x_key-x)**2+(y_key-y)**2)

# def g(g_tmp):
#     return g_tmp+10

# def check_cost(cell,g_temp,x_key,y_key):
#     print("cell:",cell)
#     x=cell[0]
#     y=cell[1]
#     for_f=[]
#     for_f.append(g(g_temp))
#     for_f.append(h(x,y,x_key,y_key))
#     print(for_f)
#     return for_f

# def find_cell_with_min_cost(cell,neighbours,x_key,y_key):
#     costs=[]
#     gs=[]
#     g_temp=0
#     for i in neighbours:
#         costs.append(sum(check_cost(neighbours,g_temp,x_key,y_key)))
#         print("costs",costs)
#         gs.append(check_cost(neighbours,g_temp,x_key,y_key)[0])
#         print(gs)
#     print("neighbours:",neighbours)
#     cells_f_ranging=sorted(neighbours,key=check_cost(neighbours,g_temp,x_key,y_key))
#     print(cells_f_ranging)
#     return cells_f_ranging.pop(0)       


# def find_route_by_A(x,y,x_key,y_key,maze):
#     route=[]
#     while x!=x_key and y!=y_key:
#             v=(x,y)
#             if v not in route:
#                 route.append(v)
#                 x, y = find_cell_with_min_cost((x,y),neighbours_list(x,y,our_maze,route),x_key,y_key)
#     return route

# route2=find_route_by_A(x, y, x_exit, y_exit, our_maze)
# print("Маршрут:\n")               
# print(route2)
# print('\n')
# print()
