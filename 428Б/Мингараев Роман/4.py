import math
import random


class SurveillanceSystem:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __init__(self, init_x, init_y, init_z):
        self.init_x = init_x
        self.init_y = init_y
        self.init_z = init_z
        self.speed_of_light = 299792458  # Скорость света в м/с

    def compute_spherical_coordinates(self, target):

        # Вычисляем разности координат
        diff_x = target.init_x - self.init_x
        diff_y = target.init_y - self.init_y
        diff_z = target.init_z - self.init_z

        # Вычисляем расстояние до объекта
        distance = math.sqrt(diff_x**2 + diff_y**2 + diff_z**2)

        # Вычисляем азимут
        azimuth = math.degrees(math.atan2(diff_y, diff_x))
        if azimuth < 0:
            azimuth += 360

        # Вычисляем угол возвышения
        elevation = math.degrees(math.atan2(diff_z, math.sqrt(diff_x**2 + diff_y**2)))

        return distance, azimuth, elevation


class AirborneObject:

    def __init__(self, init_x, init_y, init_z, velocity_x, velocity_y, velocity_z):
        self.init_x = init_x
        self.init_y = init_y
        self.init_z = init_z
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z

    def move(self, time_interval):

        # Обновляем координаты объекта с учетом времени
        self.init_x += self.velocity_x * time_interval
        self.init_y += self.velocity_y * time_interval
        self.init_z += self.velocity_z * time_interval


# Начальные координаты системы наблюдения
system_x = 0
system_y = 0
system_z = 0

# Создаем экземпляр системы наблюдения
surveillance = SurveillanceSystem(system_x, system_y, system_z)

# Количество летательных аппаратов
num_airborne_objects = int(input("Введите число воздушных объектов: "))

# Список для хранения летательных аппаратов
airborne_objects = []
for i in range(num_airborne_objects):
    pos_x = random.randint(-10, 10)
    pos_y = random.randint(-10, 10)
    pos_z = random.randint(-10, 10)
    vel_x = random.randint(-10, 10)
    vel_y = random.randint(-10, 10)
    vel_z = random.randint(-10, 10)
    airborne_objects.append(AirborneObject(pos_x, pos_y, pos_z, vel_x, vel_y, vel_z))

# Отображение начальных сферических координат
print("\nИзначальные сферические координаты объектов:")
for i, obj in enumerate(airborne_objects):
    distance, azimuth, elevation = surveillance.compute_spherical_coordinates(obj)
    print(f"Объект {i+1}: дистанция={distance:.2f} м, азимут={azimuth:.2f} градусов, угол возвышения={elevation:.2f} градусов")

# Интервал времени для перемещения объектов
time_interval = float(input("\nВведите временной промежуток в секундах для обновления координат: "))

# Обновление координат летательных аппаратов
for obj in airborne_objects:
    obj.move(time_interval)

# Отображение сферических координат после интервала времени
print(f"\nСферические координаты объектов спустя {time_interval} секунд:")
for i, obj in enumerate(airborne_objects):
    distance, azimuth, elevation = surveillance.compute_spherical_coordinates(obj)
    print(f"Объект {i+1}: дистанция={distance:.2f} м, азимут={azimuth:.2f} градусов, угол возвышения={elevation:.2f} градусов")
