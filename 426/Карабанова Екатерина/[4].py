import math

class Radar:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.x = 0
            cls._instance.y = 0
            cls._instance.z = 0
        return cls._instance
    
    def get_distance(self, obj_x, obj_y, obj_z):
        distance = math.sqrt((obj_x - self.x)**2 + (obj_y - self.y)**2 + (obj_z - self.z)**2)
        return distance
    
class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
    def get_spherical_coordinates(self, radar_x, radar_y, radar_z):
        azimuth = math.atan2(self.y - radar_y, self.x - radar_x) * 180 / math.pi
        elevation = math.atan2(self.z - radar_z, math.sqrt((self.x - radar_x)**2 + (self.y - radar_y)**2)) * 180 / math.pi
        distance = math.sqrt((self.x - radar_x)**2 + (self.y - radar_y)**2 + (self.z - radar_z)**2)
        return azimuth, elevation, distance

# Создаем радар и летающие объекты
radar = Radar()
objects = [FlyingObject(1000, 2000, 500, 10, 20, 5),
           FlyingObject(-500, 3000, 1000, -15, 10, 8)]

# Выводим текущие сферические координаты объектов относительно радара
for obj in objects:
    azimuth, elevation, distance = obj.get_spherical_coordinates(radar.x, radar.y, radar.z)
    print(f"Начальные координаты - Азимут: {azimuth}, Высота: {elevation}, Дистанция: {distance}")

# Вводим время и выводим сферические координаты через это время
time = int(input("Введите время в секундах: "))
for obj in objects:
    obj.x += obj.vx * time
    obj.y += obj.vy * time
    obj.z += obj.vz * time
    azimuth, elevation, distance = obj.get_spherical_coordinates(radar.x, radar.y, radar.z)
    print(f"Новые координаты  - Азимут: {azimuth}, Высота: {elevation}, Дистанция: {distance}")
