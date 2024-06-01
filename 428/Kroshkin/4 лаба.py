import math

class Radar:
    _instance = None

    def __new__(cls, pos_x=0, pos_y=0, pos_z=0):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.pos_x = pos_x
            cls._instance.pos_y = pos_y
            cls._instance.pos_z = pos_z
        return cls._instance

    def get_position(self):
        return self.pos_x, self.pos_y, self.pos_z

class FlyingObject:
    def __init__(self, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.vel_z = vel_z

    def update_position(self, time):
        self.pos_x += self.vel_x * time
        self.pos_y += self.vel_y * time
        self.pos_z += self.vel_z * time

    def get_position(self):
        return self.pos_x, self.pos_y, self.pos_z

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
        pos_x, pos_y, pos_z = map(float, input(f"Введите координаты (pos_x, pos_y, pos_z) для объекта {i + 1}: ").split())
        vel_x, vel_y, vel_z = map(float, input(f"Введите скорости (vel_x, vel_y, vel_z) для объекта {i + 1}: ").split())
        flying_objects.append(FlyingObject(pos_x, pos_y, pos_z, vel_x, vel_y, vel_z))

    print("\nТекущие сферические координаты объектов относительно радара:")
    radar_x, radar_y, radar_z = radar.get_position()
    for i, obj in enumerate(flying_objects):
        pos_x, pos_y, pos_z = obj.get_position()
        r, azimuth, elevation = cartesian_to_spherical(pos_x, pos_y, pos_z, radar_x, radar_y, radar_z)
        print(f"Объект {i + 1}: r = {r:.2f} м, азимут = {azimuth:.2f} градусов, угол места = {elevation:.2f} градусов")

    time = float(input("\nВведите время в секундах для обновления координат: "))

    print("\nСферические координаты объектов относительно радара через это время:")
    for i, obj in enumerate(flying_objects):
        obj.update_position(time)
        pos_x, pos_y, pos_z = obj.get_position()
        r, azimuth, elevation = cartesian_to_spherical(pos_x, pos_y, pos_z, radar_x, radar_y, radar_z)
        print(f"Объект {i + 1}: r = {r:.2f} м, азимут = {azimuth:.2f} градусов, угол места = {elevation:.2f} градусов")

if __name__ == "__main__":
    main()
