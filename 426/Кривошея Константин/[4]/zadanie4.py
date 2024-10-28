import math
import random

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Radar(metaclass=Singleton):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

def vichislenie_sfer_koord(radar, flying_object, t):
    dx = flying_object.x - radar.x
    dy = flying_object.y - radar.y
    dz = flying_object.z - radar.z

    distance = math.sqrt(dx**2 + dy**2 + dz**2)
    azimuth = math.atan2(dy, dx)
    elevation = math.atan2(dz, math.sqrt(dx**2 + dy**2))

    flying_object.x += flying_object.vx * t
    flying_object.y += flying_object.vy * t
    flying_object.z += flying_object.vz * t

    return distance, azimuth, elevation

def main():
    radar = Radar(0, 0, 0)

    nomer_objecta = int(input("Введите количество объектов: "))

    flying_objects = []
    for i in range(nomer_objecta):
        x = float(input(f"Введите x для объекта {i}: "))
        y = float(input(f"Введите y для объекта {i}: "))
        z = float(input(f"Введите z для объекта {i}: "))
        vx = float(input(f"Введите vx для объекта {i}: "))
        vy = float(input(f"Введите vy для объекта {i}: "))
        vz = float(input(f"Введите vz для объекта {i}: "))

        flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

    print("Текущие сферические координаты объектов:")
    for flying_object in flying_objects:
        distance, azimuth, elevation = vichislenie_sfer_koord(radar, flying_object, 0)
        print(f"Объект: расстояние {distance:.2f} м, азимут {azimuth:.2f}°, угол места {elevation:.2f}°")

    time = float(input("Введите время в секундах: "))

    print(f"Сферические координаты через {time} секунд:")
    for flying_object in flying_objects:
        distance, azimuth, elevation = vichislenie_sfer_koord(radar, flying_object, time)
        print(f"Объект: расстояние {distance:.2f} м, азимут {azimuth:.2f}°, угол места {elevation:.2f}°")

if __name__ == "__main__":
    main()