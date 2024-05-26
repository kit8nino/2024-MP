from random import randint
import numpy as np

def read_maze(file_name):
	with open(file_name, 'r') as r_file:
		maze = [list(line.strip()) for line in r_file]
		return maze

def save_maze(maze, file_name):
    with open(file_name, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def get_coords():
    y = randint(0, len(maze)-1)
    x = randint(0, len(maze[0])-1)
    while maze[y][x] == "#":
        y = randint(1, len(maze)-1)
        x = randint(1, len(maze[0])-1)
    return (y, x)

def dfs(graph, start, symbol='*'):
    visited = []
    stack = [start]
    y, x = start
    
    while stack:
        node = stack.pop()
        y, x = node
        if node not in visited:
            visited.append(node)
            if y == 0 or y == len(maze)-1 or x == 0 or x == len(maze[0])-1:
                #print("Граница")
                continue
            
            neighbors = []
            if graph[y+1][x] != '#' and (y+1, x) not in visited:
                neighbors.append((y+1,x))
            if graph[y-1][x] != '#' and (y-1, x) not in visited:
                neighbors.append((y-1,x))
            if graph[y][x+1] != '#' and (y, x+1) not in visited:
                neighbors.append((y,x+1))
            if graph[y][x-1] != '#' and (y, x-1) not in visited:
                neighbors.append((y,x-1))
            
            for neighbour in neighbors:
                if neighbour not in visited:
                    stack.append(neighbour)
                    
            if graph[y][x] == '*':
                visited.append(node)
                break
        #print(y, x, "->", graph[y][x], stack)
    return visited

def nearest_exit(maze, start):
    exits = []
    
    y1, y2 = 0, len(maze)-1
    for x in range(len(maze[0])):
        if maze[y2][x] != '#':
            exits.append((y2,x))
        if maze[y1][x] != '#':
            exits.append((y1,x))
    x1, x2 = 0, len(maze[0])-1
    for y in range(len(maze)):
        if maze[y][x1] != '#':
            exits.append((y,x1))
        if maze[y][x2] != '#':
            exits.append((y,x2))
    
    min_dist = len(maze) * len(maze[0])
    min_exit = exits[0]
    for exit1 in exits:
        d = ((exit1[0] - start[0])**2 + (exit1[1] - start[1])**2) ** 0.5
        if d < min_dist:
            min_dist = d
            min_exit = exit1
        
    return min_exit

def A_star(maze, start, end):
    def h(node, end):
        return ((node[0] - end[0])**2 + (node[1] - end[1])**2) ** 0.5
    
    def get_f(node):
        return g[node] + h(node, end)

    def get_current_node(Q):
        current = Q[0]
        min_f = len(maze) * len(maze[0])
        
        for node in Q:
            if get_f(node) < min_f:
                current = node
                min_f = get_f(node)
        return current
    
    def get_neighbor(node):
        neighbours = []
        g_for_neighbours = {}
        y, x = node
        
        if maze[y-1][x-1] != '#':
            neighbours.append((y-1,x-1))
            g_for_neighbours[(y-1,x-1)] = 2**0.5
        if maze[y-1][x+1] != '#':
            neighbours.append((y-1,x+1))
            g_for_neighbours[(y-1,x+1)] = 2**0.5
        if maze[y+1][x+1] != '#':
            neighbours.append((y+1,x+1))
            g_for_neighbours[(y+1,x+1)] = 2**0.5
        if maze[y+1][x-1] != '#':
            neighbours.append((y+1,x-1))
            g_for_neighbours[(y+1,x-1)] = 2**0.5
        
        if maze[y-1][x] != '#':
            neighbours.append((y-1,x))
            g_for_neighbours[(y-1,x)] = 1
        if maze[y][x-1] != '#':
            neighbours.append((y,x-1))
            g_for_neighbours[(y,x-1)] = 1
        if maze[y][x+1] != '#':
            neighbours.append((y,x+1))
            g_for_neighbours[(y,x+1)] = 1
        if maze[y+1][x] != '#':
            neighbours.append((y+1,x))
            g_for_neighbours[(y+1,x)] = 1
            
        return neighbours, g_for_neighbours
    
    U = []
    Q = [start]
    g, f, parents = dict(), dict(), dict()
    g[start] = 0
    f[start] = get_f(start)
    while len(Q) != 0:
        current = get_current_node(Q)
        if current == end:
            U.insert(0, current)
            f[current] = get_f(current)
            #print(parents)
            return parents
        
        Q.remove(current)
        U.insert(0, current)
        neighbours, g_for_neighbours = get_neighbor(current)
        g = g | g_for_neighbours
        for node in neighbours:
            tentative_score = g[current] + h(current, node)
            if node in U and tentative_score > g[node]:
                continue
            if node not in U or tentative_score <= g[node]:
                parents[node] = current
                g[node] = tentative_score
                f[node] = get_f(node)
                if node not in Q:
                    Q.insert(0, node)
    print("Выхода нет, скоро рассвет...")
    return U

def find_way1(visited):
    way = visited
    i = len(visited)-1
    while i > 1:
        delta_y = abs(way[i][0] - way[i-1][0])
        delta_x = abs(way[i][1] - way[i-1][1])
        if delta_x + delta_y > 1:
            way.pop(i-1)
        i -= 1
    return way

def find_way2(parents, start, end):
    parent = end
    child = parents[end]
    way = [end]
    while child != start:
        parent = child
        child = parents[parent]
        way.append(parent) 
    return way

maze = read_maze('maze-for-u.txt')

avatar = get_coords()
key = get_coords()
maze[avatar[0]][avatar[1]] = '+'
maze[key[0]][key[1]] = '*'

end = nearest_exit(maze, key)
way_to_key = find_way1(dfs(maze, avatar))
way_to_exit = find_way2(A_star(maze, key, end), key, end)

for i in range(1, len(way_to_key)-2):
    maze[way_to_key[i][0]][way_to_key[i][1]] = '.'
    #print(i, way_to_key[i])

for i in range(0, len(way_to_exit)):
    if maze[way_to_exit[i][0]][way_to_exit[i][1]] == '.':
        maze[way_to_exit[i][0]][way_to_exit[i][1]] = ';'
    else:
        maze[way_to_exit[i][0]][way_to_exit[i][1]] = ','
    #print(i, way_to_exit[i])

save_maze(maze, "maze-for-u-done.txt")
print("Лабиринт пройден")
