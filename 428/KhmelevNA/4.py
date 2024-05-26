import math
import time

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag, self.z / mag)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

class Radar:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.position = Vector(0, 0, 0)
        return cls._instance
    
    def emit_pulse(self):
        return time.time()
    
    def calculate_spherical_coordinates(self, obj_position):
        diff_vector = obj_position - self.position
        r = diff_vector.magnitude()
        
        azimuth = math.degrees(math.atan2(diff_vector.y, diff_vector.x))
        if azimuth < 0:
            azimuth += 360
        
        elevation = math.degrees(math.asin(diff_vector.z / r))
        
        return r, azimuth, elevation
    
    def get_current_time(self):
        return time.time()
    
    def get_time_difference(self, current_time, previous_time):
        return current_time - previous_time

class FlyingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
    def update_position(self, time_elapsed):
        self.position += self.velocity * time_elapsed
        
    def get_position(self):
        return self.position
    
    def set_position(self, position):
        self.position = position

class Aircraft(FlyingObject):
    pass

class Drone(FlyingObject):
    pass

def main():
    # Создаем радар
    radar = Radar()
    
    # Создаем летающие объекты
    aircraft1 = Aircraft(Vector(1000, 2000, 500), Vector(-50, 100, 0))
    drone1 = Drone(Vector(-500, 1500, 200), Vector(0, -50, -20))
    
    # Выводим текущие сферические координаты объектов относительно радара
    current_time = radar.get_current_time()
    aircraft1_r, aircraft1_azimuth, aircraft1_elevation = radar.calculate_spherical_coordinates(aircraft1.get_position())
    drone1_r, drone1_azimuth, drone1_elevation = radar.calculate_spherical_coordinates(drone1.get_position())
    
    print(f"Aircraft 1: R = {aircraft1_r} m, Azimuth = {aircraft1_azimuth:.2f} deg, Elevation = {aircraft1_elevation:.2f} deg")
    print(f"Drone 1: R = {drone1_r} m, Azimuth = {drone1_azimuth:.2f} deg, Elevation = {drone1_elevation:.2f} deg")
    
    # Запрашиваем время в секундах
    time_elapsed = float(input("Введите время в секундах для прогноза координат: "))
    
    # Обновляем позиции объектов и выводим новые сферические координаты
    aircraft1.update_position(time_elapsed)
    drone1.update_position(time_elapsed)
    
    aircraft1_r, aircraft1_azimuth, aircraft1_elevation = radar.calculate_spherical_coordinates(aircraft1.get_position())
    drone1_r, drone1_azimuth, drone1_elevation = radar.calculate_spherical_coordinates(drone1.get_position())
    
    print(f"\nПрогноз через {time_elapsed} секунд:")
    print(f"Aircraft 1: R = {aircraft1_r} m, Azimuth = {aircraft1_azimuth:.2f} deg, Elevation = {aircraft1_elevation:.2f} deg")
    print(f"Drone 1: R = {drone1_r} m, Azimuth = {drone1_azimuth:.2f} deg, Elevation = {drone1_elevation:.2f} deg")

if __name__ == "__main__":
    main()