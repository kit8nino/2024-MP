import numpy as np

class Radar:
    _instance = None

    def __new__(cls, x=0, y=0, z=0):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
        return cls._instance

    def position(self):
        return np.array([self.x, self.y, self.z])

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.position = np.array([x, y, z])
        self.velocity = np.array([vx, vy, vz])

    def update_position(self, t):
        self.position += self.velocity * t

class CoordinateConverter:
    @staticmethod
    def to_spherical(cartesian_coords, radar_coords):
        relative_coords = cartesian_coords - radar_coords
        x, y, z = relative_coords
        r = np.sqrt(x**2 + y**2 + z**2)
        azimuth = np.degrees(np.arctan2(y, x))
        elevation = np.degrees(np.arctan2(z, np.sqrt(x**2 + y**2)))
        return r, azimuth, elevation

# Создание объекта радара
radar = Radar(x=0, y=0, z=0)

# Ввод данных о летающих объектах
num_objects = int(input("Введите количество летающих объектов: "))
objects = []
for i in range(num_objects):
    x, y, z = map(float, input(f"Введите декартовы координаты объекта {i+1} (x, y, z): ").split())
    vx, vy, vz = map(float, input(f"Введите проекции скоростей объекта {i+1} (vx, vy, vz): ").split())
    objects.append(FlyingObject(x, y, z, vx, vy, vz))

# Вывод текущих сферических координат объектов
print("Текущие сферические координаты объектов относительно радара:")
for i, obj in enumerate(objects):
    r, azimuth, elevation = CoordinateConverter.to_spherical(obj.position, radar.position())
    print(f"Объект {i+1}: расстояние = {r:.2f} м, азимут = {azimuth:.2f} град, угол места = {elevation:.2f} град")

# Ввод времени
t = float(input("Введите время в секундах: "))

# Обновление положения объектов
for obj in objects:
    obj.update_position(t)

# Вывод сферических координат объектов после времени t
print(f"Сферические координаты объектов относительно радара через {t} секунд:")
for i, obj in enumerate(objects):
    r, azimuth, elevation = CoordinateConverter.to_spherical(obj.position, radar.position())
    print(f"Объект {i+1}: расстояние = {r:.2f} м, азимут = {azimuth:.2f} град, угол места = {elevation:.2f} град")
