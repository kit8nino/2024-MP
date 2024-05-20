import numpy as np
import random

#исходные данные
filename='C:\\Users\\maria\\Desktop\\Алгоритмы\\maze-for-u.txt'
maze=[]
with open("maze-for-u.txt", encoding="utf-8") as f:
    for line in f:
        maze.append([])
        for char in line:
            if char!='\n':
                maze[-1].append(char)
maze=np.array(maze)

#лабиринт для отладки
maze1=[['#',' ','#',' ','#'],
       ['#',' ','#',' ','#'],
       [' ',' ',' ','#','#'],
       [' ','#',' ',' ','#'],
       [' ','#','#','.',' ']]

maze1=np.array(maze1)
def is_key(key,x,y):
    return x==key[0] and y==key[1]

def is_empty(x,y,maze):
    return maze[x][y]==' ' or maze[x][y]=='*'

def generate_coords(maze):
    a=random.randint(0,maze.shape[0]-1)
    b=random.randint(0,maze.shape[1]-1)
    return a,b

def create_object(maze):
    a=0
    b=0
    while maze[a][b]=="#":
        a,b=generate_coords(maze)
    return a,b


def exits(maze):
    exits=[]
    exit_1=[0]*2
    exit_2=[0]*2
    a=maze.shape[1]
    for i in range (a):
        if maze[0][i]==' ':
            exit_1[1]=i
            exits.append(exit_1)
    for i in range (a):
        if maze[maze.shape[0]-1][i]==' ':
            exit_2[0]=maze.shape[0]-1
            exit_2[1]=i
            exits.append(exit_2)
    return exits

#РЕАЛИЗАЦИЯ ПОИСКА В ГЛУБИНУ
visited=[]
def directions():
    return [[0,1],[1,0],[0,-1],[-1,0]]

def is_in_boundaries(x,y,maze):
    return x<=maze.shape[0] and x>=0 and y<=maze.shape[1] and y>=0

def is_exit(x,y,maze):
    exits_list=exits(maze)
    #print(exits(maze))
    check=False
    for ex in exits_list:
        if x==ex[0] and y==ex[1]:
            check= True
        else:
            check= False
    return check

    
def neighbours(x,y,maze):
    list_of_neighbours=[]
    dirs=directions()
    for d in dirs:
        #print(d)
        x_new=x+d[0]
        y_new=y+d[1]

        if is_empty(x_new,y_new,maze) and is_in_boundaries(x_new,y_new,maze):
            list_of_neighbours.append([x_new,y_new])
    return list_of_neighbours

def mark_the_way(way,maze):
    for el in way:
        maze[el[0]][el[1]]='^'
    return maze

def updated_path(path,next_element,previous_element):
    path[tuple(next_element)]=previous_element
    return path

def path_to_list_using_previous_cells(came_from):
    path=came_from.values()
    list_needed=[]
    [list_needed.append(t) for t in path]
    return list_needed

def dfs(x,y,key_x,key_y,maze):

    cells_to_visit=[]
    came_from={}
    start=[x,y]
    key=[key_x,key_y]

    came_from[tuple(start)]=None
    cells_to_visit.append(start)

    while len(cells_to_visit)>0:
        previous_cell=[x,y]
        new_cell=cells_to_visit.pop(-1)
        
        if new_cell not in visited:
            x=new_cell[0]
            y=new_cell[1]
            visited.append(new_cell)
            came_from=updated_path(came_from,new_cell,previous_cell)

            if is_key(key,x, y):
                maze[x][y] = '*'
                way_to_key=path_to_list_using_previous_cells(came_from)
                maze=mark_the_way(way_to_key,maze)
                print('Поиск пути до ключа выполнен!')
                return True

            list_of_neighbours=neighbours(x,y,maze)
            [cells_to_visit.append(cell) for cell in list_of_neighbours]
    return False

#Вывод
avatar_x,avatar_y=create_object(maze)
key_x,key_y=create_object(maze)

way_to_key=dfs(avatar_x,avatar_y,key_x,key_y,maze1)


#запись в файл
with open('maze-done.txt', 'w', encoding="utf-8") as result_maze:
        
        result_maze.write('\n'.join(''.join(row) for row in maze1))
print('и записан в файл')
