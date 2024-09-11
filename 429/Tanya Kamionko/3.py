# -- coding: cp1251 --
import random
import math
from queue import PriorityQueue
from collections import deque

class Node:
    def __init__(self, dist, pos, prev):
        self.dist = dist
        self.pos = pos
        self.prev = prev

    def __lt__(self, other):
        return self.dist < other.dist


def maze_in(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    width = len(lines)
    height = len(lines[0].strip())
    maze = [list(line.strip()) for line in lines]
    return maze, width, height

def maze_out(path, maze):
    with open(path, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def set_rand_pos(maze, width, height):
    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if maze[x][y] == ' ':
            return (x, y)

def get_exit_pos(maze, width, height):
    y = height - 1
    for x in range(width):
        if maze[x][y] == ' ':
            return (x - 1, y - 1)
    return (width - 1, y - 1)

def is_in_boundaries(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def is_available(x, y, maze, width, height):
    return is_in_boundaries(x, y, width, height) and (maze[x][y] == ' ' or maze[x][y] == '.' or maze[x][y] == '*')

def neighbours(pos, maze, width, height):
    x, y = pos
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if is_available(nx, ny, maze, width, height):
            result.append((nx, ny))
    return result

def draw_path(node, ch, maze):
    while node.prev is not None:
        maze_set_char(node.pos, ch, maze)
        node = node.prev

def maze_set_char(pos, ch, maze):
    x, y = pos
    maze[x][y] = ch

def is_key(pos, key_pos):
    return pos == key_pos

def is_exit(pos, exit_pos):
    return pos == exit_pos

def cost_greedy(pos, exit_pos):
    return math.sqrt((exit_pos[0] - pos[0]) ** 2 + (exit_pos[1] - pos[1]) ** 2)

def greedy(start, key_pos, maze, width, height):
    x_0, y_0 = start
    to_visit = PriorityQueue()
    to_visit.put((cost_greedy((x_0, y_0), key_pos), Node(0, (x_0, y_0), None)))
    visited = set()

    maze[x_0][y_0] = 'S'

    while not to_visit.empty():
        t, current_node = to_visit.get()
        x, y = current_node.pos

        if is_key(current_node.pos, key_pos):
            draw_path(current_node, '.', maze)
            maze[x][y] = '*'
            return

        if current_node.pos in visited:
            continue

        visited.add(current_node.pos)

        list_of_neighbours = neighbours(current_node.pos, maze, width, height)

        for neighbour in list_of_neighbours:
            if neighbour not in visited:
                new_dist = current_node.dist + 1
                new_node = Node(new_dist, neighbour, current_node)
                new_h = cost_greedy(neighbour, key_pos)
                to_visit.put((new_h, new_node))
                
def a_star_dist(node, exit_pos):
    pos = node.pos
    g = node.dist
    f = math.sqrt((exit_pos[0] - pos[0]) ** 2 + (exit_pos[1] - pos[1]) ** 2)
    return g + f

def a_star(start, max_len, maze, width, height, exit_pos):
    to_visit = PriorityQueue()
    visited = set()
    
    to_visit.put((a_star_dist(Node(0, start, None), exit_pos), Node(0, start, None)))
    while not to_visit.empty():
        _, current_cell = to_visit.get()
        pos = current_cell.pos
        if is_exit(pos, exit_pos):
            draw_path(current_cell.prev, ',', maze)
            maze_set_char(pos, 'E', maze)
            return
        visited.add(pos)
        for neighbour in neighbours(pos, maze, width, height):
            if current_cell.dist + 1 <= max_len and neighbour not in visited:
                to_visit.put((a_star_dist(Node(current_cell.dist + 1, neighbour, current_cell), exit_pos), Node(current_cell.dist + 1, neighbour, current_cell)))


maze, width, height = maze_in("maze-for-u.txt")

start_pos = set_rand_pos(maze, width, height)
key_pos = set_rand_pos(maze, width, height)
exit_pos = get_exit_pos(maze, width, height)

greedy(start_pos, key_pos, maze, width, height)
a_star(key_pos, 5000, maze, width, height, exit_pos)

maze_out("maze-for-me.txt", maze)
