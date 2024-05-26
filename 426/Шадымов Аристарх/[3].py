import math

start = [2, 2]
key = [5, 5]
exit = [1, 7]



maze = []
file = open('mini-maze.txt', 'r')
for line in file:
	maze.append(list(line.replace('\n', '')))

# Устанавливает стартовую точку вне стены, проверяет область снизу справа и вокруг
x, y = start[0], start[1]
while maze[x][y] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if maze[i][j] == ' ':
				start = [i, j]
	x += 1
	y += 1
start = [x, y]

x, y = key[0], key[1]
while maze[x][y] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if maze[i][j] == ' ':
				start = [i, j]
	x += 1
	y += 1
key = [x, y]

x, y = exit[0], exit[1]
while maze[x][y] != ' ':
	for i in range(x-1, x+1):
		for j in range(y-1, y+1):
			if maze[i][j] == ' ':
				start = [i, j]
	x += 1
	y += 1
exit = [x, y]

print("Начало установлено на", str(start), "ключ на", str(key), "выход на", str(exit))

# Жадный алгоритм


maze[x][y] = '*'