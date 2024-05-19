import numpy as np
import random

class Radar:
    
    def __init__(self,coords = [0,0,0],dt = 0.1):
        self.coords = coords
        self.dt = dt
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Radar, cls).__new__(cls)
        return cls.instance

    def set_radar_coords(self,coords):
        self.coords = coords
    
    def set_dt(self,dt):
        self.dt = dt
    
    def get_radar_coords(self):
        return self.coords

    def get_ufo_spheric_coords(self,ufo,t):
        x,y,z = ufo.get_dec_coords(t+self.dt)
        x0,y0,z0 = self.get_radar_coords()
        r = ((x-x0)**2 + (y-y0)**2 + (z-z0)**2)**0.5
        phi = np.arctan((y-y0)/(x-x0))
        tetta = np.arctan((z-z0)/((x-x0)**2 + (y-y0)**2)**0.5)
        ufo_spheric_coords = r, phi, tetta
        return ufo_spheric_coords

class UFO:
    
    def __init__(self,dec_coords,speed):
        self.dec_coords = dec_coords #x,y,z
        self.speed = speed
    
    def set_dec_cords(self,coords):
        self.dec_coords = coords
        print("Set coords to:", coords)

    def set_speed(self,speed):
        self.speed = speed
        print("Set speed to:", speed)

    def get_dec_coords(self,t):
        x,y,z = self.dec_coords
        x += self.speed[0]*t 
        y += self.speed[1]*t 
        return x,y,z
      

N = 5 #количесво объектов класса UFO
dt = 0.1 #время возврата радиоимпульса (0.1 по умолчанию)
radar_coords = [0,0,0] #координаты радара ((0,0,0) по умолчанию)

radar = Radar() 
radar.set_radar_coords(radar_coords) 
radar.set_dt(dt)

ufo_list = []
for i in range(N):
    rand_x = random.randint(-10, 10)
    rand_y = random.randint(-10, 10)
    rand_z = random.randint(1, 10)
    rand_coords = [rand_x, rand_y, rand_z]
    
    rand_xspeed = random.randint(1, 8)
    rand_yspeed = random.randint(1, 8)
    rand_speed = [rand_xspeed,rand_yspeed]
    ufo_list += [UFO(rand_coords,rand_speed)]

print("\nInitial spheric coordinates regarding radar:")
for i in range(N):    
    r, phi, tetta = radar.get_ufo_spheric_coords(ufo_list[i],-dt) #начальные сфер. координаты без учета времени возврата радиоимпульса
    print(f'UFO {i}: r(0)={r}м phi(0)={phi}rad tetta(0)={tetta}rad')

while True:
    flag = input("\nSet time: ")
    if flag == '!': break 
    t = float(flag)
    
    for i in range(N):    
        r, phi, tetta = radar.get_ufo_spheric_coords(ufo_list[i],t) #сфер. координаты с учетом времени возврата радиоимпульса
        print(f'UFO {i}: r({t})={r}м phi({t})={phi}rad tetta({t})={tetta}rad')
    print("ENTER '!' TO FINISH")
    