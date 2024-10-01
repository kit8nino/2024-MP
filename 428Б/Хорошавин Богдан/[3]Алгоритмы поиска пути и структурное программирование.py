from numpy import copy
import random

def converting_to_an_array(file_name): #функция перобразующая в массив 
    
    with open(file_name , 'r') as f:
        Spicok = [i.rstrip() for i in f]
        
    for i in range(len(Spicok)):
        Spicok[i] = list(Spicok [i])
    
    width, height = len(Spicok[0]), len(Spicok)
        
    return Spicok,width,height

def writing_to_a_file (path, file_name): #Функция записывающая в файл
    
    with open(file_name , 'w') as f:   
        
        for i in Spicok_show:
            
            for j in i:
                f.write(f"{j}")
                
            f.write(f"\n")

def widths_get_visit_vertex(Spicok, queue, visit_the_top): #посещение вершин 
    
    while len(queue) != 0 :
        
        basic_vertex = queue.pop(0)
            
        get_step = make_step( Spicok , basic_vertex, visit_the_top, queue)
        
        queue = get_step[0]
        
        visit_vertex = get_step[1]
        
    return visit_vertex

def distance_calculation(end_coord, now_coord):#оцениваем расстояние, суммируем абсолютные значения разницы между координатами
    
        return abs(end_coord[0] - now_coord[0]) + abs(end_coord[1] - now_coord[1])
    
def Greedy_algoritm (Spicok, start, end, choose_algorithm):
    
    queue = [(0, start)]
    
    visit_the_top ={}
    
    visit_the_top [ start ] = (0, start)
    
    visit_the_top =  Greedy_get_visit_vertex (Spicok, queue, visit_the_top, end, start, choose_algorithm)
    
    path = restore_path (None, visit_the_top, start, end)
  
    return path

def Step_A(Spicok, basic_vertex, visit_the_top, queue, start, end): 
    
    coords_one_step = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ]
    
    for x_step, y_step in coords_one_step:
 
        x, y  = basic_vertex[0] + x_step, basic_vertex[1] + y_step
        
        if 0 <= x < len (Spicok) and 0 <= y < len (Spicok) and Spicok [x][y] != '#':
                
                new_cost = visit_the_top[basic_vertex][0] + 1
                
                if visit_the_top.get((x, y)) == None or new_cost < visit_the_top[(x, y)][0]:
                    
                    grade = new_cost + distance_calculation(start, (x, y)) + distance_calculation(end, (x, y)) #к стоимости добавляем расстояние от конца пути 
                
                    queue.append( (grade, (x, y)) )
                
                    visit_the_top[(x, y)] = (new_cost, basic_vertex)
           
    return visit_the_top, queue


def Step_Greedy(Spicok, basic_vertex, visit_the_top, queue, start): 
    
    coords_one_step = [ ( 0 , -1 ),( 1 , 0 ),( 0 , 1 ),( -1 , 0 ) ] 
    
    for x_step, y_step in coords_one_step:
 
        x, y = basic_vertex[0] + x_step, basic_vertex[1] + y_step
        
        if 0 <= x < len (Spicok) and 0 <= y < len (Spicok) and Spicok[x][y] != '#':
                
                new_cost = visit_the_top[basic_vertex][0] + 1
                
                if visit_the_top.get((x, y)) == None or new_cost < visit_the_top[(x, y)][0]:
                
                    grade = new_cost + distance_calculation(start, (x, y))
                
                    queue.append( (grade, (x, y)) )
                
                    visit_the_top[(x, y)] = (new_cost, basic_vertex)
           
    return visit_the_top, queue


def Greedy_get_visit_vertex (Spicok, queue, visit_the_top, end, start, choose_algorithm):

    while queue:
        
        queue.sort(reverse = True)
        basic_vertex = queue.pop()[1]

        if basic_vertex == end:
            break
            
        if choose_algorithm == 1:
            
            get_step = Step_Greedy(Spicok, basic_vertex, visit_the_top, queue, start)
            visit_the_top = get_step[0]
            queue = get_step[1]
            
        else:  
            get_step = Step_A(Spicok, basic_vertex, visit_the_top, queue, start, end)
            visit_the_top = get_step[0]
            queue = get_step[1]         
        
    return visit_the_top


def restore_path (visit_the_top, grades_visit_the_top , start, end):
    
    path = [] 
    coord = end
    
    # путь восстанавливаем с конца  до начала
    while coord != start:
        
        path.append(coord)
        
        if visit_the_top != None:   
            coord = visit_the_top[coord] # переприсваиваем ключ значением смежной вершины из словаря 
        else:                           
            coord = grades_visit_the_top[coord][1]
                
    path.append(start)    
    path.reverse()
    
    return path
#_______________________________________________________________________________________________________________________

def Draw_Spicok (Spicok, path ,sign):# отрисовка пути
    
    Spicok_show = copy(Spicok) 
    
    for coord in path:
        Spicok_show [coord[0],coord[1]] = sign
        
    return Spicok_show

def get_data (Spicok):
    
    print("\n\t Введите данные")
    x_start = int(input("Координата аватара: "))
    y_start = int(input("Координаты аватара: "))

    start = (x_start , y_start)

    x_key = int(input('Координаты ключа по х : '))
    y_key = int(input('Координаты ключа по у : '))

    Spicok [x_key][y_key] = '*'
    
    start = (x_start , y_start)
    key = ( x_key , y_key )
    
    return start , key
 

    return start,key
 
# ПОЛУЧЕНИЕ НАЧАЛЬНЫХ ДАННЫХ

Spicok,width,height = converting_to_an_array( 'maze-for-u.txt' )

Data = get_data(Spicok)
start = Data[0]
key = Data[1]

end_up = (1,1)
end_lower = (598,798)

if distance_calculation (key, end_up) < distance_calculation (key, end_lower ):
    end = end_up
    print('Ближайший выход - верхний.')
else:
    end = end_lower
    print('Ближайший выход - нижний.')

Greed_alg=1
A_start = 2

# Жадный алгоритм  

path_to_the_key = Greedy_algoritm(Spicok, start, key, Greed_alg)
path_to_the_end = Greedy_algoritm (Spicok, key, end, Greed_alg)

Spicok_show = Draw_Spicok (Spicok,path_to_the_key, "." )

print("\n\tЖадный алгоритм") 
print("Колличество шагов от старта до ключа : ", len(path_to_the_key) )
print("Колличество шагов от старта до выхода :", len(path_to_the_end) + len(path_to_the_key) )

# Алгоритм A*
path_to_the_key = Greedy_algoritm(Spicok, start, key, A_start)
path_to_the_end = Greedy_algoritm(Spicok, key, end, A_start)

print("\n\tA*") 
print("Колличество шагов от старта до ключа : ", len(path_to_the_key) )
print("Колличество шагов от старта до выхода : ", len(path_to_the_end) + len(path_to_the_key) )

# путь от ключа до выхода алгоритмом  A*
Spicok_show = Draw_Spicok (Spicok_show, path_to_the_end, "," )
writing_to_a_file (Spicok_show, 'maze-for-me-done.txt')
