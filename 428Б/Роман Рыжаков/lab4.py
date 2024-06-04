import math
import numpy as np

class Radar:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
        
    def get_spherical_coords(self, obj_x, obj_y, obj_z):
        dx = obj_x - self.x
        dy = obj_y - self.y
        dz = obj_z - self.z
        
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        theta = math.atan2(dy, dx)
        phi = math.acos(dz / r)
        
        return r, theta, phi
        
class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
    def update_position(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t
        
def main():
    
    radar = Radar(0, 0, 0)
    
    
    n = int(input("Введите количество летающих объектов: "))
    objects = []
    for i in range(n):
        x = float(input("Введите x-координату объекта: "))
        y = float(input("Введите y-координату объекта: "))
        z = float(input("Введите z-координату объекта: "))
        vx = float(input("Введите проекцию скорости по x: "))
        vy = float(input("Введите проекцию скорости по y: "))
        vz = float(input("Введите проекцию скорости по z: "))
        obj = FlyingObject(x, y, z, vx, vy, vz)
        objects.append(obj)
        
    
    print("Текущие сферические координаты объектов: \n")
    for obj in objects:
        r, theta, phi = radar.get_spherical_coords(obj.x, obj.y, obj.z)
        print(f"Объект: x={obj.x:.2f}, y={obj.y:.2f}, z={obj.z:.2f} \n")
        print(f"Расстояние: {r:.2f} м, Азимут: {np.degrees(theta):.2f} град, Угол места: {np.degrees(phi):.2f} град \n")
        
    # Обновление положения объектов
    t = float(input("Введите время в секундах:  \n"))
    for obj in objects:
        obj.update_position(t)
        
    
    print(f"Сферические координаты объектов через {t} секунд:  \n")
    for obj in objects:
        r, theta, phi = radar.get_spherical_coords(obj.x, obj.y, obj.z)
        print(f"Объект: x={obj.x:.2f}, y={obj.y:.2f}, z={obj.z:.2f} \n")
        print(f"Расстояние: {r:.2f} м, Азимут: {np.degrees(theta):.2f} град, Угол места: {np.degrees(phi):.2f} град \n")
        
if __name__ == "__main__":
    main()
