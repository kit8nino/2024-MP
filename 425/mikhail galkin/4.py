import math

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Radar(metaclass=SingletonMeta):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calculate_spherical_coordinates(self, obj):
        dx = obj.x - self.x
        dy = obj.y - self.y
        dz = obj.z - self.z
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.degrees(math.atan2(dy, dx)) % 360
        elevation = math.degrees(math.asin(dz / r))
        return r, azimuth, elevation

    def update_position(self, obj, t):
        obj.x += obj.vx * t
        obj.y += obj.vy * t
        obj.z += obj.vz * t

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

# Создание радара и летающих объектов
radar = Radar(0, 0, 0)
N = int(input("Введите количество летающих объектов: "))
flying_objects = []
for i in range(N):
    x, y, z = map(float, input(f"Введите координаты объекта {i+1}: ").split())
    vx, vy, vz = map(float, input(f"Введите проекции скоростей объекта {i+1}: ").split())
    flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

# Вывод текущих сферических координат
for i, obj in enumerate(flying_objects, 1):
    r, azimuth, elevation = radar.calculate_spherical_coordinates(obj)
    print(f"Текущие сферические координаты объекта {i}: r={r}, azimuth={azimuth}, elevation={elevation}")

# Ввод времени и вывод сферических координат через это время
t = float(input("Введите время в секундах: "))
for i, obj in enumerate(flying_objects, 1):
    radar.update_position(obj, t)
    r, azimuth, elevation = radar.calculate_spherical_coordinates(obj)
    print(f"Сферические координаты объекта {i} через {t} секунд: r={r}, azimuth={azimuth}, elevation={elevation}")
