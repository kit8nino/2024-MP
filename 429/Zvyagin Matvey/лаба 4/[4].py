import math

class FlyObject:
    def __init__(self, coords, velocity):
        self.x, self.y, self.z = coords
        self.vx, self.vy, self.vz = velocity

    def moving(self, t: float) -> None:
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t

class Radar:
    _instance = None

    def __new__(cls, coords):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x, cls._instance.y, cls._instance.z = coords
        return cls._instance

    def get_position(self, obj: FlyObject):
        rel_x = obj.x - self.x
        rel_y = obj.y - self.y
        rel_z = obj.z - self.z
        return rel_x, rel_y, rel_z

    def cartesian_to_spherical(self, obj: FlyObject):
        rel_x, rel_y, rel_z = self.get_position(obj)
        r = math.sqrt(rel_x ** 2 + rel_y ** 2 + rel_z ** 2)
        theta = math.degrees(math.atan2(rel_y, rel_x))
        phi = math.degrees(math.atan2(rel_z, math.sqrt(rel_x ** 2 + rel_y ** 2)))
        return r, theta, phi

radar = Radar((0,0,0))

num_objects = int(input("Введите количество НЛО: "))
air_objects = []

for i in range(num_objects):
    print("Для",i+1,"НЛО:")
    coords = [float(x) for x in input("Введите координаты НЛО (x y z через пробел): ").split()]
    velocity = [float(x) for x in input("Введите скорости НЛО (vx vy vz через пробел): ").split()]
    air_objects.append(FlyObject(coords, velocity))

print("Текущие сферические координаты НЛО относительно радара:")
for i, obj in enumerate(air_objects):
    r, theta, phi = radar.cartesian_to_spherical(obj)
    print("НЛО",i + 1,":r =",r,"тао =",theta,"фи =",phi)

time = float(input("Введите время в секундах: "))

print("Сферические координаты НЛО через", time, "секунд относительно радара:")
for i, obj in enumerate(air_objects):
    obj.moving(time)
    r, theta, phi = radar.cartesian_to_spherical(obj)
    print("НЛО:", i + 1,":r =",r,"тао =",theta,"фи =",phi)
