import math
import random

class Radar:
    _instance = None

    @staticmethod
    def get_instance():
        if Radar._instance is None:
            Radar()
        return Radar._instance

    def __init__(self):
        if Radar._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.coordinates = (0, 0, 0)
            Radar._instance = self

    def set_coordinates(self, x, y, z):
        self.coordinates = (x, y, z)

    def get_coordinates(self):
        return self.coordinates

    def calculate_spherical_coordinates(self, object_coords):
        dx = object_coords[0] - self.coordinates[0]
        dy = object_coords[1] - self.coordinates[1]
        dz = object_coords[2] - self.coordinates[2]
        
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        
        azimuth = math.degrees(math.atan2(dy, dx))
        if azimuth < 0:
            azimuth += 360
        
        if dz == 0:
            elevation = 0
        else:
            elevation = math.degrees(math.atan(math.sqrt(dx**2 + dy**2) / dz))
        if dz < 0:
            elevation += 90
        return (r, azimuth, elevation)

class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.coordinates = (x, y, z)
        self.velocity = (vx, vy, vz)

    def get_coordinates(self):
        return self.coordinates

    def get_velocity(self):
        return self.velocity

    def update_position(self, time):
        x = self.coordinates[0] + self.velocity[0] * time
        y = self.coordinates[1] + self.velocity[1] * time
        z = self.coordinates[2] + self.velocity[2] * time
        
        # Убедимся, что z не уходит в отрицательные координаты
        if z < 0:
            z = 0
        self.coordinates = (x, y, z)

def main():

    # Инициализация радара
    radar = Radar.get_instance()
    radar.set_coordinates(0, 0, 0)  # Установим координаты радара

    # Инициализация летающих объектов
    num_objects = int(input('Введите количество объектов: '))  # Количество летающих объектов
    max_position = 10000  # Максимальное значение координат
    max_velocity = 200  # Максимальное значение скоростей

    flying_objects = []
    for _ in range(num_objects):
        x = random.uniform(-max_position,max_position)
        y=random.uniform(-max_position,max_position)
        z=random.uniform(0,max_position)
        vx=random.uniform(-max_velocity,max_velocity)
        vy=random.uniform(-max_velocity,max_velocity)
        vz=random.uniform(-max_velocity,max_velocity)
        flying_objects.append(FlyingObject(x,y,z,vx,vy,vz))
    

    # Вывод текущих сферических координат объектов
    print("Текущие сферические координаты объектов:")
    for i, obj in enumerate(flying_objects):
        coords = obj.get_coordinates()
        spherical_coords = radar.calculate_spherical_coordinates(coords)
        print(f"Объект {i+1} в {coords}; сферические координаты {spherical_coords}")

    # Ввод времени и расчет новых позиций
    t = float(input("Введите время в секундах: "))
    print(f"Сферические координаты объектов через {t} секунд:")

    for i, obj in enumerate(flying_objects):
        obj.update_position(t)
        coords = obj.get_coordinates()
        spherical_coords = radar.calculate_spherical_coordinates(coords)
        print(f"Объект {i+1} в {coords}; сферические координаты {spherical_coords}")

if __name__ == "__main__":
    main()
