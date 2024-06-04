import numpy as np
import codecs
import random
from collections import deque

def exits(x, y, t):
    stopy = len(t) - 1
    stopx = len(t[0]) - 2
    if ((x == stopx) and ((y + 1) == stopy)) or ((x == len(t) - stopx - 1) and (y == len(t) - stopy)):
        return True
    return False

def coord(textik):
    while True:
        x = random.randint(0, len(textik)-1)
        y = random.randint(0, len(textik[0])-2)
        if textik[x, y] == ' ':
            return x, y

def poisk(start, end, graph):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    if end not in parent:
        return None, None

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, parent

file = codecs.open("maze-for-u.txt", "r", "utf_8_sig")
text = file.readlines()
textt = []
for i in range(len(text)):
    line = []
    for j in range(len(text[i]) - 2):
        simv = text[i][j]
        line += simv
    textt.append(line)
textik = np.array(textt)

coord_avA, coord_avB = coord(textik)
coord_keyA, coord_keyB = coord(textik)

graph = {}
for i in range(textik.shape[0]):
    for j in range(textik.shape[1]):
        if textik[i, j] == ' ':
            neighbors = []
            if j < textik.shape[1] - 1 and textik[i, j + 1] == ' ':
                neighbors.append((i, j + 1))
            if i < textik.shape[0] - 1 and textik[i + 1, j] == ' ':
                neighbors.append((i + 1, j))
            if j > 0 and textik[i, j - 1] == ' ':
                neighbors.append((i, j - 1))
            if i > 0 and textik[i - 1, j] == ' ':
                neighbors.append((i - 1, j))
            graph[(i, j)] = neighbors

path1, parent1 = poisk((coord_avA, coord_avB), (coord_keyA, coord_keyB), graph)
if path1 is None:
    print("Путь от аватара до ключа не найден")
    exit()

path2, parent2 = poisk((coord_keyA, coord_keyB), (599, 798), graph)
if path2 is None:
    print("Путь от ключа до выхода не найден")
    exit()

way1 = path1[1:]  # Исключение начальной точки
way2 = path2[1:]  

rezult = []

for i in range(textik.shape[0]):
    line = []
    for j in range(textik.shape[1]):
        simv = textik[i, j]
        pair = (i, j)
        if pair == (coord_keyA, coord_keyB):
            simv = '*'
        elif pair in way1:
            simv = '.'
        elif pair in way2:
            simv = ','
        line.append(simv)
    rezult.append(line)

with open('maze-for-me-done.txt', "w") as f:
    for lines in rezult:
        stroka = ""
        for index in lines:
            stroka += index
        f.write(stroka + '\n')

print("Пройденный путь:")
print(way1)
print("Найденный путь:")
print(way2)