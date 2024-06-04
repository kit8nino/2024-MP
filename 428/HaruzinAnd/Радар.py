import math
import random
from typing import List

class Radar:
    __instance = None

    @staticmethod
    def get_instance(x=0, y=0, z=0):
        if Radar.__instance is None:
            Radar(x, y, z)
        return Radar.__instance

    def __init__(self, x, y, z):
        if Radar.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.x = x
            self.y = y
            self.z = z
            Radar.__instance = self

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def get_spherical_coordinates(self, radar: Radar):
        dx = self.x - radar.x
        dy = self.y - radar.y
        dz = self.z - radar.z

        r = math.sqrt(dx**2 + dy**2 + dz**2)
        theta = math.degrees(math.atan2(dy, dx)) % 360
        phi = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))
        
        return r, theta, phi

    def update_position(self, time):
        self.x += self.vx * time
        self.y += self.vy * time
        self.z += self.vz * time

def main():
    # Создаем радар (Singleton)
    radar = Radar.get_instance(x=0, y=0, z=0)

    # Вводим количество летающих объектов
    num_objects = int(input("Введите количество летающих объектов: "))
    range_of_position = 1000
    range_of_velocity = 100

    # Создаем объекты
    flying_objects: List[FlyingObject] = []
    for i in range(num_objects):
        x = random.uniform(-range_of_position, range_of_position)
        y = random.uniform(-range_of_position, range_of_position)
        z = random.uniform(-range_of_position, range_of_position)
        vx = random.uniform(-range_of_velocity, range_of_velocity)
        vy = random.uniform(-range_of_velocity, range_of_velocity)
        vz = random.uniform(-range_of_velocity, range_of_velocity)
        flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

    # Выводим текущие сферические координаты объектов относительно радара
    print("\nТекущие сферические координаты объектов относительно радара:")
    for i, obj in enumerate(flying_objects):
        r, theta, phi = obj.get_spherical_coordinates(radar)
        print(f"Объект {i+1}: r={r:.2f}, theta={theta:.2f}, phi={phi:.2f}")

    # Вводим время в секундах
    time = float(input("\nВведите время в секундах: "))

    # Обновляем координаты объектов и выводим новые сферические координаты
    print("\nСферические координаты объектов относительно радара через указанное время:")
    for i, obj in enumerate(flying_objects):
        obj.update_position(time)
        r, theta, phi = obj.get_spherical_coordinates(radar)
        print(f"Объект {i+1}: r={r:.2f}, theta={theta:.2f}, phi={phi:.2f}")

if __name__ == "__main__":
    main()
