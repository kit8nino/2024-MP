import math
import numpy as np
import random

class Radar:
    _instance=None
    def __new__(cls,x,y,z):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.x=x
            cls._instance.y=y
            cls._instance.z=z
        return cls._instance
    
    def send_pulse(self,phi,theta):
        pass
    
    def receive_pulse(self,plane):
        return plane.x,plane.y,plane.z
    
    
class Plane:
    def __init__(self,x,y,z,velocity):
        self.x=x
        self.y=y
        self.z=z
        self.vx=velocity[0]
        self.vy=velocity[1]
        self.vz=velocity[2]
    
    def to_SSC(self,obj_x,obj_y,obj_z):
        r=np.sqrt((self.x-obj_x)**2+(self.y-obj_y)**2+(self.z-obj_z)**2)
        phi=np.degrees(math.atan2(self.y-obj_y,self.x-obj_x))
        theta=np.degrees(math.atan2(self.z-obj_z,np.sqrt((self.x-obj_x)**2+(self.y-obj_y)**2)))
        return r,phi,theta
    

My_radar=Radar(0,0,0)


n=int(input('Количество исследуемых самолетов:'))

#исходные данные задаются рандомно
planes=[]
for i in range (n):
    x=random.randint(-10000,10000)
    y=random.randint(-10000,10000)
    z=random.randint(0,10000)
    velocity=[]
    for j in range (2):
        velocity.append(random.randint(-600,600))
    velocity.append(random.randint(-600,200))
    planes.append(Plane(x,y,z,velocity))
    
for plane in planes:
    #plane.x,plane.y,plane.z=plane.relative_position(My_radar)
    r,phi,theta=plane.to_SSC(My_radar.x,My_radar.y,My_radar.z)
    print('\nr={}\n\nphi={}\n\ntheta={}\n\n'.format(r,phi,theta))
    
t=int(input("Время(в секундах):"))

for plane in planes:
    velocity1=velocity.copy()
    x1=plane.x+plane.vx*t
    y1=plane.y+plane.vy*t
    z1=plane.z+plane.vz*t
    planes.remove(plane)
    planes.append(Plane(x1,y1,z1,velocity1))
    
print("--------------------Координаты через {} c-------------------".format(t))
for plane in planes:
    r,phi,theta=plane.to_SSC(My_radar.x,My_radar.y,My_radar.z)
    print('\nr={}\n\nphi={}\n\ntheta={}\n\n'.format(r,phi,theta))
