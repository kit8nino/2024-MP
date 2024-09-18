import math

class Radar:
    __instance = None

    @staticmethod
    def get_instance():
        if Radar.__instance is None:
            Radar()
        return Radar.__instance

    def __init__(self):
        if Radar.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Radar.__instance = self
            self.azimuth = 0
            self.elevation = 0

"""
Класс летающего объекта:
    к-ты по x, к-ты по y, к-ты по z, с-ть по x, с-ть по y, с-ть по z
"""
class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

def convert_to_spherical_coordinates(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    azimuth = math.degrees(math.atan2(y, x))
    elevation = math.degrees(math.asin(z / r))
    return r, azimuth, elevation

def main():
    radar = Radar.get_instance()

    """
    Создатель летунов:
        Добавьте flying_objects.append(FlyingObject(x, y, z, vx, vy, vz)) 
        для создания нового летуна
        либо подкорректируйте имеющиеся значения
    """
    flying_objects = []
    flying_objects.append(FlyingObject(10, 0, 0, 100, 100, 100))
    
    for obj in flying_objects:
        r, azimuth, elevation = convert_to_spherical_coordinates(obj.x, obj.y, obj.z)
        print(f"Летучий объект на (r={r}, азимут={azimuth}, угол места={elevation}) по курсу от радара!.")

    time = int(input("Введите время в секундах: "))

    for obj in flying_objects:
        obj.x += obj.vx * time
        obj.y += obj.vy * time
        obj.z += obj.vz * time

        r, azimuth, elevation = convert_to_spherical_coordinates(obj.x, obj.y, obj.z)
        print(f"Спустя {time} секунд Летучий объект на (r={r}, азимут={azimuth}, угол места={elevation}) по курсу от радара!.")

if __name__ == "__main__":
    main()
