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
        self.position = (x, y, z)
    
    def emit_pulse(self):
        print("Радар излучает радиоимпульсы.")

    def calculate_spherical_coordinates(self, x, y, z):
        r = math.sqrt(x**2 + y**2 + z**2)
        azimuth = math.degrees(math.atan2(y, x)) % 360
        elevation = math.degrees(math.atan2(z, math.sqrt(x**2 + y**2)))
        return r, azimuth, elevation

    def detect_objects(self, objects):
        for obj in objects:
            r, azimuth, elevation = self.calculate_spherical_coordinates(
                obj.x - self.position[0],
                obj.y - self.position[1],
                obj.z - self.position[2]
            )
            print(f"Объект {obj.id}: дистанция = {r}, азимут = {azimuth}, угол места = {elevation}")

class FlyingObject:
    count = 0
    
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.id = FlyingObject.count
        FlyingObject.count += 1
    
    def move(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t

# Создание экземпляра радара
radar = Radar(0, 0, 0)

# Создание летающих объектов
objects = [FlyingObject(100, 200, 300, 5, 5, 5) for _ in range(10)]  #  10 реальное количество объектов

# Излучение радиоимпульсов и обнаружение объектов
radar.emit_pulse()
radar.detect_objects(objects)

# Ввод времени и перемещение объектов
t = float(input("Введите время в секундах: "))
for obj in objects:
    obj.move(t)

# Обнаружение объектов после перемещения
radar.detect_objects(objects)