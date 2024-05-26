import random
from math import degrees, atan2



class Flying_obj:
    def __init__(self, place=0, speed=0):
        self.place=place
        self.speed=speed

    def set_place(self, place):
        self.place=place

    def set_speed(self, speed):
        self.speed=speed
    
    def get_place_decart_sys(self, time):
        x,y, z=self.place
        vx, vy, vz=self.speed
        x+=vx*time
        y+=vy*time
        z+=vz*time
        return x, y, z
    

class Radar:
    def __init__(self, place=[0, 0, 0]):
        self.place=place

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Radar, cls).__new__(cls)
        return cls.instance

    def set_place(self, place):
        self.place=place

    def get_place_decart_sys(self):
        return self.place

    def get_obj_place_spheric_sys(self, obj, time):
        x_obj, y_obj, z_obj=obj.get_place_decart_sys(time)
        x_radar, y_radar, z_radar = self.place
        x, y, z= x_obj-x_radar, y_obj-y_radar, z_obj-z_radar 
        radius=(x**2+y**2+z**2)*0.5
        phi=(degrees(atan2(y, x))+360)%360
        theta=(degrees(atan2(z, (x**2+y**2)**0.5))+360)%360
        return radius, theta, phi



radar = Radar()
x_radar=random.uniform(0, 5)
y_radar=random.uniform(0, 5)
z_radar=random.uniform(0, 5)
radar.set_place((x_radar, y_radar, z_radar))

number_of_objects=4
flying_objects=[]
for i in range(number_of_objects):
    temp=Flying_obj()
    x=random.choice([random.uniform(30, 15), random.uniform(-30, -15)])
    y=random.choice([random.uniform(30, 15), random.uniform(-30, -15)])
    z=random.uniform(z_radar, 30)
    temp.set_place((x, y, z))
    vx=random.uniform(-30, 30)
    vy=random.uniform(-30, 30)
    vz=random.uniform(0, 30)
    temp.set_speed((vx, vy, vz))
    flying_objects+=[temp]

print("Координаты объектов относительно радара в начале: \n")
for i in range(number_of_objects):
    r, theta, phi=radar.get_obj_place_spheric_sys(flying_objects[i], 0)
    print(" Объект "+str(i+1)+ ":  радиус - " , str(r), ", азимут - " , phi, ", угл места - "  , theta)

time=float(input("\nВведите время: "))
print("Координаты объектов относительно радара в момент времени", time, ": \n")
for i in range(number_of_objects):
    r, theta, phi=radar.get_obj_place_spheric_sys(flying_objects[i], time)
    print(" Объект "+str(i+1)+ ":  радиус - " , str(r), ", азимут - " , phi, ", угл места - "  , theta)