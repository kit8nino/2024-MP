import math
from typing import List

# Паттерн Singleton для класса Radar
class Radar:
    _instance = None

    def __new__(cls, x=0, y=0, z=0):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
        return cls._instance

    def get_position(self):
        return (self.x, self.y, self.z)

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def get_position(self):
        return (self.x, self.y, self.z)

    def get_velocity(self):
        return (self.vx, self.vy, self.vz)

    def update_position(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    azimuth = math.degrees(math.atan2(y, x))
    elevation = math.degrees(math.atan2(z, math.sqrt(x**2 + y**2)))
    return r, azimuth, elevation

def main():
    # Ввод начальных данных
    radar_position = (0, 0, 0)  # координаты радара
    radar = Radar(*radar_position)
    
    # Ввод количества объектов и их параметров
    N = int(input("Введите количество летающих объектов: "))
    objects = []
    
    for i in range(N):
        while True:
            try:
                x, y, z = map(float, input(f"Введите координаты объекта {i+1} (x y z): ").split())
                vx, vy, vz = map(float, input(f"Введите скорости объекта {i+1} (vx vy vz): ").split())
                objects.append(FlyingObject(x, y, z, vx, vy, vz))
                break
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите корректные значения координат и скоростей.")

    # Вывод текущих сферических координат объектов
    print("Текущие сферические координаты объектов относительно радара:")
    radar_x, radar_y, radar_z = radar.get_position()
    for i, obj in enumerate(objects):
        obj_x, obj_y, obj_z = obj.get_position()
        r, azimuth, elevation = cartesian_to_spherical(obj_x - radar_x, obj_y - radar_y, obj_z - radar_z)
        print(f"Объект {i+1}: r = {r:.2f} м, азимут = {azimuth:.2f}°, угол места = {elevation:.2f}°")

    # Ввод времени и расчет новых координат
    while True:
        try:
            t = float(input("Введите время в секундах: "))
            break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректное значение времени.")

    for obj in objects:
        obj.update_position(t)
    
    # Вывод сферических координат объектов через заданное время
    print(f"Сферические координаты объектов относительно радара через {t} секунд:")
    for i, obj in enumerate(objects):
        obj_x, obj_y, obj_z = obj.get_position()
        r, azimuth, elevation = cartesian_to_spherical(obj_x - radar_x, obj_y - radar_y, obj_z - radar_z)
        print(f"Объект {i+1}: r = {r:.2f} м, азимут = {azimuth:.2f}°, угол места = {elevation:.2f}°")

if __name__ == "__main__":
    main()
