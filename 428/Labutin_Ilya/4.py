import math
import random

def spherical(x,y,z,rx,ry,rz):
    dx=x-rx
    dy=y-ry
    dz=z-rz
    radius=math.sqrt(dx**2+dy**2+dz**2)
    phi=math.degrees(math.atan2(dy,dx))
    fortheta=math.sqrt(dx**2+dy**2)
    theta=math.degrees(math.atan2(dz,fortheta))
    if theta<0:
        theta=0
    return radius,phi,theta

class Radar:
    _instance=None
    def __new__(cls,x=0,y=0,z=0):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.x=x
            cls._instance.y=y
            cls._instance.z=z
        return cls._instance
    def position(self):
        return self.x,self.y,self.z
class FlyingObj:
    def __init__(self,x,y,z,vx,vy,vz):
        self.x=x
        self.y=z
        self.z=z
        self.vx=vx
        self.vy=vy
        self.vz=vz
    def new_position(self,t):
        self.x=self.x+self.vx*t
        self.y=self.y+self.vy*t
        self.z=self.z+self.vz*t
    def position(self):
        return self.x,self.y,self.z
if __name__=="__main__":
    Radar=Radar(0,0,0)
    flyingobj=[]
    n=int(input("Введите количество объектов:"))
    max_xyz=1000
    max_vxvyvz=10
    for i in range(n):
       x=random.uniform(-max_xyz, max_xyz)
       y=random.uniform(-max_xyz, max_xyz)
       z=random.uniform(0, max_xyz)
       vx=random.uniform(-max_vxvyvz,max_vxvyvz)
       vy=random.uniform(-max_vxvyvz,max_vxvyvz)
       vz=random.uniform(-max_vxvyvz,max_vxvyvz)
       flyingobj.append(FlyingObj(x, y, z, vx, vy, vz))
    print("В сферических координатах относительно радара:")
    radarx,radary,radarz=Radar.position()
    i=0
    for objects in flyingobj:
        x,y,z=objects.position()
        radius,phi,theta=spherical(x, y, z, radarx, radary, radarz)
        print(f"Объект {i + 1}: r = {radius:.2f} м, азимут = {phi:.2f}°, угол места = {theta:.2f}°")
        i+=1
    t=int(input("\nВведите время t:"))
    i=0
    for objects in flyingobj:
        objects.new_position(t)
        x,y,z=objects.position()
        radius,phi,theta=spherical(x, y, z, radarx, radary, radarz)
        print(f"Объект {i + 1}: r = {radius:.2f} м, азимут = {phi:.2f}°, угол места = {theta:.2f}°")
        i+=1