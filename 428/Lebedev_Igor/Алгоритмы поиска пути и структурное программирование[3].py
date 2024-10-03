import numpy as np
import heapq

class MazeSolver:
    def __init__(self, maze_file):
        self.maze = self.load_maze(maze_file)
        self.start_pos = (0, 10)
        self.key_pos = (100, 1867)
        self.exit_pos = (1079, 1918)
        self.maze[self.key_pos[0]][self.key_pos[1]] = '*'
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def load_maze(self, file_name):
        maze = []
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                maze.append(list(line.strip()))
        return maze

    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] in (' ', '*', '.')

    def find_path(self, start, end, algorithm='dijkstra'):
        frontier = [(0, start, [])]
        visited = set()
        while frontier:
            cost, current, path = heapq.heappop(frontier)
            if current in visited:
                continue
            visited.add(current)
            if current == end:
                return self.trace_path(path + [end])
            for d in self.directions:
                next_pos = (current[0] + d[0], current[1] + d[1])
                if self.is_valid(next_pos):
                    next_cost = cost + (self.heuristic(next_pos, end) if algorithm == 'a_star' else 1)
                    heapq.heappush(frontier, (next_cost, next_pos, path + [current]))
        return False

    def heuristic(self, pos, end):
        return 2 * round(np.sqrt((end[0] - pos[0]) ** 2 + (end[1] - pos[1]) ** 2), 3)

    def trace_path(self, path):
        for pos in path:
            self.maze[pos[0]][pos[1]] = '.' if self.maze[pos[0]][pos[1]] != '*' else '*'
        return True

    def save_maze(self, file_name):
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write('\n'.join(''.join(row) for row in self.maze))

    def solve_maze(self):
        key_found = self.find_path(self.start_pos, self.key_pos)
        exit_found = self.find_path(self.key_pos, self.exit_pos, algorithm='a_star') if key_found else False
        self.save_maze('maze-for-me-done.txt')
        return key_found, exit_found

solver = MazeSolver('maze-for-u.txt')
key_exists, exit_exists = solver.solve_maze()
print("Путь к ключу найден!" if key_exists else "Путь к ключу не найден!")
print("Путь к выходу найден!" if exit_exists else "Путь к выходу не найден!")