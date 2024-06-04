import math
import threading

class SingletonMeta(type):

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Radar(metaclass=SingletonMeta):
    def __init__(self, x, y, z):
        self.position = (x, y, z)

    def to_spherical(self, x, y, z):
        rx, ry, rz = self.position
        dx, dy, dz = x - rx, y - ry, z - rz
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.degrees(math.atan2(dy, dx)) % 360
        elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))
        return r, azimuth, elevation

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.position = [x, y, z]
        self.velocity = [vx, vy, vz]

    def update_position(self, time):
        self.position[0] += self.velocity[0] * time
        self.position[1] += self.velocity[1] * time
        self.position[2] += self.velocity[2] * time

    def get_spherical_coords(self, radar):
        return radar.to_spherical(*self.position)

# Инициализация радара и летающих объектов
radar = Radar(0, 0, 0)
flying_objects = [
    FlyingObject(1000, 2000, 3000, 100, -100, 50),
    FlyingObject(-1500, 2500, 3500, -50, 75, -25),
]

# Вывод начальных сферических координат
for i, obj in enumerate(flying_objects, start=1):
    r, az, el = obj.get_spherical_coords(radar)
    print(f"Объект {i}: r = {r:.2f} м, азимут = {az:.2f}°, угол места = {el:.2f}°")

# Ввод времени для обновления координат объектов
time_passed = float(input("Введите время в секундах: "))

# Обновление позиций и вывод новых сферических координат
for i, obj in enumerate(flying_objects, start=1):
    obj.update_position(time_passed)
    r, az, el = obj.get_spherical_coords(radar)
    print(f"Объект {i} через {time_passed} сек: r = {r:.2f} м, азимут = {az:.2f}°, угол места = {el:.2f}°")
