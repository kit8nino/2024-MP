import numpy as np
import random
from math import inf

#исходные данные
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
       [' ',' ',' ',' ','#'],
       [' ','#',' ',' ','#'],
       [' ','#','#',' ',' ']]

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
    return x<maze.shape[0] and x>=0 and y<maze.shape[1] and y>=0

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
        if is_in_boundaries(x_new,y_new,maze):
            if is_empty(x_new,y_new,maze):
                list_of_neighbours.append([x_new,y_new])
    return list_of_neighbours

def mark_the_way(way,maze,mark):
    for el in way:
        maze[el[0]][el[1]]=mark
    return maze

def updated_path(path,next_element,previous_element):
    path[tuple(next_element)]=previous_element
    return path

def path_to_list_using_previous_cells(came_from):
    path=came_from.values()
    list_needed=[]
    [list_needed.append(t) for t in path]
    return list_needed

def is_start(next_cell,start):
    return next_cell[0]==start[0] and next_cell[1]==start[1]

def recall_the_way(start,came_from,way_to_key):
    next_cell=[key_x,key_y]
    while not is_start(next_cell,start):
        pre_cell=came_from[tuple(next_cell)]
        maze[pre_cell[0]][pre_cell[1]]='.'
        way_to_key.append(pre_cell)
        next_cell=pre_cell

def dfs(x,y,key_x,key_y,maze):
    cells_to_visit=[]
    came_from={}
    start=[x,y]
    key=[key_x,key_y]

    came_from[tuple(start)]=None
    cells_to_visit.append((x,y,[]))

    while len(cells_to_visit)>0:
        previous_cell=[x,y]
        x,y,path=cells_to_visit.pop(-1)
        new_cell=[x,y]
        if new_cell not in visited:
            x=new_cell[0]
            y=new_cell[1]
            visited.append(new_cell)
            path.append(new_cell)
            came_from=updated_path(came_from,new_cell,previous_cell)
            
            way_to_key=[]
            
            if is_key(key,x, y):
                recall_the_way(start,came_from,way_to_key)

                maze=mark_the_way(way_to_key,maze,'.')
                maze[key[0]][key[1]]='*'
                start=path.pop(0)
                maze[start[0]][start[1]]='@'
                print('Поиск пути до ключа выполнен!')
                return True

            list_of_neighbours=neighbours(x,y,maze)
            [cells_to_visit.append((cell[0],cell[1],path)) for cell in list_of_neighbours]

    return False

#Вывод
avatar_x,avatar_y=create_object(maze1)
print('start:',avatar_x,avatar_y,'\n')
key_x,key_y=create_object(maze1)
print('key:',key_x,key_y,'\n')
seek_for_key=dfs(avatar_x,avatar_y,key_x,key_y,maze1)


#запись в файл
#with open('maze-done.txt', 'w', encoding="utf-8") as result_maze:
 #       
  #      result_maze.write('\n'.join(''.join(row) for row in maze1))
#print('и записан в файл')

#реализация алгоритма A*
def heuristic(cell1,cell2):
    (x1,y1)=cell1
    (x2,y2)=cell2
    return abs(x2-x1)+abs(y2-y1)

def is_empty_a_star(x,y,maze):
    return maze[x][y]==' ' or maze[x][y]=='*' or maze[x][y]=='.'

def neighbours_a_star(x,y,maze):
    list_of_neighbours=[]
    dirs=directions()
    for d in dirs:
        #print(d)
        x_new=x+d[0]
        y_new=y+d[1]
        if is_in_boundaries(x_new,y_new,maze):
            if is_empty_a_star(x_new,y_new,maze):
                list_of_neighbours.append([x_new,y_new])
    return list_of_neighbours

def step_cost(cell1,cell2):
    return 1

def find_cell_with_min_fn(list_of_cells):
    min_cell=list_of_cells[0]
    for cell in list_of_cells:
        if cell[2]<min_cell[2]:
            min_cell=cell
    return min_cell

def second_el(tup):
    return tup[2]

def sort_by_fn(list_of_cells):
    return list_of_cells.sort(key=second_el)

def find_the_nearest_wayout(x,y,exs):
    b=inf
    ind=0
    for i in range (len(exs)):
        a=abs((x-exs[i][0])**2+(y-exs[i][1])**2)
        if a<b:
            ind=i
    return exs[ind][0],exs[ind][1]

def a_star(x,y,exit_x,exit_y,maze):
    cells_to_visit=[]
    came_from={}
    cost_so_far={}
    start=[x,y]
    exit_cell=[exit_x,exit_y]

    came_from[tuple(start)]=None
    cost_so_far[tuple(start)]=0
    fn=heuristic(exit_cell,start)
    cells_to_visit.append((x,y,fn,[]))
    
    while len(cells_to_visit)>0:
        previous_cell=[x,y]
        x,y,fn,path=cells_to_visit.pop(0)
        new_cell=[x,y]
        visited.append(new_cell)
        path.append(new_cell)
        came_from=came_from=updated_path(came_from,new_cell,previous_cell)
        
        way_out=[]
        
        if is_exit(x,y,maze):
            recall_the_way(start,came_from,way_out)

            maze=mark_the_way(way_out,maze,',')
            print('Поиск пути до выхода тоже выполнен!')
            return True
        
        list_of_neighbours=neighbours_a_star(x,y,maze)
        for neighbour in list_of_neighbours:
            new_cost=cost_so_far[tuple(new_cell)]+step_cost(new_cell,neighbour)
            if tuple(neighbour) not in cost_so_far or new_cost<cost_so_far[tuple(neighbour)]:
                cost_so_far[tuple(neighbour)]=new_cost
                fn=new_cost+heuristic(exit_cell,neighbour)
                cells_to_visit.append((neighbour[0],neighbour[1],fn,path))
                cells_to_visit=sort_by_fn(cells_to_visit)
                
        return False
    
    
#Вывод
avatar_x,avatar_y=create_object(maze1)
print('start:',avatar_x,avatar_y,'\n')
key_x,key_y=create_object(maze1)
print('key:',key_x,key_y,'\n')
seek_for_key=dfs(avatar_x,avatar_y,key_x,key_y,maze1)
exs=exits(maze)
exit_x,exit_y=find_the_nearest_wayout(key_x,key_y,exs)
seek_for_exit=a_star(key_x,key_y,exit_x,exit_y,maze)
        
#запись в файл
with open('maze-done.txt', 'w', encoding="utf-8") as result_maze:
        
        result_maze.write('\n'.join(''.join(row) for row in maze1))
print('и записан в файл')