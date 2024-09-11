from random import randint
import numpy as np


class FlyingObject:
    def __init__(self, cords):
        self.v_x, self.v_y, self.v_z = None, None, None,
        self.x, self.y, self.z = cords

    def move_object(self, time: int, speed: list) -> None:
        self.v_x, self.v_y, self.v_z = speed
        self.x += self.v_x * time
        self.y += self.v_y * time
        self.z += self.v_z * time


    def get_cords(self):
        return self.x, self.y, self.z


class Radar:
    _instance = None

    def __new__(cls):
        if not Radar._instance:
            Radar._instance = super(Radar, cls).__new__(cls)
            return Radar._instance

    def __init__(self):
        self.x, self.y, self.z = None, None, None

    def set_cords(self, cords):
        print('Setting radar coordinates.')
        self.x, self.y, self.z = cords

    def to_spherical(self, cords):
        x, y, z = cords
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        fi = np.degrees((np.arctan(y / x)
        theta = np.degrees(np.arctan(np.sqrt(x ** 2 + y ** 2) / z)

        return [r, fi, theta]

    def detect_object(self, obj):
        object_x, object_y, object_z = obj.get_cords()

        obj_cords_relative_to_radar = [object_x - self.x, object_y - self.y, object_z - self.z]

        return self.to_spherical(obj_cords_relative_to_radar)

    def get_cords(self) -> list:
        return [self.x, self.y, self.z]


radar = Radar()

radar.set_cords([randint(-1000, 1000) for _ in range(3)])

radar_cords = radar.get_cords()
print(f'Radar cords: x = {radar_cords[0]}, y = {radar_cords[1]}, z = {radar_cords[2]}\n')

N = int(input('Count of objects: '))

flying_objects = [FlyingObject([randint(1, 2000) for _ in range(3)]) for _ in range(N)]

detected_objects_1 = [radar.detect_object(fl_obj) for fl_obj in flying_objects]

for i, fl_obj in enumerate(detected_objects1):
	print(f'Object_{i + 1} cords: r = {fl_obj[0]}, fi = {fl_obj[1]}, theta = {fl_obj[2]}')

t = int(input('time = '))

detected_objects_2 = []

for fl_obj in flying_objects:
    fl_obj.move_object(t, [randint(1, 100) for _ in range(3)])
    detected_objects_2.append(radar.detect_object(fl_obj))

for i, fl_obj in enumerate(detected_objects_2):
	print(f'Object_{i + 1} cords: r = {fl_obj[0]}, fi = {fl_obj[1]}, theta = {fl_obj[2]}')
