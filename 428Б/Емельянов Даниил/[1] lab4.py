import math

class Radar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.coordinates = (0, 0, 0)  # Начальные координаты радара
        return cls._instance

    def set_coordinates(self, x, y, z):
        self.coordinates = (x, y, z)

    def get_coordinates(self):
        return self.coordinates


class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.coordinates = (x, y, z)
        self.velocities = (vx, vy, vz)

    def update_position(self, t):
        x, y, z = self.coordinates
        vx, vy, vz = self.velocities
        x += vx * t
        y += vy * t
        z += vz * t
        self.coordinates = (x, y, z)

    def get_spherical_coordinates(self, radar_coordinates):
        x, y, z = self.coordinates
        radar_x, radar_y, radar_z = radar_coordinates

        dx = x - radar_x
        dy = y - radar_y
        dz = z - radar_z

        r = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        azimuth = math.degrees(math.atan2(dy, dx))
        elevation = math.degrees(math.asin(dz / r))

        return r, azimuth, elevation


# Создание радара
radar = Radar()

# Создание летающих объектов
objects = [
    FlyingObject(100, 200, 300, 10, -5, 8),
    FlyingObject(50, 150, 200, -3, 7, -12)
]

# Вывод текущих координат объектов относительно радара
for obj in objects:
    spherical_coords = obj.get_spherical_coordinates(radar.get_coordinates())
    print(f"Текущие сферические координаты: r = {spherical_coords[0]}, azimuth = {spherical_coords[1]}, elevation = {spherical_coords[2]}")

# Ввод времени с клавиатуры
time = int(input("Введите время в секундах: "))

# Обновление позиций объектов и вывод сферических координат через указанное время
for obj in objects:
    obj.update_position(time)
    spherical_coords = obj.get_spherical_coordinates(radar.get_coordinates())
    print(f"Сферические координаты через время {time} секунд: r = {spherical_coords[0]}, azimuth = {spherical_coords[1]}, elevation = {spherical_coords[2]}")
