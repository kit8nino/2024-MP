from math import acos, atan, sqrt, degrees

class radar:
    _instance = None

    def __new__(cls, x, y, z):
        if not cls._instance:
            cls._instance = super(radar, cls).__new__(cls)
            cls.coords = (x, y, z)
        return cls._instance
    
    def get_coords(self):
        return (self.coords)
    
class plane:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
    def get_sphere_coords(self, radar_coords):
        x_coord, y_coord, z_coord = radar_coords
        dx = self.x - x_coord
        dy = self.y - y_coord
        dz = self.z - z_coord
        if dz <= 0:
            print("Аппарат приземлился (разбился)")
            dz = 0
        r = sqrt(dx**2 + dy**2 + dz**2)
        phi = degrees(atan(dy/dx))
        theta = degrees(acos(dz/r))
        return (r, phi, theta)
    
    def move(self, t):
        self.x += self.vx*t
        self.y += self.vy*t
        self.z += self.vz*t
  
# Ввод с клавиатуры:
# fliers_quantity = int(input("Введите число летательных аппаратов: "))
# fliers = []
# for i in range(fliers_quantity):
#     print("{}-й летательный аппарат:".format(i+1))
#     x = int(input("x: "))
#     y = int(input("y: "))
#     z = int(input("z: "))
#     vx = int(input("vx: "))
#     vy = int(input("vy: "))
#     vz = int(input("vz: "))
#     fliers.append(plane(x,y,z,vx,vy,vz))

rradar = radar(0, 0, 0)

fliers = [plane(10, 20, 30, 4, 5, 1),
          plane(20, 20, 30, -4, -5, -1),
          plane(30, 20, 30, -10, 10, -5)]

radar_coordinates = rradar.get_coords()

time = int(input("Введите время t: "))

print("Начальное положение:")
for flier in fliers:
    print("\nКоординаты {}-го аппарата:".format(fliers.index(flier)+1))
    print("r = {}, phi = {}, theta = {}".format(*flier.get_sphere_coords(radar_coordinates)))
    
print("\nПоложение через время t:")
for flier in fliers:
    print("\nКоординаты {}-го аппарата:".format(fliers.index(flier)+1))
    flier.move(time)
    print("r = {}, phi = {}, theta = {}".format(*flier.get_sphere_coords(radar_coordinates)))