from collections import deque
import heapq
maze = []
with open("maze-for-u.txt") as file:
    for i in file:
        if i.strip():  # проверяем, что строка не пустая
            maze.append(i[:1920])
        
graph = {}

for i in range(1080):
    for j in range(1920):
        if i < len(maze) and maze[i][j] != '#':
            way = []
            if (i-1>=0) and (i-1 < len(maze)) and (maze[i-1][j] !='#'):
                way.append((i-1, j))
            if (j-1>=0) and (maze[i][j-1]!='#'):
                way.append((i, j-1))
            if (i+1 < 1080) and (i+1 < len(maze)) and (maze[i+1][j] != '#'):
                way.append((i+1, j))
            if (j+1 < 1920) and (maze[i][j+1] != '#'):
                way.append((i, j+1))
            graph[(i, j)] = way

start = (0,1)
end = (1079,1917)

def bfs(start,end,graph):
    queue = deque([start])
    visited = {start:None}
    while queue:
        next_node = queue.popleft()
        if next_node == end:
            break
        neighbour_nodes = graph[next_node]
        for neighbour_node in neighbour_nodes:
            if neighbour_node not in visited:
                queue.append(neighbour_node)
                visited[neighbour_node] = next_node
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        if current_node == start:
            break
        current_node = visited[current_node]
    path.reverse()
    return path

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(start, end, graph):
    
    # Инициализация очереди и словаря посещенных узлов
    queue = [(0, start)]
    visited = {start: None}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while queue:
        # Извлекаем узел с наименьшим score из очереди
        _,current_node = heapq.heappop(queue)

        # Если достигли конечной точки, возвращаем путь
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            path.reverse()
            return path

       
        visited[current_node] = None

        for neighbor in graph[current_node]:
            # Вычисляем значение для соседа
            tentative_g_score = g_score[current_node] + 1
            # Если сосед не был посещен или текущий путь короче, обновляем информацию
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                visited[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(queue, (f_score[neighbor], neighbor))

    
    return []


    
path = bfs(start,end,graph)

if path:
    new_maze = [list(row) for row in maze]
    for node in path:
        new_maze[node[0]][node[1]] = ',' 


    with open("bfs-maze-done.txt", "w") as file:
        for row in new_maze:
            file.write(''.join(row) + '\n')
else:
    print("'''path no found")



path = astar((0, 1), (1079, 1917), graph)
if path:
    new_maze = [list(row) for row in maze]
    for node in path:
        new_maze[node[0]][node[1]] = ','

    with open("А-maze-done.txt", "w") as file:
        for row in new_maze:
            file.write(''.join(row) + '\n')
else:
    print("''path not found")
