from random import randint
import numpy as np

class Flying_Object:
    def __init__(self, cords):
        self.v_x, self.v_y, self.v_z = None, None, None,
        self.x, self.y, self.z = cords
    def movement_object(self, time: int, speed: list) -> None:
        self.v_x, self.v_y, self.v_z = speed
        self.x += self.v_x * time
        self.y += self.v_y * time
        self.z += self.v_z * time
    def get_cords(self):
        return self.x, self.y, self.z
    def get_speed(self):
        return self.v_x, self.v_y, self.v_z
###############################################################################

class Radar(object):
    determine = None
    def __new__(cls):
        if not Radar.determine:
            Radar.determine = super(Radar, cls).__new__(cls)
            print('Радар установлен.')
            return Radar.determine
    def __init__(self):
        self.x, self.y, self.z = None, None, None
    def setup_cords(self, cords: list) -> None:
        print('Установка координат радара.')
        self.x, self.y, self.z = cords
    def cords_to_spher(self,cords) -> list:
        x, y, z = cords
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        fi = np.degrees((np.arctan(y / x if x != 0 else 10 ** (-8))))
        tetta = np.degrees(np.arctan(np.sqrt(x ** 2 + y ** 2) / z if z != 0 
        else 10 ** (-8)))
        return [r, fi, tetta]
    def detect_flying_object(self, obj: Flying_Object) -> list:
        object_x, object_y, object_z = obj.get_cords()
        cords_to_radar = [object_x - self.x, object_y - self.y, object_z - self.z]
        spher_object_cords = self.cords_to_spher(cords_to_radar)
        return spher_object_cords
    def get_cords(self) -> list:
        return [self.x, self.y, self.z]
###############################################################################

radar = Radar()
radar.setup_cords([randint(-1000, 1000) for _ in range(3)])
radar_cords = radar.get_cords()
print(f'Координаты радара: x = {radar_cords[0]}, y = {radar_cords[1]}, z = {radar_cords[2]}\n')

N = int(input('Введите количество объектов: '))
flying_objects = [Flying_Object([randint(-5000, 5000) for _ in range(3)]) for _ in range(N)]
detected_objects_cords_1 = [radar.detect_flying_object(fl_obj) for fl_obj in flying_objects]
print()
[print(f'Object_{i + 1} координаты: r = {fl_obj[0]} m, fi = {fl_obj[1]} deg, tetta = {fl_obj[2]} deg')
 for i, fl_obj in enumerate(detected_objects_cords_1)]

print()

time = int(input('Введите время (в секундах) = '))

objects_cords_2 = []
for fl_obj in flying_objects:
    fl_obj.movement_object(time, [randint(-100, 100) for _ in range(3)])
    objects_cords_2.append(radar.detect_flying_object(fl_obj))
print()

fl_objs_speed = [fl_obj.get_speed() for fl_obj in flying_objects]
[print(f'Object_{i + 1} координаты: r = {fl_obj[0]} m, fi = {fl_obj[1]} deg, tetta = {fl_obj[2]} deg,'
       f'Vx = {fl_objs_speed[i][0]}, Vy = {fl_objs_speed[i][1]}, Vz = {fl_objs_speed[i][2]}')
 for i, fl_obj in enumerate(objects_cords_2)]


