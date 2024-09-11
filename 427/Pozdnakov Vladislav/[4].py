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
            raise Exception("Радар уже существует")
    
    def sphera(self, obj: AirObject, show=True):
        rel_x, rel_y, rel_z = obj.x-self.x, obj.y-self.y, obj.z-self.z
        distance = (rel_x**2 + rel_y**2 + rel_z**2)**0.5
        phi = 360 - math.atan(rel_y / rel_x) / math.pi * 180
        if rel_y < 0:
            phi -= 180
        omega = math.atan(rel_z / (rel_y**2 + rel_x**2)**0.5) / math.pi * 180
        if omega < 0:
            print("Объект не может находится ниже уровня земли! Проверьте координату Z")
            return 0
        if show == True:
            print("Расстояние до объекта равно", distance, "(м)")
            print("Угол в горизонтальной плоскости равен", phi, "(0-360 градусов)")
            print("Угол в вертикальной плоскости", omega, "(0-90 градусов)")
        return distance, phi, omega
        
    @staticmethod
    def get_instance():
        return Radar.__instance
    
radar = Radar((0, 0, 0))

N = int(input("Количество объектов: "))

air_objects = []
for i in range(N):
    print(f"\nОбъект №{i+1}:")
    obj_x = float(input("Координата объекта по X: "))
    obj_y = float(input("Координата объекта по Y: "))
    obj_z = float(input("Координата объекта по Z: "))
    obj_vx = float(input("Проекция скорости по X: "))
    obj_vy = float(input("Проекция скорости по Y: "))
    obj_vz = float(input("Проекция скорости по Z: "))
    coords = (obj_x, obj_y, obj_z)
    speed = (obj_vx, obj_vy, obj_vz)
    obj = AirObject(coords, speed)
    air_objects.append(obj)

for i in range(N):
    print(f"\nОбъект №{i+1}:")
    obj = air_objects[i]
    radar.sphera(obj)
    
    print()
    t = float(input("Интервал времени в секундах: "))
   
    print("Координаты спустя время t:")
    radar.sphera(obj)