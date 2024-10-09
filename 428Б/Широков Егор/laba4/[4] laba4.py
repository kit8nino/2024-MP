import math

class Radar:
    _instance = None

    def __new__(cls, x=0, y=0, z=0):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
        return cls._instance

    def get_coordinates(self):
        return (self.x, self.y, self.z)

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
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

    def get_relative_position(self, radar):
        radar_x, radar_y, radar_z = radar.get_coordinates()
        relative_x = self.x - radar_x
        relative_y = self.y - radar_y
        relative_z = self.z - radar_z
        return relative_x, relative_y, relative_z

    def get_spherical_coordinates(self, radar):
        rel_x, rel_y, rel_z = self.get_relative_position(radar)
        r = math.sqrt(rel_x**2 + rel_y**2 + rel_z**2)
        theta = math.degrees(math.atan2(rel_y, rel_x))  # азимут
        phi = math.degrees(math.atan2(rel_z, math.sqrt(rel_x**2 + rel_y**2)))  # угол места
        return r, theta, phi

# Реализация основной логики программы
radar = Radar(0, 0, 0)

flying_objects = [
    FlyingObject(100, 200, 300, 10, 5, 1),
    FlyingObject(400, 500, 600, -5, -1, 2),
]

print("Текущие сферические координаты объектов относительно радара:")
for obj in flying_objects:
    r, theta, phi = obj.get_spherical_coordinates(radar)
    print(f"Объект @ (r={r:.2f} м, θ={theta:.2f}°, φ={phi:.2f}°)")

# Ввести время в секундах
t = float(input("\nВведите время в секундах: "))

# Обновить позиции объектов и вывести их новые сферические координаты
print("\nСферические координаты объектов относительно радара через", t, "секунд:")
for obj in flying_objects:
    obj.update_position(t)
    r, theta, phi = obj.get_spherical_coordinates(radar)
    print(f"Объект @ (r={r:.2f} м, θ={theta:.2f}°, φ={phi:.2f}°)")
