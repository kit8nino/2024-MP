import math

class FlyObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def moving(self, time):
        self.x += self.vx * time
        self.y += self.vy * time
        self.z += self.vz * time

class Radar:
    _instance = None  

    def __new__(cls, radar_x, radar_y, radar_z):
        if cls._instance is None:  
            cls._instance = super(Radar, cls).__new__(cls)  
            cls._instance.radar_x = radar_x
            cls._instance.radar_y = radar_y
            cls._instance.radar_z = radar_z
        return cls._instance  

    def distance_to_object(self, obj):
        return math.sqrt((obj.x - self.radar_x)**2 + (obj.y - self.radar_y)**2 + (obj.z - self.radar_z)**2)

    def cartesian_to_spherical(self, obj):
        r = self.distance_to_object(obj)
        theta = math.acos((obj.z - self.radar_z) / r)
        phi = math.atan2(obj.y - self.radar_y, obj.x - self.radar_x)
        return r, theta, phi

radar = Radar(0, 0, 0)

num_objects = int(input("Введите количество летающих объектов: "))

objects = []
for i in range(num_objects):
    x, y, z = map(float, input(f"Введите начальные координаты объекта {i+1} (x y z): ").split())
    vx, vy, vz = map(float, input(f"Введите скорость объекта {i+1} (vx vy vz): ").split())
    objects.append(FlyObject(x, y, z, vx, vy, vz))

print("\nТекущие сферические координаты объектов относительно радара:")
for i, obj in enumerate(objects):
    r, theta, phi = radar.cartesian_to_spherical(obj)
    print(f"Объект {i+1}: r={r}, theta={theta}, phi={phi}")

time = float(input("\nВведите время для прогнозирования положения объектов: "))

print("\nСферические координаты объектов через время t:")
for i, obj in enumerate(objects):
    obj.moving(time)
    r, theta, phi = radar.cartesian_to_spherical(obj)
    print(f"Объект {i+1}: r={r}, theta={theta}, phi={phi}")
