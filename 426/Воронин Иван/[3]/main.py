import pathfinder as pf
import math

man = [10, 10]
# man[0] = int(input("Введите начальную координату игрока (x): "))
# man[1] = int(input("Введите начальную координату игрока (y): "))
key = [60, 30]
# key[0] = int(input("Введите начальную координату ключа (x): "))
# key[1] = int(input("Введите начальную координату ключа (y): "))
end = [1, 15]
# end[0] = int(input("Введите начальную координату выхода (x): "))
# end[1] = int(input("Введите начальную координату выхода (y): "))


map_array = []
file = open('maze.txt', 'r')
for line in file:
	map_array.append(list(line.strip('\n')))

man_cords = []
pf.tryToSet(map_array, man[0], man[1], '@', 0, man_cords)

key_cords = []
pf.tryToSet(map_array, key[0], key[1], '*', 0, key_cords)

end_cords = []
pf.tryToSet(map_array, end[0], end[1], '6', 0, end_cords)

print(f"Игрок: {man_cords}, ключ: {key_cords}, выход: {end_cords}")

map_graph = pf.Graph(map_array)


path, fire_front = pf.dextraPathByCoordinate(map_graph, man_cords, key_cords)
for cord in path:
	map_array[cord[1]][cord[0]] = '.'


path, fire_front = pf.dextraPathByCoordinate(map_graph, key_cords, end_cords)
# print(path)
for cord in path:
	map_array[cord[1]][cord[0]] = ','

# Вывод тепловой карты
# pf.heatMap(map_array, map_graph)

# for line in map_array:
# 	for letter in line:
# 		print(letter, end='')
# 	print()

file = open("maze-for-me-done.txt", 'w')
for line in map_array:
	for symbol in line:
		file.write(symbol)
	file.write('\n')
file.close()