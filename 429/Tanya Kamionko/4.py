# -- coding: cp1251 --
import math

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Radar(metaclass=Singleton):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Object:
    def __init__(self, x, y, z, speeds):
        self.x = x
        self.y = y
        self.z = z
        self.speeds = speeds
        
        self.r = 0.0
        self.theta = 0.0
        self.phi = 0.0

    def get_spherical(self):
        self.r = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.theta = math.atan2(self.z, math.sqrt(self.x ** 2 + self.y ** 2))
        self.phi = math.atan2(self.y, self.x)
        return self.r, self.theta, self.phi

    def update(self, dt, radar):
        self.x += self.speeds[0] * dt
        self.y += self.speeds[1] * dt
        self.z += self.speeds[2] * dt


def input_radar():
    radar_coords = input("Координаты радара (x y z): ").split()
    radar = Radar(float(radar_coords[0]), float(radar_coords[1]), float(radar_coords[2]))
    return radar

def input_objects():
    num = int(input("Количество объектов: "))
    objects = []
    print("Введите координаты и скорости объектов (x y z vx vy vz):")
    for _ in range(num):
        data = input().split()
        x = float(data[0]) - radar.x
        y = float(data[1]) - radar.y
        z = float(data[2]) - radar.z
        speeds = [float(data[3]), float(data[4]), float(data[5])]
        objects += [Object(x, y, z, speeds)]
        
    return objects

def print_spherical_coords(obj, i, t):
    coords = obj.get_spherical()
    print(f"{i}, t = {t}: r = {coords[0]}, theta = {coords[1]}, phi = {coords[2]}")


radar = input_radar()
objects = input_objects()
dt = float(input("Промежуток времени (c): "))

for i in range(len(objects)):
    print_spherical_coords(objects[i], i, 0)
    objects[i].update(dt, radar)
    print_spherical_coords(objects[i], i, dt)
