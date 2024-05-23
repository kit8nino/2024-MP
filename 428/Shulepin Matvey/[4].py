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

    def get_position(self):
        return self.x, self.y, self.z

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def update_position(self, time):
        self.x += self.vx * time
        self.y += self.vy * time
        self.z += self.vz * time

    def get_position(self):
        return self.x, self.y, self.z

def cartesian_to_spherical(x, y, z, radar_x, radar_y, radar_z):
    dx = x - radar_x
    dy = y - radar_y
    dz = z - radar_z
    r = math.sqrt(dx**2 + dy**2 + dz**2)
    azimuth = math.degrees(math.atan2(dy, dx))
    elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))
    return r, azimuth, elevation

def main():
    radar = Radar(0, 0, 0)

    n = int(input("Введите количество летающих объектов: "))
    flying_objects = []

    for i in range(n):
        x, y, z = map(float, input(f"Введите координаты (x, y, z) для объекта {i + 1}: ").split())
        vx, vy, vz = map(float, input(f"Введите скорости (vx, vy, vz) для объекта {i + 1}: ").split())
        flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

    print("\nТекущие сферические координаты объектов относительно радара:")
    radar_x, radar_y, radar_z = radar.get_position()
    for i, obj in enumerate(flying_objects):
        x, y, z = obj.get_position()
        r, azimuth, elevation = cartesian_to_spherical(x, y, z, radar_x, radar_y, radar_z)
        print(f"Объект {i + 1}: r = {r:.2f} м, азимут = {azimuth:.2f} градусов, угол места = {elevation:.2f} градусов")

    time = float(input("\nВведите время в секундах для обновления координат: "))

    print("\nСферические координаты объектов относительно радара через это время:")
    for i, obj in enumerate(flying_objects):
        obj.update_position(time)
        x, y, z = obj.get_position()
        r, azimuth, elevation = cartesian_to_spherical(x, y, z, radar_x, radar_y, radar_z)
        print(f"Объект {i + 1}: r = {r:.2f} м, азимут = {azimuth:.2f} градусов, угол места = {elevation:.2f} градусов")

if __name__ == "__main__":
    main()
