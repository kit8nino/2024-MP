our_maze = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [2, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]

cells_to_visit = []

x, y = 2, 0

def is_exit(x, y):
    return x > 5

def add_to_visit_list(list_of_neighbours, list_to_visit):
    return list_to_visit.extend(list_of_neighbours)

def is_in_boundaries(x, y, maze):
    return x < 6 and x >= 0 and y < 6 and y >= 0

def is_empty(x, y, maze):
    return maze[x, y] == 0

def is_aviable(x, y, d, maze):
    x_new = x + d[0]
    y_new = y + d[1]
    return is_in_boundaries(x_new, y_new, maze) and is_empty(x_new, y_new, maze)

def neighbours_list(x, y, maze=our_maze):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    neighbours = []
    for d in directions:
        if is_aviable(x, y, d, maze):
            neighbours.append((x + d[0], y + d[1]))
    return neighbours

def choose_cell_to_visit(list_to_visit):

    return list_to_visit.pop(0)


while not is_exit(x, y, maze=our_maze):
    add_to_visit_list(neighbours_list(x, y, maze))

    x, y = choose_cell_to_visit(cells_to_visit)
