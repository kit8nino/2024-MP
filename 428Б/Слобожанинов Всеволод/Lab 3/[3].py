# -*- coding: utf-8 -*-
"""
Created on Mon May 27 07:08:28 2024

@author: vs890
"""

import random

# Функция для чтения лабиринта из файла
def read_maze(file_name):
    with open(file_name, 'r') as file:
        maze = []
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Функция для поиска свободных координат
def find_empty_spot(maze):
    x = random.randint(0, len(maze)-1)
    y = random.randint(0, len(maze[0])-1)
    while maze[x][y] == '#':
        x = random.randint(0, len(maze)-1)
        y = random.randint(0, len(maze[0])-1)
    return x, y

# Чтение лабиринта из файла
maze = read_maze('maze-for-u.txt')

# Нахождение координат аватара
avatar_x, avatar_y = find_empty_spot(maze)

# Вывод аватара на лабиринт
maze[avatar_x][avatar_y] = 'A'

# Вывод обновленного лабиринта
for row in maze:
    print(''.join(row))