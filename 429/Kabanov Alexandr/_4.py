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
        self.position = (x, y, z)

class FlyingObject:
    def __init__(self, x, y, z, velocity):
        self.position = (x, y, z)
        self.velocity = velocity
        
    def to_spherical(self):
        x, y, z = self.position
        r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        theta = math.atan2(z, math.sqrt(x ** 2 + y ** 2))
        phi = math.atan2(y, x)
        return r, theta, phi

    def move(self, dt):
        x, y, z = self.position
        self.position = (x + self.velocity[0] * dt,
                         y + self.velocity[1] * dt,
                         z + self.velocity[2] * dt)

class Main:
    def __init__(self):
        self.radar = self.get_radar_input()
        self.flying_objects = self.get_objects_input()

    def get_radar_input(self):
        coordinates = input("Введите координаты радара (x y z): ").split()
        return Radar(float(coordinates[0]), float(coordinates[1]), float(coordinates[2]))

    def get_objects_input(self):
        num_objects = int(input("Введите количество объектов: "))
        objects = []
        print("Введите координаты и скорости объектов (x y z vx vy vz):")
        for _ in range(num_objects):
            data = input().split()
            x = float(data[0]) - self.radar.position[0]
            y = float(data[1]) - self.radar.position[1]
            z = float(data[2]) - self.radar.position[2]
            velocity = [float(data[3]), float(data[4]), float(data[5])]
            objects.append(FlyingObject(x, y, z, velocity))
        return objects

    def display_spherical_coordinates(self, obj, i, t):
        r, theta, phi = obj.to_spherical()
        print(f"Объект {i}, t = {t}: r = {r:.2f}, theta = {theta:.2f}, phi = {phi:.2f}")

    def run(self):
        for i, obj in enumerate(self.flying_objects):
            self.display_spherical_coordinates(obj, i, 0)
        time_interval = float(input("Введите время (в секундах): "))
        for i, obj in enumerate(self.flying_objects):
            obj.move(time_interval)
            self.display_spherical_coordinates(obj, i, time_interval)

Main().run()