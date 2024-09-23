from random import randint
import numpy as np

class FlyingObject:
def init(self, cords):
self.v_x, self.v_y, self.v_z = None, None, None,
self.x, self.y, self.z = cords

def move_object(self, time: int, speed: list) -> None:
self.v_x, self.v_y, self.v_z = speed
self.x += self.v_x * time
self.y += self.v_y * time
self.z += self.v_z * time

def get_speed_projections(self):
return self.v_x, self.v_y, self.v_z

def get_cords(self):
return self.x, self.y, self.z

class Radar(object):
_instance = None

def new(cls):
if not Radar._instance:
Radar._instance = super(Radar, cls).new(cls)
print('Radar initialized.')
return Radar._instance

def init(self):
self.x, self.y, self.z = None, None, None

def set_cords(self, cords: list) -> None:
print('Setting radar coordinates.')
self.x, self.y, self.z = cords

@staticmethod
def translate_cords_to_spherical(cords) -> list:
x, y, z = cords
r = np.sqrt(x 2 + y 2 + z ** 2)
fi = np.degrees((np.arctan(y / x if x != 0 else 10 ** (-8))))
theta = np.degrees(np.arctan(np.sqrt(x 2 + y 2) / z if z != 0 else 10 ** (-8)))

return [r, fi, theta]

def detect_flying_object(self, obj: FlyingObject) -> list:
object_x, object_y, object_z = obj.get_cords()

obj_cords_relative_to_radar = [object_x - self.x, object_y - self.y, object_z - self.z]

spherical_object_cords = self.translate_cords_to_spherical(obj_cords_relative_to_radar)

return spherical_object_cords

def get_cords(self) -> list:
return [self.x, self.y, self.z]

radar = Radar()

radar.set_cords([randint(-1000, 1000) for _ in range(3)])

radar_cords = radar.get_cords()
print(f'Radar coordinates: x = {radar_cords[0]}, y = {radar_cords[1]}, z = {radar_cords[2]}\n')

N = int(input('Count of objects: '))

flying_objects = [FlyingObject([randint(-2000, 2000) for _ in range(3)]) for _ in range(N)]

detected_objects_cords_1 = [radar.detect_flying_object(fl_obj) for fl_obj in flying_objects]

print()
[print(f'Object_{i + 1} coordinates: r = {fl_obj[0]} m, fi = {fl_obj[1]} deg, theta = {fl_obj[2]} deg')
for i, fl_obj in enumerate(detected_objects_cords_1)]

print()

t = int(input('time = '))

detected_objects_cords_2 = []

for fl_obj in flying_objects:
fl_obj.move_object(t, [randint(-100, 100) for _ in range(3)])
detected_objects_cords_2.append(radar.detect_flying_object(fl_obj))

print()

fl_objs_speed = [fl_obj.get_speed_projections() for fl_obj in flying_objects]
[print(f'Object_{i + 1} coordinates: r = {fl_obj[0]} m, fi = {fl_obj[1]} deg, theta = {fl_obj[2]} deg,'
f'Vx = {fl_objs_speed[i][0]}, Vy = {fl_objs_speed[i][1]}, Vz = {fl_objs_speed[i][2]}')
for i, fl_obj in enumerate(detected_objects_cords_2)]
