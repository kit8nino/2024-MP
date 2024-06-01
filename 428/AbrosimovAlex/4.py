import math

class Radar:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Radar, cls).__new__(cls)
        return cls._instance

    def __init__(self, x, y, z):
        if not hasattr(self, 'initialized'):
            self.x = x
            self.y = y
            self.z = z
            self.initialized = True

    def get_spherical_coordinates(self, obj):
        dx = obj.x - self.x
        dy = obj.y - self.y
        dz = obj.z - self.z
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.atan2(dy, dx) * 180 / math.pi
        elevation = math.atan2(dz, math.sqrt(dx**2 + dy**2)) * 180 / math.pi
        return r, azimuth, elevation

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

def main():
    radar_x, radar_y, radar_z = 0, 0, 0
    radar = Radar(radar_x, radar_y, radar_z)

    n = int(input("Введите количество летающих объектов: "))
    flying_objects = []
    for i in range(n):
        x, y, z, vx, vy, vz = map(float, input(f"Введите координаты и проекции скоростей для объекта {i+1}: ").split())
        flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

    print("Текущие сферические координаты объектов относительно радара:")
    for obj in flying_objects:
        r, azimuth, elevation = radar.get_spherical_coordinates(obj)
        print(f"Объект {flying_objects.index(obj)+1}: r={r:.2f}м, azimuth={azimuth:.2f}град, elevation={elevation:.2f}град")

    while True:
        t = float(input("Введите время в секундах (или 0 для выхода): "))
        if t == 0:
            break
        for obj in flying_objects:
            obj.update_position(t)
        print("Сферические координаты объектов относительно радара через {} секунд:".format(t))
        for obj in flying_objects:
            r, azimuth, elevation = radar.get_spherical_coordinates(obj)
            print(f"Объект {flying_objects.index(obj)+1}: r={r:.2f}м, azimuth={azimuth:.2f}град, elevation={elevation:.2f}град")

if __name__ == "__main__":
    main()