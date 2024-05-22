import random

# Генерация текстового представления лабиринта
def generate_maze(rows, cols):
    maze = []
    for _ in range(rows):
        row = ['.' if random.random() < 0.7 else '#' for _ in range(cols)]
        maze.append(row)
    return maze

def save_maze_to_file(maze, file_name):
    with open(file_name, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def find_path_to_key(maze):
    start_row, start_col = 0, 0  # Начальная позиция аватара
    key_row, key_col = -1, -1  # Позиция ключа

    # Позицию ключа в лабиринте
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '*':
                key_row, key_col = i, j
                break

    #Поиск пути от аватара до ключа с помощью BFS
    queue = [(start_row, start_col)]
    visited = set()
    parent = {}
    found_path = False

    while queue:
        current_row, current_col = queue.pop(0)
        if (current_row, current_col) == (key_row, key_col):
            found_path = True
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = (current_row, current_col)

    if not found_path:
        return None

    # Восстановливаем путь от аватара до ключа
    path = []
    while (key_row, key_col) != (start_row, start_col):
        path.append((key_row, key_col))
        key_row, key_col = parent[(key_row, key_col)]
    path.append((start_row, start_col))
    path.reverse()

    return path

if __name__ == "__main__":
    rows = 10
    cols = 10
    maze = generate_maze(rows, cols)
    maze[0][0] = 'A'  # Помещаем аватара в начальную позицию
    maze[random.randint(0, rows-1)][random.randint(0, cols-1)] = '*'  # Помещаем ключ в случайное место

    save_maze_to_file(maze, 'maze-for-u.txt')
    print("Лабиринт успешно создан и сохранен в файл 'maze-for-u.txt'")

    # лабиринт из файла
    maze_from_file = []
    with open('maze-for-u.txt', 'r') as f:
        for line in f:
            maze_from_file.append(list(line.strip()))

    # Путь от аватара до ключа
    path_to_key = find_path_to_key(maze_from_file)
    if path_to_key:
        print("Найден путь от аватара до ключа:", path_to_key)
    else:
        print("Путь от аватара до ключа не найден.")
