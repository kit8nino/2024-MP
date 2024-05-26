import math
import random

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def mul(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def to_spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = math.atan2(self.y, self.x)  # азимут
        phi = math.atan2(self.z, math.sqrt(self.x**2 + self.y**2))  # угол места
        return r, math.degrees(theta), math.degrees(phi)

class Radar:
    def __init__(self, position):
        self.position = position

    def get_relative_position(self, flying_object):
        relative_position = flying_object.position.add(flying_object.velocity.mul(flying_object.time))
        relative_position.x -= self.position.x
        relative_position.y -= self.position.y
        relative_position.z -= self.position.z
        return relative_position

class FlyingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.time = 0  # начальное время

    def update_position(self, time):
        self.time = time

    def get_spherical_coordinates(self, radar):
        relative_position = radar.get_relative_position(self)
        return relative_position.to_spherical()

if __name__ == "__main__":
    # Исходные данные
    radar_position = Vector3D(500, 500, 500)  # Новые начальные координаты радара
    radar = Radar(radar_position)

    num_objects = int(input('Введите количество объектов: '))
    max_position = 10000
    max_velocity = 200

    objects = []
    for _ in range(num_objects):
        position = Vector3D(random.uniform(-max_position, max_position),
                            random.uniform(-max_position, max_position),
                            random.uniform(-max_position, max_position))
        velocity = Vector3D(random.uniform(-max_velocity, max_velocity),
                            random.uniform(-max_velocity, max_velocity),
                            random.uniform(-max_velocity, max_velocity))
        objects.append(FlyingObject(position, velocity))

    print("Начальные координаты объектов:")
    for i, obj in enumerate(objects):
        r, theta, phi = obj.get_spherical_coordinates(radar)
        print(f"Object {i+1}: r={r:.2f}, θ={theta:.2f}°, φ={phi:.2f}°")

    time = float(input("Введите время в секундах: "))

    print(f"Координаты объектов после {time} секунд:")
    for i, obj in enumerate(objects):
        obj.update_position(time)
        r, theta, phi = obj.get_spherical_coordinates(radar)
        print(f"Object {i+1}: r={r:.2f}, θ={theta:.2f}°, φ={phi:.2f}°")
