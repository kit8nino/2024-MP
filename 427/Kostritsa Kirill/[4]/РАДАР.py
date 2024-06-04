import math

class AirObject:
    def __init__(self, coords, speed):
        self.x, self.y, self.z = coords
        self.vx, self.vy, self.vz = speed
        
    def motion(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t

class Radar:
    __instance = None

    def __init__(self, coords): 
        if Radar.__instance is None:
            Radar.__instance = self
            self.x, self.y, self.z = coords
        else:
            raise Exception("Экземпляр радара уже существует")
    
    def sphera(self, obj: AirObject, show=True):
        rel_x, rel_y, rel_z = obj.x-self.x, obj.y-self.y, obj.z-self.z
        distance = (rel_x**2 + rel_y**2 + rel_z**2)**0.5
        phi = 360 - math.atan(rel_y / rel_x) / math.pi * 180
        if rel_y < 0:
            phi -= 180
        omega = math.atan(rel_z / (rel_y**2 + rel_x**2)**0.5) / math.pi * 180
        if omega < 0:
            print("Летящий объект не может быть ниже уровня земли! Пересмотрите z-координату")
            return 0
        if show == True:
            print("-> Расстояние до объекта равно (м)", distance)
            print("-> Угол в горизонтальной плоскости (0-360 градусов) равен ", phi)
            print("-> Угол в вертикальной плоскости (0-90 градусов)", omega)
        return distance, phi, omega
        
    @staticmethod
    def get_instance():
        return Radar.__instance
    
radar = Radar((0, 0, 0))

N = int(input("Введите количество объектов: "))

air_objects = []
for i in range(N):
    print(f"\nОбъект №{i+1}:")
    obj_x = float(input("Введите х-координату объекта: "))
    obj_y = float(input("Введите y-координату объекта: "))
    obj_z = float(input("Введите z-координату объекта: "))
    obj_vx = float(input("Введите проекцию скорости по x: "))
    obj_vy = float(input("Введите проекцию скорости по y: "))
    obj_vz = float(input("Введите проекцию скорости по z: "))
    coords = (obj_x, obj_y, obj_z)
    speed = (obj_vx, obj_vy, obj_vz)
    obj = AirObject(coords, speed)
    air_objects.append(obj)

for i in range(N):
    print(f"\nОбъект №{i+1}:")
    obj = air_objects[i]
    radar.sphera(obj)
    
    print()
    t = float(input("Введите интервал времени в секундах: "))
   
    print("Координаты спустя время t:")
    radar.sphera(obj)