import math

class Radar:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, x_coord, y_coord, z_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

    def get_spherical_coords(self, objects):
        for obj in objects:
            obj.print_spherical_coords(self.x_coord, self.y_coord, self.z_coord)

    def get_spherical_coords_after_time(self, objects, time):
        for obj in objects:
            obj.update_coords(time, obj.speed_proj_x, obj.speed_proj_y, obj.speed_proj_z)
        self.get_spherical_coords(objects)

class FlyingObject:
    def __init__(self, x_coord, y_coord, z_coord, speed_proj_x, speed_proj_y, speed_proj_z):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord
        self.speed_proj_x = speed_proj_x
        self.speed_proj_y = speed_proj_y
        self.speed_proj_z = speed_proj_z

    def update_coords(self, time,speed_proj_x, speed_proj_y, speed_proj_z):
        self.x_coord += time * speed_proj_x
        self.y_coord += time * speed_proj_y
        self.z_coord += time * speed_proj_z

    def print_spherical_coords(self, radar_x, radar_y, radar_z):
        r = math.sqrt((self.x_coord - radar_x) ** 2 + (self.y_coord - radar_y) ** 2 + (self.z_coord - radar_z) ** 2)
        phi = math.degrees(math.atan2(self.y_coord - radar_y, self.x_coord - radar_x))
        # для того, чтобы были фи был в диапазоне [0, 360)
        if phi < 0:
            phi += 360
    
        thetta = math.degrees(math.atan2(self.z_coord - radar_z, math.sqrt((self.x_coord - radar_x) ** 2 + (self.y_coord - radar_y) ** 2)))
        # для того, чтобы тетта был в диапазоне [0, 180)
        if thetta < 0:
            thetta += 180
        print(f'Object: r={r:.2f}m, phi={phi:.2f}°, thetta={thetta:.2f}°')

class RadarSystem:
    def __init__(self, radar_x, radar_y, radar_z, num_objects):
        self.radar = Radar(radar_x, radar_y, radar_z)
        self.objects = []
        for _ in range(num_objects):
            x_coord, y_coord, z_coord, speed_proj_x, speed_proj_y, speed_proj_z = self.get_object_data()
            self.objects.append(FlyingObject(x_coord, y_coord, z_coord, speed_proj_x, speed_proj_y, speed_proj_z))

    def get_object_data(self):
        x_coord = float(input('Enter object x-coordinate (m): '))
        y_coord = float(input('Enter object y-coordinate (m): '))
        z_coord = float(input('Enter object z-coordinate (m): '))
        speed_proj_x = float(input('Enter object x-speed projection (m/s): '))
        speed_proj_y = float(input('Enter object y-speed projection (m/s): '))
        speed_proj_z = float(input('Enter object z-speed projection (m/s): '))
        return x_coord, y_coord, z_coord, speed_proj_x, speed_proj_y, speed_proj_z

    def run(self):
        self.radar.get_spherical_coords(self.objects)
        time = float(input('\nEnter time (s) to display new spherical coordinates: '))
        self.radar.get_spherical_coords_after_time(self.objects, time)

if __name__ == '__main__':
    # Задаем координаты радара 
    radar_x = 10.0
    radar_y = 20.0
    radar_z = 30.0
    num_objects = int(input('Enter number of flying objects: '))
    radar_system = RadarSystem(radar_x, radar_y, radar_z, num_objects)
    radar_system.run()
