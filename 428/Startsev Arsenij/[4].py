import math
import threading

class Radar:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, x=0, y=0, z=0):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Radar, cls).__new__(cls)
                cls._instance.x = x
                cls._instance.y = y
                cls._instance.z = z
        return cls._instance

    def spherical_coordinates(self, x, y, z): #тут мы преобразуем  декартовы координаты в сферические
        dx = x - self.x
        dy = y - self.y
        dz = z - self.z
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = math.degrees(math.atan2(dy, dx)) % 360
        elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))
        return r, azimuth, elevation

class FlyingObject: #этот класс содержит текущие координаты и скорости объектов
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def current_spherical_coordinates(self, radar): #вычисление текущих сферических координат объекта относительно радара
        return radar.spherical_coordinates(self.x, self.y, self.z)

    def future_spherical_coordinates(self, radar, t): #функция вычисляет координаты объекта через заданное время
        future_x = self.x + self.vx * t
        future_y = self.y + self.vy * t
        future_z = self.z + self.vz * t
        return radar.spherical_coordinates(future_x, future_y, future_z)

def main():
    # Создание радара
    radar = Radar(0,0,0)
    
    # Ввод данных о летающих объектах (координаты по осям x, y, z; проекции скоростей объекта на оси x, y, z)
    flying_objects = [
        FlyingObject(1000, 2000, 3000, 70, -5, 2), #1 объект
        FlyingObject(500, 400, 200, -20, 3, -1), #2 объект
        FlyingObject(250, 100, 1500, -55, 6, 4) #3 объект
        
    ]
    
    # Вывод текущих сферических координат объектов
    print("Текущие сферические координаты объектов:")
    for obj in flying_objects:
        r, azimuth, elevation = obj.current_spherical_coordinates(radar)
        print(f"Объект {obj}: r={r:.2f} м, азимут={azimuth:.2f}°, угол места={elevation:.2f}°")
    
    # Ввод времени и расчет будущих сферических координат
    t = float(input("\nВведите время в секундах: "))
    print("\nСферические координаты объектов через {} секунд:".format(t))
    for obj in flying_objects:
        r, azimuth, elevation = obj.future_spherical_coordinates(radar, t)
        print(f"Объект {obj}: r={r:.2f} м, азимут={azimuth:.2f}°, угол места={elevation:.2f}°")

if __name__ == "__main__":
    main()