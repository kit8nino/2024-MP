import math

class Radar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.objects = []
        return cls._instance

    def add_object(self, obj):
        self.objects.append(obj)

    def get_object_coordinates(self, time):
        coordinates = []
        for obj in self.objects:
           
            x = obj.initial_x + obj.velocity_x * time
            y = obj.initial_y + obj.velocity_y * time
            z = obj.initial_z + obj.velocity_z * time
            rho, phi, theta = cartesian_to_spherical(x, y, z)
            coordinates.append((rho, phi, theta))
        return coordinates

def cartesian_to_spherical(x, y, z):
    rho = math.sqrt(x**2 + y**2 + z**2)
    phi = math.atan2(y, x)
    theta = math.acos(z / rho)
    return rho, phi, theta

class FlyingObject:
    def __init__(self, initial_x, initial_y, initial_z, velocity_x, velocity_y, velocity_z):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.initial_z = initial_z
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z

def main():
    radar = Radar()

    radar_instance = Radar()

    flying_objects = [
        FlyingObject(1000, 1000, 1000, 50, 0, 0),
        FlyingObject(-500, -500, 2000, 0, 40, -10),
        FlyingObject(2000, -2000, 500, -30, 20, 0)
    ]
    for obj in flying_objects:
        radar_instance.add_object(obj)

    current_coordinates = radar_instance.get_object_coordinates(0)
    print("Текущие координаты объектов относительно радара:")
    for idx, coord in enumerate(current_coordinates):
        print(f"Объект {idx+1}: rho={coord[0]}, phi={coord[1]}, theta={coord[2]}")

    time = float(input("Введите время в секундах: "))

    future_coordinates = radar_instance.get_object_coordinates(time)
    print(f"Координаты объектов относительно радара через {time} секунд:")
    for idx, coord in enumerate(future_coordinates):
        print(f"Объект {idx+1}: rho={coord[0]}, phi={coord[1]}, theta={coord[2]}")

if __name__ == "__main__":
    main()