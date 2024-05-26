import numpy as np

#Input
radar_coord = np.array([0,0,2]) #Координаты радара
N = 10 #Кол-во объектов
angle_grad = True #Если True, то углы в градусах

class Radar():
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Radar, self).__new__(self)
            self.x = radar_coord[0]
            self.y = radar_coord[1]
            self.z = radar_coord[2]
            return self.instance
            
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x
    def get_z(self):
        return self.z

class FlyObj():
    def __init__(self):
        self.x = np.random.randint(-10,10) - radar.get_x()
        self.y = np.random.randint(-10,10) - radar.get_x()
        self.z = np.random.randint(1,10) - radar.get_z()
        self.vx = 1 - np.random.random()*2
        self.vy = 1 - np.random.random()*2
        self.vz = np.random.random()
    def get_coord(self):
        return np.array([self.x,self.y,self.z])
    def get_speed(self):
        return np.array([self.vx,self.vy,self.vz])
    def movement(self,t):
        self.x += self.vx*t
        self.y += self.vy*t
        self.z += self.vz*t
        
def sfer_coord(obj):
    x = obj[0]
    y = obj[1]
    z = obj[2]
    
    r = np.sqrt(x**2+y**2+z**2)
    fi = np.arctan2(y,x)
    if fi<0:
        fi += np.pi*2
    teta = np.arctan2(z, abs(x))

    if angle_grad:
        fi = int(fi*180/np.pi)
        teta = int(teta*180/np.pi)
        
    return np.array([r,fi,teta])
    
radar = Radar()
fly_objects = []

print('Coordinates(t = 0)(ro,fi,teta):\n')
for i in range(N):
    fly_objects.append(FlyObj())
    coords = sfer_coord(fly_objects[i].get_coord())
    print(f'Object {i+1}: {coords[0]} | {coords[1]} | {coords[2]}')

time = float(input('------------\nEnter time: '))

print(f'------------\nCoordinates(t = {time} sec)(ro,fi,teta):\n')
for i in range(N):
    fly_objects[i].movement(time)
    coords = sfer_coord(fly_objects[i].get_coord())
    print(f'Object {i+1}: {coords[0]} | {coords[1]} | {coords[2]}')
