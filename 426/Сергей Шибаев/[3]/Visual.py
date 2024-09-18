from PIL import Image

# Открываем файл с лабиринтом
with open("maze-for-me-done.txt") as f:
    lines = f.readlines()
# Открываем файл с лабиринтом

# Убираем символы переноса строки
lines = [line.strip() for line in lines]

# Определяем ширину и высоту лабиринта
width = len(lines[0])
height = len(lines)

# Определяем размеры пикселей в изображении
pixel_size = 3

# Создаем новое изображение
img = Image.new("RGB", (width*pixel_size, height*pixel_size), "white")

# Определяем цвета для каждого символа
colors = {
    "#": (0, 0, 0),     # черный
    ".": (255, 255, 0), # желтый
    ",": (0, 0, 255),   # синий
    ";": (225, 10, 210) # розовый
}

# Проходимся по каждому символу в лабиринте и устанавливаем соответствующий цвет пикселя
for y in range(height):
    for x in range(width):
        color = colors.get(lines[y][x], (255, 255, 255))
        for i in range(pixel_size):
            for j in range(pixel_size):
                img.putpixel((x*pixel_size+i, y*pixel_size+j), color)

# Сохраняем изображение в файл
img.save("maze.png")
