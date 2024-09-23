import numpy as np
from collections import deque
import os

def save_maze(filename, maze):
    with open(filename, 'w') as file:
        for line in maze:
            file.write(''.join(line) + '\n')

def copy_maze_file(source_filename, destination_filename):
    with open(source_filename, 'r') as source_file:
        with open(destination_filename, 'w') as dest_file:
            for line in source_file:
                dest_file.write(line)

def load_maze(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

source_filename = 'maze-for-u.txt'  
destination_filename = 'maze-for-me-done.txt'

copy_maze_file(source_filename, destination_filename)


# проверяем, попадает ли аватар или ключ на свободный проход 
def is_valid_move(maze, position):
    x, y = position
    return ((0 <= x < len(maze) and 
            0 <= y < len(maze[0])) and 
            (maze[x][y] == ' ' or maze[x][y] == '@'))

# ищем ближайший свободный проход, если заспавнились на стене
def move_avatar(maze, start):
    queue = deque([start])
    visited = set()
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (право, вниз, влево, вверх)

    while queue:
        current = queue.popleft()
        
        for direction in directions:
            next_x = current[0] + direction[0]
            next_y = current[1] + direction[1]
            next_position = (next_x, next_y)

            if next_position not in visited and is_valid_move(maze, next_position):
                return next_position
            
            if next_position not in visited and maze[next_x][next_y] == ' ':
                queue.append(next_position)
                visited.add(next_position)

    return start  # вернём стартовую позицию, если не нашли подходящую


# ищем путь от аватара до ключа и от ключа до выхода
def poisk_v_shirinu(maze, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (право, вниз, влево, вверх)

    while queue:
        current, path = queue.popleft()
        if current == target:
            for pos in path:
                maze[pos[0]][pos[1]] = '@'
            return path
        
        for direction in directions:
            next_x = current[0] + direction[0]
            next_y = current[1] + direction[1]
            next_position = (next_x, next_y)

            if is_valid_move(maze, next_position) and next_position not in visited:
                visited.add(next_position)
                queue.append((next_position, path + [next_position]))
    
    return []  # если не нашли путь



# основная функция
def main():
    maze = load_maze(destination_filename)

    avatar_start = tuple(map(int, input("Введите координаты аватара (x y): ").split()))
    key_position = tuple(map(int, input("Введите координаты ключа (x y): ").split()))
    exit_position = tuple(map(int, input("Введите координаты выхода (x y): ").split()))

    if maze[avatar_start[0]][avatar_start[1]] == '#':
        avatar_start = move_avatar(maze, avatar_start)
    
    if maze[key_position[0]][key_position[1]] == '#':
        key_position = move_avatar(maze, key_position)

    # Поиск ключа
    path_to_key = poisk_v_shirinu(maze, avatar_start, key_position)
    if path_to_key:
        print("Путь к ключу:", path_to_key)
    else:
        print("Пу-пу-пу, ключ не найден...")

    # Поиск выхода
    path_to_exit = poisk_v_shirinu(maze, key_position, exit_position)
    if path_to_exit:
        print("Путь к выходу:", path_to_exit)
    else:
        print("Пу-пу-пу, выход не найден...")
        
    save_maze('maze-for-me-done.txt', maze)

if __name__ == "__main__":
    main()




print('Нажмите любую клавишу для завершения программы')
a = input()
