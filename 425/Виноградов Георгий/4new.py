import numpy as np

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Radar(metaclass=SingletonMeta):
    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z])

    def calc_spherical_coords(self, obj):
        rel_coords = obj.pos - self.pos
        x, y, z = rel_coords
        r = np.sqrt(x**2 + y**2 + z**2)
        az = np.degrees(np.arctan2(y, x)) % 360
        el = np.degrees(np.arctan2(z, np.sqrt(x**2 + y**2)))
        return r, az, el

    def update_obj_pos(self, obj, t):
        obj.pos += obj.vel * t

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.pos = np.array([x, y, z])
        self.vel = np.array([vx, vy, vz])

# Создаем радар и летающие объекты
radar = Radar(0, 0, 0)
N = int(input("Введите количество летающих объектов: "))
flying_objects = []
for i in range(N):
    x, y, z = map(float, input(f"Введите координаты объекта {i+1}: ").split())
    vx, vy, vz = map(float, input(f"Введите скорости объекта {i+1}: ").split())
    flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

# Выводим текущие сферические координаты
for i, obj in enumerate(flying_objects, 1):
    r, az, el = radar.calc_spherical_coords(obj)
    print(f"Текущие сферические координаты объекта {i}: r={r:.2f}, азимут={az:.2f}, угол места={el:.2f}")

# Обновляем и выводим координаты после времени t
t = float(input("Введите время в секундах: "))
for i, obj in enumerate(flying_objects, 1):
    radar.update_obj_pos(obj, t)
    r, az, el = radar.calc_spherical_coords(obj)
    print(f"Сферические координаты объекта {i} через {t} секунд: r={r:.2f}, азимут={az:.2f}, угол места={el:.2f}")
