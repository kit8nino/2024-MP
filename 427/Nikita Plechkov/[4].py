from math import sqrt,degrees,atan2
from random import uniform
class FlyingObject:
    def __init__(self,coords,velocity_components):
        self.x, self.y , self.z = coords
        self.vx,self.vy,self.vz = velocity_components
    def fly(self,time):
        self.x += self.vx * time
        self.y += self.vy * time

class Radar:
    _instance = None 
    def __new__(cls,coords):
        if Radar._instance == None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x, cls._instance.y, cls._instance.z = coords
        return cls._instance
    def get_position(self, obj: FlyingObject):
        res_x = obj.x - self.x
        res_y = obj.y - self.y
        res_z = obj.z - self.z
        return res_x, res_y, res_z
        
    def transformaton_to_spherical_coords(self, obj: FlyingObject):
        res_x, res_y, res_z = self.get_position(obj)
        rad = sqrt(res_x**2+res_y**2+res_z**2)
        phi = degrees(atan2(res_z, sqrt(res_x ** 2 + res_y ** 2)))
        tetta = degrees(atan2(res_y, res_x))
        return rad,phi,tetta

radar =Radar((1,2,3))
number_of_flying_ovjects = int(input("Введите количество объектов: "))
max_coord = 1000
min_coord = -1000
max_speed = 15
flying_obj = [FlyingObject([uniform(min_coord,max_coord),uniform(min_coord,max_coord),uniform(min_coord,max_coord)],[uniform(-max_speed,max_speed),uniform(-max_speed,max_speed),
               uniform(-max_speed,max_speed)])for i in range(number_of_flying_ovjects)]

print("Сферические координаты объектов относительно радара в начальный момент времени: ")
for obj in flying_obj:
    rad, tetta, phi = radar.transformaton_to_spherical_coords(obj)
    print(f"Объект номер {flying_obj.index(obj)} имеет сферические координаты: rad = {rad}, tetta ={tetta}, phi =  {phi}")

time = float(input("Введите время в секундах: "))

print(f"Сферические координаты объектов через {time} секунд относительно радара: ")
for obj in flying_obj:
    obj.fly(time)
    rad, tetta, phi = radar.transformaton_to_spherical_coords(obj)
    print(f"Объект номер {flying_obj.index(obj)} имеет сферические координаты: rad = {rad}, tetta ={tetta}, phi =  {phi}")

    

    
   

