import numpy as np

class Radar:
    _instance = None

    def __new__(cls, x, y, z):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
        return cls._instance

    def get_spherical_coordinates(self, obj):
        dx = obj.x - self.x
        dy = obj.y - self.y
        dz = obj.z - self.z
        r = np.sqrt(dx**2 + dy**2 + dz**2)
        azimuth = np.arctan2(dy, dx) * 180 / np.pi
        elevation = np.arctan2(dz, np.sqrt(dx**2 + dy**2)) * 180 / np.pi
        return r, azimuth, elevation


class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def update_position(self, time):
        self.x += self.vx * time
        self.y += self.vy * time
        self.z += self.vz * time


def main():
    radar = Radar(0, 0, 0)  # Устанавливаем координаты радара

    num_objects = int(input("Введите количество летающих объектов: "))
    objects = []

    for i in range(num_objects):
        x = float(input(f"Введите x-координату объекта {i + 1}: "))
        y = float(input(f"Введите y-координату объекта {i + 1}: "))
        z = float(input(f"Введите z-координату объекта {i + 1}: "))
        vx = float(input(f"Введите vx проекцию скорости объекта {i + 1}: "))
        vy = float(input(f"Введите vy проекцию скорости объекта {i + 1}: "))
        vz = float(input(f"Введите vz проекцию скорости объекта {i + 1}: "))
        objects.append(FlyingObject(x, y, z, vx, vy, vz))

    print("\nТекущие сферические координаты объектов относительно радара:")
    for i, obj in enumerate(objects):
        r, azimuth, elevation = radar.get_spherical_coordinates(obj)
        print(f"Объект {i + 1}: r = {r:.2f} м, азимут = {azimuth:.2f} градусов, угол места = {elevation:.2f} градусов")

    time = float(input("\nВведите время в секундах: "))
    for obj in objects:
        obj.update_position(time)

    print("\nСферические координаты объектов относительно радара через заданное время:")
    for i, obj in enumerate(objects):
        r, azimuth, elevation = radar.get_spherical_coordinates(obj)
        print(f"Объект {i + 1}: r = {r:.2f} м, азимут = {azimuth:.2f} градусов, угол места = {elevation:.2f} градусов")


if __name__ == "__main__":
    main()