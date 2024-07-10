import sys
import numpy as np

sys.setrecursionlimit(9000)

wall, path, key, avatar, way, a_way = "#", " ", "*", "$", ".", ","


def read_maze():
    maze = []
    with open("maze-for-u.txt") as f:
        for line in f:
            maze.append(list(line))
    for i in range(len(maze)):
        maze[i].pop(-1)
    height = len(maze)
    width = len(maze[0])
    return maze, width, height


def create_avatar(x_max, y_max):
    while True:
        y_avatar = int(input(f"Enter y coord of avatar (y < {y_max}): "))
        x_avatar = int(input(f"Enter x coord of avatar (x < {x_max}): "))
        if maze[y_avatar][x_avatar] == wall:
            print("Enter another x and y coord")
        else:
            return [y_avatar, x_avatar]


def create_key(x_max, y_max):
    while True:
        y_key = int(input(f"Enter y coord of key (y < {y_max}): "))
        x_key = int(input(f"Enter x coord of key (x < {x_max}): "))
        if maze[y_key][x_key] == wall:
            print("Enter another x and y coord")
        else:
            return [y_key, x_key]


def mark_nodes(x_max, y_max):
    mark_dict = dict()
    count = 1
    for i in range(y_max):
        for j in range(x_max):
            if maze[i][j] == path or maze[i][j] == key or maze[i][j] == avatar:
                mark_dict[count] = [i, j]
                count += 1
    return mark_dict



def create_dict(x_max, y_max):
    d1 = {}
    count = 1
    for i in range(y_max):
        for j in range(x_max):
            pos_list = {}
            if maze[i][j] != wall:
                if i != y_max-1:
                    if maze[i+1][j] != wall:
                        pos_list[key_list[val_list.index([i+1, j])]] = 1
                if i != 0:
                    if maze[i-1][j] != wall:
                        pos_list[key_list[val_list.index([i-1, j])]] = 1
                if j != x_max-1:
                    if maze[i][j+1] != wall:
                        pos_list[key_list[val_list.index([i, j+1])]] = 1
                if j != 0:
                    if maze[i][j-1] != wall:
                        pos_list[key_list[val_list.index([i, j-1])]] = 1
                d1[count] = pos_list
                count += 1
    return d1


def greedy(v, p, t, b, e, choose):
    for x in G[v]:
        if choose == 1:  # общая стоимость узла для А*
            xm = p[v] + G[v][x] + np.sqrt((mark_dict[e][0] - mark_dict[x][0])**2 +
                                          (mark_dict[e][1] - mark_dict[x][1])**2)
        else:  # общая стоимость узла для алгоритма Дейкстры
            xm = p[v] + G[v][x]
        if not x in p:
            p[x] = xm
            b[x] = v
        elif not x in t:
            if p[x] > xm:
                p[x] = xm
                b[x] = v
    t.append(v)
    if v == e:
        s = []
        s.insert(0, e)
        global way_list
        while True:
            if b[e] == -1:
                break
            e = b[e]
            s.insert(0, e)
        way_list = s.copy()
        return s
    for d in p:
        if d not in t:
            dm = p[d]
            break
    for y in p:
        if p[y] < dm and not y in t:

            dm = p[y]
            d = y
    v = d
    greedy(v, p, t, b, e, choose)


def restore_path(choose):
    for i in way_list:
        r = mark_dict[i]
        if maze[r[0]][r[1]] == path:
            if choose == 1:
                maze[r[0]][r[1]] = a_way
            else:
                maze[r[0]][r[1]] = way
        elif maze[r[0]][r[1]] == way:
            maze[r[0]][r[1]] = ";"


def create_maze_done():
    maze_string = []
    for i in maze:
        string = ""
        for j in i:
            string += str(j)
        maze_string.append(string)

    with open("maze-for-me-done.txt", "w+") as file:
        file.writelines("%s\n" % line for line in maze_string)


maze, width, height = read_maze()
avatar_coord,key_coord = create_avatar(width, height), create_key(width, height)
print(width, height)
maze[key_coord[0]][key_coord[1]] = key
maze[avatar_coord[0]][avatar_coord[1]] = avatar
coord = avatar_coord


mark_dict = mark_nodes(width, height)
key_list = list(mark_dict.keys())
val_list = list(mark_dict.values())
G = create_dict(width, height)

N = len(G)

# Жадный Алгоритм
t = []
p = {}
b = {}
v = key_list[val_list.index(avatar_coord)]
e = key_list[val_list.index(key_coord)]
p[v] = 0
b[v] = -1
way_list = []
greedy(v, p, t, b, e, 0)
restore_path(0)

# Алгоритм A*
end_coord = [0, 1]
way_list.clear()
t = []
p = {}
b = {}
v = key_list[val_list.index(key_coord)]
e = key_list[val_list.index(end_coord)]
p[v] = 0
b[v] = -1
greedy(v, p, t, b, e, 1)
restore_path(1)

create_maze_done()
for row in maze:
    print(*row)