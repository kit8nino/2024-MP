import math
import random


class Radar:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.speed_of_light = 299792458  

    def spheric_coords(self, object):
 
        dx = object.x - self.x
        dy = object.y - self.y
        dz = object.z - self.z

 
        distance = math.sqrt(dx**2 + dy**2 + dz**2)


        azimuth = math.degrees(math.atan2(dy, dx))
        if azimuth < 0:
            azimuth += 360


        elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))

        return distance, azimuth, elevation


class Flying_Object:

    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def new_coordinat(self, dt):

        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt
        

radar_x = 0
radar_y = 0
radar_z = 0


radar = Radar(radar_x, radar_y, radar_z)


num_objects = int(input("Введите количество летающих объектов: "))


flying_objects = []
for i in range(num_objects):

    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    z = random.randint(-10, 10)
    vx = random.randint(-10, 10)
    vy = random.randint(-10, 10)
    vz = random.randint(-10, 10)
    flying_objects.append(Flying_Object(x, y, z, vx, vy, vz))


print("\nТекущие сферические координаты объектов:")
for i, obj in enumerate(flying_objects):
    distance, azimuth, elevation = radar.spheric_coords(obj)
    print(f"Объект {i+1}: расстояние={distance:.2f} м, азимут={azimuth:.2f} градусов, угол места={elevation:.2f} градусов")


dt = float(input("\nВведите время в секундах: "))


for obj in flying_objects:
    obj.new_coordinat(dt)

print("\nСферические координаты объектов через", dt, "секунд:")
for i, obj in enumerate(flying_objects):
    distance, azimuth, elevation = radar.spheric_coords(obj)
    print(f"Объект {i+1}: расстояние={distance:.2f} м, азимут={azimuth:.2f} градусов, угол места={elevation:.2f} градусов")
        




    


