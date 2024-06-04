import random
from queue import PriorityQueue # используется для хранения позиций, которые нужно обработать.
''' 
Очередь обрабатывается в порядке приоритета, который определяется с помощью эвристики.
Использование приоритетной очереди позволяет ускорить работу алгоритма, так как позволяет выбирать на каждом шаге наиболее перспективную позицию для обработки.
Благодаря этому алгоритм может быстрее достигать целевой позиции и находить кратчайший путь до нее.
'''
# Функция для чтения лабиринта из файла
def read_maze(filename):
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

# Функция для записи лабиринта в файл
def write_maze(filename, maze, avatar, key, exit):
    with open(filename, 'w') as f:
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (i, j) == avatar:
                    f.write('A')
                elif (i, j) == key:
                    f.write('*')
                elif (i, j) == exit:
                    f.write('E')
                else:
                    f.write(maze[i][j])
            f.write('\n')

def get_random_position(maze):
    # Генерируем случайные координаты внутри лабиринта
    row = random.randint(1, len(maze)-2)
    col = random.randint(1, len(maze[0])-2)
    # Проверяем, не является ли выбранная позиция стеной
    while maze[row][col] == '#':
        row = random.randint(1, len(maze)-2)
        col = random.randint(1, len(maze[0])-2)
    # Возвращаем кортеж с координатами выбранной позиции
    return (row, col)

# Функция get_neighbors озвращает список соседних позиций для заданной позиции в лабиринте.
def get_neighbors(maze, pos):
    row, col = pos
    neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])]

# Функция heuristic использует Манхэттенское расстояние для оценки расстояния между двумя позициями в лабиринте
def heuristic(a, b):
    #Манхэттенское расстояние между двумя точками равно сумме модулей разностей их координат по осям X и Y.
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, start, goal): # Восстанавливает путь от начальной позиции до целевой позиции.
    current = goal
    path = []
    # Идем по словарю came_from, пока не дойдем до начальной позиции
    while current != start:
        path.append(current)
        current = came_from[current]
    # Добавляем начальную позицию в путь и разворачиваем список
    path.append(start)
    path.reverse()
    # Возвращаем список позиций, представляющих путь от начальной позиции до целевой позиции
    return path

# Реализация Жадного алгоритма для поиска пути в лабиринте
def greedy_search(maze, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None
    # Пока очередь не пуста
    while not frontier.empty():
        current = frontier.get()
        # Если достигли целевой позиции, прерываем цикл
        if current == goal:
            break
        # Идем по соседним позициям
        for neighbor in get_neighbors(maze, current):
            # Проверяем, что соседняя позиция не выходит за границы лабиринта и не является стеной
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != '#' and neighbor not in came_from:
                # Вычисляем эвристическую оценку расстояния от соседней позиции до целевой позиции
                priority = heuristic(goal, neighbor)
                # Добавляем соседнюю позицию в очередь с приоритетом, равным ее эвристической оценке расстояния до целевой позиции
                frontier.put(neighbor, priority)
                # Добавляем информацию о том, из какой позиции была достигнута соседняя позиция
                came_from[neighbor] = current
    # Восстанавливаем путь от начальной позиции до целевой позиции           
    path = reconstruct_path(came_from, start, goal)
    return path

# Ищет кратчайший путь от начальной позиции до целевой позиции в лабиринте с помощью алгоритма A*
def a_star_search(maze, start, goal, max_cost):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    # Ищем кратчайший путь от начальной позиции до целевой позиции
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for neighbor in get_neighbors(maze, current):
            new_cost = cost_so_far[current] + 1
            # Проверяем, что соседняя позиция находится в пределах лабиринта, не является стеной, не превышает максимальное расстояние и еще не была посещена
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != '#' and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]) and new_cost <= max_cost:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                frontier.put(neighbor, priority)
                came_from[neighbor] = current
                
    path = reconstruct_path(came_from, start, goal)
    return path

# Генерируем координаты аватара и ключа вне стен
maze = read_maze('maze-for-u.txt')
avatar = get_random_position(maze)
key = get_random_position(maze)
while key == avatar:
    key = get_random_position(maze)
exit = get_random_position(maze)
while exit == avatar or exit == key:
    exit = get_random_position(maze)

# Находим путь от аватара до ключа с помощью жадного алгоритма
path_to_key = greedy_search(maze, avatar, key)

# Находим путь от ключа до выхода с помощью A* алгоритма
max_cost = len(path_to_key) * 2 # Максимальная стоимость пути для A* алгоритма
path_to_exit = a_star_search(maze, key, exit, max_cost)

# Добавляем путь от аватара до ключа в лабиринт
for pos in path_to_key:
    maze[pos[0]][pos[1]] = '.'

# Добавляем путь от ключа до выхода в лабиринт
for pos in path_to_exit:
    maze[pos[0]][pos[1]] = ','

# Выводим лабиринт с аватаром, ключом и выходом, а также найденные пути
write_maze('maze-for-me-done.txt', maze, avatar, key, exit)
print('Лабиринт с аватаром, ключом и выходом, а также найденные пути сохранены в файле maze-with-path.txt')

# Выводим информацию о найденных путях
path_to_key_str = ' -> '.join([str(pos) for pos in path_to_key])
path_to_exit_str = ' -> '.join([str(pos) for pos in path_to_exit])
print('Путь от аватара до ключа:', path_to_key_str)
print('Путь от ключа до выхода:', path_to_exit_str)
