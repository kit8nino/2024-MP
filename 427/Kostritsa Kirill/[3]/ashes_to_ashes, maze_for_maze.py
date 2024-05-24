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

def find_way(visited):
    way = visited
    i = len(way) - 1
    while i != 1:
        delta1 = abs(way[i][0]-way[i-1][0])
        delta2 = abs(way[i][1]-way[i-1][1])
        if delta1 + delta2 > 1:
            way.pop(i-1)
        i -= 1
    return way


maze = read_maze('maze-for-u_prob.txt')
avatar = get_coords()
key = get_coords()
maze[avatar[0]][avatar[1]] = '+'
maze[key[0]][key[1]] = '*'

visited = dfs(maze, avatar)
way = find_way(visited)

for i in range(1, len(way)-2):
    maze[way[i][0]][way[i][1]] = "."
    #print(i, way[i])







save_maze(maze, "maze-for-u-done_prob.txt")
print("Лабиринт пройден (от старта до ключа")



