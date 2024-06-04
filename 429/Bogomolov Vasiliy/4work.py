import  math as m
import random


class Radar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.position = None  
        return cls._instance

    def set_position(self, position):
        self.position = position

    def get_relative_position(self, fly_object):
        relative_position = fly_object.position + fly_object.velocity * fly_object.time
        relative_position.x -= self.position.x
        relative_position.y -= self.position.y
        relative_position.z -= self.position.z
        return relative_position

class Object:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.time = 0 

    def recalculate_position(self, time):
        self.time = time

    def get_spherical_coordinates(self, radar):
        relative_position = radar.get_relative_position(self)
        return relative_position.decart_to_spherical()

class Parameters:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, coordinate):
        return Parameters(self.x + coordinate.x, self.y + coordinate.y, self.z + coordinate.z)

    def __mul__(self, scalar):
        return Parameters(self.x * scalar, self.y * scalar, self.z * scalar)

    def decart_to_spherical(self):
        r = m.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = m.atan2(self.y, self.x) 
        alfa = m.atan2(self.z, m.sqrt(self.x**2 + self.y**2)) 
        return r, m.degrees(theta), m.degrees(alfa)

def output_current_coordinates(objects,radar):
    num_obj = 0
    for obj in objects:
            r, theta, alfa = obj.get_spherical_coordinates(radar)
            print(f"№{num_obj+1} object r={r:.0f}, theta={theta:.0f} degrees, alfa={alfa:.0f} degrees")
            num_obj+=1
def new_current_coordinates(objects,time):
    for obj in objects:
            obj.recalculate_position(time)
            
radar_position = Parameters(0, 0, 0)
radar = Radar()
radar.set_position(radar_position)
time = 0


num_objects = int(input('Введите количество обьектов: ')) 
range_of_position = 1000 
range_of_velocity = 100 

objects = []
for i in range(num_objects):
        position = Parameters(random.uniform(-range_of_position, range_of_position),
                            random.uniform(-range_of_position, range_of_position),
                            random.uniform(-range_of_position, range_of_position))
        velocity = Parameters(random.uniform(-range_of_velocity, range_of_velocity),
                            random.uniform(-range_of_velocity, range_of_velocity),
                            random.uniform(-range_of_velocity, range_of_velocity))
        objects.append(Object(position, velocity))

print("Начальные координаты обьектов:")
output_current_coordinates(objects,radar)

while True:
    time = float(input("Введите время в секундах(чтобы закончить введите отрицательное число): "))
    if time < 0:
        break;
    print(f"Текущие координаты обьектов после {time:.0f} секунд:")
    new_current_coordinates(objects,time)
    output_current_coordinates(objects,radar)
