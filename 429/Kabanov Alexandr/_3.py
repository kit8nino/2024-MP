# -- coding: cp1251 --
import random
import math
from queue import PriorityQueue

def load_maze(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    height = len(lines)
    width = len(lines[0].strip())
    maze = [list(line.strip()) for line in lines]
    return maze, height, width

def save_maze(file_path, maze):
    with open(file_path, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def random_empty_position(maze, height, width):
    while True:
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        if maze[x][y] == ' ':
            return (x, y)

def find_exit(maze, height, width):
    for x in range(width):
        if maze[height - 1][x] == ' ':
            return (height - 1, x)
    return (height - 1, width - 1)

def is_within_bounds(x, y, height, width):
    return 0 <= x < height and 0 <= y < width

def is_walkable(x, y, maze, height, width):
    return is_within_bounds(x, y, height, width) and maze[x][y] in (' ', '.', '*')

def get_neighbors(position, maze, height, width):
    x, y = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_walkable(nx, ny, maze, height, width):
            neighbors.append((nx, ny))
    return neighbors

def mark_path(node, marker, maze):
    while node is not None:
        x, y = node[1]
        if maze[x][y] == ' ':
            maze[x][y] = marker
        node = node[2]

def heuristic_distance(pos, target_pos):
    return math.sqrt((target_pos[0] - pos[0]) ** 2 + (target_pos[1] - pos[1]) ** 2)

def greedy_search(start, key_pos, maze, height, width):
    queue = PriorityQueue()
    queue.put((heuristic_distance(start, key_pos), (0, start, None)))
    visited = set()

    maze[start[0]][start[1]] = 'S'

    while not queue.empty():
        _, current_node = queue.get()
        x, y = current_node[1]

        if current_node[1] == key_pos:
            mark_path(current_node, '.', maze)
            maze[x][y] = '*'
            return

        if current_node[1] in visited:
            continue

        visited.add(current_node[1])
        for neighbor in get_neighbors(current_node[1], maze, height, width):
            if neighbor not in visited:
                new_distance = current_node[0] + 1
                new_node = (new_distance, neighbor, current_node)
                queue.put((heuristic_distance(neighbor, key_pos), new_node))

def a_star_search(start, max_steps, maze, height, width, exit_pos):
    queue = PriorityQueue()
    visited = set()
    queue.put((heuristic_distance(start, exit_pos), (0, start, None)))

    while not queue.empty():
        _, current_node = queue.get()
        pos = current_node[1]

        if pos == exit_pos:
            mark_path(current_node, ',', maze)
            maze[pos[0]][pos[1]] = 'E'
            return

        visited.add(pos)
        for neighbor in get_neighbors(pos, maze, height, width):
            if current_node[0] + 1 <= max_steps and neighbor not in visited:
                new_node = (current_node[0] + 1, neighbor, current_node)
                queue.put((heuristic_distance(neighbor, exit_pos) + new_node[0], new_node))

maze, height, width = load_maze("maze-for-u.txt")

start_position = random_empty_position(maze, height, width)
key_position = random_empty_position(maze, height, width)
exit_position = find_exit(maze, height, width)

greedy_search(start_position, key_position, maze, height, width)
a_star_search(key_position, 5000, maze, height, width, exit_position)

save_maze("maze-for-me-done.txt", maze)