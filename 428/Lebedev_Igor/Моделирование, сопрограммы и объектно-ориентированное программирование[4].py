import math
import random

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Radar(metaclass=SingletonMeta):
    def __init__(self):
        self.position = Vector3D(0, 0, 0)

    def track(self, obj):
        return obj.position.offset_by_time(obj.velocity, obj.time).relative_to(self.position)

class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def offset_by_time(self, velocity, time):
        return Vector3D(self.x + velocity.x * time,
                        self.y + velocity.y * time,
                        self.z + velocity.z * time)

    def relative_to(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def to_spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = math.degrees(math.atan2(self.y, self.x))
        phi = math.degrees(math.atan2(self.z, math.sqrt(self.x**2 + self.y**2)))
        return r, theta, phi

class FlyingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.time = 0

    def update_time(self, time):
        self.time = time

def generate_random_vector3d(range_position, range_velocity):
    return Vector3D(random.uniform(-range_position, range_position),
                    random.uniform(-range_position, range_position),
                    random.uniform(-range_position, range_position))

def display_spherical_coordinates(objects, radar):
    for i, obj in enumerate(objects, start=1):
        r, theta, phi = radar.track(obj).to_spherical()
        print(f"Object {i}: r={r:.0f}, theta={theta:.0f}°, phi={phi:.0f}°")

def main():
    radar = Radar()
    num_objects = int(input('Введите количество обьектов: '))
    objects = [FlyingObject(generate_random_vector3d(1000, 100), generate_random_vector3d(100, 100)) for _ in range(num_objects)]

    print("Initial coordinates of objects:")
    display_spherical_coordinates(objects, radar)

    while True:
        time_input = float(input("Введите время в секундах(чтобы закончить введите отрицательное число): "))
        if time_input < 0:
            break
        for obj in objects:
            obj.update_time(time_input)
        print(f"Coordinates of objects after {time_input:.0f} seconds:")
        display_spherical_coordinates(objects, radar)

if __name__ == "__main__":
    main()