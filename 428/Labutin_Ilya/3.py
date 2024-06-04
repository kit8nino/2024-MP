from collections import deque
from heapq import heappop, heappush
def key_place(maze_file,key_pos):
    with open(maze_file,'r+') as file:
        maze=[list(line.strip()) for line in file]
        if (maze[key_pos[0]][key_pos[1]]) != ' ':
            return False
        maze[key_pos[0]][key_pos[1]]='*'
        file.seek(0)
        file.writelines([''.join(row)+'\n' for row in maze])
        file.truncate()
        return True
def read(filename): 
    maze=[]
    with open(filename,'r') as file:
        for line in file:
            row=line.strip()
            maze.append(list(row))
    return maze
def entrance_and_exit(maze):
    rows=len(maze)
    cols=len(maze[0])
    start=None
    end=None
    print("Укажите начальные координаты:")
    while True:
        try:
            start_row=int(input("Строка: "))
            start_col=int(input("Столбец: "))
            if maze[start_row][start_col]==' ':
                start=(start_row, start_col)
                break
            else:
                print("Введите другие координаты")
        except (ValueError, IndexError):
            print("Неправильные координаты")
    for i in range(cols):
        if maze[rows-1][i]==' ':
            end=(rows-1,i)
    return start, end
def greedy_path(maze,start,goal): 
    queue=deque([(start,[])])
    visited=set()
    while queue:
        current,path=queue.popleft()
        if current==goal:
            return path+[current]
        visited.add(current)
        row,col=current
        neighbors=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        neighbors=sorted(neighbors,key=lambda neighbor: abs(neighbor[0]-goal[0])+abs(neighbor[1]-goal[1]),)
        for neighbor in neighbors:
            n_row,n_col = neighbor
            if (0<=n_row<len(maze) and 0<=n_col<len(maze[0]) and maze[n_row][n_col]!="#" and neighbor not in visited):
                queue.append((neighbor,path+[current]))
    return None
def a_search(maze,start,goal,g_weight,h_weight,max_steps):
    def r(node,goal):
        return abs(node[0]-goal[0])+abs(node[1]-goal[1])
    queue = [(r(start, goal),0,start,[])]
    visited=set()
    while queue:
        i,cost,current,path=heappop(queue)
        if current==goal:
            return path+[current]
        visited.add(current)
        row,col=current
        neighbors=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        for neighbor in neighbors:
            n_row,n_col=neighbor
            if (0<=n_row<len(maze) and 0<= n_col<len(maze[0]) and maze[n_row][n_col]!="#"and neighbor not in visited):
                newcost=cost+1
                prior=newcost*g_weight+r(neighbor,goal)*h_weight
                if prior<=max_steps:
                    heappush(queue,(prior,newcost,neighbor,path+[current]))
    return None
def mark(maze,path,symbol): 
    marked_maze=[row.copy() for row in maze]
    for pos in path:
        row,col=pos
        marked_maze[row][col]=symbol
    return marked_maze
data='maze-for-u.txt'
key_pos = input("Введите координаты ключа (строка, столбец): ")
key_pos = tuple(map(int, key_pos.split(',')))
key_is_placed = key_place(data, key_pos)
while not key_is_placed:
    print("Введите другие координаты")
    key_pos = tuple(map(int, input("Введите координаты ключа (строка, столбец): ").split(',')))
    key_is_placed = key_place(data, key_pos)
maze=read(data)
start,end=entrance_and_exit(maze)
greedy_path1=greedy_path(maze,start,key_pos)
a_path=a_search(maze,key_pos,end,g_weight=1,h_weight=1,max_steps=3000)
marked_maze=mark(maze,greedy_path1,".")
if a_path:
    marked_maze=mark(marked_maze,a_path,",")
marked_combined_maze_file="maze-for-me-done.txt" 
with open(marked_combined_maze_file,"w") as file:
    for row in marked_maze:
        file.write("".join(row)+"\n")
print("Файл: maze-for-me-done.txt")