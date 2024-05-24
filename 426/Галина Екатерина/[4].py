import math
# Иницилизируем радар с заданными координатами x, y, z
class Radar:
    _instance = None

    def __new__(cls, x, y, z, frequency):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
            cls._instance.frequency = frequency
        return cls._instance
# Иницилизируем летающий объект с заданными координатами
class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
# Вычисление расстояния между летающим объектом и радаром
    def calculate_distance_to_radar(self, radar):
        return math.sqrt((self.x - radar.x)**2 + (self.y - radar.y)**2 + (self.z - radar.z)**2)
#Моделирование работы радиолокацонной системы
    def calculate_spherical_coordinates(self, radar):
        distance = self.calculate_distance_to_radar(radar)
        azimuth = math.atan2(self.y - radar.y, self.x - radar.x)
        elevation = math.asin((self.z - radar.z) / distance)
        return math.degrees(azimuth), math.degrees(elevation)

# Создаем радар и летающие объекты N=3
radar = Radar(0, 0, 0, 5e9) 
flying_objects = [
    FlyingObject(1000, 1000, 1000, 10, 10, 10),
    FlyingObject(-500, 2000, 500, -5, 15, 5),
    FlyingObject(200, 900, 1000, 7, 10,7)
]

# Вводим время с клавиатуры
time = float(input("Введите время (в секундах): "))

# Выводим текущие сферические координаты объектов относительно радара через заданное время
for obj in flying_objects:
    obj.x += obj.vx * time
    obj.y += obj.vy * time
    obj.z += obj.vz * time

    azimuth, ygol = obj.calculate_spherical_coordinates(radar)
    print(f"Объект: ({obj.x}, {obj.y}, {obj.z}), Азимут: {azimuth} градусов, Угол места: {ygol} градусов")
