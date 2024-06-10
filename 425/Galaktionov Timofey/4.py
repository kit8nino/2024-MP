import numpy as np
from math import sqrt, atan2, degrees, radians, sin, cos, asin

# Паттерн Singleton для класса Radar
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Radar(metaclass=Singleton):
    def __init__(self, x, y, z):
        self.position = np.array([x, y, z])

    def get_spherical_coordinates(self, obj_position):
        relative_position = obj_position - self.position
        r = np.linalg.norm(relative_position)
        azimuth = degrees(atan2(relative_position[1], relative_position[0]))
        elevation = degrees(asin(relative_position[2] / r))
        return r, azimuth, elevation

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.position = np.array([x, y, z])
        self.velocity = np.array([vx, vy, vz])

    def update_position(self, time):
        self.position += self.velocity * time

# Функция для ввода данных о летающих объектах
def input_flying_objects(n):
    objects = []
    for i in range(n):
        print(f"Введите координаты и скорости объекта {i+1}:")
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
        vx = float(input("vx: "))
        vy = float(input("vy: "))
        vz = float(input("vz: "))
        objects.append(FlyingObject(x, y, z, vx, vy, vz))
    return objects

# Основная программа
def main():
    # Ввод координат радара
    radar_x = float(input("Введите координату x радара: "))
    radar_y = float(input("Введите координату y радара: "))
    radar_z = float(input("Введите координату z радара: "))
    radar = Radar(radar_x, radar_y, radar_z)

    # Ввод количества летающих объектов
    n = int(input("Введите количество летающих объектов: "))
    flying_objects = input_flying_objects(n)

    # Вывод текущих сферических координат объектов
    print("Текущие сферические координаты объектов относительно радара:")
    for i, obj in enumerate(flying_objects):
        r, azimuth, elevation = radar.get_spherical_coordinates(obj.position)
        print(f"Объект {i+1}: r = {r:.2f} м, азимут = {azimuth:.2f}°, угол места = {elevation:.2f}°")

    # Ввод времени и обновление координат объектов
    time = float(input("Введите время в секундах: "))
    for obj in flying_objects:
        obj.update_position(time)

    # Вывод сферических координат объектов после времени
    print(f"Сферические координаты объектов относительно радара через {time} секунд:")
    for i, obj in enumerate(flying_objects):
        r, azimuth, elevation = radar.get_spherical_coordinates(obj.position)
        print(f"Объект {i+1}: r = {r:.2f} м, азимут = {azimuth:.2f}°, угол места = {elevation:.2f}°")

if __name__ == "__main__":
    main()
