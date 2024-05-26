import numpy as np

'''
Ввод лабиринта и расчет его размеров и содержимого
'''
def lab_input():
    y_max = 0
    my_labyrinth = []
    
    with open('maze-for-u.txt') as labyrinth_t:
        for line in labyrinth_t:
            my_labyrinth.append(line.strip('\n'))
    x_max, y_max = len(my_labyrinth[0]), len(my_labyrinth)
    return x_max, y_max, my_labyrinth

#Инициализация
max_x, max_y, my_labyrinth = lab_input() #Максимальные координаты x и y
labyrinth_list = list(my_labyrinth) #Лабиринт в виде списка строк
POSSIBLE_WAYS = ('N', 'S', 'W', 'E') #Возможные направления

def set_start(krd, sign):
    global labyrinth_list
    lab_row = list(labyrinth_list[krd[1]])
    lab_row[krd[0]] = sign
    labyrinth_list[krd[1]] = ''.join(lab_row)
    
def get_start(my_labyrinth, row):
    return [my_labyrinth[row].find(" "), row]

'''
Проверка всяких условий
'''
#Проверка на наличие в лабиринте
def krd_in_lab(my_labyrinth, krd):
    if krd[0] < 0 or krd[0] > len(my_labyrinth[0]) - 1:
        return False
    if krd[1] < 0 or krd[1] > len(my_labyrinth) - 1:
        return False
    return True

#Проверка на выход
def krd_are_exit(krd):
    if krd[1] > len(my_labyrinth) - 2:
        return True
    return False

#проверка на сокровище
def krd_are_loot(krd):
    global loot
    if krd[1] == loot[1] and krd[0] == loot[0]:
        return True
    return False

#Проверка на стенку, запрещает ехать через стену
def road_clean(my_labyrinth, krd):
    if my_labyrinth[krd[1]][krd[0]] == 'o':
        return False
    return True

#функция шага
def step(krd, direction):
    if direction == 'N':
        return step_N(krd)
    elif direction == 'S':
        return step_S(krd)
    elif direction == 'W':
        return step_W(krd)
    elif direction == 'E':
        return step_E(krd)

#Шаг вверх
def step_N(krd):
    print("Вверх")
    return [krd[0], krd[1] - 1]
#Шаг вправо
def step_E(krd):
    print("Вправо")
    return [krd[0] + 1, krd[1]]
#Шаг вниз
def step_S(krd):
    print("Вниз")
    return [krd[0], krd[1] + 1]
#Шаг влево
def step_W(krd):
    print("Влево")
    return [krd[0] - 1, krd[1]]

#условие "ни шагу назад", запрещает ехать назад
def no_wai(direction):
    if direction == 'N':
        return ('N', 'E', 'W')
    if direction == 'S':
        return ('S', 'E', 'W')
    if direction == 'E':
        return ('N', 'E', 'S')
    if direction == 'W':
        return ('N', 'S', 'W')

#Метит дорогу символом 'о'
def create_path(krd):
    global labyrinth_list, road_to_exit
    for node in road_to_exit:
        set_start(krd, 'o')
        krd = step(krd, node)
        
so_long_ways = 0

#Ищем путь
def find_way(my_labyrinth, krd, possible_ways):
    global road_to_exit, current_road, so_long_ways
    
    if krd_are_exit(krd):
        print('Выход')
        print('Нынешняя дорога:', current_road)
        return
    if krd_are_loot(krd):
        print('Дополз до сокровищ. Ищем новую дорогу')
        road_to_exit = current_road.copy()
        return
    if len(current_road) > len(road_to_exit):
        so_long_ways += 1
        return
    
    for direction in possible_ways:
        if road_clean(my_labyrinth, step(krd, direction)):
            current_road.append(direction)
            print('Нынешнее направление:', direction)
            print('Нынешняя дорога:', current_road)
            find_way(my_labyrinth, step(krd, direction),  no_wai(direction))
            current_road.pop()
            return
    
passed_roads = [[-1 for j in range(max_x)] for i in range(max_y)]    

#Ищем выход
def find_exit(loot, end):
    queue = []
    queue.append(loot)
    passed_roads[loot[1]][loot[0]] = 0
    
    while queue:
        node = queue.pop(0)
        for i in [[-1, 0 ], [1, 0], [0, -1], [0, 1]]:
            x = node[0] + i[0]
            y = node[1] + i[1]
            if (x < 0 or x >= max_x or y < 0 or y >= max_y):
                continue
            if (my_labyrinth[y][x] == " " and passed_roads[y][x] == -1):
                passed_roads[y][x] = [node[0], node[1]]
                queue.append([x,y])
    
    x = end[0]
    y = end[1]
    while passed_roads[y][x] != 0:
        set_start([x, y], 'o')
        temp_x = passed_roads[y][x][0]
        temp_y = passed_roads[y][x][1]
        x, y = temp_x, temp_y
        
road_to_exit = []
current_road = []

start_point = get_start(my_labyrinth, 0)
end_point = get_start(my_labyrinth, max_y-1)

print("Старт:", start_point)
print("Конец:", end_point)

#Генерация точки с сокровищем [лутом]
loot = ()

while not (loot and road_clean(my_labyrinth, loot)):
    x = np.random.randint(40, 85)
    y = np.random.randint(90, 190) 
    loot = (abs(x) if abs(x) < max_x - 1 else max_x - 1, abs(y) if abs(y) < max_y - 1 else max_y - 1)
    
set_start(loot, '*')
print("О, лутец на", loot)    

find_way(my_labyrinth, start_point, POSSIBLE_WAYS)
create_path(start_point)

find_exit(loot, end_point)

'''
Вывод в файл
'''

f = open('maze-for-me-done.txt', 'w')
for i in range(len(labyrinth_list)):
    f.write(labyrinth_list[i])
    f.write("\n")
f.close()

print('Кол-во слишком длинных путей: ', so_long_ways)
