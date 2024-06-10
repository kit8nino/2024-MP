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
        if y-y0 > 0 and x-x0 < 0:
            phi += np.pi
        elif y-y0 < 0 and x-x0 < 0:
            phi += np.pi
        elif y-y0 < 0 and x-x0 >0:
            phi += 2*np.pi
        phi *= (180/np.pi)
        tetta = (180/np.pi)*np.arctan((z-z0)/((x-x0)**2 + (y-y0)**2)**0.5)
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
        z += self.speed[2]*t
        return x,y,z
      

N = 5 #количесво объектов класса UFO
dt = 0.1 #время возврата радиоимпульса (0.1 по умолчанию)
radar_coords = [0,0,0] #координаты радара ((0,0,0) по умолчанию)

#радар
radar = Radar() 
radar.set_radar_coords(radar_coords) 
radar.set_dt(dt)

#летающие объекты
ufo_list = []
for i in range(N):
    rand_x = random.randint(-10, 10) #рандомные декартовы координаты в м
    rand_y = random.randint(-10, 10)
    rand_z = random.randint(1, 10)
    while rand_x == radar_coords[0]:
        rand_x = random.randint(-10, 10)
    while rand_y == radar_coords[1]:
        rand_y = random.randint(-10, 10)
    rand_coords = [rand_x, rand_y, rand_z]
    
    rand_xspeed = random.randint(-8, 8)  #рандомные проекции скоростей в м/c
    rand_yspeed = random.randint(-8, 8)
    rand_zspeed = random.randint(0, 8)
    while rand_xspeed == 0 and rand_yspeed == 0:
        rand_xspeed = random.randint(-8, 8)
        rand_yspeed = random.randint(-8, 8)
    rand_speed = [rand_xspeed,rand_yspeed,rand_zspeed]
    ufo_list += [UFO(rand_coords,rand_speed)]

print("\nInitial spheric coordinates regarding radar:")
for i in range(N):    
    r, phi, tetta = radar.get_ufo_spheric_coords(ufo_list[i],-dt) #начальные сфер. координаты без учета времени возврата радиоимпульса
    print(f'UFO {i}: r(0)={r:0.2f}м phi(0)={phi:0.2f}deg tetta(0)={tetta:0.2f}deg')

while True:
    flag = input("\nSet time: ")
    if flag == '!': break 
    t = int(flag)
    
    for i in range(N):    
        r, phi, tetta = radar.get_ufo_spheric_coords(ufo_list[i],t) #сфер. координаты с учетом времени возврата радиоимпульса
        print(f'UFO {i}: r({t})={r:0.2f}м phi({t})={phi:0.2f}deg tetta({t})={tetta:0.2f}deg')
    print("ENTER '!' TO FINISH")
    