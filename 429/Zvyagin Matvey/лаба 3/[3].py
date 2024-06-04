import heapq

#Читаем файл
maze_file='maze-for-u.txt'
def read(file_name):
    with open(file_name, 'r') as f:
        maze_array = [i.rstrip() for i in f]
    for i in range(len(maze_array)):
        maze_array[i]=list(maze_array[i])
    return maze_array
maze=read(maze_file)
maze_visual=maze.copy()
#Начальные данные
Avatar=(8,15)
print("Avatar coord:",Avatar)
Key=(2,10)
Key_visual=[10,2]
print("Key coord",Key)
exit1_coord=(0,1)
exit2_coord=(599,798)

print(f"Exit coord: exit_1={exit1_coord} exit_2={exit2_coord}",)

#Объявляем функцию поиска в глубину
def dfs(graph, source, end, path = []):
       if len(path)>0:
           if end in path:
               return path
       if source not in path:
           path.append(source)
           if source not in graph:
               return path
           for neighbour in graph[source]:
               path = dfs(graph, neighbour, end, path)
       return path
#Функция переводящая считанный лабиринт в граф
def to_graph(maze):
    ver={}
    for j in range(len(maze[0])):
        for i in range(len(maze)):
            V=[]#    
            if maze[i][j] != "#" and (j-1 >= 0):
                if maze[i][j-1] != "#":
                    V.append((i, j-1))
            if maze[i][j] != "#" and (j+1 < len(maze[0])):
                if maze[i][j+1] != "#":
                    V.append((i, j+1))
            if maze[i][j] != "#" and (i-1 >= 0):
                if maze[i-1][j] != "#":
                    V.append((i-1, j))
            if maze[i][j]!= "#" and (i+1 < len(maze)):
                if maze[i+1][j] != "#":
                    V.append((i+1, j))
            ver[(i, j)]=set(V)
    return ver
#Преобразуем в граф:
ver = to_graph(maze)
visited = dfs(ver, Avatar, Key)

for i in visited:
    if i != Key:
        maze_visual[i[0]][i[1]] = '.'
maze_visual[Avatar[0]][Avatar[1]] = "A"
maze_visual[Key_visual[1]][Key_visual[0]] = "*"
print("Путь от аватара до ключа найден!")
print("Массив вершин В поиске в глубину:", visited)
visited=[]

#Функция для А*
def A_star(graph, start, end):
    
    def check_distance(n):
        x1, y1 = n
        x2, y2 = end
        return abs(x1 - x2) + abs(y1 - y2)
    heap = [(0, start)]
    visited = []
    parent = {}
    g_score = {start: 0}
    h_score = {start: check_distance(start)}
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if current_node == end:
            path = []
            while current_node in parent:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            path.reverse()
            return path
        visited.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor in visited:
                continue
            if (neighbor in graph[current_node]):
                new_cost = h_score[current_node] + 1
            if neighbor not in h_score or new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                h_score[neighbor] = new_cost + check_distance(neighbor)
                parent[neighbor] = current_node
                heapq.heappush(heap, (h_score[neighbor], neighbor))
    return None
visited=A_star(ver, Key, exit1_coord)
print("Выход найден!")

for i in visited:
    if i!=Key:
        maze_visual[i[0]][i[1]] = ','
print("Массив вершин для А*", visited)
#Запись в файл
def save_maze(maze,file_name):
    with open( file_name , 'w') as f:   
        for i in maze:
            for j in i:
                f.write(f"{j}")
            f.write(f"\n")
save_maze(maze_visual, "maze-for-me-done.txt")
print("saved as maze-test-done.txt")