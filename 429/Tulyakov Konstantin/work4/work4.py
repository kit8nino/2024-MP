import math

class Radar:
    _instance = None

    @staticmethod
    def get_instance():
        if Radar._instance is None:
            Radar._instance = Radar()
        return Radar._instance

    def __init__(self):
        if Radar._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.x = 0
            self.y = 0
            self.z = 0

    def set_coordinates(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_spherical(self, x, y, z):
        dx = x - self.x
        dy = y - self.y
        dz = z - self.z
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.degrees(math.atan2(dy, dx))
        elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))
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

class RadarSystem:
    def __init__(self):
        self.radar = Radar.get_instance()
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def get_spherical_coordinates(self):
        coords = []
        for obj in self.objects:
            coords.append(self.radar.to_spherical(obj.x, obj.y, obj.z))
        return coords

    def update_positions(self, t):
        for obj in self.objects:
            obj.update_position(t)

def main():
    # Инициализация радара и объектов
    radar_system = RadarSystem()
    radar_system.radar.set_coordinates(0, 0, 0)

    # Добавление летающих объектов
    print("Введите количество объектов: ")
    num_objects = int(input())
    for i in range(num_objects):
        print("Введите координату x: ")
        x = int(input())
        print("Введите координату y: ")
        y = int(input())
        print("Введите координату z: ")
        z = int(input())
        print("Введите скорость vx: ")
        vx = int(input())
        print("Введите скорость vy: ")
        vy = int(input())
        print("Введите скорость vz: ")
        vz = int(input())
        radar_system.add_object(FlyingObject(x, y, z, vx, vy, vz))
        #radar_system.add_object(FlyingObject(1000, 2000, 3000, 100, 175, 100))
        #radar_system.add_object(FlyingObject(4000, 5000, 6000, -50, -100, -150))

    # Текущие сферические координаты объектов
    coords = radar_system.get_spherical_coordinates()
    print("Сферические координаты:")
    for i, (r, azimuth, elevation) in enumerate(coords):
        print(f"Объект {i+1}: r={r:.2f}, azimuth={azimuth:.2f}, elevation={elevation:.2f}")

    # Ввод времени и обновление координат объектов
    t = float(input("Введите время в секундах: "))
    radar_system.update_positions(t)

    # Сферические координаты объектов через заданное время
    new_coords = radar_system.get_spherical_coordinates()
    print("Сферические координаты через время t:")
    for i, (r, azimuth, elevation) in enumerate(new_coords):
        print(f"Объект {i+1}: r={r:.2f}, azimuth={azimuth:.2f}, elevation={elevation:.2f}")

if __name__ == "__main__":
    main()
