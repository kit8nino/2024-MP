import math
import random

class Radar:
    def  __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def Objects(self, objects, time):
        for obj in objects:
            distance, azimuth, elevation = self.cordinate_counting(obj, time)
            print(f"Координаты объекта ({obj.x:.2f}, {obj.y:.2f}, {obj.z:.2f}) со скоростью ({obj.vx:.2f}, {obj.vy:.2f}, {obj.vz:.2f}):")
            print(f"Растояние: {distance:.2f}, Азимут: {azimuth:.2f}, Угол места: {elevation:.2f}")
            print()

    def cordinate_counting(self, obj, time):
        dx = obj.x + obj.vx * time - self.x
        dy = obj.y + obj.vy * time - self.y
        dz = obj.z + obj.vz * time - self.z
        distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        azimuth = math.atan2(dx, dy) * 180 / math.pi
        if azimuth < 0:
            azimuth += 360
        elevation = math.atan2(dz, math.sqrt(dx ** 2 + dy ** 2)) * 180 / math.pi
        
        return distance, azimuth, elevation

class FlyObject:
    def  __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y 
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz


# Генерация координат
radar_x = random.randint(-1000, 1000)
radar_y = random.randint(-1000, 1000)
radar_z = random.randint(-1000, 1000)
radar = Radar(radar_x, radar_y, radar_z)

num_objects = int(input("Введите кол-во объектов:"))
objects = []
for i in range(num_objects):
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    z = random.randint(-1000, 1000)
    vx = random.randint(-100, 100)
    vy = random.randint(-100, 100)
    vz = random.randint(-100, 100)
    objects.append(FlyObject(x, y, z, vx, vy, vz))

time = float(input("Введите время в секундах: "))

# Вывод результатов
print("Изначальное положение объекта:")
radar.Objects(objects, 0)
print(f"Положение объекта после {time} секунд:")
radar.Objects(objects, time)

