import math

class Flying_Object:
    def __init__(self, x, y, z, vx, vy, vz):
        self.coords = (x, y, z)
        self.velocity = (vx, vy, vz)

    def move(self, t):
        coords_list = list(self.coords) 
        for i in range(3):
            coords_list[i] += self.velocity[i] * t 
        self.coords = tuple(coords_list)

class Radar:
    def __init__(self, coords):
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def get_position(self, obj: Flying_Object):
        return tuple(a - b for a, b in zip(obj.coords, self.coords))

    def cartesian_to_spherical(self, obj: Flying_Object):
        rel_x, rel_y, rel_z = self.get_position(obj)
        if (rel_x == 0 and rel_y == 0) or (rel_x < 0 or rel_y < 0 or rel_z < 0):
            return 0, 0, 0 
        r = math.sqrt(rel_x*2 + rel_y*2 + rel_z*2)
        theta = math.degrees(math.atan2(rel_y, rel_x))
        phi = math.degrees(math.atan2(rel_z, math.sqrt(rel_x*2 + rel_y*2)))
        return r, theta, phi


radar = Radar((0,0,0))


num_objects = int(input("Введите количество летающих объектов: "))
air_objects = []

for i in range(num_objects):
    print("Для",i+1,"объекта:")
    coords = [float(x) for x in input("Введите координаты объекта (x y z): ").split()]
    velocity = [float(x) for x in input("Введите скорости объекта (vx vy vz): ").split()]
    air_objects.append(Flying_Object(coords[0], coords[1], coords[2], velocity[0], velocity[1], velocity[2]))

print("Текущие сферические координаты объектов относительно радара:")
for i, obj in enumerate(air_objects):
    r, theta, phi = radar.cartesian_to_spherical(obj)
    print("Объект",i + 1,":r =",r,"тао =",theta,"фи =",phi)

time = float(input("Введите время в секундах: "))

for obj in air_objects:
    obj.move(time)

print("Сферические координаты объектов через", time, "секунд относительно радара:")
for i, obj in enumerate(air_objects):
    r, theta, phi = radar.cartesian_to_spherical(obj)
    print("Объект", i + 1, ": r =", r, "theta =", theta, "phi =", phi)
