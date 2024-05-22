import pathfinder as pf
import math


man = [1, 1]
# man[0] = int(input("Введите начальную координату игрока (x): "))
# man[1] = int(input("Введите начальную координату игрока (y): "))
key = [4, 4]
# key[0] = int(input("Введите начальную координату ключа (x): "))
# key[1] = int(input("Введите начальную координату ключа (y): "))

print(f"Игрок: {man}, ключ: {key}")

map_array = []
file = open('maze.test', 'r')
for line in file:
	map_array.append(list(line.strip('\n')))

man_cords = []
pf.tryToSet(map_array, man[0], man[1], '@', 0, man_cords)

key_cords = []
pf.tryToSet(map_array, key[0], key[1], '*', 0, key_cords)

map_graph = pf.Graph(map_array)


path = pf.dextraPathByCoordinate(map_graph, man_cords, key_cords)
for cord in path:
	map_array[cord[1]][cord[0]] = '.'

for line in map_array:
	for letter in line:
		print(letter, end='')
	print()