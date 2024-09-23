import math

class Letaushiy_Object:
    def __init__(self, coords, velocity):
        self.x, self.y, self.z = coords
        self.vx, self.vy, self.vz = velocity
        
    def move_coords(self, time: float):
        self.x += self.vx * time
        self.y += self.vy * time
        self.z += self.vz * time

class Radar:
    _instance = None

    def __new__(cls, coords):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x, cls._instance.y, cls._instance.z = coords
        return cls._instance

    def spherical_coords(self, object):
        rel_x = object.x - self.x
        rel_y = object.y - self.y
        rel_z = object.z - self.z
        r = math.sqrt(rel_x ** 2 + rel_y ** 2 + rel_z ** 2)
        phi = math.degrees(math.atan2(rel_y, rel_x))
        teta = math.degrees(math.atan2(rel_z, math.sqrt(rel_x ** 2 + rel_y ** 2)))
        return r, phi, teta

class Programm:
    def __init__(self):
        num_objects = int(input("Введите количество летающих объектов: "))
        self.let_objects = []
        for i in range(num_objects):
            print(i+1,":")
            while True:
                coords = [float(x) for x in input("Введите координаты летающего объекта через пробел(x y z): ").split()]
                if coords[2] < 0:
                    print("Летающий объект под землёй ._.")
                else:
                    break
            velocity = [float(x) for x in input("Введите проекции скорости летающего объекта через пробел(по x y z): ").split()]
            self.let_objects.append(Letaushiy_Object(coords, velocity))
            
                
                
        print("\nСферические координаты:")
        for i, object in enumerate(self.let_objects):
            r, phi, teta = radar.spherical_coords(object)
            print(i + 1,": r =",r,"phi =",phi,"teta =",teta)

        time = float(input("\nВведите время (в секундах): "))
        
        print("Сферические координаты объектов через", time, "секунд относительно радара:")
        for i, object in enumerate(self.let_objects):
            object.move_coords(time)
            r, phi, teta = radar.spherical_coords(object)
            print(i + 1,": r =",r,"phi =",phi,"teta =",teta)

radar = Radar((0,0,0))
programa = Programm()

