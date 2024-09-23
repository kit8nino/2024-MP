from queue import PriorityQueue
with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

def dijkstra(maze, start, end):
    #очередь с приоритетом
    queue = PriorityQueue()
    queue.put((0, start))
    distances = {start: 0}
    previous = {}

    while not queue.empty():
        #достаем с наименьшим расстоянием от начала
        current_distance, current_position = queue.get()
        if current_position == end:
            break
        #перебор всех соседних
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_position[0] + dx, current_position[1] + dy
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
                continue
            if maze[x][y] == "#":
                continue
            distance = current_distance + 1

            #если не посещяли/нашли короткий путь
            if (x, y) not in distances or distance < distances[(x, y)]:
                distances[(x, y)] = distance
                previous[(x, y)] = current_position
                priority = distance
                queue.put((priority, (x, y)))
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path

def heuristic(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx * dx + dy * dy) ** 0.5

def a_star(maze, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))
    distances = {start: 0}
    previous = {}

    while not queue.empty():
        current_distance, current_position = queue.get()
        if current_position == goal:
            break
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_position[0] + dx, current_position[1] + dy
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
                continue
            if maze[x][y] == "#":
                continue
            distance = distances[current_position] + 1

            if (x, y) not in distances or distance < distances[(x, y)]:
                distances[(x, y)] = distance
                previous[(x, y)] = current_position
                priority = distance + heuristic(goal, (x, y))
                queue.put((priority, (x, y)))
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return path



for Y in range(len(maze[0])):
    if maze[0][Y] == " ":
        start = (0, Y)
        break
for Y in range(len(maze[0])):
    if maze[len(maze) - 1][Y] == " ":
        end = (len(maze) - 1, Y)
        break

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "*":
            key = (i, j)
            maze[i][j] = " "
            break

ToKey = dijkstra(maze,start,key)
ToExit = a_star(maze,key,end)


for coords in ToKey:
    x, y = coords
    maze[x][y] = "."

for coords in ToExit:
    x, y = coords
    maze[x][y] = ","

maze[key[0]][key[1]]="*"
with open('maze-for-me-done.txt', 'w') as f:
    for line in maze:
        f.write("".join(line) + "\n")