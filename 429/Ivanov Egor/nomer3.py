import random
import sys

sys.setrecursionlimit(4000)
f=open("maze-for-u.txt", "r")
maze=[[char for char in line] for line in f]

f1=open("maze-for-u2.txt", "r")
#maze=[[char for char in line] for line in f1]


#поиск в глубину
def create_object(maze):
    x=random.randrange(0, len(maze)-1)
    y=random.randrange(0, len(maze[0])-1)
    while maze[x][y]=="#":
        x=(x+1)% (len(maze)-1)
        y=(y+1)% (len(maze[0])-1)
    return [x, y]

def element_of_maze(avatar, maze):
    x, y=avatar
    return maze[x][y]


def chek_this_point(place, maze):
    x, y = place
    maze[x][y]="."


def next_points_from_this_place(place, maze, key):
    x, y=place
    answer=[]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(i)==abs(j):
                continue
            if x+i>=len(maze) or y+j>=len(maze[0]) or x+i<0 or y+j<0:
                continue
            if [x+i, y+j]==key:
                return [[x+i, y+j]]
            if element_of_maze([x+i, y+j], maze)==" " or element_of_maze([x+i, y+j], maze)==",":
                answer+=[[x+i, y+j]]
    return answer
            


def dfs(avatars_place, key_place, maze):
    if avatars_place==key_place:
        return False
    
    if element_of_maze(avatars_place, maze)=="#":
        return True
    
    if element_of_maze(avatars_place, maze)==" ":
        chek_this_point(avatars_place, maze)
        next_points=next_points_from_this_place(avatars_place, maze, key_place)
        #print(avatars_place, next_points)
        for place in next_points:
            if dfs(place, key_place, maze)==False:
                return False


avatar_place=create_object(maze)
key_place=create_object(maze)
# avatar_place=[24, 10]#create_object(maze)
# key_place=[2, 40]#create_object(maze)

print("Аватар: ", avatar_place,"\nКлюч: ", key_place)
answer_maze=dfs(avatar_place, key_place, maze)

#[print(*elem) for elem in maze]
maze[key_place[0]][key_place[1]]="*"
maze[avatar_place[0]][avatar_place[1]]="$"
f = open('maze-for-me-done.txt', 'w')
for i in range(len(maze)):
	for j in range(len(maze[0])):
		f.write(maze[i][j])
f.close()
print("Поиск в глубину выполнен")

# A*

""" """
def exits(maze):
    exits=[]
    n=len(maze)
    for i in range(len(maze[0])-1):
        if maze[0][i]!="#":
            exits+=[[0, i]]

    for i in range(len(maze[-1])-1):
        if maze[-1][i]!="#":
            exits+=[[n-1, i]]

    return exits


def cost(place, avatar_place=avatar_place, maze=maze):
    x, y=place
    x_0, y_0=avatar_place
    x_exit, y_exit=exits(maze)[0]
    g = abs(x - x_0) + abs(y - y_0)
    h = ((x_exit - x) ** 2 + (y_exit - y) ** 2)**0.5
    f = g + h
    return f

def cell_selector(cells_to_visit):
    min_cost_cell = min(cells_to_visit, key=cost_key)
    return min_cost_cell

def cost_key(cell):
    return cell[2]

def way_drawer_a_star(way, maze=maze):
    for px, py in way:
        if maze[px][py]==".":
            maze[px][py]="|"
        else:
            maze[px][py] = ','
    return maze

def add_to_visit_list_a_star(list_of_neighbours, way, visited, way_length, max_way_length, cells_to_visit):
    for nx, ny in list_of_neighbours:
        if (nx, ny) in visited:
            continue

        new_way = way + [(nx, ny)]
        new_cost = cost([nx, ny])
        new_way_length = way_length + 1  

        if new_way_length <= max_way_length: 
            if (nx, ny, new_cost, new_way, new_way_length) not in cells_to_visit:
                cells_to_visit.append([nx, ny, new_cost, new_way, new_way_length])
                
    return cells_to_visit

def is_exit(place, maze):

    return place in exits(maze)

def maze_output(file_name, maze=maze):
    
    with open(file_name, 'w', encoding="utf-8") as file_out_maze:
        
        file_out_maze.write('\n'.join(''.join(row) for row in maze))
    
    print("Поиск А* выполнен")

def a_star(place, maze, max_way_length, avatar_place):
    x_0, y_0=place
    cells_to_visit = [(x_0, y_0, cost(place, avatar_place, maze), [], 0)]
    visited = set()
    while cells_to_visit:
        current_cell = cell_selector(cells_to_visit)
        x, y, _, way, way_length = current_cell

        if is_exit([x, y], maze):
            maze = way_drawer_a_star(way)
            print("Выход найден")
            return True
        cells_to_visit.remove(current_cell)
        visited.add((x, y))

        list_of_neighbours = next_points_from_this_place([x, y], maze, exits(maze)[0])

        cells_to_visit = add_to_visit_list_a_star(list_of_neighbours, way, visited, way_length, max_way_length, cells_to_visit)

    print("Выход не найден")
    return False

f=open("maze-for-u.txt", "r")
maze2=[[char for char in line] for line in f]

f1=open("maze-for-u2.txt", "r")
#maze2=[[char for char in line] for line in f1]

maze2[key_place[0]][key_place[1]]="*"
maze2[avatar_place[0]][avatar_place[1]]="$"

max_way_length=5000
a_star(key_place, maze2, max_way_length, avatar_place)



maze_output('maze_for_me_done.txt', maze)
