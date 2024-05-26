import math

class Radar:
    _instance = None
    def __new__(cls, сoordinates):
        if not cls._instance:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x, cls._instance.y, cls._instance.z = сoordinates
        return cls._instance

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def spherical_coordinates(self, object):
        
        dx = object.x - self.x
        dy = object.y - self.y
        dz = object.z - self.z
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.atan2(dy, dx) * 180 / math.pi
        elevation = math.atan2(dz, math.sqrt(dx**2 + dy**2)) * 180 / math.pi
        return r, azimuth, elevation


class SkyObject:
   
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def new_position(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t


if __name__ == "__main__":
    # Радар
    radar = Radar(0, 0, 0)

    #  летающие объекты
    objects = []
    for i in range(int(input("Ввод количество объектов: "))):
        x, y, z, vx, vy, vz = map(int, input("Введите координаты и проекции скоростей для объекта {}: ".format(i+1)).split())
        objects.append(SkyObject(x, y, z, vx, vy, vz))

    # Получаем текущие сферические координаты
    for obj in objects:
        r, azimuth, elevation = radar.get_spherical_coordinates(obj)
        print("Текущие сферические координаты объекта {}: r={:.2f} м, azimuth={:.2f} градусов, elevation={:.2f} градусов".format(i+1, r, azimuth, elevation))

    # Получаем сферические координаты через время t
    t = float(input("Ввод время в секундах: "))
    for obj in objects:
        obj.update_position(t)
        r, azimuth, elevation = radar.get_spherical_coordinates(obj)
        print("Сферические координаты объекта {} через {} секунд: r={:.2f} м, azimuth={:.2f} градусов, elevation={:.2f} градусов".format(i+1, t, r, azimuth, elevation))