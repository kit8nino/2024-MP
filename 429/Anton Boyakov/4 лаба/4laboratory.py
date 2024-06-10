import numpy as np
import random

class RLS:

    instances = {}
    def singleton(cls):
        instances = {}

        def getinstance():
            if cls not in instances:
                instances[cls] = cls()
            return instances[cls]

        return getinstance

    def set_rls_coords(self, coords):
        self.coords = coords

    def set_dt(self, dt):
        self.dt = dt

    def get_rls_coords(self):
        return self.coords

    def get_fl_obj_sph_coords(self, ufo, t):
        x, y, z = ufo.get_dec_coords(t + self.dt)
        x0, y0, z0 = self.get_rls_coords()

        r = ((x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2) ** 0.5
        phi = np.arctan((y - y0) / (x - x0))
        tetta = np.arctan((z - z0) / ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5)

        ufo_spheric_coords = r, phi, tetta
        return ufo_spheric_coords


class Flight_object:

    def __init__(self, dec_coords, speed):
        self.dec_coords = dec_coords  # x,y,z
        self.speed = speed

    def set_dec_cords(self, coords):
        self.dec_coords = coords
        print("Декартовы координаты РЛС:", coords)

    def get_dec_coords(self, t):
        x, y, z = self.dec_coords
        x += self.speed[0] * t
        y += self.speed[1] * t
        return x, y, z


objects_count = 3  # количесво объектов класса flight_object
dt = 0.1  # время возврата радиоимпульса
rls_coords = [10, 10, 0]  # координаты радара
rls = RLS()
rls.set_rls_coords(rls_coords)
rls.set_dt(dt)

objects = []
for i in range(objects_count):
    random_x = random.randint(0, 20)
    random_y = random.randint(0, 20)
    random_z = random.randint(1, 20)
    random_coords = [random_x, random_y, random_z]

    random_xspeed = random.randint(1, 10)
    random_yspeed = random.randint(1, 10)
    random_speed = [random_xspeed, random_yspeed]
    objects += [Flight_object(random_coords, random_speed)]

print("\nНачальные сферические координаты объектов относительно РЛС:")
for i in range(objects_count):
    r, phi, tetta = rls.get_fl_obj_sph_coords(objects[i],-dt)  # начальные сфер. координаты без учета времени возврата радиоимпульса
    print(f'Летающий объект №{i}: r(0)={r}м phi(0)={phi}рад tetta(0)={tetta}рад')

t = int(input("\nВремя в секундах: "))
for i in range(objects_count):
    r, phi, tetta = rls.get_fl_obj_sph_coords(objects[i],t)  # сфер. координаты с учетом времени возврата радиоимпульса
    print(f'Летающий объект №{i}: r({t})={r}м phi({t})={phi}рад tetta({t})={tetta}рад')
