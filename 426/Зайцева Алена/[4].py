import math
import random

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

class Radar(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def spherical_coords(self, point):
        dx = point.x - self.x
        dy = point.y - self.y
        dz = point.z - self.z
        r = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        azimuth = math.atan2(dy, dx) * 180 / math.pi
        if azimuth < 0:
            azimuth += 360
        elevation = math.degrees(math.atan(math.sqrt(dx**2 + dy**2) / dz))
        if dz < 0:
            elevation += 90
        return r, azimuth, elevation

class FlyObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update_position(self, time):
        dx = self.velocity.x * time
        dy = self.velocity.y * time
        dz = self.velocity.z * time
        self.position.x += dx
        self.position.y += dy
        self.position.z += dz

# Создание радара, ввод количества летающих объектов и создание летающих объектов со случайными начальными позициями и скоростями
radar = Radar(0, 0, 0)
num_objects = int(input("Введите количество летающих объектов: "))
fly_objects = []
for _ in range(num_objects):
    position = Point(random.randint(-10000, 10000), random.randint(-10000, 10000), random.randint(0, 10000))
    velocity = Vector(random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100))
    fly_objects.append(FlyObject(position, velocity))

# Вывод декартовых и сферических координат
for obj in fly_objects:
    r, azimuth, elevation = radar.spherical_coords(obj.position)
    print(f"Декартовы координаты: ({obj.position.x}, {obj.position.y}, {obj.position.z})")
    print(f"Сферические координаты: Расстояние: {r:.2f} м, Азимут: {azimuth:.2f}°, Угол места: {elevation:.2f}°")

# Ввод времени с клавиатуры
time_input = float(input("Введите время: "))

# Обновление позиций объектов через заданное время
for obj in fly_objects:
    obj.update_position(time_input)

# Вывод декартовых и сферических координат через заданное время
print(f"\nКоординаты объектов через {time_input} секунд:")
for obj in fly_objects:
    r, azimuth, elevation = radar.spherical_coords(obj.position)
    print(f"Декартовы координаты: ({obj.position.x}, {obj.position.y}, {obj.position.z})")
    print(f"Сферические координаты: Расстояние: {r:.2f} м, Азимут: {azimuth:.2f}°, Угол места: {elevation:.2f}°")
