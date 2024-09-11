import math


class Radar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = 0
            cls._instance.y = 0
            cls._instance.z = 0
        return cls._instance


class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def get_spherical_coordinates(self):
        radar = Radar()
        dx = self.x - radar.x
        dy = self.y - radar.y
        dz = self.z - radar.z

        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.degrees(math.atan2(dy, dx))
        elevation = math.degrees(math.asin(dz / r))

        return r, azimuth, elevation

# Создание радара и летающих объектов
radar = Radar()
objects = [
    FlyingObject(100, 50, 20, 10, 5, 2),
    FlyingObject(70, -30, 40, -5, 8, 3),
    FlyingObject(70, -45, 60, 5, 1, 3)
]

# Вывод текущих сферических координат объектов относительно радара
for obj in objects:
    r, azimuth, elevation = obj.get_spherical_coordinates()
    print(f"Объект: Расстояние - {r} м, Азимут - {azimuth} градусов, Угол места - {elevation} градусов")

# Ввод времени с клавиатуры
time = float(input("Введите время в секундах: "))

# Вычисление новых координат объектов через заданное время
for obj in objects:
    obj.x += obj.vx * time
    obj.y += obj.vy * time
    obj.z += obj.vz * time

# Вывод новых сферических координат объектов относительно радара
print("\nПосле прошествия времени:")
for obj in objects:
    r, azimuth, elevation = obj.get_spherical_coordinates()
    print(f"Объект: Расстояние - {r} м, Азимут - {azimuth} градусов, Угол места - {elevation} градусов")
