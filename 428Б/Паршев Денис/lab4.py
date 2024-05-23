import numpy as np
import math
import random

class RadarSystem:
    _instance = None
    
    def __new__(cls, x=0, y=0, z=0):
        # Реализация паттерна Singleton:
        if cls._instance is None:
            cls._instance = super(RadarSystem, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
        return cls._instance
    
    def get_position(self):
        # Возвращает текущие координаты радара в виде массива NumPy
        return np.array([self.x, self.y, self.z])
    
class AirborneObject:
    def __init__(self, x, y, z, vx, vy, vz):
        # Инициализация координат и скорости объекта
        self.coordinates = np.array([x, y, z])
        self.speed = np.array([vx, vy, vz])
    
    def move(self, time):
        # Обновление координат объекта на основании времени и скорости
        self.coordinates += self.speed * time
        
class CoordinateTransformation:
    def cartesian_to_spherical(cartesian_coords, radar_coords):
        # Преобразование декартовых координат в сферические координаты
        relative_coords = cartesian_coords - radar_coords
        dx, dy, dz = relative_coords
        radius = np.sqrt(dx**2 + dy**2 + dz**2)
        azimuth_angle = np.degrees(np.arctan2(dy, dx))
        elevation_angle = np.degrees(np.arctan2(dz, np.sqrt(dx**2 + dy**2)))
        return radius, azimuth_angle, elevation_angle
    
# Инициализация объекта радара с координатами (0, 0, 0)
radar = RadarSystem(x=0, y=0, z=0)
# Ввод количества воздушных объектов
num_aircrafts = int(input("Количество летающих объектов: "))
aircrafts = []
for i in range(num_aircrafts):
    # Ввод координат и скорости для каждого объекта
    x, y, z = map(float, input(f"Введите координаты объекта {i+1} (x, y, z): ").split())
    vx, vy, vz = map(float, input(f"Введите компоненты скорости объекта {i+1} (vx, vy, vz): ").split())
    aircrafts.append(AirborneObject(x, y, z, vx, vy, vz))

# Вывод текущих сферических координат объектов относительно радара
print("Текущие сферические координаты объектов относительно радара:")
for i, aircraft in enumerate(aircrafts):
    radius, azimuth_angle, elevation_angle = CoordinateTransformation.cartesian_to_spherical(aircraft.coordinates, radar.get_position())
    print(f"Объект {i+1}: расстояние = {radius:.2f} м, азимут = {azimuth_angle:.2f} град, угол места = {elevation_angle:.2f} град")

# Ввод времени для обновления координат объектов
time_interval = float(input("Введите время в секундах: "))

# Обновление положения объектов на основании введенного времени
for aircraft in aircrafts:
    aircraft.move(time_interval)
    
# Вывод сферических координат объектов после времени time_interval
print(f"Сферические координаты объектов относительно радара через {time_interval} секунд:")
for i, aircraft in enumerate(aircrafts):
    radius, azimuth_angle, elevation_angle = CoordinateTransformation.cartesian_to_spherical(aircraft.coordinates, radar.get_position())
    print(f"Объект {i+1}: расстояние = {radius:.2f} м, азимут = {azimuth_angle:.2f} град, угол места = {elevation_angle:.2f} град")
