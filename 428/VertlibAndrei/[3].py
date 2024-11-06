#Координаты старта, ключа, конца маршрута
def getDataFromMaze(maze):
    startX = int(input('Позиция аватара X: ')) #20
    startY = int(input('Позиция аватара Y: ')) #51

    keyX = int(input('Позиция ключа X: ')) #113
    keyY = int(input('Позиция ключа Y: ')) #86
    maze[keyX][keyY] = " "

    start = (startX, startY)
    key = (keyX, keyY)

    for y in range(len(maze[0])):
        if maze[len(maze) - 1][y] == " ":
            end = (len(maze) - 1, y)

    return start, end, key

#Проверка доступных направлений
def pathCheck(maze, curPos):
    sizeY = len(maze[0])
    sizeX = len(maze)
    x, y = curPos
    ways = []

    if (x - 1) >= 0 and maze[x - 1][y] == " ":
        ways.append((x - 1, y))
    if (x + 1) < sizeX and maze[x + 1][y] == " ":
        ways.append((x + 1, y))
    if (y - 1) >= 0 and maze[x][y - 1] == " ":
        ways.append((x, y - 1))
    if (y + 1) < sizeY and maze[x][y + 1] == " ":
        ways.append((x, y + 1))

    return ways

#DFS
def dfs(start, end, maze):
    stack = [start]
    visited = {start}
    paths = {start: []}

    while stack:
        curPos = stack.pop()
        if curPos == end:
            return paths[curPos]
        for neighbor in pathCheck(maze, curPos):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                paths[neighbor] = paths[curPos] + [curPos]

    return None

#А*
def heuristic(cur, end):
    return abs(cur[0] - end[0]) + abs(cur[1] - end[1])

def AStar(start, end, maze):
    openStack = [start]
    closedStack = []
    cameFrom = {}
    gScore = {start: 0}
    fScore = {start: heuristic(start, end)}

    while openStack:
        cur = min(openStack, key = lambda x: fScore[x])
        if cur == end:
            path = [end]
            while cur in cameFrom:
                cur = cameFrom[cur]
                path.append(cur)
            path.reverse()
            return path

        openStack.remove(cur)
        closedStack.append(cur)

        for neighbor in pathCheck(maze, cur):
            if neighbor in closedStack:
                continue
            preGScore = gScore[cur] + 1
            if neighbor not in openStack or preGScore < gScore[neighbor]:
                cameFrom[neighbor] = cur
                gScore[neighbor] = preGScore
                fScore[neighbor] = preGScore + heuristic(neighbor, end)
                if neighbor not in openStack:
                    openStack.append(neighbor)

    return openStack

#Отрисовка маршрута
def drawPath(pathToKey, pathToExit, key):
    for coords in pathToKey:
        x, y = coords
        maze[x][y] = "."

    for coords in pathToExit:
        x, y = coords
        if maze[x][y] == ".":
            maze[x][y] = ";"
        else:
            maze[x][y] = ","

    maze[key[0]][key[1]] = '*'

#main 

#Загрузка лабиринта
with open('maze-for-u.txt', 'r') as file:
    maze = [list(line.strip()) for line in file.readlines()]

start, end, key = getDataFromMaze(maze)

#Решение задачи
pathToKey = dfs(start, key, maze)
pathToExit = AStar(key, end, maze)

#Отрисовка маршрута
drawPath(pathToKey, pathToExit, key)

#Сохранение файла
with open('maze-for-me-done.txt', 'w') as file:
    for line in maze:
        file.write("".join(line) + "\n")