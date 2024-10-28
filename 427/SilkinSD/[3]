from random import randint

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
