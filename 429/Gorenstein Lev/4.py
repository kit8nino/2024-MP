import numpy as np
import math
import random

class Coordinates:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
class Object:
    def __init__(self, coordinates, velocity_x, velocity_y, velocity_z):
        self.coordinates = coordinates
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z
        

class Radar:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.objects = []
        return cls._instance
    
    def add_object(self, obj):
        self.objects.append(obj)
    
    def calc_spher_coords(self, time_sec):
        for obj in self.objects:
            new_x = obj.coordinates.x + obj.velocity_x * time_sec
            new_y = obj.coordinates.y + obj.velocity_y * time_sec
            new_z = obj.coordinates.z + obj.velocity_z * time_sec
            
            distance = np.sqrt(new_x**2 + new_y**2 + new_z**2)
            azimuth = math.degrees(math.atan2(new_y, new_x))
            h = math.degrees(math.asin(new_z / distance))
            
            print(f"Объект: Дистанция = {distance} метров, Азимут = {azimuth} градусов, Угол = {h} градусов")
            
radar = Radar()
ufo1 = Object(Coordinates(random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)), random.randint(-15, 15), random.randint(-15, 15), random.randint(-15, 15))
ufo2 = Object(Coordinates(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)), random.randint(-13, 13), random.randint(-13, 13), random.randint(-13, 13))
radar.add_object(ufo1)
radar.add_object(ufo2)

t = int(input("Время (с): "))
radar.calc_spher_coords(t)