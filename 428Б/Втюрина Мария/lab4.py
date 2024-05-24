import math
import numpy as np
import random

class Radar:
    def __new__(cls):
        instance=None
        if instance is None:
            instance = super().__new__(cls)
        return instance
    
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
    
    def to_SSC(self):
        r=np.sqrt(self.x**2+self.y**2)
        phi=np.degrees(math.atan2(self.y,self.x))
        theta=np.degrees(math.atan2(self.z,np.sqrt(self.x**2+self.y**2)))
        return r,phi,theta
    
#пусть радар стоит в точке начала отсчета
My_radar=Radar()

n=int(input('Количество исследуемых самолетов:'))

#исходные данные задаются рандомно
planes=[]
for i in range (n):
    x=random.randint(-10,10)
    y=random.randint(-10,10)
    z=random.randint(0,10)
    velocity=[]
    for j in range (3):
        velocity.append(random.randint(-600,600))
    planes.append(Plane(x,y,z,velocity))
    
for plane in planes:
    r,phi,theta=plane.to_SSC()
    print('r={}\n\nphi={}\n\ntheta={}\n\n'.format(r,phi,theta))
    
t=int(input("Время(в секундах):"))

for plane in planes:
    velocity1=velocity.copy()
    x1=plane.x+plane.vx*t
    y1=plane.y+plane.vy*t
    z1=plane.z+plane.vz*t
    planes.remove(plane)
    planes.append(Plane(x1,y1,z1,velocity1))
    
    print("Координаты через время:{} c".format(t))
for plane in planes:
    r,phi,theta=plane.to_SSC()
    print('r={}\nphi={}\n\ntheta={}\n\n'.format(r,phi,theta))
