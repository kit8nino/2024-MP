import math
import random

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Radar(metaclass = SingletonMeta):
    def __init__(self):
        self.position = Vector3D(0, 0, 0)

    def track(self, obj):
        return obj.position.offsetByTime(obj.velocity, obj.time).relative_to(self.position)

class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def offsetByTime(self, velocity, time):
        return Vector3D(self.x + velocity.x * time,
                        self.y + velocity.y * time,
                        self.z + velocity.z * time)

    def relative_to(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def toSpherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = math.degrees(math.atan2(self.y, self.x))
        phi = math.degrees(math.atan2(self.z, math.sqrt(self.x**2 + self.y**2)))
        return r, theta, phi

class FlyingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.time = 0

    def updateTick(self, time):
        self.time = time

def generateRandom3Vector(posRange):
    return Vector3D(random.uniform(-posRange, posRange),
                    random.uniform(-posRange, posRange),
                    random.uniform(-posRange, posRange))

def displaySphericalCoordinates(objects, radar):
    for i, obj in enumerate(objects, start=1):
        r, theta, phi = radar.track(obj).toSpherical()
        print(f"Объект {i}: ({r:.0f}, {theta:.0f}°, {phi:.0f}°)")

def main():
    radar = Radar()
    numOfObjects = int(input('Введите количество обьектов: '))
    objects = [FlyingObject(generateRandom3Vector(1000), generateRandom3Vector(100)) for _ in range(numOfObjects)]

    print("Начальные координаты объектов: ")
    displaySphericalCoordinates(objects, radar)

    while True:
        inputTime = float(input("Введите время в секундах('-1' для остановки): "))
        if inputTime < 0:
            break
        for obj in objects:
            obj.updateTick(inputTime)
        print(f"Координаты объектов спустя {inputTime:.0f} секунд: ")
        displaySphericalCoordinates(objects, radar)

if __name__ == "__main__":
    main()