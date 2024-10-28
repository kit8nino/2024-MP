# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random


def read_maze(file_name):
    maze = []
    with open(file_name, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

def write_maze(file_name, maze):
    with open(file_name, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def create_avatar(maze):
    while True:
        i = random.randint(0, len(maze) - 1)
        j = random.randint(0, len(maze[i]) - 1)
        if maze[i][j] != '#':
            return i, j

def find_exit_position(maze):
    possible_exits = []
    for i in range(len(maze)):
        if maze[i][0] != '#':
            possible_exits.append((i, 0))
        if maze[i][-1] != '#':
            possible_exits.append((i, len(maze[i]) - 1))
    for j in range(len(maze[0])):
        if maze[0][j] != '#':
            possible_exits.append((0, j))
        if maze[-1][j] != '#':
            possible_exits.append((len(maze) - 1, j))
    return random.choice(possible_exits)


def get_neighbours(position, maze):
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Верх, низ, лево, право
    for direction in directions:
        x = position[0] + direction[0]
        y = position[1] + direction[1]
        if 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != '#':
            neighbours.append((x, y))
    return neighbours


def depth_first_search(maze, start, key):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        visited.add(current)

        if current == key:
            return path

        neighbours = get_neighbours(current, maze)
        unvisited_neighbours = [n for n in neighbours if n not in visited]

        if unvisited_neighbours:
            for neighbour in unvisited_neighbours:
                stack.append((neighbour, path + [neighbour]))
                visited.add(neighbour)
    return None
def calculate_distance(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

def a_star_search(maze, start, goal, max_steps):
    open_list = [(start, 0, calculate_distance(start, goal))]
    closed_list = set()
    parent = {}
    g_scores = {start: 0}

    while open_list:
        current, g_score, f_score = min(open_list, key=lambda x: x[2])
        open_list.remove((current, g_score, f_score))
        closed_list.add(current)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        if len(closed_list) > max_steps:
            return None

        neighbours = get_neighbours(current, maze)
        for neighbour in neighbours:
            if neighbour in closed_list:
                continue

            tentative_g_score = g_score + 1
            if neighbour not in g_scores or tentative_g_score < g_scores[neighbour]:
                g_scores[neighbour] = tentative_g_score
                f_score = tentative_g_score + calculate_distance(neighbour, goal)
                open_list.append((neighbour, tentative_g_score, f_score))
                parent[neighbour] = current

    return None



maze = read_maze('maze-for-u.txt')


start_position = create_avatar(maze)
print("start position=",start_position)
exit_position = find_exit_position(maze)


key_position = create_avatar(maze) 
while key_position == start_position: 
    key_position = create_avatar(maze)
maze[key_position[0]][key_position[1]] = '*' 

dfs_path = depth_first_search(maze, start_position, key_position)

if dfs_path is not None:
   
    for position in dfs_path:
        maze[position[0]][position[1]] = '.'

   
    a_star_path = a_star_search(maze, key_position, exit_position, len(maze) * len(maze[0]))

    if a_star_path is not None:
       
        for position in a_star_path:
            maze[position[0]][position[1]] = ','

        
        maze[start_position[0]][start_position[1]] = 'A'
        maze[exit_position[0]][exit_position[1]] = 'E'
        maze[key_position[0]][key_position[1]] = '*'

       
        write_maze('maze-for-me-done.txt', maze)
        print("result saved in 'maze-for-me-done.txt'.")
    else:
        print("Cannot find exit.")
else:
    print("Cannot find key.")