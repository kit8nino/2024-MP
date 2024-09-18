import math
import random

class Radar:
    __instance = None

    def __new__(cls):
        if Radar.__instance is None:
            Radar.__instance = object.__new__(cls)
        return Radar.__instance

    def send_pulse(self, azimuth, elevation):
        # отправка радиоимпульса
        pass

    def receive_pulse(self, object_coordinates):
        # получаем отраженный радиоимпульс
        pass

class Object:
    def __init__(self, coordinates, velocity):
        self.coordinates = coordinates
        self.velocity = velocity

class Coordinates:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        azimuth = math.degrees(math.atan2(self.y, self.x))
        elevation = math.degrees(math.atan2(self.z, math.sqrt(self.x**2 + self.y**2)))
        return r, azimuth, elevation

# Создание радара
radar = Radar()

# Запрос количества объектов
num_objects = int(input("Введите количество объектов: "))

# Создание списка объектов с заполнением данными
objects = []
for _ in range(num_objects):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    z = random.randint(-100, 100)
    vx = random.randint(-10, 10)
    vy = random.randint(-10, 10)
    vz = random.randint(-10, 10)
    objects.append(Object(Coordinates(x, y, z), (vx, vy, vz)))

# Вывод текущих сферических координат объектов
for object in objects:
    r, azimuth, elevation = object.coordinates.to_spherical()
    print("Объект: Расстояние - {}, Азимут - {}, Угол места - {}".format(r, azimuth, elevation))

# Ввод времени с клавиатуры
time = int(input("Введите время в секундах: "))

# Вывод сферических координат объектов через заданное время
for object in objects:
    new_x = object.coordinates.x + object.velocity[0] * time
    new_y = object.coordinates.y + object.velocity[1] * time
    new_z = object.coordinates.z + object.velocity[2] * time
    new_coordinates = Coordinates(new_x, new_y, new_z)
    r, azimuth, elevation = new_coordinates.to_spherical()
    print("Объект через время {}: Расстояние - {}, Азимут - {}, Угол места - {}".format(time, r, azimuth, elevation))
