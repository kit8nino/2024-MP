from typing import List
import math

class Radar:
    __instance = None

    @staticmethod
    def get_instance():
        if Radar.__instance is None:
            Radar.__instance = Radar()
        return Radar.__instance

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def spherical_coordinates(self, obj):
        dx = obj.x - self.x
        dy = obj.y - self.y
        dz = obj.z - self.z
        range_ = math.sqrt(dx**2 + dy**2 + dz**2)
        elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))
        azimuth = math.degrees(math.atan2(dy, dx))
        return range_, elevation, azimuth

class FlyingObject:
    def __init__(self, x=0, y=0, z=0, vx=0, vy=0, vz=0):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def update_position(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t

# Создание экземпляров классов
radar = Radar.get_instance()
# Создание экземпляров класса FlyingObject
xs = [10, 5, -3]
ys = [2, 7, 4]
zs = [0, 3, -2]

vxs = [1, 2, 0.5]
vys = [-1, 0.5, 2]
vzs = [0, 0, 1]

objects = [FlyingObject(x, y, z, vx, vy, vz) for x, y, z, vx, vy, vz in zip(xs, ys, zs, vxs, vys, vzs)]

# Вычисление текущих сферических координат объектов относительно радара
for obj in objects:
    range_, elevation, azimuth = radar.spherical_coordinates(obj)
    print(f"Объект: {obj.x}, {obj.y}, {obj.z}")
    print(f"Дальность: {range_: .2f} м, Угол места: {elevation: .2f} градусов, Азимут: {azimuth: .2f} градусов")
    print()

# Ввод времени с клавиатуры
t = float(input("Введите время в секундах: "))

# Обновление положения объектов
for obj in objects:
    obj.update_position(t)
# Вычисление новых сферических координат объектов относительно радара
for obj in objects:
    range_, elevation, azimuth = radar.spherical_coordinates(obj)
    print(f"Объект: {obj.x}, {obj.y}, {obj.z}")
    print(f"Дальность: {range_: .2f} м, Угол места: {elevation: .2f} градусов, Азимут: {azimuth: .2f} градусов")
    print()
    # Вывести новые декартовы координаты объектов
for obj in objects:
    print(f"Новые координаты объекта: {obj.x: .2f}, {obj.y: .2f}, {obj.z: .2f}")

